# CVE Vulnerability Verification Dataset Samples

本目录是 CVE 漏洞验证数据集的发布样例，面向大模型安全训练、漏洞定位、修复建议生成、PoC 验证和 Docker 化复现环境评测。样例覆盖 3 个项目、8 个 CVE case，每个 CVE 目录都提供独立的构建配置、漏洞版与修复版源码版本、验证脚本、根因分析和结构化标注。

本数据集仅用于授权安全研究、模型训练和防御性验证。请勿将其中的 PoC、测试脚本或漏洞描述用于未授权系统。

## 数据集内容

| 项目目录 | 语言 | CVE 数量 | 覆盖类型 |
| --- | --- | ---: | --- |
| `caddy/` | Go | 3 | 路由绕过、Host 匹配绕过、`forward_auth` 授权绕过 |
| `cms/` | PHP | 3 | 路径穿越、动态 collection 加载、session return URL 写入 |
| `saleor/` | Python | 2 | 存储型 XSS、GraphQL IDOR |

## 目录结构

```text
sample/
├── README.md
├── <project>/
│   ├── project_meta.json
│   ├── sast_standardized.json
│   └── findings/
│       └── <CVE-ID>/
│           ├── Dockerfile
│           ├── docker-compose.yml
│           ├── deployment.json
│           ├── docker-env/
│           │   ├── .env
│           │   ├── compose.sh
│           │   ├── build-vul.sh
│           │   ├── build-fix.sh
│           │   ├── run-vul.sh
│           │   ├── run-fix.sh
│           │   ├── fetch_source.sh
│           │   └── common.sh
│           └── verify_requirements/
│               ├── sast_standardized.json
│               ├── verification_plan.json
│               ├── verification_result.json
│               ├── remediation_result.json
│               ├── root_cause.md
│               ├── root_cause_zh.md
│               ├── fix.md
│               ├── fix_zh.md
│               ├── one_issue.txt
│               └── tests/
```

## 项目级字段

每个一级项目目录代表一个开源项目或产品线。

| 文件 | 功能 |
| --- | --- |
| `project_meta.json` | 项目元信息，包括项目名、主要语言和执行环境。 |
| `sast_standardized.json` | 项目级漏洞标注集合。包含该项目下所有 finding 的统一结构化描述、漏洞位置、数据流和修复建议。 |
| `findings/` | CVE case 集合。每个子目录是一个可独立构建、运行和验证的漏洞样例。 |

`sast_standardized.json` 的核心字段：

| 字段 | 含义 |
| --- | --- |
| `summary` | 统计信息，目前保留 finding 总数。 |
| `findings[]` | 逐条 CVE 的结构化漏洞记录。 |
| `findings[].finding_id` | CVE 编号。 |
| `findings[].cwe` | CWE 分类，可能为空或包含多个 CWE。 |
| `findings[].vuln_type` | 数据集内部归一化漏洞类型。 |
| `findings[].severity` / `cvss` | 严重级别和 CVSS 分数。 |
| `findings[].description` | 漏洞背景，通常合并 NVD 描述和任务描述。 |
| `findings[].recommendation` | 验证结论和修复建议。 |
| `findings[].vul_pos` | 漏洞相关代码位置，含文件、行号、角色和代码片段。 |
| `findings[].dataflow` | 从 source 到 sink 的数据流解释，可用于训练漏洞推理模型。 |
| `findings[].fix_version` | 已知修复版本。 |

说明：历史整理过程中的内部质检字段、误报字段和流水线验证元数据已从发布样例中移除。验证证据统一保留在各 CVE 的 `verify_requirements/verification_result.json` 中。

## CVE 目录字段

每个 `findings/<CVE-ID>/` 是一个独立样例，建议把它作为最小训练和验证单元。

| 文件或目录 | 功能 |
| --- | --- |
| `Dockerfile` | 构建漏洞版和修复版镜像的定义。构建时会根据 `docker-env/.env` 下载对应源码版本。 |
| `docker-compose.yml` | 统一声明 `vul` 和可选 `fix` service。这些 Compose 配置主要提供构建与验证环境，不默认代表长期运行的业务服务。 |
| `deployment.json` | 机器可读部署元数据，适合自动化评测系统读取。 |
| `docker-env/` | Docker 复现环境入口，包含 Compose 封装脚本、源码拉取配置和漏洞版/修复版容器运行脚本。 |
| `verify_requirements/` | 验证材料，不是构建镜像的核心依赖，主要用于 PoC、证据、根因和修复说明。 |

`deployment.json` 的核心字段：

