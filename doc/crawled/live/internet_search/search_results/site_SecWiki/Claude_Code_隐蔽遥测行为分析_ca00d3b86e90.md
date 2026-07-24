# Claude Code 隐蔽遥测行为分析

### 来源信息
- **URL**: https://mp.weixin.qq.com/s/6F4JPNaS0KcrjUVxmXP7Jw
- **来源站点**: SecWiki
- **页面抓取**: 成功

### 页面正文
今天刷到一篇文章说 Claude Code 会检测用户是否使用代理和所在时区，然后修改 system prompt 中的几个字符偷偷上报这些信息。原帖在 Reddit，标题是“Anthropic embedded spyware in Claude Code — and attempted to hide it from you”。以下是我的验证过程。我的环境是 Windows 11，Claude Code 版本为 2.1.196，通过 npm 安装。
Claude Code 是通过 Bun 打包为二进制的，因此首先要做的是把二进制还原为 javascript 代码。我使用的工具来源于 Github Gist（TheCjw/extract_bun.js），代码如下：
extract_bun.js
复制代码 隐藏代码#!/usr/bin/env bun
import { mkdirSync, readFileSync, writeFileSync } from"node:fs";
import path from"node:path";
constTRAILER = Buffer.from("\n---- Bun! ----\n");
constBUN_SECTION_NAME = ".bun";
constOFFSET_STRUCT_SIZE = 32;
constMODULE_RECORD_SIZE = 52;
constENCODINGS = {
0: "binary",
1: "latin1",
2: "utf8",
};
constMODULE_FORMATS = {
0: "none",
1: "esm",
2: "cjs",
};
constSIDES = {
0: "server",
1: "client",
};
constLOADERS = {
0: "jsx",
1: "js",
2: "ts",
3: "tsx",
4: "css",
5: "file",
6: "json",
7: "jsonc",
8: "toml",
9: "wasm",
10: "napi",
11: "base64",
12: "dataurl",
13: "text",
14: "bunsh",
15: "sqlite",
16: "sqlite_embedded",
17: "html",
18: "yaml",
19: "json5",
20: "md",
};
functiondie(message) {
thrownewError(`error: ${message}`);
}
functionreadUInt64LE(buffer, offset, what) {
const value = buffer.readBigUInt64LE(offset);
if (value > BigInt(Number.MAX_SAFE_INTEGER)) {
die(`${what} exceeds JavaScript safe integer range: ${value}`);
}
returnNumber(value);
}
functioncheckedSlice(buffer, offset, size, what) {
if (offset < 0 || size < 0 || offset + size > buffer.length) {
die(
`${what} out of bounds: offset=${offset} size=${size} blob_size=${buffer.length}`,
);
}
return buffer.subarray(offset, offset + size);
}
functionreadCString(buffer, offset, size, what) {
const data = checkedSlice(buffer, offset, size, what);
return data.length > 0 && data[data.length - 1] === 0
? data.subarray(0, -1)
: data;
}
functiondecodeUtf8(buffer) {
return buffer.toString("utf8").replace(/\u0000+$/u, "");
}
constELF_MAGIC = Buffer.from([0x7f, 0x45, 0x4c, 0x46]);
// PE field offsets
constPE_OFFSET_PTR = 0x3c; // DOS header: offset of PE signature
constPE_NUM_SECTIONS_OFF = 0x06; // COFF header: NumberOfSections (relative to PE sig)
constPE_OPT_HDR_SIZE_OFF = 0x14; // COFF header: SizeOfOptionalHeader (relative to PE sig)
constPE_COFF_HDR_SIZE = 0x18; // size of COFF header (PE sig + COFF fields)
constPE_OPT_MAGIC_OFF = 0x18; // Optional header Magic (relative to PE sig)
constPE_OPT_MAGIC_PE32P = 0x20b; // PE32+ (64-bit)
constPE_SECTION_ENTRY_SIZE = 0x28; // 40 bytes per section header entry
constPE_SECT_RAW_SIZE_OFF = 0x10; // SizeOfRawData (relative to section entry)
constPE_SECT_RAW_OFF_OFF = 0x14; // PointerToRawData (relative to section entry)
constPE_SECT_NAME_LEN = 0x08; // section name field length
// ELF field offsets
constELF_EI_CLASS = 0x04; // e_ident[EI_CLASS]: 1=32-bit, 2=64-bit
constELF_EI_DATA = 0x05; // e_ident[EI_DATA]: 1=LE, 2=BE
constELF_CLASS_64 = 0x02;
constELF_DATA_LE = 0x01;
// Elf64_Ehdr field offsets
constELF64_E_SHOFF = 0x28; // u64
constELF64_E_SHENTSIZE = 0x3a; // u16
constELF64_E_SHNUM = 0x3c; // u16
constELF64_E_SHSTRNDX = 0x3e; // u16
// Elf32_Ehdr field offsets
constELF32_E_SHOFF = 0x20; // u32
constELF32_E_SHENTSIZE = 0x2e; // u16
constELF32_E_SHNUM = 0x30; // u16
constELF32_E_SHSTRNDX = 0x32; // u16
// Elf64_Shdr field offsets (relative to shdr entry)
constELF64_SH_NAME = 0x00; // u32
constELF64_SH_OFFSET = 0x18; // u64
constELF64_SH_SIZE = 0x20; // u64
// Elf32_Shdr field offsets (relative to shdr entry)
constELF32_SH_NAME = 0x00; // u32
constELF32_SH_OFFSET = 0x10; // u32
constELF32_SH_SIZE = 0x14; // u32
// Mach-O magic values (read as big-endian u32)
constMH_MAGIC = 0xfeedface; // 32-bit LE
constMH_CIGAM = 0xcefaedfe; // 32-bit BE
constMH_MAGIC_64 = 0xfeedfacf; // 64-bit LE
constMH_CIGAM_64 = 0xcffaedfe; // 64-bit BE
constFAT_MAGIC = 0xcafebabe;
constFAT_CIGAM = 0xbebafeca;
constFAT_MAGIC_64 = 0xcafebabf;
constFAT_CIGAM_64 = 0xbfbafeca;
// fat_header field offsets (always BE)
constFAT_NFAT_ARCH_OFF = 0x04; // u32
constFAT_ARCH_ENTRY_SIZE = 0x14; // 20 bytes
constFAT_ARCH_TABLE_OFF = 0x08; // first fat_arch
constFAT_ARCH_OFFSET_OFF = 0x08; // offset field within fat_arch entry
// mach_header field offsets
constMACH_NCMDS_OFF = 0x10; // u32 (relative to thin header base)
constMACH_HDR_SIZE_32 = 0x1c; // 28 bytes
constMACH_HDR_SIZE_64 = 0x20; // 32 bytes
constLC_SEGMENT = 0x01;
constLC_SEGMENT_64 = 0x19;
constLC_CMD_OFF = 0x00; // u32 cmd
constLC_CMDSIZE_OFF = 0x04; // u32 cmdsize
constLC_SEGNAME_OFF = 0x08; // char[16]
constLC_SEGNAME_LEN = 0x10;
// segment_command (32-bit) field offsets
constSEG32_NSECTS_OFF = 0x30; // u32
constSEG32_SECTS_OFF = 0x38; // first section entry
constSECT32_ENTRY_SIZE = 0x44; // 68 bytes
constSECT32_SECTNAME_OFF = 0x00; // char[16]
constSECT32_SIZE_OFF = 0x1c; // u32
constSECT32_OFFSET_OFF = 0x20; // u32
// segment_command_64 field offsets
constSEG64_NSECTS_OFF = 0x40; // u32
constSEG64_SECTS_OFF = 0x48; // first section_64 entry
constSECT64_ENTRY_SIZE = 0x50; // 80 bytes
constSECT64_SECTNAME_OFF = 0x00; // char[16]
constSECT64_SIZE_OFF = 0x28; // u64
constSECT64_OFFSET_OFF = 0x30; // u32
functionfindBunElfSection(buf) {
if (buf.length < 0x40) die("ELF file too small");
const is64 = buf[ELF_EI_CLASS] === ELF_CLASS_64;
if (!is64) die("ELF: only 64-bit executables are supported");
const le = buf[ELF_EI_DATA] === ELF_DATA_LE;
const dv = newDataView(buf.buffer, buf.byteOffset, buf.byteLength);
constr16 = (o) => dv.getUint16(o, le);
constr32 = (o) => dv.getUint32(o, le);
constr64 = (o) => {
const lo = le ? dv.getUint32(o, true) : dv.getUint32(o + 4, false);
const hi = le ? dv.getUint32(o + 4, true) : dv.getUint32(o, false);
return hi * 0x100000000 + lo;
};
const shoff = r64(ELF64_E_SHOFF);
const shentsize = r16(ELF64_E_SHENTSIZE);
const shnum = r16(ELF64_E_SHNUM);
const shstrndx = r16(ELF64_E_SHSTRNDX);
checkedSlice(buf, shoff, shnum * shentsize, "ELF section header table");
const shstrOff = shoff + shstrndx * shentsize;
const shstrFileOff = r64(shstrOff + ELF64_SH_OFFSET);
const shstrSize = r64(shstrOff + ELF64_SH_SIZE);
checkedSlice(buf, shstrFileOff, shstrSize, "ELF shstrtab");
const matches = [];
for (let i = 0; i < shnum; i++) {
const shdrOff = shoff + i * shentsize;
const nameIdx = r32(shdrOff + ELF64_SH_NAME);
let nameEnd = shstrFileOff + nameIdx;
while (nameEnd < buf.length && buf[nameEnd] !== 0) nameEnd++;
const name = buf.toString("ascii", shstrFileOff + nameIdx, nameEnd);
if (name === ".bun") {
const rawOffset = r64(shdrOff + ELF64_SH_OFFSET);
const rawSize = r64(shdrOff + ELF64_SH_SIZE);
checkedSlice(buf, rawOffset, rawSize, ".bun section raw data");
matches.push({
format: "ELF",
name,
rawOffset,
rawSize,
data: buf.subarray(rawOffset, rawOffset + rawSize),
});
}
}
if (matches.length === 0) die("ELF has no .bun section");
if (matches.length > 1) die("ELF has multiple .bun sections");
return matches[0];
}
functionparseThinMacho(buf, base) {
if (buf.length < base + MACH_HDR_SIZE_32) die("Mach-O thin header too small");
const magic = buf.readUInt32LE(base);
const be = magic === MH_CIGAM || magic === MH_CIGAM_64;
const is64 = magic === MH_MAGIC_64 || magic === MH_CIGAM_64;
if (!is64) die("Mach-O: only 64-bit executables are supported");
constr32 = (o) => (be ? buf.readUInt32BE(o) : buf.readUInt32LE(o));
const ncmds = r32(base + MACH_NCMDS_OFF);
const hdrSize = MACH_HDR_SIZE_64;
const matches = [];
let off = base + hdrSize;
for (let i = 0; i < ncmds; i++) {
const cmd = r32(off + LC_CMD_OFF);
const cmdsize = r32(off + LC_CMDSIZE_OFF);
if (cmdsize < 8) die("Mach-O load command size too small");
if (cmd === LC_SEGMENT_64) {
const segname = buf
.toString(
"ascii",
off + LC_SEGNAME_OFF,
off + LC_SEGNAME_OFF + LC_SEGNAME_LEN,
)
.replace(/\0+$/, "");
if (segname === "__BUN") {
const nsects = r32(off + SEG64_NSECTS_OFF);
for (let j = 0; j < nsects; j++) {
const s = off + SEG64_SECTS_OFF + j * SECT64_ENTRY_SIZE;
const sectname = buf
.toString(
"ascii",
s + SECT64_SECTNAME_OFF,
s + SECT64_SECTNAME_OFF + LC_SEGNAME_LEN,
)
.replace(/\0+$/, "");
if (sectname === "__bun") {
const rawSize = Number(buf.readBigUInt64LE(s + SECT64_SIZE_OFF));
const rawOffset = be
? buf.readUInt32BE(s + SECT64_OFFSET_OFF)
: buf.readUInt32LE(s + SECT64_OFFSET_OFF);
matches.push({ rawOffset, rawSize });
}
}
}
}
off += cmdsize;
}
return matches;
}
functionfindBunMachoSection(buf) {
const magic = buf.readUInt32BE(0);
constFAT_SET = newSet([FAT_MAGIC, FAT_CIGAM, FAT_MAGIC_64, FAT_CIGAM_64]);
const allMatches = [];
if (FAT_SET.has(magic)) {
const nfat = buf.readUInt32BE(FAT_NFAT_ARCH_OFF);
for (let i = 0; i < nfat; i++) {
const archEntry = FAT_ARCH_TABLE_OFF + i * FAT_ARCH_ENTRY_SIZE;
const archFileOff = buf.readUInt32BE(archEntry + FAT_ARCH_OFFSET_OFF);
allMatches.push(...parseThinMacho(buf, archFileOff));
}
} else {
allMatches.push(...parseThinMacho(buf, 0));
}
if (allMatches.length === 0) die("Mach-O has no __BUN,__bun section");
if (allMatches.length > 1) die("Mach-O has multiple __BUN,__bun sections");
const { rawOffset, rawSize } = allMatches[0];
checkedSlice(buf, rawOffset, rawSize, "__BUN,__bun section raw data");
return {
format: "Mach-O",
name: "__BUN,__bun",
rawOffset,
rawSize,
data: buf.subarray(rawOffset, rawOffset + rawSize),
};
}
functionfindBunPeSection(buf) {
if (buf.length < 0x40 || buf.toString("ascii", 0, 2) !== "MZ") {
die("invalid PE file: missing MZ header");
}
const peOffset = buf.readUInt32LE(PE_OFFSET_PTR);
checkedSlice(buf, peOffset, PE_COFF_HDR_SIZE, "PE header");
if (buf.toString("ascii", peOffset, peOffset + 4) !== "PE\0\0") {
die("invalid PE file: missing PE signature");
}
const optMagic = buf.readUInt16LE(peOffset + PE_OPT_MAGIC_OFF);
if (optMagic !== PE_OPT_MAGIC_PE32P) {
die(
`PE: only 64-bit (PE32+) executables are supported (optional header magic: 0x${optMagic.toString(16)})`,
);
}
const numberOfSections = buf.readUInt16LE(peOffset + PE_NUM_SECTIONS_OFF);
const sizeOfOptHdr = buf.readUInt16LE(peOffset + PE_OPT_HDR_SIZE_OFF);
const sectionTableOffset = peOffset + PE_COFF_HDR_SIZE + sizeOfOptHdr;
checkedSlice(
buf,
sectionTableOffset,
numberOfSections * PE_SECTION_ENTRY_SIZE,
"section table",
);
const matches = [];
for (let index = 0; index < numberOfSections; index++) {
const sectionOffset = sectionTableOffset + index * PE_SECTION_ENTRY_SIZE;
const rawName = buf.subarray(
sectionOffset,
sectionOffset + PE_SECT_NAME_LEN,
);
const nulIndex = rawName.indexOf(0);
const name = rawName
.subarray(0, nulIndex === -1 ? rawName.length : nulIndex)
.toString("ascii");
const rawSize = buf.readUInt32LE(sectionOffset + PE_SECT_RAW_SIZE_OFF);
const rawOffset = buf.readUInt32LE(sectionOffset + PE_SECT_RAW_OFF_OFF);
if (name === BUN_SECTION_NAME) {
checkedSlice(buf, rawOffset, rawSize, ".bun section raw data");
matches.push({
format: "PE",
name,
rawOffset,
rawSize,
data: buf.subarray(rawOffset, rawOffset + rawSize),
});
}
}
if (matches.length === 0) die("PE has no .bun section");
if (matches.length > 1) die("PE has multiple .bun sections");
return matches[0];
}
constMACHO_MAGIC_SET = newSet([
FAT_MAGIC,
FAT_CIGAM,
FAT_MAGIC_64,
FAT_CIGAM_64,
MH_MAGIC,
MH_CIGAM,
MH_MAGIC_64,
MH_CIGAM_64,
]);
functionfindBunSection(buf) {
if (buf.length < 4) die("file too small to determine format");
const magic = buf.readUInt32BE(0);
if (buf.subarray(0, 4).equals(ELF_MAGIC)) returnfindBunElfSection(buf);
if (MACHO_MAGIC_SET.has(magic)) returnfindBunMachoSection(buf);
returnfindBunPeSection(buf);
}
functionparsePayload(sectionData) {
if (sectionData.length < 8) {
die(".bun section is too small for length prefix");
}
const payloadSize = readUInt64LE(sectionData, 0, ".bun payload length");
if (payloadSize + 8 > sectionData.length) {
die(
`.bun payload length exceeds raw section: payload=${payloadSize} raw=${sectionData.length}`,
);
}
const payload = sectionData.subarray(8, 8 + payloadSize);
if (payload.length < OFFSET_STRUCT_SIZE + TRAILER.length) {
die(".bun payload is too small for Offsets + trailer");
}
if (!payload.subarray(payload.length - TRAILER.length).equals(TRAILER)) {
die(".bun payload trailer mismatch");
}
return { payloadSize, payload };
}
functionparseOffsets(payload) {
const start = payload.length - TRAILER.length - OFFSET_STRUCT_SIZE;
const offsets = {
byte_count: readUInt64LE(payload, start, "byte_count"),
modules_offset: payload.readUInt32LE(start + 8),
modules_size: payload.readUInt32LE(start + 12),
entry_point_id: payload.readUInt32LE(start + 16),
compile_exec_argv_offset: payload.readUInt32LE(start + 20),
compile_exec_argv_size: payload.readUInt32LE(start + 24),
flags: payload.readUInt32LE(start + 28),
};
if (offsets.byte_count > payload.length) {
die(
`byte_count exceeds payload: ${offsets.byte_count} > ${payload.length}`,
);
}
if (offsets.modules_size % MODULE_RECORD_SIZE !== 0) {
die(
`modules table size is not a multiple of ${MODULE_RECORD_SIZE}: ${offsets.modules_size}`,
);
}
checkedSlice(
payload,
offsets.modules_offset,
offsets.modules_size,
"modules table",
);
checkedSlice(
payload,
offsets.compile_exec_argv_offset,
offsets.compile_exec_argv_size,
"compile_exec_argv",
);
return offsets;
}
functionreadPointerPairs(record) {
const pairs = [];
for (let offset = 0; offset < 48; offset += 8) {
pairs.push([record.readUInt32LE(offset), record.readUInt32LE(offset + 4)]);
}
return pairs;
}
functionparseFiles(payload, offsets, sectionFileOffset) {
const files = [];
const count = offsets.modules_size / MODULE_RECORD_SIZE;
if (offsets.entry_point_id >= count) {
die(`entry_point_id out of range: ${offsets.entry_point_id} >= ${count}`);
}
const table = checkedSlice(
payload,
offsets.modules_offset,
offsets.modules_size,
"modules table",
);
for (let index = 0; index < count; index += 1) {
const record = table.subarray(
index * MODULE_RECORD_SIZE,
(index + 1) * MODULE_RECORD_SIZE,
);
const pointers = readPointerPairs(record);
const encodingId = record.readUInt8(48);
const loaderId = record.readUInt8(49);
const moduleFormatId = record.readUInt8(50);
const sideId = record.readUInt8(51);
const [nameOffset, nameSize] = pointers[0];
const [contentOffset, contentSize] = pointers[1];
const [sourcemapOffset, sourcemapSize] = pointers[2];
const [bytecodeOffset, bytecodeSize] = pointers[3];
const [moduleInfoOffset, moduleInfoSize] = pointers[4];
const [bytecodeOriginPathOffset, bytecodeOriginPathSize] = pointers[5];
const name = decodeUtf8(
readCString(payload, nameOffset, nameSize, `module[${index}].name`),
);
checkedSlice(
payload,
contentOffset,
contentSize,
`module[${index}].contents`,
);
if (sourcemapSize) {
checkedSlice(
payload,
sourcemapOffset,
sourcemapSize,
`module[${index}].sourcemap`,
);
}
if (bytecodeSize) {
checkedSlice(
payload,
bytecodeOffset,
bytecodeSize,
`module[${index}].bytecode`,
);
}
if (moduleInfoSize) {
checkedSlice(
payload,
moduleInfoOffset,
moduleInfoSize,
`module[${index}].module_info`,
);
}
let bytecodeOriginPath = "";
if (bytecodeOriginPathSize) {
bytecodeOriginPath = decodeUtf8(
readCString(
payload,
bytecodeOriginPathOffset,
bytecodeOriginPathSize,
`module[${index}].bytecode_origin_path`,
),
);
}
files.push({
index,
entry: index === offsets.entry_point_id,
name,
content_payload_offset: contentOffset,
content_file_offset: sectionFileOffset + 8 + contentOffset,
content_size: contentSize,
loader: LOADERS[loaderId] ?? `unknown(${loaderId})`,
encoding: ENCODINGS[encodingId] ?? `unknown(${encodingId})`,
module_format:
MODULE_FORMATS[moduleFormatId] ?? `unknown(${moduleFormatId})`,
side: SIDES[sideId] ?? `unknown(${sideId})`,
bytecode_payload_offset: bytecodeSize ? bytecodeOffset : null,
bytecode_size: bytecodeSize,
module_info_payload_offset: moduleInfoSize ? moduleInfoOffset : null,
module_info_size: moduleInfoSize,
bytecode_origin_path: bytecodeOriginPath,
sourcemap_payload_offset: sourcemapSize ? sourcemapOffset : null,
sourcemap_size: sourcemapSize,
});
}
return files;
}
functioniterLimited(files, limit) {
return limit == null ? files : files.slice(0, limit);
}
constBUN_VIRTUAL_ROOTS = newSet(["~BUN", "$bunfs"]);
functionoutputRelativePath(name) {
const normalized = name.replaceAll("\\", "/");
let parts = normalized
.split("/")
.filter((p) => p !== "" && p !== "." && p !== ".." && !p.endsWith(":"));
if (parts.length > 0 && BUN_VIRTUAL_ROOTS.has(parts[0])) {
parts = parts.slice(1);
if (parts.length > 0 && parts[0] === "root") parts = parts.slice(1);
}
return parts.length === 0 ? "unnamed" : path.join(...parts);
}
functionextractFiles(payload, files, outputDir) {
const extracted = [];
mkdirSync(outputDir, { recursive: true });
const resolvedOut = path.resolve(outputDir);
for (const file of files) {
const relativePath = outputRelativePath(file.name);
const destination = path.join(outputDir, relativePath);
const resolved = path.resolve(destination);
if (
resolved !== resolvedOut &&
!resolved.startsWith(resolvedOut + path.sep)
) {
die(
`refusing to write outside output dir: ${JSON.stringify(file.name)} -> ${destination}`,
);
}
mkdirSync(path.dirname(destination), { recursive: true });
const content = checkedSlice(
payload,
file.content_payload_offset,
file.content_size,
`module[${file.index}].contents`,
);
writeFileSync(destination, content);
extracted.push({
index: file.index,
entry: file.entry,
original_name: file.name,
saved_path: destination,
content_payload_offset: file.content_payload_offset,
content_file_offset: file.content_file_offset,
content_size: file.content_size,
loader: file.loader,
side: file.side,
bytecode_size: file.bytecode_size,
module_info_size: file.module_info_size,
bytecode_origin_path: file.bytecode_origin_path,
});
}
const manifestPath = path.join(outputDir, "manifest.json");
writeFileSync(
manifestPath,
`${JSON.stringify(extracted, null, 2)}\n`,
"utf8",
);
return extracted;
}
functionprintText(exePath, section, payloadSize, offsets, files, limit) {
console.log(`exe: ${exePath}`);
console.log(
`${section.format}${section.name}: raw_offset=0x${section.rawOffset.toString(16)} raw_size=${section.rawSize} payload_size=${payloadSize}`,
);
console.log(
`graph: byte_count=${offsets.byte_count} modules_offset=${offsets.modules_offset} modules_size=${offsets.modules_size} module_count=${files.length} entry_point_id=${offsets.entry_point_id} flags=0x${offsets.flags.toString(16)}`,
);
console.log(
"index\tentry\tloader\tside\tcontent_payload_offset\tcontent_file_offset\tcontent_size\tname",
);
for (const file ofiterLimited(files, limit)) {
console.log(
`${file.index}\t${Number(file.entry)}\t${file.loader}\t${file.side}\t${file.content_payload_offset}\t0x${file.content_file_offset.toString(16)}\t${file.content_size}\t${file.name}`,
);
}
if (limit != null && files.length > limit) {
console.log(
`... ${files.length - limit} more file(s) omitted; use --limit 0 for all`,
);
}
}
functionparseLimit(value) {
const n = Number.parseInt(value, 10);
if (!Number.isInteger(n) || n < 0)
die("--limit must be a non-negative integer");
return n === 0 ? null : n;
}
functionparseSubArgs(argv, validFlags) {
// Returns { exe, flags... }; exe is required positional arg
const result = { exe: null };
for (let i = 0; i < argv.length; i++) {
const arg = argv[i];
if (arg === "-h" || arg === "--help") {
result._help = true;
return result;
}
const flag = validFlags.find(
(f) => arg === f.flag || (f.short && arg === f.short),
);
if (flag) {
if (flag.takesValue) {
i++;
if (i >= argv.length) die(`${arg} requires a value`);
result[flag.key] = flag.parse ? flag.parse(argv[i]) : argv[i];
} else {
result[flag.key] = true;
}
} elseif (arg.startsWith("-")) {
die(`unknown option: ${arg}`);
} elseif (result.exe === null) {
result.exe = arg;
} else {
die(`unexpected positional argument: ${arg}`);
}
}
return result;
}
functionprintHelp() {
console.log(`Usage: bun extract_bun.js <command> EXE [options]
Parse Bun build --compile embedded files from PE/ELF/Mach-O executables.
Commands:
print EXE Print embedded module graph information
extract EXE Extract embedded files and write manifest.json
Options for print:
--limit N Maximum records to print; 0 means no limit (default: all)
--json Emit JSON instead of TSV-like text
-h, --help Show this help message
Options for extract:
-o, --output DIR Output directory (required)
-h, --help Show this help message`);
}
functionprintExtractedText(
exePath,
section,
payloadSize,
offsets,
files,
extracted,
outputDir,
) {
console.log(`exe: ${exePath}`);
console.log(
`${section.format}${section.name}: raw_offset=0x${section.rawOffset.toString(16)} raw_size=${section.rawSize} payload_size=${payloadSize}`,
);
console.log(
`graph: module_count=${files.length} entry_point_id=${offsets.entry_point_id} flags=0x${offsets.flags.toString(16)}`,
);
console.log("index\tentry\tloader\tside\tsize\tsaved_path\toriginal_name");
for (const file of extracted) {
console.log(
`${file.index}\t${Number(file.entry)}\t${file.loader}\t${file.side}\t${file.content_size}\t${file.saved_path}\t${file.original_name}`,
);
}
console.log(`extracted: ${extracted.length} file(s) -> ${outputDir}`);
console.log(`manifest: ${path.join(outputDir, "manifest.json")}`);
}
functionmain(argv = process.argv.slice(2)) {
const [subcmd, ...rest] = argv;
if (!subcmd || subcmd === "-h" || subcmd === "--help") {
printHelp();
process.exit(0);
}
if (subcmd === "print") {
const args = parseSubArgs(rest, [
{ flag: "--limit", key: "limit", takesValue: true, parse: parseLimit },
{ flag: "--json", key: "json" },
]);
if (args._help) {
console.log(
`Usage: bun extract_bun.js print EXE [--limit N] [--json] [-h]`,
);
process.exit(0);
}
if (!args.exe) die("print requires an EXE argument");
const buf = readFileSync(args.exe);
const section = findBunSection(buf);
const { payloadSize, payload } = parsePayload(section.data);
const offsets = parseOffsets(payload);
const files = parseFiles(payload, offsets, section.rawOffset);
const limit = args.limit ?? null;
if (args.json) {
console.log(
JSON.stringify(
{
exe: args.exe,
bun_section: {
format: section.format,
name: section.name,
raw_offset: section.rawOffset,
raw_size: section.rawSize,
payload_size: payloadSize,
},
graph: { ...offsets, module_count: files.length },
files: iterLimited(files, limit),
omitted: limit == null ? 0 : Math.max(0, files.length - limit),
extracted: [],
},
null,
2,
),
);
} else {
printText(args.exe, section, payloadSize, offsets, files, limit);
}
} elseif (subcmd === "extract") {
const args = parseSubArgs(rest, [
{ flag: "--output", short: "-o", key: "output", takesValue: true },
]);
if (args._help) {
console.log(`Usage: bun extract_bun.js extract EXE -o DIR [-h]`);
process.exit(0);
}
if (!args.exe) die("extract requires an EXE argument");
if (!args.output) die("extract requires -o/--output DIR");
const buf = readFileSync(args.exe);
const section = findBunSection(buf);
const { payloadSize, payload } = parsePayload(section.data);
const offsets = parseOffsets(payload);
const files = parseFiles(payload, offsets, section.rawOffset);
const extracted = extractFiles(payload, files, args.output);
printExtractedText(
args.exe,
section,
payloadSize,
offsets,
files,
extracted,
args.output,
);
} else {
die(
`unknown command: ${subcmd}\nRun 'bun extract_bun.js --help' for usage.`,
);
}
}
try {
main();
} catch (error) {
console.error(error.message);
process.exit(1);
}
虽然作者说要用 Bun 运行，但实测用 Node 也不影响。运行以下命令即可把 claude.exe 解包为 js 代码：
复制代码 隐藏代码bun extract_bun.js extract claude.exe -o extract
入口模块位于 src/entrypoints/cli.js。可以先把这个文件格式化一下方便后续查看。
复制代码 隐藏代码// cli.js:114617
functionArt() {
let e = process.env.ANTHROPIC_BASE_URL;
if (!e) return !0; // 未设代理 → 视为"第一方"
returnTrt(e); // 代理主机为 api.anthropic.com 时返回 true
}
// cli.js:114622
functionTrt(e) {
try {
return ["api.anthropic.com"].includes(newURL(e).host);
} catch {
return !1;
}
}
Art() 在 ANTHROPIC_BASE_URL 未设置或指向 api.anthropic.com 时返回 true。这是后续检测的前置判断，只有当该函数返回 false 时才会做后续的域名和时区检测。
复制代码 隐藏代码// cli.js:274138
functionWup() {
if (Art()) returnnull; // 直连/官方端点 → 不做任何检测
let e = jup(), // 取 ANTHROPIC_BASE_URL 的 hostname
t = tkt(), // 取系统时区
n = t === "Asia/Shanghai" || t === "Asia/Urumqi";
if (!e) return { known: !1, labKw: !1, cnTZ: n, host: null };
return {
known: Fup().some((r) => e === r || e.endsWith("." + r)), // 命中域名白名单
labKw: Bup().some((r) => e.includes(r)), // 命中 AI 实验室关键词
cnTZ: n,
host: e,
};
}
// cli.js:274129 —— jup() 的实现
functionjup() {
let e = process.env.ANTHROPIC_BASE_URL;
if (!e) returnnull;
try {
returnnewURL(e).hostname.toLowerCase();
} catch {
returnnull;
}
}
// cli.js:12714 —— tkt() 的实现
functiontkt() {
if (!fTr) fTr = Intl.DateTimeFormat().resolvedOptions().timeZone;
return fTr;
}
核心检测逻辑在 Wup()。如果发现用户没走官方端点，就会进一步检测域名和时区，最后返回包含 4 个字段的检测结果：
knownANTHROPIC_BASE_URL 的域名是否命中域名白名单labKwANTHROPIC_BASE_URL 的域名是否命中 AI 实验室关键词cnTZhostANTHROPIC_BASE_URL 的域名复制代码 隐藏代码// cli.js:274151
functionVup(e, t) {
// e = known(域名命中) t = labKw(ai实验室命中)
if (!e && !t) return"'"; // 都不命中 → 普通 ASCII 撇号 U+0027
if (e && !t) return"\u2019"; // 仅域名 → ’ RIGHT SINGLE QUOTATION MARK
if (!e && t) return"\u02BC"; // 仅实验室 → ʼ MODIFIER LETTER APOSTROPHE
return"\u02B9"; // 都命中 → ʹ MODIFIER LETTER PRIME
}
// cli.js:274157
functionLla(e) {
// e = 当前日期 "YYYY-MM-DD"
let t = Wup(),
n = Vup(t?.known ?? !1, t?.labKw ?? !1),
r = t?.cnTZ ? e.replaceAll("-", "/") : e; // 中国时区 → YYYY/MM/DD
return`Today${n}s date is ${r}.`;
}
Claude Code 的系统提示词中有一段 Today's date is 当前日期.，而这两个函数会修改其中的撇号和日期格式。
正常情况下，当前日期应该是 YYYY-MM-DD 的格式，但如果之前的检测发现用户是中国时区，就会把 - 替换成 /。此外还会根据是否命中域名白名单（known）和是否命中 AI 实验室关键词（labKw）来选择 Today's 中的撇号，一共有 4 中情况：
| ' | |||
| ’ | |||
| ʼ | |||
| ʹ | 
这 4 种撇号在视觉上差别很小，因此用户很难发现异常。
复制代码 隐藏代码// cli.js:274163
varNup = 91,
$up = "ODV3KDo1MC46...", // 域名白名单（base64+XOR91）
Uup = "Pz4+Kyg+PjB3...", // AI 实验室关键词
Fup,
Bup;
varOla = E(() => {
ea();
H0();
Ms();
((Fup = wn(() =>Mla($up))), // 惰性解码并缓存
(Bup = wn(() =>Mla(Uup))));
});
// cli.js:274123
functionMla(e) {
let t = Buffer.from(e, "base64"),
n = "";
for (let r of t) n += String.fromCharCode(r ^ Nup); // 逐字节 XOR 0x5B(=91)
return n.split(",");
}
之前提到的域名白名单和 AI 实验室关键词是被加密保存的。解密方式是先 Base64 解码，然后逐字节异或一个 key 91。我们可以写个简单的脚本来解密：
复制代码 隐藏代码constNup = 91;
functionMla(e) {
let t = Buffer.from(e, "base64"),
n = "";
for (let r of t) n += String.fromCharCode(r ^ Nup);
return n.split(",");
}
const $up =
"ODV3KDo1MC46MnU4NDZ3NT4vPjooPnU4NDZ3am1odTg0Nnc5OjI/LnYyNS91ODQ2dzk6Mj8udTg0Nnc6NzI5Ojk6djI1OHU4NDZ3OjcyKzoidTg0Nnc6NS88KTQuK3YyNTh1ODV3MC46MigzNC51ODQ2dzkiLz4/OjU4PnU1Pi93IzI6NDM0NTwoMy51ODQ2dzgvKTIrODQpK3U4NDZ3MT91ODQ2dzE/ODc0Lj91ODQ2dzkyNzI5MjcydTg0dzI9NyIvPjB1ODQ2dygvPis9LjV2MjU4dTg0Nnc6NzIiLjU4KHU4NDZ3ODV2KDM6NTwzOjJ1PTg6Kyt1KS41dzg1djk+MjEyNTx1PTg6Kyt1KS41dyM6NjI1MjZ1ODQ2dzY0NDUoMzQvdToydzo1Iik0Li8+KXUvNCt3Kzo4MCI6KzJ1ODQ2dzoyODQ/PjYyKSk0KXU4NDZ3OjI8NDg0Pz51ODQ2dzM0NTwoMzo1dTg0NncyLDM6Nz44NzQuP3U4NDZ3PzM4ND8+KXU1Pi93Nz42NDU8Ky91LzQrdyEzMjMuMjorMnUvNCt3MjUvKDI8dTU+L3czMjwzdj0yLT52OjJ1IyIhdzg3NC4/KCw6InU1Pi93byg6KzJ1ODQ2d25pYmJtanU4NDZ3Y2NiYm11ODc0Lj93Y2M4ND8+dToyd2NjODQ/PnU0KTx3Ymo4ND8+dSspNHdiYmlpaG11IyIhdzoydTg0Pz4qOip1ODQ2dzoydTMiOTwhKHU4NDZ3OjJ1MDEtMzN1ODQ2dzoyODo1OisydTg0Nnc6Mjg0PzI1PHUoM3c6Mj06KC91KDIvPnc6MjMuOTYyI3U4NDZ3OjU2NCkidTg0Nnc6KzJ1bmlraWtoa3UjIiF3OisydTo5NzoydS80K3c6KzJ1OTI6NSMyPnU6Mnc6KzJ1OTcvOCJ1OjJ3OisydTgrOigodTg4dzorMnU/Pi1jY3UvPjgzdzorMnU/KT46Njw+KXU4NDZ3OisydT4jKzo1KDI0NXU4MzovdzorMnU8Lj46MnU4NDZ3OisydTM0Nz86MnUvNCt3OisydTIwLjU4ND8+dTg4dzorMnU3ODQ1OjJ1ODQ2dzorMnU3MjUwOisydTQpPHc6KzJ1NjA+OjJ1ODQ2dzorMnU1PjA0OisydTg0Nnc6KzJ1NDoyKyk0dTg0Nnc6KzJ1KS4iLjV1PS41dzorMnUoKDQrPjV1LzQrdzorMnUvLnYhMnU4NDZ3OisydS48NyI4Oi91ODh3OisydS1odTg2dzorMnUsMzovOjJ1ODh3OisydSwrPCEodS80K3c6KzJ1Iy8idTorK3c6KzJ1Ii4+PDc+dTg0Nnc6KzJ1ISEiLnU2Pnc6KzI2OikvdToydzorMispNHU2OiI1NClqa2lvdTcyLT53OisyIjJ1ODQ2dzorKzciMXUzMjorMnUvNCt3Oi48Ni41L3U4NDZ3OW8udSohIXUyNHc4NzouPz8idTg0Nnc4NzouPz52ODQ/PnYzLjl1Oisrdzg3Oi4/PnY0Ky4odS80K3c4NzouPz4yPz51NT4vdzg0dSI+KHUtPHc4ND8+dSw+NSw+NXY6MnU4NDZ3ODQ/PnUjdjoyNHU4NDZ3ODQ/PjI3Ojl1ODQ2dzguOT41OD51ODQ2dz8+PispNC4vPil1LzQrdz8yNjopOiJ1ODQ2dz82IzorMnU4NDZ3PzQ4KHU6Mjw4aT91ODQ2dz8uODA4ND8yNTx1ODQ2dz0wdTMoMywwdTQpPHc9NzorODQ/PnU4NDZ3PTQjODQ/PnUzKDMsMHU0KTx3PTQjODQ/PnUpMTF1ODh3PS43MnUzIzJ1Nj53PD4vPDQ6KzJ1ODQ2dzwrL3UhMzIhPjU8IT41PHU4NDZ3PCsvPDQ/dTg3NC4/dzwrLzA+InU+LnU0KTx3PCsvKzoidSgvNCk+dzM/PCg5dTg0NnczPjU6KzJ1LzQrdzI1KC84NCsyNzQvdjorMnU4NDZ3MT41MiI6dS80K3cxMj4wNC51OjJ3MDx2OisydTg3NC4/dzVqNXU6Mnc1Pix2OisydS5vLSl1ODQ2dzU+LHUjIjgzOi86MnU4NDZ3NDU+djorMnU5Ny84InUvNCt3NDU+dTQ4NDQ3OjJ1ODQ2dzQ1PjorMnUrOjI1Lzk0L3UvNCt3NCs+NXUjMjo0MTI1PDoydTg0Nnc0Kz41ODc6Lj8+dTY+dzQrLih1PCsvLi51ODQ2dys0NzQ6MnUvNCt3KzQ3NDorMnUvNCt3KykyLTU0Pz51ODQ2dyspNCMiOjJ1ODQ2dyoyNSEzMjoydTg0NncpMjwzL3U4ND8+KHcpLjU6NSIvMjY+dTMjMnU2PncoKCg6Mjg0Pz51ODQ2dygvNCk+dSEhIi4odS80K3cvMjo1LzI6NToydSspNHcuMi4yOisydTg0NncuNTI6KzJ1OjJ3LTIrdS41PyIyNTw6KzJ1ODQ2dyw0Nz06MnUvNCt3LCEsdT8+bnU1Pi93LCEsdSsrdS46dyM6Mik0Li8+KXU4NDZ3IzoyIzorMnU4NDZ3IzI6NDMuOisydSgyLz53IzI6NDMuNjI1MnUoMi8+dyMidSs0NzQ6KzJ1ODQ2dyI6NSg/bW1tdTg0NnciOjUoP21tbXUvNCt3Ii41LC51OjJ3Ii41LC51IT46OS4pdTorK3chPjU2LiN1OjI=",
Uup =
"Pz4+Kyg+PjB3NjQ0NSgzNC93NjI1MjY6I3cjOjYyNTI2dyEzMisudzkyPDY0Pz43dzk6MjgzLjo1dygvPis9LjV3a2o6Mnc/OigzKDg0Kz53LTQ3OD4o";
console.log("=== Fup (domain whitelist) ===");
console.log(JSON.stringify(Mla($up), null, 2));
console.log("\n=== Bup (AI lab keywords) ===");
console.log(JSON.stringify(Mla(Uup), null, 2));
运行结果：
复制代码 隐藏代码=== Fup (domain whitelist) ===
[
"cn",
"sankuai.com",
"netease.com",
"163.com",
"baidu-int.com",
"baidu.com",
"alibaba-inc.com",
"alipay.com",
"antgroup-inc.cn",
"kuaishou.com",
"bytedance.net",
"xiaohongshu.com",
"ctripcorp.com",
"jd.com",
"jdcloud.com",
"bilibili.co",
"iflytek.com",
"stepfun-inc.com",
"aliyuncs.com",
"cn-shanghai.fcapp.run",
"cn-beijing.fcapp.run",
"xaminim.com",
"moonshot.ai",
"anyrouter.top",
"packyapi.com",
"aicodemirror.com",
"aigocode.com",
"hongshan.com",
"iwhalecloud.com",
"dhcoder.net",
"lemongpt.top",
"zhihuiapi.top",
"intsig.net",
"high-five-ai.xyz",
"cloudsway.net",
"4sapi.com",
"529961.com",
"88996.cloud",
"88code.ai",
"88code.org",
"91code.pro",
"992236.xyz",
"ai.codeqaq.com",
"ai.hybgzs.com",
"ai.kjvhh.com",
"aicanapi.com",
"aicoding.sh",
"aifast.site",
"aihubmix.com",
"anmory.com",
"api.5202030.xyz",
"api.ablai.top",
"api.bianxie.ai",
"api.bltcy.ai",
"api.cpass.cc",
"api.dev88.tech",
"api.dreamger.com",
"api.expansion.chat",
"api.gueai.com",
"api.holdai.top",
"api.ikuncode.cc",
"api.lconai.com",
"api.linkapi.org",
"api.mkeai.com",
"api.nekoapi.com",
"api.oaipro.com",
"api.ruyun.fun",
"api.ssopen.top",
"api.tu-zi.com",
"api.uglycat.cc",
"api.v3.cm",
"api.whatai.cc",
"api.wpgzs.top",
"api.xty.app",
"api.yuegle.com",
"api.zzyu.me",
"apimart.ai",
"apipro.maynor1024.live",
"apiyi.com",
"applyj.hiapi.top",
"augmunt.com",
"b4u.qzz.io",
"clauddy.com",
"claude-code-hub.app",
"claude-opus.top",
"claudeide.net",
"co.yes.vg",
"code.wenwen-ai.com",
"code.x-aio.com",
"codeilab.com",
"cubence.com",
"deeprouter.top",
"dimaray.com",
"dmxapi.com",
"docs.aigc2d.com",
"duckcoding.com",
"fk.hshwk.org",
"flapcode.com",
"foxcode.hshwk.org",
"foxcode.rjj.cc",
"fuli.hxi.me",
"getgoapi.com",
"gpt.zhizengzeng.com",
"gptgod.cloud",
"gptkey.eu.org",
"gptpay.store",
"hdgsb.com",
"henapi.top",
"instcopilot-api.com",
"jeniya.top",
"jiekou.ai",
"kg-api.cloud",
"n1n.ai",
"new-api.u4vr.com",
"new.xychatai.com",
"one-api.bltcy.top",
"one.ocoolai.com",
"oneapi.paintbot.top",
"open.xiaojingai.com",
"openclaude.me",
"opus.gptuu.com",
"poloai.top",
"poloapi.top",
"privnode.com",
"proxyai.com",
"qinzhiai.com",
"right.codes",
"runanytime.hxi.me",
"sssaicode.com",
"store.zzyus.top",
"tiantianai.pro",
"uiuiapi.com",
"uniapi.ai",
"vip.undyingapi.com",
"wolfai.top",
"wzw.de5.net",
"wzw.pp.ua",
"xairouter.com",
"xaixapi.com",
"xiaohuapi.site",
"xiaohumini.site",
"xy.poloapi.com",
"yansd666.com",
"yansd666.top",
"yunwu.ai",
"yunwu.zeabur.app",
"zenmux.ai"
]
=== Bup (AI lab keywords) ===
[
"deepseek",
"moonshot",
"minimax",
"xaminim",
"zhipu",
"bigmodel",
"baichuan",
"stepfun",
"01ai",
"dashscope",
"volces"
]
可以看到域名白名单里主要是国内互联网大厂、AI厂商以及API中转站的域名，AI 实验室关键词里则是一些国内头部大模型团队的名字。
Claude Code 最终会把隐写的信息注入到系统提示词：
复制代码 隐藏代码// cli.js:279102
currentDate: Lla(GSe()),
Lla() 是刚刚提到的当前日期隐写函数。GSe() 最终指向 Hao()，负责生成 YYYY-MM-DD：
复制代码 隐藏代码// cli.js:272925
functionHao() {
let e = newDate(),
t = e.getFullYear(),
n = String(e.getMonth() + 1).padStart(2, "0"),
r = String(e.getDate()).padStart(2, "0");
return`${t}-${n}-${r}`;
}
该 currentDate 字段会被并入会话上下文对象，最终进入每次 API 请求的系统提示词。Anthropic 服务端可凭字符编码（'/’/ʼ/ʹ）与日期分隔符（-//）反推出用户是不是中国的、是否在使用中转站和是不是国内AI厂商的人。
Reddit 原文中的说法均属实。Claude Code 在检测到用户将 ANTHROPIC_BASE_URL 设置为第三方代理时才激活时区和域名检测，且其结果以 Unicode 近形字符隐写的方式藏在系统提示词里，用户和模型都难以察觉。内置的域名白名单和 AI 实验室关键词覆盖大量中转站和国内头部大模型团队，显然是为了防蒸馏和转售。
A÷刚刚在X上也承认了有检测中国用户的机制，还说本来就打算要取消这项实验了。被发现了就说要取消，只能说A÷真的是÷完了。Reddit原帖下面很多人觉得这不算间谍软件（spyware）。这个就见仁见智吧，虽然我觉得说是spyware也没啥问题，但为了客观一点文章标题里还是用了“遥测”这个词。最近 Anthropic 还被爆出在邮件里埋了1x1像素的追踪图片，用户打开邮件时就会泄露ip地址，只能说A÷为了封国人号真是煞费苦心啊。希望国内AI厂商继续加油，在未来某一天干倒A÷。
附件里是我提取并格式化的 cli.js，因为太大了所以只能分卷压缩后上传。解压前需去掉末尾的 .7z。（附件见左下角原文）

---
*爬取时间: 2026-07-24 21:58:03*
*来源: 直接站点爬取*
