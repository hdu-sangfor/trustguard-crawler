# LLM Observer Proxy： 基于 Go 与 Bifrost 的大模型运行域可观...

### 来源信息
- **URL**: https://github.com/xxyyue/llm-observer-proxy-go
- **来源站点**: SecWiki
- **页面抓取**: 成功

### 页面正文
LLM Observer Proxy runs an embedded Bifrost data plane for each evaluation or agent run and stores its observable LLM traffic under a stable run_id. The observer records requests, responses, streaming output, tool calls, token usage, cost estimates, errors, and provider-visible reasoning content. It does not require Python, LiteLLM, Docker, or a separate Bifrost process.
It is independently installable and can be embedded into any evaluation platform, agent runner, or orchestration service through its HTTP API.
There are two HTTP layers:
- The control plane listens on port 8790by default. An orchestrator uses it to create, inspect, and stop run-scoped proxies.
- Each data plane listens on a separate, automatically allocated port. An agent uses the returned URL as an OpenAI-compatible or Anthropic-compatible LLM endpoint.
One control-plane process can manage multiple concurrent data planes using goroutines. Stopping a data plane preserves its history on disk, and history remains readable after the control plane restarts.
The observer can only record information exposed by the upstream API. It cannot obtain hidden chain-of-thought that a provider does not return.
- Go 1.26.4 or newer, as required by Bifrost Core
- An upstream API key and model catalog
- Local permission to bind control-plane and data-plane ports
Older Go installations with GOTOOLCHAIN=auto can download the toolchain declared in go.mod automatically.
Install the command from GitHub:
go install github.com/xxyyue/llm-observer-proxy-go/cmd/llm-observer-proxy@latestThe repository and module path are named llm-observer-proxy-go; the installed command and service are named llm-observer-proxy. Ensure $(go env GOPATH)/bin is on PATH, then verify the installation:
llm-observer-proxy --versionFor a source checkout, run or build the same command:
go run ./cmd/llm-observer-proxy
go build -o llm-observer-proxy ./cmd/llm-observer-proxyThe embedded fallback catalog includes gpt-5.5 and reads the OpenAI credential from the environment:
export OPENAI_API_KEY=your-openai-api-key
llm-observer-proxyIn another terminal, check the control plane:
curl http://127.0.0.1:8790/healthzCreate a data plane for a run:
curl -X POST http://127.0.0.1:8790/api/runs/run-001/proxy \
  -H 'Content-Type: application/json' \
  -d '{}'The data plane serves every model in the selected catalog. Each LLM request selects a model through its own model field. The create response includes a dynamically allocated bare base_url, for example http://127.0.0.1:45678, plus openai_base_url (http://127.0.0.1:45678/v1) and anthropic_base_url (http://127.0.0.1:45678). Use the explicit URL for the client SDK, or call an endpoint directly:
curl http://127.0.0.1:45678/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "gpt-5.5",
  "messages": [{"role": "user", "content": "Reply with one short sentence."}]
  }'Read the normalized history:
