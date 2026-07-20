# 弱点编号: CWE-1321
## 弱点名称: Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')

###  Top 25 排名
- **排名**: #22
- **综合评分**: 6.78


### 状态
Incomplete

### 基本描述
The product receives input from an upstream component that specifies attributes that are to be initialized or updated in an object, but it does not properly control modifications of attributes of the object prototype.

### 适用平台
- **Language**: JavaScript (Undetermined)

### 常见后果
- **范围**: Confidentiality, Integrity, Availability
  **影响**: Read Application Data, Modify Application Data
  **说明**: This weakness is usually exploited by using a special attribute of objects called proto, constructor, or prototype. Such attributes give access to the object prototype. An attacker can inject attributes that are used in other components by adding or modifying attributes of an object prototype. This creates attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the product depends on existence or non-existence of certain attributes, or uses pre-defined attributes of the object prototype (such as hasOwnProperty, toString, or valueOf).
- **范围**: Availability
  **影响**: DoS: Crash, Exit, or Restart
  **说明**: An attacker can override existing attributes with ones that have incompatible type, which may lead to a crash.

### 缓解措施
- **阶段**: Implementation
  **措施**: By freezing the object prototype first (for example, Object.freeze(Object.prototype)), modification of the prototype becomes impossible.
- **阶段**: Architecture and Design
  **措施**: By blocking modifications of attributes that resolve to object prototype, such as proto or prototype, this weakness can be mitigated.
- **阶段**: Implementation
  **措施**: When handling untrusted objects, validating using a schema can be used.
- **阶段**: Implementation
  **措施**: By using an object without prototypes (via Object.create(null) ), adding object prototype attributes by accessing the prototype via the special attributes becomes impossible, mitigating this weakness.
- **阶段**: Implementation
  **措施**: Map can be used instead of objects in most cases. If Map methods are used instead of object attributes, it is not possible to access the object prototype or modify it.

### 检测方法
- **方法**: Automated Static Analysis
  **说明**: Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

### 相关攻击模式 (CAPEC)
- CAPEC-1
- CAPEC-180
- CAPEC-77

---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: 2026-07-17 13:43:38*