| 字段 | 含义 |
| --- | --- |
| `method` | 部署方式，本样例为 `docker-compose`。 |
| `compose_files` | Compose 文件列表。 |
| `env_file` | Compose 必须加载的环境变量文件。 |
| `working_directory` | 命令执行目录，通常为 CVE 根目录。 |
| `entry_script` | 统一入口脚本。 |
| `build_mode` | 构建模式，本样例为 `app`。 |
| `cve_id` | 当前 CVE 编号。 |
| `images.vul` / `images.fix` | 漏洞版和修复版镜像名。 |
| `services.required` | 必需服务，通常为 `vul`。 |
| `services.optional` | 可选服务，通常为 `fix`。 |
| `scripts` | 常用脚本入口。 |
| `commands` | 推荐构建、进入 shell 或验证命令。 |
| `startup` | 启动步骤说明，可供自动化系统执行。 |
| `startup_timeout_seconds` | 建议超时时间。 |
| `source_urls.vul` / `source_urls.fix` | 漏洞版和修复版源码 tarball 地址。 |

`docker-env/.env` 的核心字段：

| 字段 | 含义 |
| --- | --- |
| `CVE_ID` | CVE 编号。 |
| `IMAGE_NAME` | 镜像名前缀，最终镜像通常为 `<IMAGE_NAME>:vul` 和 `<IMAGE_NAME>:fix`。 |
| `VUL_DOWNLOAD_URL` | 漏洞版源码下载地址。 |
| `VUL_STRIP_COMPONENTS` | 解压漏洞版源码时传给 `tar --strip-components` 的层数。 |
| `FIX_DOWNLOAD_URL` | 修复版源码下载地址。 |
| `FIX_STRIP_COMPONENTS` | 解压修复版源码时的 strip 层数。 |
| `WORK_DIR` | 容器内源码工作目录，如 `/app` 或 `/workspace`。 |
| `BUILD_MODE` | 构建模式。 |
| `FETCH_SOURCE` | 是否在构建阶段自动拉取源码。 |
| `VERIFY_MOUNT` | `verify_requirements` 在容器内的挂载路径，通常为 `/workspace/verify_requirements`。 |

`docker-env/` 中的脚本入口：

| 文件 | 功能 |
| --- | --- |
| `compose.sh` | 统一 Docker Compose 入口，会自动切换到 CVE 根目录并加载 `docker-env/.env`。 |
| `build-vul.sh` | 构建漏洞版镜像，对应 Compose service `vul`。 |
| `run-vul.sh` | 运行漏洞版容器。可传入 `bash` 进入交互 shell，也可传入测试命令直接执行。 |
| `build-fix.sh` | 构建修复版镜像，对应 Compose service `fix` 和 profile `fix`。 |
| `run-fix.sh` | 运行修复版容器。用法与 `run-vul.sh` 相同。 |
| `fetch_source.sh` / `common.sh` | 镜像构建阶段使用的源码下载与解压辅助脚本。 |

这些镜像的主要用途是准备固定源码版本、依赖和工作目录，供 `verify_requirements/tests/` 中的 PoC 或回归测试运行。多数 case 的 `Dockerfile` 不定义长期运行的 `CMD` / `ENTRYPOINT`，`docker compose up` 通常不会启动可访问的 Web/API 服务，也多数没有宿主机端口映射。因此推荐使用 `docker-env/build-*.sh` 和 `docker-env/run-*.sh`，而不是把这些 Compose 文件当作服务部署配置使用。

`verify_requirements/` 的核心字段：

| 文件 | 功能 |
| --- | --- |
| `sast_standardized.json` | 当前 CVE 的结构化漏洞标注，字段与项目级 finding 基本一致。 |
| `verification_plan.json` | 验证计划，记录漏洞类型、建议执行环境和验证方法。 |
| `verification_result.json` | 漏洞验证结果，包含测试脚本路径、容器内测试命令、可从 CVE 根目录执行的容器命令、退出码、日志尾部和说明。 |
| `remediation_result.json` | 修复验证摘要，记录漏洞类型、修复后状态、验证方法、PoC 路径、修复涉及文件和复用的验证命令。 |
| `root_cause.md` / `root_cause_zh.md` | 英文和中文根因分析。 |
| `fix.md` / `fix_zh.md` | 英文和中文修复说明。 |
| `one_issue.txt` | 单条 issue 描述，适合生成任务输入。 |
| `tests/` | PoC、单元测试或流量测试脚本。具体执行入口以 `verification_result.json` 为准。 |

`verification_result.json` 中的命令字段含义：

| 字段 | 含义 |
| --- | --- |
| `tests[].command` | 在已经准备好的漏洞版容器/源码工作目录中执行的测试命令。 |
| `tests[].run_in_vul_container` | 从 CVE 根目录执行的漏洞验证命令；前提是已经通过 `docker-env/build-vul.sh` 构建好漏洞版镜像。 |
| `tests[].reproduce_in_vul_container` | 从 CVE 根目录执行的完整漏洞复现命令，会先构建漏洞版镜像，再进入 `vul` 容器运行测试。 |

`remediation_result.json` 中的命令字段含义：