curl http://127.0.0.1:8790/api/runs/run-001/historyStop the data plane without deleting its history:
curl -X DELETE http://127.0.0.1:8790/api/runs/run-001/proxyThe command accepts these options:
--host HOST  Control-plane bind host (default: 127.0.0.1)
--port PORT  Control-plane port (default: 8790)
--env-file PATH  KEY=VALUE file loaded before startup (default: .env)
--artifact-root PATH  Artifact storage root
--model-catalog PATH  Model catalog JSON
--log-level LEVEL  Bifrost log level
--version  Print the build version
Paths are resolved in this order:
- --artifact-rootand- --model-catalog
- LLM_OBSERVER_PROXY_ARTIFACT_ROOTand- LLM_OBSERVER_PROXY_MODEL_CATALOG_PATH
- ./artifactsand- ./config/models.jsonin the working directory
- The binary's secret-free embedded model catalog
Relative paths are resolved against the process working directory. The optional .env file is loaded before environment-based path and credential resolution, and existing process environment values take precedence.
The service embeds Bifrost Core v1.6.3 and the official OpenAI and Anthropic provider packages. It does not start the full Bifrost server, a Docker container, or another process. The data plane keeps the public OpenAI-compatible /v1/* routes and Anthropic-compatible /v1/messages route, and records exact request and response payloads in events.jsonl, including Anthropic system content blocks and cache-control markers.
The HTTP path selects the request protocol: /v1/messages uses the Anthropic adapter, while other /v1/* paths use the OpenAI adapter. Every catalog model is accepted through either format so an upstream that supports both formats can translate as needed.
A model catalog has this shape:
{
  "llm_observer_proxy": {
  "base_url": "https://api.openai.com",
  "api_key": "os.environ/OPENAI_API_KEY"
  },
  "models": [
  {
  "id": "gpt-5.5",
  "upstream_api": "openai"
  }
  ]
}id is the public model name accepted by the data plane. upstream_api must be openai or anthropic for catalog compatibility, but the request path selects the adapter at runtime. Optional per-million-token prices under pricing are used for local cost estimates. Other model properties are ignored. api_key accepts a literal value, os.environ/NAME, env.NAME, or ${NAME}. All catalog models currently share one upstream base_url and credential. See config/models.example.json for a complete example.
The legacy top-level catalog key llm_proxy remains accepted when llm_observer_proxy is absent.
| Method | Path | Purpose | 
|---|---|---|
| GET | /healthz | Check control-plane health | 
| GET | /api/proxies | List process-local running and stopped proxies | 
| POST | /api/runs/{run_id}/proxy | Create a run-scoped data plane | 
| GET | /api/runs/{run_id}/proxy | Read proxy state | 
| DELETE | /api/runs/{run_id}/proxy | Stop a data plane | 
| GET | /api/runs/{run_id}/history | Read normalized history | 
| GET | /api/runs/{run_id}/conversation | Read the latest conversation | 
The create payload may be empty. Optional active fields are port and bind_host. Compatibility fields including model, mode, backend, litellm_config_path, litellm_env, and strip_callbacks are accepted and ignored, as are unknown fields. The complete request and response contract is documented in docs/control-plane-api.md.
Each run writes:
artifacts/runs/<run_id>/platform/llm/
  config.json
  conversation_snapshot.json
  events.jsonl
  bifrost.log
events.jsonl retains raw requests and responses, streaming bodies, usage, tool calls, visible reasoning, errors, and normalized summaries. conversation_snapshot.json contains the latest reconstructed conversation. config.json contains non-secret run metadata, and bifrost.log is retained as a compatibility path.
Incoming Authorization and x-api-key headers are redacted in artifacts. Request and response bodies are intentionally retained and may contain sensitive data, so apply appropriate filesystem permissions, access control, and retention policies to the artifact root.
The supported data-plane surface is OpenAI-compatible /v1/* routes and Anthropic /v1/messages, plus the control and history APIs documented above. Bifrost's management server, administration UI, database persistence, plugins, governance features, other providers, and MCP runtime are not part of this project's compatibility contract. Bifrost's shared schemas package imports MCP types, so mcp-go remains a transitive compile dependency even though no MCP code is configured or executed.
- Proxy creation returns 400: check the run ID, requested port, bind address, catalog, and filesystem permissions.
- Proxy creation returns 409: therun_idalready has a running data plane.
- An LLM request fails: confirm the upstream base_url, credential environment variable, request path, and model name. Provider errors are recorded inevents.jsonl.
- History is empty: confirm the agent is using the returned data-plane URL, not the provider URL directly.
- llm-observer-proxyis not found after installation: add- $(go env GOPATH)/binto- PATH.
The control API is an administrative interface: it can start listeners, select listening ports, and store LLM traffic. Version 0.1.x has no built-in authentication. Bind it to loopback or a trusted private network and read .github/SECURITY.md before remote deployment.
History can contain prompts, model output, tool output, and credentials. Apply appropriate filesystem permissions, access control, and retention policies to the artifact root.
test -z "$(gofmt -l cmd internal)"
go mod tidy
git diff --exit-code -- go.mod go.sum
go vet ./...
go test -race ./...
go build -trimpath ./cmd/llm-observer-proxyApache-2.0. See LICENSE and NOTICE.
- Shuqiao Zhang stevenjoezhang@gmail.com
- Yue Xiong xxyyyue@gmail.com

---
*爬取时间: 2026-07-24 16:01:07*
*来源: 直接站点爬取*