| 字段 | 含义 |
| --- | --- |
| `verification_command` | 在已经准备好的修复版容器/源码工作目录中复用的验证命令。 |
| `run_in_fix_container` | 从 CVE 根目录执行的修复验证命令；前提是已经通过 `docker-env/build-fix.sh` 构建好修复版镜像。 |
| `reproduce_in_fix_container` | 从 CVE 根目录执行的完整修复验证命令，会先构建修复版镜像，再进入 `fix` 容器运行测试。 |

## 使用方式

准备环境：

- Docker
- Docker Compose v2
- 能访问 `docker-env/.env` 中的源码下载地址
- 部分 Python/PHP/Go case 在容器内执行验证时还需要访问依赖源

网络与代理：

发布样例不会内置任何组织内部代理地址。Dockerfile 中保留了公开依赖源镜像配置，例如 Go/Python/Composer/npm 相关镜像；如果使用者所在网络无法直接访问 GitHub、系统包源或语言包源，可以在本地构建时按标准 Docker/Compose 方式临时传入代理，而不是修改数据集字段。

示例：

```bash
HTTP_PROXY=http://127.0.0.1:7890 \
HTTPS_PROXY=http://127.0.0.1:7890 \
http_proxy=http://127.0.0.1:7890 \
https_proxy=http://127.0.0.1:7890 \
bash docker-env/build-vul.sh
```

进入任意 CVE 目录后执行：

```bash
cd <project>/findings/<CVE-ID>
```

构建漏洞版：

```bash
bash docker-env/build-vul.sh
```

等价 Docker Compose 命令：

```bash
docker compose --env-file docker-env/.env build vul
```

进入漏洞版容器：

```bash
bash docker-env/run-vul.sh bash
```

等价 Docker Compose 命令：

```bash
docker compose --env-file docker-env/.env run --rm vul bash
```

构建和进入修复版：

```bash
bash docker-env/build-fix.sh
bash docker-env/run-fix.sh bash
```

等价 Docker Compose 命令：

```bash
docker compose --env-file docker-env/.env --profile fix build fix
docker compose --env-file docker-env/.env --profile fix run --rm fix bash
```

注意：所有 Compose 命令都必须在 CVE 根目录执行，并加载 `--env-file docker-env/.env`。否则镜像名、源码 URL、工作目录等变量会为空。

## 样例 Case 快速索引

| CVE | 项目 | 漏洞类型 | 主要验证入口 |
| --- | --- | --- | --- |
| `CVE-2026-27587` | `caddy` | percent-escape path matcher 绕过 | `go test ./verify_requirements/tests` |
| `CVE-2026-27588` | `caddy` | 大 Host 列表大小写匹配绕过 | `go test ./verify_requirements/tests -run TestHostMatcherLargeListBecomesCaseSensitive -count=1` |
| `CVE-2026-30851` | `caddy` | `forward_auth copy_headers` 授权绕过 | `go test ./verify_requirements/tests -run TestForwardAuthAllowsClientHeaders -count=1` |
| `CVE-2025-30207` | `cms` | Kirby PHP built-in server 路径穿越 | `bash verify_requirements/tests/test_path_traversal.sh` |
| `CVE-2025-31493` | `cms` | Kirby dynamic collection 路径穿越 | `php verify_requirements/tests/test_collection_traversal.php` |
| `CVE-2025-35939` | `cms` | Craft CMS session return URL 写入 | `php verify_requirements/tests/traffic_session_return_url.php` |
| `CVE-2026-22849` | `saleor` | rich text 存储型 XSS | `bash /workspace/verify_requirements/tests/run_traffic_test.sh` |
| `CVE-2026-24136` | `saleor` | GraphQL order IDOR | `bash /workspace/verify_requirements/tests/run_traffic_test.sh` |

表中的“主要验证入口”是容器内测试命令。更准确的预期结果和容器注意事项请优先参考每个 CVE 目录下的 `verify_requirements/verification_result.json`、`deployment.json` 与实际测试脚本；其中 `tests[].run_in_vul_container` 是从 CVE 根目录直接执行的推荐命令。

## 推荐训练用法

漏洞定位任务：

1. 输入 `project_meta.json`、`verify_requirements/one_issue.txt`、`verify_requirements/sast_standardized.json` 和源码上下文。
2. 以 `sast_standardized.json` 中的 `vul_pos`、`dataflow`、`vuln_type` 作为监督标签。

漏洞解释任务：

1. 输入 `description`、`vul_pos` 和测试脚本。
2. 以 `root_cause.md` 或 `root_cause_zh.md` 作为目标答案。

修复建议任务：

1. 输入 `description`、`dataflow`、`verification_result.json`。
2. 以 `fix.md`、`fix_zh.md` 和 `recommendation` 作为目标答案。

验证执行任务：

1. 进入对应 CVE 目录。
2. 构建 `vul` 镜像。
3. 根据 `verification_result.json` 执行 `verify_requirements/tests/` 中的测试。
4. 如需对比修复效果，构建 `fix` 镜像并重复验证。
