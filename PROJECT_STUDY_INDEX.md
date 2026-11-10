# GPT Researcher 学习索引

基于当前工作区的 Git 跟踪文件生成。清单列出全部跟踪文件；`.env`、`.venv`、运行日志和输出文件不在清单中。
跟踪文件：763；源码与配置文件：471。

## 学习进度

流程图要求补充（2026-10-24）：用户提醒必要时画流程图，涉及分支、并发或跨组件调用时使用简洁Mermaid配具体例子；简单一行操作不强制画图，继续每轮单个适合消化单元。

手写定位要求（2026-10-22）：每次新增函数或方法，必须同时交代所在文件/类/相对位置及缩进、为什么归属该类（职责和状态归属）、谁调用它及输入输出；不能只说放在哪而不解释。方法在类中按调用流程排放主要为阅读便利，不误称同类方法必须定义在调用者之前。本轮补充第四章手写第1步的位置原因，并公布上一轮两空均为self.researcher.visited_urls；不推进新填空、不宣称已保存或验证。

讲解去重规则（2026-10-22，用户最新澄清）：按功能大类选择一至两个代表讲透，例如所有检索器整体算一类，不能再按服务商或细分类型不断增加讲解。其余同类文件由助手阅读并在索引记录用途与覆盖情况，不逐个向用户讲流程，也不把每个适配差异单独扩成一节；只有影响主调用链理解的差异才集中简要说明。当前检索器代表已超额讲过，立即停止继续讲其他检索器并收束第四章核心范围；未读文件仍如实记未读，未讲不等于已讲，不因此勾选整章完成。避免重讲历史内容。Google及后续同类适配器已读，已交付的差异讲解保留为历史记录，不继续扩展。

- [ ] 1. 项目全景与 HTTP 普通报告主调用链
- [x] 2. 请求入口、配置优先级与 GPTResearcher 初始化
- [x] 3. Agent 角色选择、搜索规划与提示词
- [x] 4. Retriever、网页抓取与来源去重（约定核心完成；其余辅助适配器阅读仍有待补项）
- [x] 5. 文档加载、Embedding、上下文压缩与混合检索（约定核心完成；Milvus真实链路已验证，真实Embedding效果评测留第12章）
- [x] 6. 报告生成、引用、格式导出与失败路径（约定核心讲解、手写、17项隔离检查及工程注意点完成；真实模型质量评测留第12章）
- [x] 7. DeepResearch 递归流程与成本控制（约定核心讲解与手写完成，18项隔离检查及第六章17项回归通过；金额硬预算/共享抓取等待仅讲解）
- [x] 8. LangGraph multi_agents 流程与人工反馈（约定 LangGraph 核心讲解、手写、17项集成检查与工程复盘完成；第6/7章35项回归通过。AG2独立实现、真实模型质量与浏览器反馈端到端仍待覆盖）
- [x] 9. Deep Agents 示例、工具边界与 Benchmark（源码、约定核心手写、SDK装配、14项离线检查及工程复盘完成；统计指标手写按用户要求跳过，真实模型质量评测待第10/12章）
- [x] 10. MCP 接入、LLM Provider、可观测性（约定核心与注入式集成检查完成，启动工厂装配另通过4项隔离检查；费用及剩余可观测性按要求跳过，真实服务效果待第12章）
- [x] 11. 前端、WebSocket、后端 API 与部署（按用户要求完成整章业务流程讲解，不逐行精读或手写；源码静态核对完成约定主线，浏览器端到端与实际部署验证留第12章）
- [ ] 12. 测试、评测、调试实战与面试复盘（已讲测试分层、证据链调试、可重复对比及架构面试复盘；真实服务/浏览器部署验证、评测解析错误修复仍待闭环）

学习方式必须按单元分阶段执行（以最新要求为准）：先用具体例子拉通整章业务流程，再每轮只追一条从输入到输出的完整调用链，说明每步目的、输入输出、状态变化及关键代码位置。用户最新要求不再强制复述或设置固定检查题；相似步骤简要串联，新环节讲一遍，随后按用户的继续推进。源码作为链路中的定位和解释依据，不再按文件或函数顺序连续逐段灌输；尚未覆盖的代码保留在原十二单元清单中，随后按场景逐步补齐。确认本章约定核心已讲清后，经用户确认再手写核心代码。每章核心手写完成并由助手验证后，必须补讲原工程中的边界、缺陷及工程注意点，再进入下一章；这些工程细节以解释为主，不要求加入练习代码。讲解阶段的“继续”只表示继续讲解。手写下一轮先给上一轮全部填空答案。用户要求配置尽量简化，练习使用普通字典；省略 ReportGenerator.research_params。教学代码沿用用户命名 ResearcherConductor、researcher_conductor、researcher_generator、BasicReport.gpt_research。后台开关、ID/哈希及辅助导出代码不安排手写。测试由助手负责，未经验证不能宣称通过。第二单元约定的简化核心骨架已通过实际文件的集成检查；真实检索器、Embedding、其余辅助组件尚未在练习中装配，将随对应后续单元补齐，不能称为原版初始化全部复现。第三单元源码讲解已完成，用户于 2026-10-22 确认开始核心手写。第三单元约定核心已完成：用户已授权直接修正练习文件的四组错误，实际保存文件的十项核心检查通过。现进入第四单元源码讲解，讲解完成并确认后再手写核心。真实模型不作为第三单元必做项。下文历史步骤中的待验证状态以最新记录为准。

第 2 单元源码阅读进度：已讲配置文件选择与合并、环境变量覆盖和类型转换、检索器名称解析、模型/Embedding 的 provider:model 解析、推理强度校验，以及旧环境变量兼容逻辑（覆盖顺序、警告、Embedding 分支与失败路径）。用户要求跳过剩余配置讲解，文档目录、其余配置辅助方法和剩余默认字段暂记为跳过，不能视为已覆盖。GPTResearcher 初始化已讲调用入口、构造参数及 agent.py 第 138–168 行：任务属性、研究状态、容器共享、来源与上下文的区别、成本初始状态；已对照后续角色赋值、访问 URL 登记和上下文替换位置。组件装配已讲第 186 行及 ResearchConductor.__init__ 全部语句，重点是两个 self、同一研究对象引用、日志入口与 MCP 缓存锁。已讲第 169 行提示词族选择、get_prompt_family 工厂的全部分支、名称到类再到实例的转换，以及无效名称回退缺少 config 参数的问题。已讲第 172–179 行：MCP 参数处理方法、检索器选择优先级与类工厂、Memory 装配及 OpenAI 分支/取底层客户端接口；其余 Embedding 提供方实现留待文档与 Provider 单元。已讲第 182–183 行 encoding 的提取与 kwargs 清理、第 187 行及 ReportGenerator.__init__ 全部字段，并对照写作前的参数浅复制和角色补取（writer.py 第 107–110 行）。已讲 agent.py 第 188–190 行、ContextManager/BrowserManager/SourceCurator 的构造方法、WorkerPool 构造中的线程池/信号量/全局限速器及共享配置边界；业务方法只说明输入输出和状态写入位置，完整实现留在检索与文档处理单元。已讲 agent.py 第 191–198 行：DeepResearchSkill 构造的全部状态与共享引用、ImageGenerator 构造及 _init_provider/is_enabled 分支、available_images 和 ID 初始值；指出图片初始化读取大写配置属性而 Config 写入小写属性的问题。递归研究和图片生成执行体留在对应业务单元。已讲 agent.py 第 201 行及 _resolve_mcp_strategy 全部分支、研究 ID 的延迟生成与缓存用途，并收束初始化完整流程。第 2 单元约定范围源码及核心手写完成（剩余配置按用户要求跳过）。2026-10-21 对实际文件 D:\桌面\新建文件夹\1.py 验证：核心委托链、状态隔离、空上下文错误、run_agent 两种返回形式通过；ASGI POST /report/ 返回 200 且响应字段正确，缺少 task 返回 422，未实现的两种报告类型返回 400；已补缺失的 HTTPException 导入。真实 Word 导出通过，PDF 因缺少 libgobject-2.0-0 未成功，留在第 6/11 单元处理；未宣称真实检索或模型调用成功。所有导出检查使用临时目录，临时检查脚本已移除。

第 3 单元源码讲解进度：已讲普通研究中的角色选择条件与状态赋值（agent.py 第 343–380 行）、choose_agent 参数及正常路径/异常入口（agent_creator.py 第 18–62 行）、auto_agent_instructions 的作用与三个示例所约束的字段（prompts.py 第 489–515 行）。区分角色名称/角色提示词与多 Agent 编排、消息角色与研究角色；深度研究提前走独立分支。已讲 agent_creator.py 第 65–131 行完整恢复链：json_repair、日志、正则提取、默认角色及未捕获 KeyError 边界；区分格式修复和结构校验、恢复和重新调用模型。通过提取实际函数进行本地检查：尾逗号修复、None 默认回退、缺少角色字段引发 KeyError、贪婪正则合并多个对象；执行现有正则回归文件的 4 个检查函数均通过（未加载整个测试模块）。已讲普通 web 分支到 plan_research 的调用点、ResearchConductor 中第二处角色检查、researcher.py 第 50–95 行的完整规划入口、query_processing.py 第 43–80 行的初搜包装：取首个检索器类、MCP 构造参数、max_results 转发、to_thread 执行阻塞搜索。说明初搜与后续子查询搜索不同、outline 是查询列表、初搜为空仍向下规划及异常传播。已讲 query_processing.py 第 157–214 行完整规划分流、82–155 行子查询生成调用与三层模型异常路径；指出 agent_role_prompt 未使用/未转发，标准调用未显式传 prompt_family，初次 reasoning_effort 固定 medium。以模拟模型调用验证实际函数控制流：首轮成功、战略模型重试、smart 降级、全部失败上抛、MCP 单独跳过、MCP 混合继续生成六种路径。未调用真实模型。已讲 prompts.py 第 212–259 行规划提示词完整构造（任务拼接、可选初搜背景、动态数量示例、自然语言查询约束、UTC 日期、仅列表输出），以及 query_processing.py 第 7–35 行规范化全部分支和 for-else。说明只统一为字符串列表，不校验语义、数量或去重；列表中的 None/数字/字典会被字符串化，首个空列表键会优先命中。提取实际规范化函数及现有 unittest 测试类，8 项检查通过，额外核对混合类型、空优先键、重复查询、空 fallback 四个边界。未调用真实模型。已讲 researcher.py 第 360–396 行普通 Web 规划结果使用、追加原问题可能重复、gather 的调度/参数解包/结果顺序、空结果过滤和合并、内外两层异常边界及其他任务不自动取消；对照第 261–292 行向量库分支的列表返回和异常传播，说明其仍复用初搜规划。提取实际 Web 方法并模拟子任务，验证乱序完成仍按输入合并、原问题重复、全部为空、异常逃逸时返回空列表但其他任务继续四种行为。第三单元约定范围源码讲解完成；检索/抓取、上下文压缩及 MCP 子任务执行体分别留在第 4/5/10 单元。用户已确认进入核心手写。手写讲解已推进到角色选择、初搜规划、解析与规范化、重试与备用调用、并发调度；用户磁盘文件尚未保存上述全部步骤，整章集成尚未验证。

第三单元手写当前核对：第 3 步填空答案 self.query、self.call_model。2026-10-22 再读用户磁盘文件时，agent_role_promt 拼写与旧 conduct_research 仍在，尚未看到 demo_model/self.call_model/角色委托保存；可能尚未保存，不能标记已接通。继续布置第 4 步：demo_search 测试替身和 build_plan_messages，明确测试背景不是真实检索，不登记为实际来源；提示词数量限制还需后处理落实。真实模型与搜索未接入，整章未完成。

第三单元手写第 5 步：上一轮规划消息填空答案 query、context。布置 normalize_queries 和 generate_sub_queries 正常路径：支持数组、裸字符串及常见 queries/query 字典，过滤非字符串、去空白、去重、截断数量并空结果回退原问题；这些严格校验/去重是教学改进，未照搬原版强制字符串化。模型函数仍由调用者传入，须返回规划查询 JSON 而非角色 JSON。重试/降级、规划驱动和调度尚待接入，整章未完成；用户文件当前步骤尚未验证。

第三单元手写第 6 步：上一轮 generate_sub_queries 填空答案 await、response。布置 demo_plan_model 规划测试替身、GPTResearcher 的 search/plan_model 函数引用，以及 ResearcherConductor.plan_research(query)：先 await 初搜，再将背景交给 generate_sub_queries。规划返回查询列表，不把初搜或查询列表误存为最终 context。模型重试/降级与子任务并发尚未接入，旧 conduct_research 固定材料输出待后续统一替换，整章未完成。

第三单元手写第 7 步：上一轮 plan_research 填空答案 query、search_results。再次读取用户磁盘文件仍只有角色消息/解析与第二章骨架，未见规划代码保存，agent_role_promt 拼写仍待修正；不据此宣称此前步骤已接通。继续布置 generate_sub_queries 的有限失败处理：主调用最多两次，均失败后在提供 fallback_model 时调用备用一次，否则抛出；备用失败向上抛出。JSON 解析放在调用重试之外，解析失败不会触发此重试。教学版省略原版第二次战略模型调用的 token 参数调整，备用函数是否对应不同模型取决于后续实际装配。下一轮填空答案 await、messages。备用调用装配、子任务调度与整章集成在本步之后继续；第三单元不强制接入真实模型。

真实接入安排（以用户最新要求为准）：按原有十二单元清单推进，第三单元不强制接入真实模型。第三单元先完成角色选择、提示词、初搜规划、解析与规范化、重试与备用调用、并发调度及现有入口的集成验证；允许使用明确标注的测试替身验证这些核心流程。撤回上一轮 real_model、将 call_model/plan_model 改为真实函数、将 backup_plan_model 设为 None 的手写安排；本阶段继续保留 demo_model、demo_plan_model、demo_backup_plan_model、demo_search。真实检索/抓取、Embedding/上下文处理、报告生成、Provider 适配按照第四、五、六、十单元范围逐步讲解和接入；不额外设置第三单元真实模型接入期限。最终仍要区分教学替身与实际业务实现，模拟测试不计为真实连通。测试由助手负责，不读取或展示 .env 密钥。

第三单元手写第 8 步：上一轮填空答案 await、messages；第一次主调用成功不会进入 except，也不会执行第二次调用。本步布置备用规划函数的装配：demo_backup_plan_model(messages) 为明确标注的测试替身，从规划消息提取原问题并返回只含原问题的 JSON 数组；GPTResearcher 保存 backup_plan_model 函数引用，ResearcherConductor.plan_research 将其作为 fallback_model 传给 generate_sub_queries。备用调用函数暂未连接真实接口，不宣称具备跨模型降级能力；本步与此前规划代码在用户实际文件中的保存/集成尚未验证。此后继续子任务调度与整章验证。下一轮填空答案 self.researcher.backup_plan_model。

第三单元手写第 9 步：上一轮填空答案 self.researcher.backup_plan_model。本步替换 ResearcherConductor.conduct_research 的固定材料输出：await plan_research(query)，按需追加原问题且避免新增重复，以 asyncio.gather 调度 _process_sub_query，将空结果过滤为字符串列表返回；GPTResearcher 原有外层赋值负责更新 context。新增 _process_sub_query：暂通过现有 search 接口取 content 并合并，单任务 Exception 返回空字符串，其余任务继续。此为教学骨架，尚无真实网页抓取/上下文压缩；demo_search 无实际挂起点，不能声称已测出并发收益。教学版 context 保持列表以适配当前 ReportGenerator，与原版普通 Web 分支合并为字符串不同。用户文件保存和集成尚未验证。下一轮填空答案 self.plan_research(query)、self._process_sub_query(sub_query)。整章集成验证尚待完成；真实模型不作为本章必做项。

第三单元最新实际核对（2026-10-22）：用户已保存大部分第三章核心代码。实际文件 D:\桌面\新建文件夹\1.py 存在四组阻断：第 176 行误用未 await 的 _process_sub_query 作为查询列表，应 await plan_research；第 41/51/53 行备用参数 fallbak_model/fallback_mode 与调用方 fallback_model 不一致；第 54–56 行解析与 return 缩进在 except 内导致首次成功返回 None；第 91 行消息用英文冒号，而第 106/112 行测试替身按中文冒号提取导致 IndexError。本轮仅在内存中修正后验证十项核心行为全部通过：完整角色/规划/材料/写作链、角色复用、主调用重试、备用降级、全部失败/无备用传播、JSON 解析错误不重试、部分任务失败与输入顺序、原问题去重、空材料拒绝写作、规范化与实例隔离。未修改练习文件、未联网，不将内存修正版通过记为用户实际文件通过；第三章仍待用户修正保存后复验。真实模型接入不是本章必做项。

第三单元核心范围核对：角色选择与状态保存、角色提示词和规划提示词、结构解析/校验/回退、先初搜再规划、有限模型重试与降级、查询规范化及原问题处理、异步子任务调度与结果合并、接回现有研究入口及异常验证。源码已讲，核心手写于 2026-10-22 完成约定范围，并验证实际保存文件的十项核心行为。手写采用简单配置和统一模型/搜索接口；接口可用模拟响应自动测试，模拟测试不能宣称真实联网能力。真实搜索/抓取、Embedding/压缩、报告正文生成、MCP 工具执行和 Provider 底层适配按第 4/5/6/10 单元分别实现。JSON 修复库细节、正则技巧、日志和旧配置兼容不要求逐字手写；手写对原实现做严格校验或去重等改进时须明确标记。不得仅以空类或固定上下文占位认定本章核心完成。

第三单元完成验证（2026-10-22，替代此前待修正状态）：用户明确要求助手直接修改并继续；已原位修正 D:\桌面\新建文件夹\1.py 的四组错误，保留原有换行格式和其余代码。直接从实际保存文件提取核心定义执行，未做内存改写，十项检查全部通过；覆盖正常角色/规划/材料/报告链、角色复用、主调用重试、备用降级、全部失败与无备用传播、JSON 解析错误不重试、部分子任务失败与输入顺序、原问题去重、空上下文拒绝写作、规范化及实例隔离。整份文件语法通过。未联网、未执行导出、未启动服务；本章教学核心完成不代表真实检索或模型连通。被检文件 SHA-256：9c6f11e9394419e7b167b93292ec1c02932b1fc5c41b415b5bbfa94d459abce9。

第四单元源码讲解第 1 节：检索器类到搜索调用入口。已读 actions/retriever.py 全部映射和选择逻辑、query_processing.py 第 43–80 行、researcher.py 第 50–95/801–907 行、TavilySearch 全文件及 retrievers/__init__.py。当前仅讲 get_retriever 返回类、agent.py 第 176 行保存类列表、初搜取第一类、get_search_results 构造实例与 MCP 参数差异、max_results 条件转发、to_thread 调用同步 search、返回与异常传播。指出 get_search_results 文档称实例而实际接收类；Tavily 搜索结果为 href/body，不等同教学 demo_search 的 content，更不保证全文。后续继续 Tavily 请求与结果处理、多检索器循环、其他检索器适配、URL 去重、抓取管理/各抓取器及失败路径。第四单元尚未讲完，不开始核心手写。

第三单元工程补充（2026-10-22，用户要求）：核心手写已完成并验证，本轮回到第三章说明真实工程中的注意点，不修改练习代码。覆盖：角色名称/提示词与自主 Agent 的区别及 plan_research_outline 未消费 agent_role_prompt；JSON 可解析与字段/类型有效的区别、handle_json_error 缺字段仍可 KeyError；提示词非硬限制、原版规范化强制字符串化/无数量上限和去重、追加原问题重复；战略两轮加 smart 降级与内层最多十轮重试的放大效应，调用异常与解析异常边界及分类重试/预算；初搜背景直接插入提示词的质量、长度、来源和不可信指令问题；gather 的并发/速率限制、排序和阻塞调用边界；单任务空字符串回退、部分成功与全部失败的质量状态、规划失败在 gather try 外；超时/取消及 gather 不自动取消兄弟任务、线程调用取消不等同底层工作停止；角色和 visited_urls 等状态的任务生命周期、共享边界；阶段日志、调用/成本/耗时指标与查询质量评估。明确区分已读源码行为与工程改进建议，后续章节按原清单深入实现，真实模型接入不作为本章必做项。第四章已讲的检索调用入口保留进度，下一步继续第四章源码讲解。

第四单元源码讲解第 2 节：TavilySearch 搜索前的准备，范围为 tavily_search.py 第 7–58、104–130 行。逐段说明 import/正则/类型注释用途，构造时保存 query、topic、base_url、域名与 api_key；headers 在取 key 前后两种用途及最终覆盖为 Content-Type，get_api_key 按传入 headers 再进程环境取值、缺失返回空字符串而不终止构造；未读取 .env 或输出密钥。说明 search 与 _search 的外层整理/内层 HTTP 职责，site 正则提取、删除算符、去路径、合并域名并保序去重、局部变量不改 self.query、query[:400] 按字符串截断以及 _search 参数传递。用 example.com/example.org/example.net 说明变化，无真实联网。下节继续第 61–102 行 HTTP 参数字典/序列化/状态码和第 131–148 行结果清洗与异常。第四单元尚处源码讲解阶段，不开始手写。

第四单元源码讲解第 3 节：tavily_search.py 第 61–102、131–148 行，完成 Tavily HTTP 调用与返回处理。解释 _search 参数默认值、字典到 JSON 请求体、requests.post 的地址/请求头/timeout、Response 对象与 response.json 的区别、仅 200 显式解析，raise_for_status 只对 4xx/5xx 抛异常，其他非 200 情况可能隐式返回 None；search 再取 results 列表，跳过非字典和无 URL 项，content/snippet/空字符串优先级，输出 href/body，异常统一打印并返回空列表。当前 search 不主动要求 raw_content，也不保留其他来源字段，摘要与全文仍需区分。已核对本地 requests 的 raise_for_status 源码及 timeout 文档。提取实际 TavilySearch 类，在绕过构造、不读任何凭证的条件下用合成 HTTP 响应检查五项全部通过：请求序列化/字段清洗、空结果、401、无效 JSON、非预期 201；未联网、不修改练习代码。下一节沿 _search_relevant_source_urls 讲多个检索器、摘要/预取全文分流，再到 URL 去重及抓取。全章源码尚未讲完，不进入手写。

第四单元源码讲解第 4 节：researcher.py 第 824–870 行 _search_relevant_source_urls，沿第 595 行 _process_sub_query → 第 887 行 _scrape_data_by_urls 的真实调用点进入。解释两个局部收集列表、query_domains 为 None 时置空列表、每个子查询内依次遍历当前检索器类、按名称跳过 MCP、构造实例并 to_thread 执行同步 search/传数量上限、空结果继续、href 优先再 url、raw_content 非空且长度大于 100 时作为已取得正文保留并 add_research_sources；其余有 URL 的结果入待抓取列表，无 URL 不收集。add_research_sources 在 agent.py 第 680–686 行仅 extend research_sources，不等于登记 visited_urls。说明逐检索器 try 边界：当前结果异常会退出该检索器剩余处理，但已收集项保留、继续其他检索器；跨子查询并发与单子查询内检索器顺序执行的区别。末尾调用 _get_new_urls、random.shuffle 后返回 (new_search_urls, prefetched_content)，去重内部及抓取留下一节。示例均为结构演示，无联网，不修改练习代码。指出 body 再长也不触发全文分支、100 是长度阈值而非正文完整性证明；预取正文不经过此处的 URL 去重分支。第四单元仍在源码讲解阶段。

第四单元源码讲解第 5 节：researcher.py 第 801–822 行 _get_new_urls 全部语句及第 867–870/887–902 行先去重后抓取的顺序。解释局部 new_urls 与共享 visited_urls、逐项成员判断/立即 add/追加返回列表、同批重复与跨查询重复、列表输入与 docstring set 描述不一致、精确字符串比较不做 URL 规范化、verbose 条件下 await stream_output 的参数含义（actions/utils.py 第 7–32 行，True 为 output_log，url 为 metadata）。已核对 BrowserManager.browse_urls 到抓取调用的后续路径，无失败 URL 回滚；这一条普通 Web 链上 visited_urls 表示抓取前已登记，不能等同成功取得正文。日志发送异常会向上传递且保留已登记状态。说明异步原因是可等待进度输出，成员判断与 add 之间没有 await；同一事件循环共享集合时先登记可抑制重复领取，不推断为多线程/多进程安全。random.shuffle 仅打乱返回列表。提取实际方法做五项本地检查全部通过：同批/共享集合去重、未抓取已登记导致下次过滤、URL 字符串差异不合并、状态先于输出更新、输出失败无回滚；未联网、不修改练习代码。下一节进入 _scrape_data_by_urls 与 BrowserManager.browse_urls 的真实抓取链。全章仍未讲完，不开始手写。

第四单元源码讲解第 6 节：抓取调度与结果合并，覆盖 researcher.py 第 872–907 行 _scrape_data_by_urls，以及 skills/browser.py 第 7–84 行 BrowserManager 的导入、构造和 browse_urls。说明 agent.py 第 189 行 scraper_manager 的实际对象是 BrowserManager；其保存同一 researcher，并以抓取工作数/间隔创建 WorkerPool，具体调度留后续。browse_urls 的输入为地址列表，await actions.web_scraping.scrape_urls 后解包正文与图片，先登记 research_sources，再 select_top_images(k=4) 和登记 research_images，verbose 日志三个阶段后返回正文列表。add_research_sources/add_research_images 均 extend 对应共享列表；当前图片选择返回 URL 字符串，筛选内部留下一节。外层只对 new_search_urls 调用抓取，再 extend(prefetched_content) 合并已取得正文；可选 vector_store.load 是同步形式调用，内部留第五章。区分 extend 与 append、抓取正文与最终 context、BrowserManager 职责与底层 Scraper。异常从当前两层向上层子查询传播，来源已登记后图片或日志失败可能留下部分状态；底层 scrape_urls 自带异常处理，下节深入。示例为 A/B 地址新抓内容加 C 预取内容，无联网，不修改练习代码。第四单元尚处源码讲解阶段，未开始核心手写。

第四单元源码讲解第 7 节：BrowserManager.select_top_images 全部代码（skills/browser.py 第 86–115 行），及 scraper/utils.py 第 84–103 行 get_image_hash，核对 agent.py 第 653–670 行图片 getter/追加方法。说明 score 候选结构、sorted/key lambda/reverse、局部 seen_hashes、默认获取已有图片前十条、逐项 hash/已有 URL 判断、保留 URL 与 k 上限。明确修正本轮开场按图片内容去重的概括：实际 get_image_hash 不下载图片、不比较像素，仅拼接 URL 最后文件名与名为 url 的查询参数后取 MD5；域名/目录和其他参数不入标识，不同图片可被误合并。已有图片按当前调用链保存 URL 字符串，getter/adder 的字典类型注释与该调用链不一致；seen_hashes 仅当前调用使用，已有 URL 检查只看 getter 默认前十项且不预先计算已有图片哈希。score 在已读 HTML 路径由 get_relevant_images 的标签/尺寸规则产生，完整提取稍后讲。hash 辅助函数异常记录并返回 None；select_top_images 无统一捕获，缺 score/url 等错误可向上传播。文档将 k 描述为没有高分时的备选数量，但当前代码无分数阈值分支，正数 k 直接限制选中条数。提取实际函数做七项无联网检查全部通过：同文件名跨域同标识、普通查询参数忽略、url 参数保留、排序/本批去重/k、已有 URL 不预置哈希、仅查已有前十条、缺 score 异常传播。不修改练习代码。BrowserManager 已讲完；下节继续 actions/web_scraping.py 的 scrape_urls 和资源释放，随后 Scraper 与 WorkerPool。全章尚未完成，不开始手写。

第四单元源码讲解第 8 节：actions/web_scraping.py 第 1–48 行 scrape_urls 主流程。解释 Any/颜色工具/WorkerPool/Scraper/Config/logger 的用途及本函数实际异常输出使用 print；输入 urls、cfg、已有工作池，返回正文与图片两个列表。初始化空结果、设置 User-Agent、scraper=None、创建 Scraper 实例（与 cfg.scraper 后端名称区分）、await run、逐页 image_urls extend、不在本层做图片排序去重。说明 try 内不同失败阶段保留不同状态；finally 检查对象和 session 后关闭连接，释放本批 HTTP Session，未关闭传入工作池；getattr 默认值防止属性缺失，清理异常本身仍可外抛。指出 cfg 注释 optional 与 cfg.scraper 实际访问不符；cfg=None 在 try 内失败返回空结果，缺 user_agent 则在 try 前外抛。提取实际函数，用模拟 Scraper 验证六项行为全部通过：正常收集/关闭、run 失败返回空/关闭、图片收集出错保留正文和部分图片、None 配置不进入构造、try 前属性异常传播、关闭异常传播。无联网、不修改练习代码。文件末尾三个辅助方法仍待说明，随后进入 Scraper 构造、执行与后端选择。第四单元未讲完，不开始手写。

第四单元源码讲解第 9 节：说明 actions/web_scraping.py 第 51–107 行三个辅助函数，完成此文件源码覆盖。全仓 Python 静态调用检索仅发现定义与 process_scraped_data 内对 extract_main_content 的调用，不将这些辅助函数画入已读普通 Web 抓取主链。filter_urls 逐地址用 any 检查 excluded_domains 子字符串，not 后保留，没有解析主机名；当前 config 目录 Python 源码未检索到 excluded_domains 定义，不能假定默认配置具备该字段；自身无 await 和异常捕获。extract_main_content 直接原样返回 HTML，是占位实现，未清洗/解析正文，自身无 await。process_scraped_data 遍历有 status/content 字段的记录，success 分支等待占位提取函数后重建 url/content/status 三字段字典，其他状态原样保留原记录引用，config 参数未读取，缺字段异常会传播。此输入 schema 与当前 Scraper 主链的 url/raw_content/image_urls/title 不同，不能直接接上；async 声明和 await 占位函数不代表实际 I/O 或并发。示例说明子字符串误匹配、HTML 原样返回及成功字段重建；不新增练习代码。下一节沿真实主链进入 scraper/scraper.py 的构造与 run，仍先讲源码，第四章尚未讲完。

第四单元源码讲解第 10 节：scraper/scraper.py 第 7–107 行的导入、Scraper.__init__、run 与 _check_pkg。说明各导入用途、保序的本批 URL 去重与已读 visited_urls 跨调用去重的区别、重复数量日志、创建 requests.Session 并更新 User-Agent、保存后端名称与传入工作池；同一 Session 引用传入本批各 URL 提取协程，关闭仍由上层 finally 负责。_check_pkg 对 tavily_extract/firecrawl 的 pip 包名和导入名做映射，find_spec 不存在时使用 sys.executable -m pip install，成功 invalidate_caches，安装失败转 ImportError；该同步安装在构造路径上可能阻塞调用线程，本轮仅阅读未安装。run 生成逐 URL 协程并 gather，结果按输入 URL 顺序，过滤仅 raw_content is not None，空字符串在本层不会被过滤；真正长度验证与工作池限流在下节单 URL 方法展开。run 无整体 catch，逃逸异常或结构不符向上传播到 scrape_urls，不能只凭 gather 认定任务内 HTTP 全部无限并发。示例 A/B/A 去重后 A/B，正常记录与 raw_content=None 记录的筛选，无联网、不修改练习代码。下一节精读 extract_data_from_url 及 get_scraper 后端路由；之后完整展开工作池与具体后端。第四章仍在源码阶段，未开始手写。

第四单元源码讲解第 11 节：scraper/scraper.py 第 109–170 行 extract_data_from_url 全部路径。说明由 run 为每 URL 调用，async with worker_pool.throttle 先取得执行资格并覆盖本页全流程；try 在上下文内部，进入/退出限流的异常不在此 try 内。局部大写 Scraper 为 get_scraper 返回的具体后端类，区别于外层批量调度类；按 link/session 创建实例、记录类名。hasattr(scrape_async) 决定直接 await 原生异步接口，否则 get_running_loop().run_in_executor 向传入工作池的 executor 提交 scraper.scrape 方法引用；两分支都解包正文、图片、标题。len(content)<100 返回 raw_content=None/空图片并保留标题；成功时四字段记录；五条日志只记录结果，后面的重复短内容判断对正常字符串无新增筛选作用，None 在第一次 len 时先报错并进入 except，异常记录的 title 为空。恰好 100 字符可通过本页检查，前面预取全文分支却要求大于 100，边界不同。方法自身不登记来源，交由上层；run 按 raw_content=None 过滤失败记录。提取实际函数用模拟后端与真实本地线程池检查六项全部通过：原生异步及100字符、同步走指定线程池、99字符保留标题的失败记录、None 正文捕获、后端构造失败转换记录、限流进入异常上抛；未联网、不修改练习代码。下一节精读 get_scraper 的后端路由，之后完整展开 WorkerPool 与具体抓取实现。第四章仍未讲完，不开始手写。

第四单元源码讲解第 12 节：scraper/scraper.py 第 172–217 行 get_scraper 全部分支。说明 SCRAPER_CLASSES 八项键到类映射，不创建后端实例；scraper/__init__.py 统一导入导出后端和批量 Scraper，__all__ 列出星号导入名称。先 urlparse(link).path.lower().endswith(.pdf)，再判断整个原始 link 是否包含大小写敏感的 arxiv.org，否则使用 self.scraper 配置名；因此 PDF 优先于 arXiv，也优先于普通后端配置，查询参数/片段不妨碍 path PDF 后缀判断。arXiv 判断未验证 hostname，查询参数中出现 arxiv.org 也可误命中，大写 ARXIV.ORG 则不会匹配这一分支；不根据 URL 后缀判断就宣称已核验真实 MIME。字典 get 无匹配时抛 Scraper not found，交上一节单页方法转换为 raw_content=None；函数为普通同步函数，做解析/判断/查表，不发网络请求。用带查询参数 PDF、arXiv PDF 与摘要 URL、普通网页、无效配置说明选择，均未访问。单页具体后端实现后续逐个讲；Scraper 类已覆盖，下一节进入 WorkerPool/throttle 与全局限速器，再到实际网页/PDF/论文等抓取器。未修改练习代码，第四章源码未讲完。

第四单元源码讲解第 13 节：utils/workers.py 第 1–50 行 WorkerPool 全文件。解释 ThreadPoolExecutor、asyncio.Semaphore、asynccontextmanager 和 get_global_rate_limiter 的导入；time 在本文件未使用。构造保存工作数/间隔，创建本池线程池与本池信号量，取得进程内共享限速器并 configure。区分线程池执行同步任务、信号量约束整个单页任务、共享限速器约束各池单页任务的放行间隔；原生异步分支也受 semaphore 约束但不靠线程池执行。逐句解释 throttle：先取得 semaphore，等待共享限速器，再 yield 将执行交给调用方 async with 块，块退出后释放许可；等待放行时也占并发名额。并发上限属于每个 WorkerPool，不是全应用统一并发上限；共享限速对象只在同一 Python 进程内，不等同多进程/跨机器限流。放行粒度为单页任务，不能保证后端内部每个 HTTP 请求都单独限速。以 max_workers=2、间隔1秒、每页3秒的理想示例区分并发数与放行频率。全局对象和等待算法下一节逐行讲；构造重新 configure、线程池无关闭方法等工程边界留章末补充。不修改练习代码，第四章仍在源码讲解。

第四单元源码讲解第 14 节：utils/rate_limiter.py 的共享对象与配置生命周期，覆盖导入和类属性、第 24–42 行 __new__/__init__、第 51–58 行 configure、第 81–92 行 reset/模块实例/getter。说明 ClassVar 类级属性、cls 与 self、__new__ 分配并缓存对象、_initialized 防止复用对象时重新清零；__init__ 中 _lock=None 仍未实际创建锁，真正 get_lock 与等待算法下一节讲。模块导入创建 _global_rate_limiter，WorkerPool 两处 getter 返回同一引用；__new__ 同时约束直接调用类复用。configure 只覆盖共享 delay，不重置上次放行时间，也不验证数值；后创建工作池的 configure 会覆盖此前工作池实际读取的全局间隔，本池保存的 rate_limit_delay 属性可能与共享实际配置不同。reset 只清 last_request_time，不清 delay/锁，不是每页自动调用。以池 A 间隔1秒、池 B 间隔0秒说明后续共享配置被关闭，现有等待如何变化留算法部分分析。四项独立本地运行检查通过：getter 同对象、直接重复构造保留状态、配置覆盖共享、reset 保留间隔；无网络、不修改练习代码。下一节 get_lock 和 wait_if_needed，之后具体后端。第四章仍在源码讲解阶段。

教学方式调整与第四章链路复盘（2026-10-22）：用户明确要求停止连续逐函数精读，改为整章先拉通、每次一条完整调用链、具体例子和自主复述；原十二章清单及核心手写后测试/工程补充规则继续。原计划的锁与等待算法本轮尚未讲，不能记为已覆盖。本轮以第三章已经规划出的 RAG 工作原理 子查询为输入，显式设定 retriever=TavilySearch、scraper=bs、初始 visited_urls 空、无向量存储、示例页面无图片，仅串普通 HTML 成功链：_scrape_data_by_urls → 搜索/取 href-body → URL 登记去重 → BrowserManager.browse_urls → scrape_urls → Scraper.run → 单 URL 限流/后端选择 → 线程中 BeautifulSoupScraper.scrape → _fetch GET → clean_soup/get_text_from_soup/标题提取 → 长度检查和四字段记录 → run 过滤 → wrapper 收集图片并关闭 Session → BrowserManager 登记来源 → 外层合并预取正文 → 返回材料列表供第五章上下文筛选。新读 BeautifulSoupScraper 全文件与对应清洗工具后，按真实代码讲故事，不宣称这些文件已逐段讲完。示例 URL、搜索响应与网页为演示输入，未实际联网；不修改练习代码。以 搜→筛→抓→洗→交 帮助复述，最后请用户讲述查询如何变成带来源的正文材料，再据其理解推进下一条链。其余抓取后端、失败重试链、锁算法及其他检索器仍待按原第四章范围覆盖。

第四章链路场景 2（2026-10-22）：用户已复述普通网页成功链，已澄清 URL 去重避免重复抓取而非阻止重复搜索、抓取材料先交上下文筛选；用户确认搜索摘要信息不够完整。继续按单条完整链讲网页首次 GET 返回 503、第二次返回 200 的恢复场景，仍使用 Tavily + bs，无 PDF/MCP/图片分支：搜索取得 URL/摘要 → 去重登记 → 工作池放行并在线程中调用 BeautifulSoupScraper → _fetch 第一次 GET 503 → 属于可重试状态且 attempt=1，time.sleep(1) → 同一网页任务内部第二次 GET → 200 且页面体积正常 → 解析清洗 → 正文长度通过 → 统一页面记录 → 汇总/Session 关闭/来源登记 → 交上下文筛选。强调最多两次尝试、重试同一 URL 不重新做搜索/规划/去重；内部重试沿用已领取任务，所以不被 visited_urls 阻止；time.sleep 位于同步后端线程，会占该线程和单页并发名额，事件循环可继续调度其他任务。示例为源码推演，未真实联网，不修改练习代码。最后请用户复述从首次503到得到材料的过程；暂不展开两次失败等其他分支。共享锁等待算法仍待后续链路场景覆盖。

第四章链路场景 3（2026-10-22）：用户明确理解重试不重新搜索/去重，因为仍是原网页任务。本轮只追首次 GET 503、等一秒、第二次仍503的单页完全失败链（Tavily + bs，唯一URL，无预取/向量存储/图片）：_fetch 两次上限后返回 None → BeautifulSoupScraper.scrape 返回空正文/图片/标题 → 单页调度按短正文返回四字段失败记录 raw_content=None → Scraper.run 过滤该记录后返回空列表 → scrape_urls 正常收尾并关闭Session → BrowserManager无新增正文/图片 → _scrape_data_by_urls返回空材料列表。避免把此处无材料等同整个HTTP请求一定报错或报告必然停止，当前结论只到抓取材料边界。抓取前登记的 visited_urls 未回滚，该URL仍在集合；同一研究后续普通URL去重路径会跳过它，不因此证明成功抓取。最后请用户用自己的话解释失败后URL是否仍在集合、能否表示正文成功。源码已复核，示例未实际联网，不修改练习代码。共享锁算法及其他后端仍待覆盖。

第四章链路场景 4（2026-10-22）：用户已理解 visited_urls 不等于抓取成功，本轮进一步说明它是抓取前已登记，可能尚未发请求。新场景只追 PDF 成功链：Tavily 查询 RAG 工作原理 → 示例返回 https://example.com/rag.pdf?download=1 → URL 去重登记 → 工作池放行 → URL path 的 .pdf 分支优先于 bs 配置 → 线程池调用 PyMuPDFScraper.scrape → 网络URL判断 → requests.get 流式下载字节（本例正常HTTPS，无SSL回退）→ 8192字节分块写本地临时PDF → PyMuPDFLoader.load 取得文档列表 → finally 尝试删除下载临时文件 → join 所有 page_content，标题取第一项元数据，图片固定空列表 → 正文长度检查 → 四字段页面记录 → 批量汇总/来源登记 → 交上下文筛选。说明封面短不代表整篇无正文，当前代码合并全部页面后才返回单页调度器验证；下游记录格式与HTML路径一致。已完整阅读 pymupdf.py，故事仅覆盖远程PDF正常分支，本地路径、超时/解析失败、SSL回退、下载阶段临时文件清理边界等仍待其他链路或章末工程补充，不宣称均已教完。示例数据为源码推演，无联网、不生成文件、不修改练习代码。请用户按下载/解析/合并/返回四步复述。

第四章链路场景 5（2026-10-22）：用户理解 PDF 会合并所有页面后验证。本轮用 PubMedCentralSearch 的默认 PMC 正常分支说明检索器已取得正文的完整链：子查询 RAG 医疗问答 → 检索论文ID → 逐ID取回XML → 提取标题/摘要/body并组合 full_content → search 返回包含 URL 与 raw_content 的记录 → _search_relevant_source_urls 发现 URL、非空 raw_content 且长度>100 → 收集到 prefetched_content 并登记 URL 来源 → 待抓取 URL 列表为空 → 外层仍调用 browse_urls([])，不产生单URL抓取任务 → 合并预取正文 → 返回 url/raw_content 材料供上下文筛选。解释并非无网络请求，正文获取发生在检索器内部；不能把只有 body 的摘要当成该分支条件。此分支仅显式保留 url/raw_content，登记 research_sources，不经当前 _get_new_urls 的 visited_urls 登记；visited_urls 不能当作所有已取得来源的完整列表。完整读取 pubmed_central.py，配置环境字段仅说明用途、不读取值；pubmed数据库分支、异常/空结果、参数覆盖等尚未按场景讲，章末工程需回看 PMID/PMC ID转换、无请求超时、预取正文去重与来源元数据。示例论文与文本为源码推演，不涉及真实文献或医疗结论，无联网、不修改练习代码。请用户复述正文在哪里取得、为何不用再次抓页面；共享锁算法及其他后端仍待覆盖。

第四章链路场景 6（2026-10-22）：用户明确要求相似流程讲一遍即可，不用复述或固定问答；已修改学习方式总则，历史复述要求不再适用。本轮串一个子查询搜到三条不同普通HTML地址的并发/限速完整链：结果分流/去重登记 → Scraper.run 为三页创建协程并 gather → 本池信号量上限3，三页均可取得名额 → 共享锁保护上次放行时间检查/等待/更新时间 → 以间隔1秒、每页处理3秒的理想时间线说明 A约0秒放行，B约1秒，C约2秒，约3/4/5秒完成 → 正文清理与长度验证 → 输入顺序汇总，过滤失败（本例全成功）→ 关闭本批Session/登记来源 → 交上下文筛选。get_lock 首次创建后共享同一把异步锁；wait_if_needed 在 delay<=0 直接返回，否则在锁内按剩余间隔 await asyncio.sleep，睡醒后刷新 last_request_time，再退出锁；锁只覆盖放行检查，不覆盖整段网页抓取。等待期间其他协程可运行，但当前任务继续持有本池信号量许可；C等共享锁时尚不计算自己的剩余间隔。讲清线程池执行同步抓取、semaphore控制本池进入数量、共享锁与时间戳控制放行节奏。时间线为源码推演而非实测，无网络、不修改练习代码。全局锁等待算法正常配置路径至此按场景讲过，配置在等待中变化/取消/跨事件循环与墙钟调整等留章末工程补充；其他后端和检索器仍待覆盖。结尾不要求用户复述。

第四章链路场景 7（2026-10-22）：只追搜索得到 arXiv 摘要页地址的完整链：子查询搜索 → href URL 去重登记 → 批量调度/工作池 → get_scraper 在非 .pdf 且链接包含 arxiv.org 时选择 ArxivScraper → 同步 scrape 在线程池执行 → _paper_id_from_link 正则提取论文ID（无匹配时取最后路径段）→ arxiv.Client + Search(id_list=[paper_id], max_results=1) 按已知ID取论文记录 → 拼接发布日期、作者和 summary，标题单独返回、图片固定空列表 → 单页长度验证 → 标准 url/raw_content/image_urls/title 记录 → 来源登记/返回材料供上下文筛选。明确这条实现取元数据与摘要，不下载论文全文，类名或 context 名称不能证明全文；PDF路径后缀优先，只有实际路由到PDF后端才走之前的下载解析链，不能断言所有 arXiv /pdf/ 地址都走PDF。无结果时 StopIteration 转 ValueError，再由外层单页异常处理变为失败记录并过滤。示例为源码推演，无真实API请求、不修改练习代码；不设置复述或固定检查题。来源为 arxiv/arxiv.py 全文件及 scraper.py 第172–217行。

第四章链路场景 8（2026-10-22）：新读 BrowserScraper 全文件及 overlay.js、processing/scrape_skills.py、processing/html.py；本轮只讲配置 browser 后的动态HTML成功链。示例初始HTML仅app占位，JS生成正文：搜索URL/去重 → 普通地址按配置选BrowserScraper（不是bs失败自动升级）→ 同步scrape交线程池 → 惰性导入Selenium并默认创建Chrome（headless=False）→ 先访问Google等2秒并保存/重加Cookie，向当时页面注入分析遮罩 → get目标URL → 最多20秒等待body存在 → 滚到底部、等2秒并对比高度，直到连续一次高度相等 → execute_script取当前DOM outerHTML → BeautifulSoup清理/取文本图片标题 → 返回三元组/长度检查/统一记录/来源登记/交上下文筛选 → finally关闭driver并清Cookie临时文件。澄清浏览器执行JS，BeautifulSoup只解析结果；body存在和高度稳定均不保证业务正文完全加载；滚动循环无次数/总时限，线程及单页许可会被占用。异常正常捕获时返回空三元组，等待body超时返回短错误字符串随后被外层长度过滤；driver.quit若失败会打断后续Cookie清理，应章末补充。Google/Cookie/遮罩为当前实现的额外步骤，遮罩在目标导航前注入，不误称目标页处理。可选真实浏览器Cookie分支、PDF/arxiv内部支路及辅助链接函数用途未在本场景展开，保留后续工程说明；新读文件不计为全部已讲。无真实浏览器启动或网络访问、不修改练习代码、不设置复述题。

第四章链路场景 9（2026-10-22）：完整阅读 browser/nodriver_scraper.py，本轮按配置nodriver的动态HTML链解释：搜索/去重 → 外层工作池放行 → 识别scrape_async并直接await（不提交该方法到线程池）→ get_browser在类级锁内首次用zendriver创建默认可见浏览器，已有时取processing_count最低者，最低负载>=8且实例数<5才新建，阈值不是单浏览器硬上限 → Browser.get先增加processing_count，再在本浏览器的域名信号量内打开标签页 → 等complete、短暂停顿、等idle（封装捕获asyncio.TimeoutError仅日志继续）→ 随机分段滚动，到底或累计滚动值>=500结束 → get_content取HTML → BS清洗/文本图片标题 → 返回三元组 → finally关闭标签页并减计数，空闲浏览器停止并移出集合 → 外层统一长度检查/来源登记/上下文筛选。以150字符正文说明内层<200只是警告、默认debug=False不截图，外层<100才拒绝；不能把200当过滤阈值。域名限流属于本浏览器实例，只包driver.get，不覆盖后续整页抓取，也不是全局站点并发控制。纠正本轮开头“失败回退”预告：实际没有自动更换后端/重试，异常返回str(e)可能被外层长度>=100误收为正文；浏览器池是并发复用且空闲即关，非永久保活。成功例为源码推演，未启动浏览器/联网/运行测试，不修改练习代码，不设置复述题。其他边界如简陋域名归并、异步上下文异常吞噬、分配与计数竞态及取消清理等留章末工程说明。

第四章链路场景 10（2026-10-22）：完整阅读 tavily_extract/tavily_extract.py，另预读 firecrawl/firecrawl.py 与 web_base_loader/web_base_loader.py（后两者尚未讲解）。本轮只追普通网页配置tavily_extract的完整链：子查询经搜索取得href/body → 去重登记 → 普通URL按配置选择TavilyExtract → 构造SDK客户端（环境变量TAVILY_API_KEY只讲代码用途，未读取其值）→ 同步scrape在线程池中执行 → client.extract(urls=link)提交已知URL取得raw_content → failed_results非空直接空三元组 → 成功后仍用共享Session.get(link,timeout=4)另取HTML → BS提取图片及标题 → SDK raw_content作为正文返回三元组 → 外层长度检查、来源登记、交上下文筛选。区分TavilySearch的query发现地址与TavilyExtract的URL正文提取；当前抓取器未请求本地clean_soup/get_text作正文抽取。重要失败链：远端正文已成功但补抓HTML异常，整体except仍返回空三元组，丢掉可用正文；无自动后端切换/本层重试。缺少环境key在构造时抛出，由外层单页异常处理，不在scrape自己的try内。response字段缺失/结果空也会转空结果。例子为源码推演，无真实SDK调用、无联网、不安装依赖、不修改练习代码、不设置复述题。第四章继续源码场景讲解，尚未开始手写。

第四章链路场景 11（2026-10-22）：复核并讲解 firecrawl/firecrawl.py 的普通URL成功链：配置firecrawl分支 → 构造FirecrawlApp（key来自环境，服务地址可配置、缺省官方地址，只讲源码未读取值）→ 同步scrape在线程池调用SDK scrape(url=link,formats=[markdown]) → 返回对象metadata.error非空拒绝；status_code有值且不等200拒绝，缺metadata/缺状态不能据此认定验证了200 → 从response.markdown取正文、metadata.title取标题 → 本地Session.get(timeout=4)补HTML并用BS取图片 → 返回三元组 → 外层长度过滤/统一记录/来源登记/上下文筛选。强调与TavilyExtract是配置二选一，同URL无默认并行或自动降级；正文为Markdown字符串，当前适配不再转HTML或调用本地正文清洗，来源标题和正文来自服务、图片来自本地。SDK响应按对象属性读取，区别于Tavily字典；注释声称匹配某版本不等于已验证实际安装SDK兼容。补HTML异常仍会丢掉已取得正文；缺key构造异常与scrape运行异常分别由外层与内层处理。例子为源码推演，无网络/SDK执行/依赖安装，不修改练习代码。WebBaseLoader及其他检索器后续按场景覆盖，本章仍处讲解阶段。

第四章链路场景 12（2026-10-22）：复核并讲解 web_base_loader/web_base_loader.py 全文件：配置web_base_loader的普通URL经搜索/去重/外层工作池 → 构造WebBaseLoaderScraper保存URL、使用传入Session或新建 → 同步scrape在线程池内惰性导入LangChain WebBaseLoader，创建loader并设置requests_kwargs verify=False → loader.load获取Document列表 → 逐项将page_content直接拼接成字符串（无分隔符，未保留metadata，未执行Embedding/向量检索）→ 本地Session.get同URL再次取HTML，用html.parser提取图片和标题 → 返回正文/图片/标题 → 外层长度检查/统一记录/来源登记/上下文筛选。正文来自LangChain loader，不是本地补抓HTML的正文；两套请求没有在该适配中显式共享Session，不把verify=False误称同时作用于第二次GET。异常统一空三元组，补抓失败丢已有正文；第二次GET无显式timeout；构造自建Session未见本类关闭；urljoin导入未使用；docstring声称返回字符串而实际返回三元组。未读取安装库内部实现，不声称全部网页加载细节已讲。无真实网络/loader调用、不修改练习代码。八类抓取后端的主要成功链至此均已覆盖；其余辅助分支及工程边界继续保留，第四章检索器侧的剩余实现尚待覆盖，不宣称整章完成。

第四章链路场景 13（2026-10-22）：完整阅读 retrievers/arxiv/arxiv.py，以配置ArxivSearch的子查询为输入串搜索→抓取：构造保存query并将sort字符串Relevance/SubmittedDate映射为SDK枚举，assert拒绝其他值，query_domains参数接收未使用 → 外层to_thread执行同步search → arxiv.Client.results(Search(query,max_results,sort_by))转列表以取得结果 → 每论文输出title、href=result.pdf_url、body=result.summary → 无raw_content，故即使摘要长也进入URL去重/抓取，不走预取全文分支 → 具体抓取器取决返回URL形态。本场景显式假设href=https://arxiv.org/pdf/2005.11401（无.pdf后缀）：路由命中ArxivScraper而非PDF，按ID再获取摘要/作者/日期，返回统一材料；若path实际以.pdf结尾才是PyMuPDF下载全文。强调字段名pdf_url不决定本地路由、搜索结果不等于全文、ArxivSearch与ArxivScraper分别负责按query发现与按ID取记录，不混为一步。search无本地try，空结果返回[]，异常由本次所选普通子查询外层捕获后继续其他检索器，初搜包装的错误边界不同不混讲。示例URL及响应为源码推演、非真实SDK输出，无联网/模型/测试执行，不修改练习代码，无复述题。第四章其他检索器仍待覆盖。

第四章链路场景 14（2026-10-22）：完整阅读 retrievers/duckduckgo/duckduckgo.py，串普通查询通过Duckduckgo发现网页并交bs抓取的链：factory名称duckduckgo映射类 → 构造check_pkg(ddgs)，该helper只find_spec并缺失抛ImportError不自动安装 → 创建DDGS保存query/domains → 外层to_thread执行同步search → ddg.text(query,region=wt-wt,max_results) → 将第三方href/link/url归一为href、body/snippet/description归一为body、非空title保留，跳过非dict和无URL条目 → islice按调用者要求截取规范化结果 → 因无raw_content而走URL登记去重和配置抓取器 → 统一材料交上下文筛选。例子具体演示SDK的link/snippet字段如何变成href/body，强调适配层消除字段差异而非新增正文能力；query_domains保存但TODO未实现过滤。text调用异常打印并空列表，返回后遍历/规范化不在该try内；构造错误/逸出错误由普通搜索外层记录后尝试其他配置检索器。预读retrievers/utils.py全文件，本轮只解释check_pkg，其日志推送/动态名称扫描与fallback名单未计已讲。无真实搜索/联网/安装/测试执行，不修改练习代码、不设置复述题。

第四章链路场景 15（2026-10-22）：完整阅读 retrievers/google/google.py，按子查询RAG & Agent、限定example.com/docs.example.org串搜索链：构造保存query/domains，API key与CX优先取传入headers对应字段、否则环境（只说明用途未读值；普通子查询构造未显式传headers，不误称HTTP请求头自动全链路透传）→ 将domain拼接为(site:example.com OR site:docs.example.org) 原问题，局部search_query不改self.query → urlencode组装key/cx/q/start=1，避免&/#等破坏查询参数 → 外层to_thread里requests.get请求Google接口 → json.loads(resp.text)与dict类型检查 → 读取items，跳过非dict/缺link/包含youtube.com的地址 → title/link/snippet归一为title/href/body并切片max_results → URL登记去重/按抓取配置取正文/上下文筛选。说明max_results只对当前响应切片，未传num也无翻页，不能保证补足数量；域名约束是搜索查询语法，不是返回链接hostname严格校验。非2xx只打印并继续解析，无raise_for_status；JSON失败/非dict空列表，网络错误可上抛到普通子查询搜索外层；requests.get未显式timeout。首行Tavily注释与GoogleSearch实现不符，以代码为准。例子为源码推演，无请求/测试/密钥读取，不修改练习代码、不设置复述题。第四章其他检索器及工程收束待继续。

第四章链路场景 16（2026-10-22）：按同类最多两例规则，完整阅读custom/custom.py，以已规划子查询RAG工作原理接企业自建HTTP搜索接口，讲扩展边界而非重讲通用抓取：配置custom映射CustomRetriever → 构造从RETRIEVER_ENDPOINT确定服务地址，缺失直接ValueError；RETRIEVER_ARG_前缀参数去前缀转小写并保持字符串 → 外层to_thread执行search，requests.get(endpoint,params={**params,query:self.query},timeout20)，显式query覆盖同名附加参数 → raise_for_status并解析JSON → 顶层必须为list，null/对象/请求或JSON错误返回[]，列表元素结构未校验 → 演示接口返回[{url,raw_content}]且正文>100，外层复用已讲预取正文分支，登记来源、无重复单URL抓取、交上下文筛选；返回href/body则仍走普通URL抓取。说明接口适配让上层不感知企业ES/数据库/内部服务如何检索，但当前文件本身没有实现数据库/向量算法/鉴权；max_results参数未使用、未发送和截断，query_domains也未使用；不是只配任意URL即可适配任意响应格式。只展示虚构地址/返回值，不扫描环境值，无网络/测试/练习改动。并预读groundroute/groundroute.py与crw/crw.py全文件，尚未对用户讲解；后续只补差异：GroundRoute本地仅单HTTP调用+字段归一化，不把docstring多引擎路由/缓存/成本选择当本仓库已实现；CRW支持服务地址覆写、业务success标志，markdown被放body而非raw_content仍触发后续抓取。第四章继续源码阶段。

第四章同类检索器合并说明 17（2026-10-22）：遵守同类完整流程最多两例，完整阅读Bing/Brave/BoCha/Serper/SerpApi/SearchApi/Searx七个适配文件，合并说明用途和差异，不再各画重复调用链。Bing传count、无显式timeout/raise_for_status、域名TODO，过滤youtube子串；Brave请求count=min(max_results,20)、20秒超时与状态校验、域名TODO；BoCha POST开启summary且count传服务、10秒超时，输出仍snippet为body，域名未用，长摘要不等正文；Serper支持地区语言时间与排除站点、site拼词，num传服务、10秒超时但无状态raise且网络异常可上抛；SerpApi site拼词、10秒超时、仅200处理、本地按有效条目计数限制并过滤YouTube；SearchApi固定engine=google、Bearer头、20秒超时、query_domains未用，结果字段用下标，缺字段可触发except将已收集结果清空；Searx地址可配、GET/search format=json、无显式timeout，参数域名未用、按有效条目本地计数限制，网络/解析异常上抛。重点示例：同样传query_domains不意味着所有后端生效；max_results有服务端限制、本地限制或二者差异；SearchApi第二条缺snippet可令前面已收集结果一并丢弃，SerpApi对缺snippet有默认空串。七类输出仅href/body(/title)，未保留raw_content，均复用普通URL抓取路径，不把summary选项当预取全文。记录为代码阅读与差异讲解，不代表SDK/服务当前可用性验证。无环境值读取/联网/测试/练习代码修改。GroundRoute和CRW预读待差异交代，学术/社交检索器及其他辅助路径待继续，第四章未完。

第四章同类检索器合并说明 18（2026-10-22）：完整阅读ExaSearch文件并结合已读GroundRouteSearch/CRWRetriever，仅讲内容字段与接口能力差异。Exa普通search调用client.search（默认type=neural、use_autoprompt=False、include_domains转发、num_results与额外filters），返回对象text或summary放body而非raw_content，不能称普通search已调用get_contents。CRW /v1/search支持自定义服务地址、可选Bearer，100秒超时、raise_for_status及success=False业务失败，data中markdown优先description但仍放body。GroundRoute本地只POST query/max_results，20秒超时，解析列表或results列表，URL/摘要归一化；topic/domains存了未发，docstring的多引擎/缓存/质量成本路由不是本仓库实现，不能据此解释成本算法。以服务响应含3000字正文但适配存body的假设说明普通子查询外层仍去重并抓URL，不走预取；字段约定可导致重复请求，raw_content必须以已验证内容能力为前提才能改，不能盲目重命名摘要。Exa find_similar与get_contents各自用途和输出：相似URL搜索返回href/body，按ID取内容返回id/content；静态扫描gpt_researcher/backend/multi_agents/deep_agents/tests/evals，只见该文件SDK调用与tests/test_exa_null_attrs.py测试使用，不能把辅助方法串入已讲普通主链；空属性与缺URL/ID过滤，无本层try。另完整预读SemanticScholar/OpenAlex文件，但尚未交付讲解；后续补开放PDF过滤与倒排摘要还原新机制。无环境值读取/真实网络/测试执行/练习修改，第四章仍未结束。

第四章差异机制说明 19（2026-10-22）：复核并讲解OpenAlex与SemanticScholar，避免重复学术搜索完整链。OpenAlex search发送查询、排序、per_page=min(max_results,25)（本地设定非宣称API实际极限），10秒超时；可选身份参数仅说明代码不读取值、不验证服务当前免费/认证政策。_pick_href依次最佳开放PDF、primary落地页、OpenAlex id（并非总是PDF）；_reconstruct_abstract展开word→positions为(位置,词)列表，int转换跳过不合法位置，按位置排序后空格join；具体演示RAG[0,4]/uses[1,5]/retrieval[2]/and[3]/generation[6]还原原序列。空/非dict/无有效位置返回None、上层默认Abstract not available，非列表位置跳过，未保证异常位置/词全校验；输出body摘要无raw_content，继续URL抓取。说明倒排结构用于恢复接口数据，未构建项目向量库。SemanticScholar搜索请求指定字段，保留isOpenAccess为真且openAccessPdf为dict且url非空者，其余剔除，不自动下载全文；保留sort大小写，query_domains未用，GET无显式timeout，json解析在RequestException try之外。差异表与已讲Arxiv、PMC对照只说明URL选择/摘要与全文/再抓取，不重讲相同流程。补PMC pubmed分支搜索所得ID被直接传给固定db=pmc的抓取，未见ID转换，不能宣称两数据库切换已正确实现；仅点明代码风险不实际验证远端数据。无网络/库调用/密钥读取/测试/练习改动。社交检索器、部分辅助路径和章末收束仍待讲。

第四章核心收束 20（2026-10-22）：按用户按功能大类取一两例的最新要求，停止扩展服务商，复核researcher.py 508–651/801–907与BrowserManager，收束普通Web主链：第三章子查询 → 按当前配置检索 → 区分仅URL/摘要与已有raw_content → 普通URL在共享visited_urls登记去重 → 工作池限制并发并抓取/清洗/长度验证/失败过滤 → 合并预取正文并记录来源 → 返回材料列表 → researcher.py 600交ContextManager，最终上下文筛选留第五章。具体例子初始visited已有A，搜索A/A/B和预取正文C：A均跳过，B登记后失败，C长度足够直接保留；返回仅C正文材料，visited含A/B但不因此含C，失败B不回滚。强调三种状态visited、research_sources、context不同，材料不等于最终context；本例为源码推演未运行。普通Web核心讲解范围已完成，第四章手写/集成测试尚未开始，原章节复选框保持未完成；未读社交检索器等辅助实现仍保留未覆盖，后续由助手阅读记录不逐个扩成课程，MCP归第十章。下一轮须按用户确认进入核心手写，沿现有外部1.py保留命名，配置简化；实现搜索适配、共享URL登记去重、限并发/抓取、HTML清洗/失败过滤、预取正文合并、材料与来源返回，不手写所有服务商/PDF/浏览器/图片辅助实现；随后由助手验证并补章末工程注意点再到第五章。本轮未修改练习代码、无联网或测试执行。

第四章核心手写第1步（2026-10-22）：用户在核心范围收束后说继续，按该上下文进入手写。先实际读取D:\桌面\新建文件夹\1.py全335行，确认仍为第三章已验证骨架：demo_search返回title/content；_process_sub_query直接合并content；GPTResearcher已有实例visited_urls=set()；本章抓取/材料分流尚未接入。开头预告搜索摘要/正文分离，核对后按最小可写单元先布置ResearcherConductor._get_new_urls普通同步方法（在同一类内、与__init__同级），复用researcher.visited_urls，逐URL判断/先登记/收集新URL。教学版无异步日志、只操作内存，因此用def，与原版因日志await使用async def不同。示例空集合输入[A,B,A]返回[A,B]并登记集合，后续[B,C]只返回C；标记发生在抓取前，不代表成功，不额外新建局部set导致失去跨查询共享。给两处填空：if url not in self.researcher.visited_urls；self.researcher.visited_urls.add(url)，下一轮先公布。尚未接入现有_process_sub_query，未修改实际练习文件、未执行本步测试，不宣称已有真实搜索/抓取或第四章完成；后续接搜索格式、抓取清洗、并发/失败过滤、预取正文合并，由助手验证。

第四章核心手写第2步（2026-10-22）：上一轮两空答案均self.researcher.visited_urls。布置ResearcherConductor._split_search_results(self,results)普通同步辅助方法，位于_get_new_urls后、与__init__/conduct_research同级；原因是检索结果分流与去重同属流程编排，状态仍归GPTResearcher。其功能来自原版_search_relevant_source_urls 850–870行，为降低学习粒度把分流抽出，明确不是原仓库同名方法。遍历已规范搜索结果，href优先url；无地址跳过；raw_content非空且len>100保留{url,raw_content}，否则URL入待抓列表；最后返回(self._get_new_urls(urls),prefetched)。自身只处理内存用def，后续获取搜索结果的方法调用；不把body摘要当正文、不对预取支路虚构visited登记。例子A仅摘要、A重复、B超过100字正文，初始visited空，返回[A]和B正文，visited只含A。给两空①item.get("raw_content")、②self._get_new_urls(urls)，下一轮先公布。尚未接入demo_search/旧_process_sub_query（当前仍title/content），本轮不改已有数据格式、不宣称整链已运行；来源列表记录后续接入时集中处理。未读取/修改外部练习文件、未运行测试。下一步抓取后端/HTML清洗，最终再接回已有入口并由助手验证。

第四章核心手写第3步（2026-10-22）：先公布第2步答案item.get("raw_content")与self._get_new_urls(urls)。布置模块级同步scrape_page(url)函数，放在外部1.py的ResearcherConductor类之前、顶格，与demo_search同级；在顶部导入requests与BeautifulSoup。定位原因是该函数只负责一个URL的IO/解析，不需要researcher共享状态，作为独立抓取工具由后续调度通过asyncio.to_thread调用，流程编排仍留Conductor。核心实现with requests.get(url,timeout10)自动关闭Response、raise_for_status、以response.content和html.parser创建soup、去script/style/nav/header/footer、取标题与正文、len<100返回None、成功直接四字段记录url/raw_content/title/image_urls空列表、异常打印后None。教学版把原版后端三元组与外层记录包装合并，不手写图片与完整重试/体积/编码策略，明确get_text只是通用清理不保证仅文章正文；使用同步requests因此函数def，将来to_thread而不是只加async。两填空①response.raise_for_status()、②soup.get_text(" ", strip=True)，下一轮先给。真实HTTP实现已布置但尚未接入调用、不宣称联网成功或实际文件已保存；测试由助手后续执行。本轮只更新学习索引，不修改外部练习文件、不发网络请求。

第四章核心手写第4步（2026-10-22）：先公布第3步答案response.raise_for_status()、soup.get_text(" ", strip=True)。布置简化BrowserManager类，置于模块级scrape_page之后、ResearcherConductor之前，class顶格，方法四空格：__init__(max_workers=3)持有asyncio.Semaphore；_scrape_url在async with semaphore内await asyncio.to_thread(scrape_page,url)；browse_urls用gather调度每URL协程、按输入顺序取得结果并过滤None。定位原因是单页工具只负责取内容，管理器负责批量并发；GPTResearcher构造中self.visited_urls后新增self.scraper_manager=BrowserManager(max_workers=3)，每研究对象持有并发控制器，后续Conductor通过self.researcher.scraper_manager.browse_urls调用。两填空①await asyncio.to_thread(scrape_page,url)、②self._scrape_url(url)，下一轮先公布。解释调用链、许可覆盖整个单页线程等待、正常或异常退出自动释放、gather本身不限制并发、同步requests仍需to_thread，三许可并非开三个新线程，完成次序与gather结果顺序分离。教学管理器不复制原版researcher引用/WorkerPool/global限速/图片日志；线程使用asyncio默认执行器，仅限制本管理器在途任务，不声明全进程HTTP限流或失败自动重试。例子四URL、前三获许可、释放后第四进入，单页失败None过滤，保留成功结果。未修改实际练习文件/未测试/未联网，不宣称已接通；下步统一连接搜索分流与抓取并合并预取正文。

第四章核心手写第5步（2026-10-22）：先公布第4步两空await asyncio.to_thread(scrape_page,url)、self._scrape_url(url)。只读核对外部1.py磁盘定义，仍是第三章骨架，未见scrape_page/BrowserManager/_get_new_urls/_split_search_results，可能尚未保存，不因此宣称已接通或执行测试。继续布置Conductor内async _scrape_data_by_urls(self,query)，放_split_search_results后与其他方法同级，原因它串研究流程且通过self.researcher访问共享搜索/抓取管理器：await search(query) → 分流得urls,prefetched → await scraper_manager.browse_urls(urls) → materials.extend(prefetched) → self.researcher.research_sources.extend(materials) → return materials。新增GPTResearcher.__init__实例research_sources=[]，紧邻visited_urls；区分已登记待抓集合与已取得的来源材料列表，不每次调用清空。明确教学版将预取/新抓的来源登记集中在合并后，区别原版分两处登记，BrowserManager教学版尚不登记来源所以不重复。下一轮填空①self._split_search_results(results)，②await self.researcher.scraper_manager.browse_urls(urls)。具体结果新抓A/C预取B则extend扁平三记录而非append嵌套。由后续_process_sub_query调用本方法；当前demo_search仍title/content需后续换为href/body或真实适配，旧_process仍直接合并content，不能现在称全链完成。本步未改练习文件、未网络或测试；后续入口接线/搜索适配/验证继续。

第四章核心手写第6步（2026-10-22）：上一轮第5步两空已在用户截图纠错时公布，再提示①self._split_search_results(results)、②await self.researcher.scraper_manager.browse_urls(urls)。截图发现_search调用少await、materials置空而未抓urls，已给完整纠正方法，变量materias只要一致不是根因。用户随后追问to_thread和对象链，已分别解释；目前继续布置替换Conductor现有_process_sub_query，不新增第二个同名方法。位置与原方法相同，原因它是第三章gather调用的子查询任务入口，用新_scrape_data_by_urls替换旧search后直接读content的实现。方法try里await获得materials，提取各item的raw_content暂以双换行join返回字符串，except打印查询/错误后返回空串以复用已有外层过滤。不直接写self.researcher.context，继续由外层conduct_research汇总与GPTResearcher赋值，避免单子查询覆盖整次研究状态。本步只是第五章前临时拼正文，无相关性筛选/Embedding/压缩，不称最终上下文算法已完成。两空①await self._scrape_data_by_urls(query)，②item["raw_content"]，下一轮先公布。旧demo_search仍title/content无URL，下一步接适配搜索接口并整链验证，不宣称当前demo已能抓真实网页；仍无外部练习文件写入/测试/联网。第四章手写未全部完成。

第四章核心手写第7步（2026-10-22）：先公布第6步答案await self._scrape_data_by_urls(query)、item["raw_content"]。布置模块级async search_web(query)，位于demo_search后或其他模块级工具区、ResearcherConductor之前，与demo_search同级；顶部导入原项目TavilySearch类。函数创建TavilySearch(query)，await asyncio.to_thread(retriever.search,max_results=5)并返回统一href/body列表；两空①query、②retriever.search（函数引用不加括号），下一轮先公布。理由是该函数封装外部搜索调用，不依赖研究共享状态，保留原有async search接口，便于初搜与子查询共用及测试替换；不手写另一个同类搜索适配器，也不把模型集成提前。GPTResearcher.__init__原self.search=demo_search替换为self.search=search_web（不加括号），其角色/规划模型替身保持。明确这是普通TavilySearch发现URL，不是TavilyExtract抓取后端；正文仍由scrape_page+BS完成。search返回字段适配旧demo的title/content问题已通过新入口与新_process读取raw_content解决；接线代码未等同实测可用，依赖用户本机环境与项目env，不读取/展示.env或密钥。手写集成测试待实际保存后由助手执行，不要求用户跑测试；未修改外部练习文件、未调用API。第四章阶段为手写接线待验证，工程补充尚待后续，不勾选整章完成。

第四章接线核验待保存（2026-10-22）：用户继续后先公布第7步答案query、retriever.search，再完整只读外部1.py，磁盘仍335行第三章版本：demo_search/content与旧_process、self.search=demo_search，缺scrape_page/BrowserManager/search_web及Conductor._get_new_urls/_split_search_results/_scrape_data_by_urls，与用户截图中新代码不同。用项目venv对磁盘文件compile+AST静态检查：语法通过，以上六个新增定义均缺失；未执行模块、导入backend/配置、读取环境或发网络请求。因此第四章不能做实际文件集成验证，不以旧第三章运行或内存拼装冒充通过。需要用户将编辑器代码保存到已知1.py，或给出实际新文件路径；不覆盖其可能未保存的编辑。未勾第四章完成，未进入第五章，核心手写集成/测试和章末工程补充仍待继续。

第四章实际修正与验证完成（2026-10-22）：用户保存后重读1.py共424行，复现GPTResearcher构造因max_worker/max_workers不一致TypeError。按已讲核心自动修正六组：BrowserManager参数统一max_workers；search_web误用gather（用户同期保存成to_threadr，首轮精确匹配失败未写入，重读后按AST定位整个函数修正）改await to_thread；_split只读取raw_content、不回退body；去重/return移出for，避免仅处理首条及空结果None；_scrape_data_by_urls的browse_urls补await；research_souorces更正research_sources。保留用户其他命名如retriver、materias、scrape_urls和现有格式/换行/BOM。外部文件修正经require_escalated完成，写前核对文件未变化、编译后原目录原子替换。保存SHA256为69d64be74712fc537c1e434536ee064c001776f8d7f0eb3ca598ed9a9f878571。随后对该实际文件的核心AST定义（没有内存修正）进行八组检查全部通过：构造/实例状态隔离；完整结果分流/摘要不作全文/100边界/共享去重；真实BS解析清洗/短文及HTTP错误过滤/响应关闭；搜索adapter await与真实后台线程；真实线程+信号量并发峰值2/输入顺序/部分失败；预取正文合并登记且无重复GET；子查询搜索失败隔离/空报告拒绝；BasicReport→角色/初搜规划→四子查询→共享URL去重→抓取→来源→报告整链。网络SDK/HTTP全模拟，asyncio/线程/解析器为真实执行；共五次搜索调用、公共A及失败B仅各一次GET、预取正文不入visited、来源不含失败B。未导入整个练习模块、未启动HTTP服务、未调用真实API/LLM、未执行Word/PDF导出，不读取.env/密钥，测试脚本通过stdin执行无残留。复核文件hash未在测试中变化。第四章约定核心讲解/手写/测试完成并在最终答复补工程说明：visited与成功来源及getter语义、URL规范化/失败重试与预取去重、并发与限速/任务超时及线程取消边界、静默失败与可观测性、清洗不等相关性筛选和内容可信。章节勾选仅表示约定核心完成，社交检索器等未读辅助仍明确待补，不能视作全仓/全适配器已覆盖。下一轮进入第五章讲解，继续每大类一两代表，不立即手写。

阶段复习（2026-10-23）：用户要求先复习前两天内容，暂停第五章新课。复核学习索引与外部1.py现有定义，第四章修正后的方法/装配仍在，不重新运行测试或宣称今日真实网络验证。复习范围按一条普通报告请求串入口、初始化、角色/初搜规划/规范化与重试、子查询并发、Tavily URL搜索、结果分流/共享去重、限并发与to_thread抓取、HTML清洗/失败过滤、材料与来源/上下文汇总、简化报告与导出返回。以“什么是RAG”说明demo规划原理/应用/局限再按需追加原问题；角色/规划/报告仍是教学实现，Tavily与requests已真实接线但未验证外网连通。集中复习类职责/对象引用、三种状态、async/await/to_thread/gather/Semaphore、body不等raw_content、return循环缩进等已修错误；无新增手写/填空/复述要求，不进入第五章，不变更练习文件。原配置跳过范围及各辅助适配器未覆盖项保持记录。

第五章讲解第1单元（2026-10-23）：用户明确继续第五章，开始讲解不手写。实际阅读skills/context_manager.py、context/compression.py、context/retriever.py、document/langchain_document.py、memory/embeddings.py全文件及默认pretty_print_docs/相关配置，另读取本地已安装EmbeddingsFilter实现以核实相似度/k/threshold控制，不运行模块或读取环境值；路径config/default.py不存在已通过rg定位variables/default.py，无遗漏依赖错误。按一个普通Web长材料案例串researcher.py600→ContextManager.get_similar_content_by_query（拿memory中现有Embedding对象，传similarity_threshold/promptfamily/kwargs，async_get_context max_results10）→ContextCompressor检查总字符与篇数→本例明确假设缺省8000阈值、三页合计12000字符走标准路径→SearchAPIRetriever将原始字典转Document并每页上限50000字符、保留source/title元数据，名字含SearchAPI但此处不发搜索请求→RecursiveCharacterTextSplitter目标1000字符/重叠100→Embedding片段和query→默认余弦相似度按高低及阈值过滤（本地依赖k默认20，再pretty_print最多10）→默认格式化Source/Title/Content上下文字符串返回子查询，再由研究外层汇总。具体示意原理/广告/应用片段与查询相似度为虚构推演非API实测，强调语义相似不验证事实。小材料路径单独简要说明总字符<8000且篇数<=max_results时只转Document/格式化不做Embedding筛选，不能把方法名compression当每次必运行压缩；默认配置similarity_threshold=.42，类独立fallback=.35，两者有传参优先关系，本轮仅说明场景阈值不展开配置。压缩是选块非LLM改写摘要、不需先存永久向量库，当前主链不是混合检索；本地文档/已有向量库/混合检索后续分别讲，不能混画一条流程。第五章其他源文件虽预读不计全部讲完；不逐个讲Embedding提供商、不新增手写/填空/复述题、不修改练习文件、不联网或执行测试。

第五章面试补充：参数设置（2026-10-23）：用户问chunk/阈值如何回答，核对普通压缩1000字符/100重叠、默认配置similarity_threshold=.42、类未传参数时环境fallback=.35、压缩触发阈值缺省8000字符且还需篇数条件；另向量库入库分块1000/200，与普通Web压缩不同不混报。讲参数选择的实际权衡（片段完整性/主题噪声/重复量/费用、阈值召回与噪声），0.42不是42%准确率，更换Embedding或语料后需重新验证。提供面试话术区分目前沿用基线与将来的验证方案：固定资料和标注证据的问题集，分阶段比较chunk/overlap/阈值，检查证据召回、回答依据、上下文长度、时延与费用，再看典型漏召回/噪声案例。示例候选值仅实验设计非最优结论，不编造已调优或提升幅度。没有执行新评测/联网/读取配置环境值，不改练习代码、不推进下一单元。

第五章讲解第2单元（2026-10-23）：参数面试补充后继续普通Web标准压缩路径，只追片段经过Embedding筛选这一条，不扩Provider。核对本地已安装ContextualCompressionRetriever先base_retriever.invoke再compress_documents、DocumentCompressorPipeline按splitter/filter顺序执行、EmbeddingsFilter及stateful-doc helper：embed_documents输入片段文本列表，embed_query输入当前子查询；若已有state向量可复用但不是跨请求持久化缓存；默认相似函数为余弦，默认k20先按分数降序取候选再严格大于threshold过滤，状态记录query_similarity_score，格式化阶段最多10项。用人工设定二维向量query[1,0]、原理片段[.9,.1]、广告[.1,.9]说明余弦约.994/.110，阈值.42保留前者，明确人工教学数据非真实Embedding输出，不给向量维度虚构词义。说明Memory.get_embeddings拿现有模型对象不是生成向量/聊天历史；生成片段向量和问题向量才发生在filter执行。整条同步invoke由项目to_thread托管，标准路径错误上抛到普通子查询异常处理可变空字符串，不宣称自动降级；筛选保留原片段并非生成摘要，当前路径不要求持久化向量库。最多10块不是精确token预算，事实正确性未由相似度保证。无网络/Embedding调用/测试执行/练习修改/填空/复述要求，继续讲解阶段，其他第五章核心待覆盖。

第五章讲解第3单元（2026-10-23）：实际阅读document/document.py与online_document.py全文件，复核researcher.py local/hybrid等入口及plan_research/子查询调用；本轮只讲local目录内一份PDF的完整入口链，不逐格式扩课。明确假设无向量库/MCP：report_source=local→DocumentLoader(cfg.doc_path).load→目录os.walk或文件列表isfile过滤→按扩展名选择PyMuPDFLoader→load返回页Document列表→每个非空page_content分别转换{raw_content,url=basename(source)}→传document_data给_get_context_by_web_search→该方法仍调用plan_research，初搜使用首个检索器故local不是严格离线→各子查询复用已有非空document_data，_process_sub_query不再执行网页材料搜索/抓取→复用前两单元压缩/格式化→汇总研究上下文。强调此PDF入口保留每页一条材料，不同于第四章远程PDF抓取器先合并所有页；当前只保留文件名，页码/完整路径/原metadata丢弃。方法名web_search不代表每步都抓网页，应看scraped_data条件；但规划初搜实有网络可能，不误导完全离线。异步边界：DocumentLoader._load_document内部同步loader.load无await/to_thread，所以gather不保证PDF并行解析，可能阻塞事件循环；loader_dict值为所有loader实例而非类，未选中加载器的构造也可能因依赖出错，异常返回[]，最终无材料抛ValueError。路径字符串按目录walk，不直接load单文件，单文件需列表；不扩配置细节。OnlineDocumentLoader仅预读，其临时文件/来源/异常和Azure等入口留集中辅助说明，未计已讲。无真实文件读取解析/联网/模型调用/测试执行，不修改练习代码、不手写/复述。

第五章讲解第4单元（2026-10-23）：完整阅读vector_store/vector_store.py，复核agent.py154–155包装、ReportSource枚举和researcher.py204–205/261–292/780–799以及ContextManager66–87/VectorstoreCompressor36–82。只讲已有向量库场景，分准备与请求两阶段：准备时wrapper.load将材料转Document(source元数据)，按1000字符/200重叠切块，add_documents交实际vectorstore对象，Embedding/索引/持久化由后端实现，wrapper未实现数据库算法且元数据只保留source。查询时显式report_source=langchain_vectorstore，plan_research仍先初搜与规划、并发子查询→_process_sub_query_with_vectorstore→ContextManager→VectorstoreCompressor→wrapper.asimilarity_search→实际库异步搜索(query,k=8,filter)→Document列表→默认Source/Title/Content格式→汇总上下文。本路没有调用普通ContextCompressor的0.42阈值/临时分块管线，也未在查询处再load全库；阈值、距离及filter语法由后端决定，不以接口名推断默认余弦。max_results最终本链传8，不用构造7或方法默认5混报；filter例为来源rag.pdf且需后端支持，当前入库不保留页码/标题/权限元数据，不宣称已实现权限过滤。仅传vector_store参数不自动切换研究路径，local/web中可写库但仍走原上下文筛选。持久化配置与模型匹配后续工程说明。异步搜索委托后端；vector子任务无普通Web同样的catch返回空串，错误可从gather向上抛出。无真实库/Embedding/API访问、无新手写/测试/复述要求；下一单元混合来源研究，与BM25+向量混合检索区分。

第五章讲解第5单元（2026-10-23）：复核researcher.py171–184/360–396/593–600及PromptFamily.join_local_web_documents。只讲report_source=hybrid普通无MCP/无向量库示例：用户问企业RAG方案的适用场景，先加载本地方案文件（document_urls有值则优先OnlineDocumentLoader，否则目录DocumentLoader），加载完成才gather并发两条独立_get_context_by_web_search调用：文档路传非空document_data，网络路传[]；两路各自plan_research故可能两次初搜/独立子查询，非共用一次规划。文档子任务因已有正文跳过网页材料抓取，网络子任务搜索/去重/抓取，均复用前面分块与筛选。两路分别汇总字符串后默认join_local_web_documents仅按Context from local documents / Context from web sources加标签拼接，交研究context（后续若curate_sources启用另有流程，未在本例混入）。明确此hybrid为本地/文档来源+网页来源，不是该分支实现BM25+向量召回融合，未见RRF/统一分数/全局去重重排/矛盾裁决；同时传vector_store可写入本地资料但分支未自动改走vectorstore搜索。故障：先加载文件无材料抛错时尚未启动两路，不自动退化为纯网页；初搜规划等逸出异常可使gather向上传播，普通子查询内部部分异常则空串，不能宣称全局容错。具体资料/输出是源码推演，无真实文档或网络访问，不改手写代码、不新增练习/复述。同类机制不逐服务商扩课，后续补章节剩余核心再确认手写。

第五章讲解第6单元（2026-10-23）：完整阅读skills/curator.py与prompts.py319–350，复核researcher.py207–225和默认CURATE_SOURCES=False。只讲可选来源筛选SourceCurator链：常规各来源上下文先汇总赋researcher.context → 开关启用才await curator.curate_sources(research_data) → system用研究角色、user用原研究query+已有资料+最多10项要求，调用smart模型（temperature.2/max_tokens8000/cost_callback）→ json.loads → 外层把list按Title/Content/Source规范成字符串并替换context，否则直接赋返回对象。区分Embedding问题/片段语义相似筛选与LLM按研究整体目标/来源时效/多样性/数据价值等提示词筛选，不把模型判断说成事实核验，不将日志Verified等同已验证可信。提示词要求保留原文不改写摘要、鼓励广覆盖、不严格删除重复；max_results10仅传提示词、未在代码硬截断；缺少JSON结果结构/来源白名单校验，格式可解析不代表内容可信。异常捕获通常返回原source_data，属于保留未精筛材料的降级，默认关闭无需每次额外模型。明确类型注解List与普通Web/hybrid实际字符串输入不一致，len日志可能是字符数，不把它当来源数；外层预期大写字段但prompt只要求原格式，不能宣称强schema已实现。示例不同质量来源为演示，未真实LLM/网络测试，不改练习或安排必须手写此可选项。当前核心讲解接近收束，尚未确认/开始第五章手写。

第五章讲解第7单元/主链收束（2026-10-23）：用户继续，按已约定功能大类取代表收束而非追加同类课程。实际读完azure_document_loader.py与各包__init__，复核LangChainDocumentLoader和已读OnlineDocumentLoader；辅助用途集中交代：Online下载临时文件后解析并清理，输出来源可能为临时路径而非原URL；Azure同步Blob下载到临时目录返回路径给DocumentLoader，带_get_blob_path路径越界检查，不在本轮展开云API；LangChainDocumentLoader把现有Document转换成raw_content/url，默认来源metadata键为title可传source；包init导出统一导入名。WrittenContentCompressor与SectionRetriever/ContextManager草稿方法已有全文预读，静态确认由backend详细报告detailed_report.py176使用；功能是从已写章节中找相关内容，非此次普通Web研究必经节点，完整调用保留第六章详细报告路径不混画。收束已讲普通Web压缩、小材料快路、本地加载、已有向量库、文档+网页hybrid、可选SourceCurator，输入/输出边界与具体实现分支清楚；第五章约定主链讲解完成，练习代码尚未添加第五章，核心手写与测试/章末工程补充未开始，复选框保持未完成。给核心手写范围：文档/材料统一格式并保留来源、分块、Embedding相似度筛选及格式化、替换旧子查询正文直接join、复用研究入口接local/hybrid，已有向量库仅写适配调用不重造数据库；Embedding provider按一例/接口装配，余提供商不扩课，模型/配置简化沿用要求。手写需用户确认后开始，不把继续讲解提前当作写代码请求。未修改练习、未运行真实模型/网络/测试；辅助边界后续工程补充和对应单元继续记录，不称所有全仓代码已讲完。

第五章覆盖核对（2026-10-24）：用户问是否讲完，重新核对学习索引七个讲解单元、参数面试补充、十个相关源码文件AST方法清单以及详细报告中的已写章节检索调用点，并只读检查练习文件类定义。结论：第五章约定主链/核心讲解完成（统一文档材料、分块/重叠、Embedding及相似度阈值、小材料快路、来源格式、已有向量库、local/web hybrid、可选来源筛选、主要异步与异常边界）；同类入口仅用途说明符合用户要求，不宣称所有辅助方法逐句讲过。WrittenContentCompressor/SectionRetriever与草稿章节去重流程已明确留第六章详细报告场景，不计为漏讲普通研究主链；Embedding其余Provider/云存储细节不逐个扩课，后续第十/十一章按需覆盖。练习1.py仍只有前四章的六个类，没有第五章ContextManager等新实现，故第五章核心手写、实际文件验证和完成后工程补充均未开始，章节复选框保持未完成。无网络/模型调用/源码修改或新测试执行。下一步可在用户确认后开始核心手写，不重讲已覆盖同类实现。

第五章核心手写第1步（2026-10-24）：用户明确“开始”，进入手写；上一轮无填空。先实际读取外部1.py导入和Conductor/GPT状态，确认第四章基础仍在且尚无ContextManager。第一步只新增ContextManager._to_documents(self,materials)，不揉入Embedding/分块/接线：顶部导入langchain_core.documents.Document；类模块级放在ResearcherConductor之前（当前scrape_page之后），class顶格、方法四空格，原因材料转换属于上下文处理准备，与后续分块/筛选同组件；Conductor仍负责业务调度，之后由ContextManager自己的处理入口调用本方法，不误称必须按定义顺序。遍历raw_content或空串、跳过空正文，构造Document(page_content=content,metadata={source:item.get(url,''),title:item.get(title,'')})并返回列表，完整正文先保留，截断/快路后续统一接。解释Document是正文+来源元数据的容器，不生成向量/不调LLM；元数据后续随分块保留，本地file来源也能承载。两填空①content、②item.get("url", "")，下一轮先公布。方法普通def只做内存转换，示例url/title/raw_content到page_content/metadata，不重新请求网页、不写researcher.context。此教学版把原SearchAPIRetriever转换逻辑收进ContextManager，避免另建BaseRetriever包装；尚未实例化/接入原_process。未修改练习文件或测试/联网，章未完成；后续按约定补分块、向量筛选/格式、装配入口、文档/local/hybrid与向量库适配，助手验证后工程补充。

第五章核心手写第2步（2026-10-24）：用户已追问Document是否预留接口及为何使用，明确它是langchain_core已实现类，转换为正文/元数据结构以适配split_documents并随分块保留来源，不是自动Embedding；自写全链可以保留dict，此处复用现成工具。继续先给第1步答案content、item.get("url", "")。本轮顶部新增RecursiveCharacterTextSplitter导入，ContextManager内_to_documents之后同级新增def _split_documents(self,documents)：创建splitter(chunk_size1000,chunk_overlap100)，return splitter.split_documents(documents)，仅最后参数一空documents，下轮先公布。定位原因是正文分块属于上下文准备，由后续ContextManager筛选入口先调用_to_documents再调用_split_documents，非Conductor负责解析细节；方法普通def只在内存处理，未来整体筛选同步工作可to_thread。强调splitter与Document均现成库能力，不要求实现递归算法；按分隔符递归切分、1000为目标/上限设置非每块恰好长度、重叠并非简单固定位置切片，元数据随块复制，输出仍Document列表。不新增组件装配、不接入旧_process、不执行真实Embedding或测试/练习写入。磁盘定义检索仅用于核对，不据未保存状态宣称本章代码已完成。

第五章核心手写第3步（2026-10-24）：先公布第2步答案documents。复核原ContextCompressor与本地EmbeddingsFilter现有实现，布置在ContextManager类头新增__init__(embeddings,similarity_threshold=.42,max_results=10)保存传入模型对象/阈值/结果上限，原两个方法保留；在_split_documents后同级新增普通def _filter_documents(self,query,documents)，创建现成EmbeddingsFilter(embeddings=self.embeddings,similarity_threshold=self.similarity_threshold,k=self.max_results)，return relevance_filter.compress_documents(documents,query)。顶部导入langchain_classic.retrievers.document_compressors.EmbeddingsFilter，明确已实现库类，内部执行embed_documents/embed_query、默认余弦排序与严格阈值过滤，非要用户再手写该类。两填空①embeddings（构造传入值）、②self.embeddings（筛选器接已保存模型对象），下一轮先公布。必须解释参数对象不是模型名字字符串/测试假数据，需具备embed_documents和embed_query等协议，之后装配步骤创建并传入，此时尚无ContextManager实例、不称真实模型已接通。定位理由：转换/分块/筛选同属上下文处理，构造保存本组件策略，Conductor只调入口；后续上下文入口调用filter，对同步模型调用外包to_thread，不把def改async当消除阻塞。简化版k直接取最终10，原版默认候选20后格式化10，不复刻多层截断。示例两Document入→保留相关Document出、元数据不丢、空结果[]，调用失败向上抛由后续入口策略处理，不悄悄当真实成功。未修改实际练习、无网络/Embedding调用或新测试，仍待装配/格式化/上下文入口/文档分支与整体验证。

第五章核心手写第4步（2026-10-24）：用户追问compress_documents，已先解释它属于现成EmbeddingsFilter类，输入Document列表和query，内部调用模型生成片段/查询向量并按相似度/k/阈值选原片段，输出Document列表而非向量/回答，不要求手写库方法。本轮先公布第3步答案embeddings、self.embeddings，再布置自写ContextManager._format_context(self,documents)，位于_filter_documents后且def同级，原因上下文格式转换是ContextManager末步，由后续统一入口将筛选结果传入，Conductor只需要返回字符串。用显式for循环建立blocks，逐Document用metadata.get(source/title默认空)与page_content构造Source/Title/Content段落，最后双换行join；两空①doc.page_content、②blocks，下轮先公布。示例两个相关片段输出两个带来源段落，空列表得到空串，元数据只参与格式而非正文相似度计算；格式化不调用模型、无新搜索、不完成第六章的引用编号/真实性验证。普通def，无等待。当前已布置转换/分块/筛选/格式四步但尚无上下文总入口/模型实例/研究接线，未声称接通。未改外部练习文件或运行网络/模型/测试。

第五章核心手写第5步（2026-10-24）：先公布第4步答案doc.page_content、blocks。布置ContextManager内async get_similar_content_by_query(self,query,materials)，放_format_context后且方法同级；原因这是提供给Conductor调用的统一上下文接口，内部组织同组件四个辅助方法，业务执行器不再自己拼正文。实现_to_documents→空则空串；sum有效Document正文长度，<8000且有效文档数<=self.max_results则直接_format_context返回，不调用Embedding；标准路径每Document的page_content截前50000字符（沿用原标准路径保护，不宣称精确token预算）→_split_documents→await asyncio.to_thread(self._filter_documents,query,chunks)→_format_context筛选结果。两空①self._split_documents(documents)、②relevant_docs，下轮先公布。说明to_thread接同步方法引用及参数，await等待筛选结果，转换/分块/格式本身仍同步；异步原因模型计算或请求可能阻塞，先依照已讲方案把筛选托管线程。异常不在本入口静默吞掉，交原子查询异常策略；新接口不修改researcher.context，外层仍负责汇总。主线示例3篇12000字符走标准，2篇3000字符快路；快速路径不执行相似度，所以不是只要调用该方法就肯定筛过。教学版本地固定8000/50000以简化配置，不读环境。当前模型对象未创建/ContextManager未装配、旧_process未替换，尚不能称第五章接通；下一步创建模型对象并装配、接研究入口，后续补文档/local/hybrid/向量库适配。未修改外部练习文件或执行网络/模型/测试。

第五章核心手写第6步（2026-10-24）：先公布第5步答案self._split_documents(documents)、relevant_docs。复核memory/embeddings.py74–108/227–235与agent.py177–188，明确Memory为原仓库已实现类、不是用户要另写的预留接口，get_embeddings普通方法直接返回保存的模型客户端。布置顶部导入Memory，在GPTResearcher.__init__的self.cfg之后、self.context之前新增self.memory=Memory(embedding_provider='openai',model='text-embedding-3-small')，再self.context_manager=ContextManager(embeddings=self.memory.get_embeddings(),similarity_threshold=.42,max_results10)。采用原项目默认Embedding提供方/模型举一个装配例，不扩其它Provider，不把此前cfg中deepseek聊天占位自动当Embedding服务；模型运行需实际环境支持，构造客户端可校验配置，不调用本步真实服务、不读取密钥。唯一填空self.memory.get_embeddings()，下轮先公布，强调带括号取得对象而非传方法引用，这与to_thread故意传函数引用的情形不同。位置原因研究对象拥有供多个子查询共享的组件/策略，Conductor在后续通过self.researcher.context_manager调用统一入口；构造先创建依赖的模型包装再创建依赖它的上下文管理器。对照原版ContextManager(self)与教学版直接传embeddings的简化区别，避免照抄参数不匹配。当前磁盘AST仍未见ContextManager，可能未保存，不宣称已装配或测试；本轮只布置手写，不改练习文件/联网。下一步替换_process正文直接join为await新上下文入口，再接文档/local/hybrid和向量库适配，完成后助手验证。

第五章手写第6步纠正（2026-10-24）：用户明确“我没有实现你就要带我写”，纠正上一轮直接导入原仓库Memory的教学方案。本项目自己的核心组件若练习尚未实现，应先带写简化实现，再装配；第三方现成类如Document/RecursiveCharacterTextSplitter/EmbeddingsFilter/客户端可导入，但必须先说明归属、作用、输入输出，不把项目内部未写类当已完成。撤回from gpt_researcher.memory.embeddings import Memory，改顶部from langchain_openai import OpenAIEmbeddings（第三方已实现客户端），在ContextManager前模块级手写Memory：__init__(embedding_provider,model)仅允许openai，否则ValueError；创建并保存self._embeddings=OpenAIEmbeddings(model=model)；普通get_embeddings返回该对象。参数保留与上一步Memory装配调用兼容，不展开多提供商/复杂配置。先公布上一轮装配空答案self.memory.get_embeddings()。完整给出简化类，无新增填空；解释Memory拥有模型客户端、ContextManager拥有筛选策略，构造不生成文档向量、getter不发模型请求，实际客户端可校验环境配置，不读取/展示密钥、不做真实调用。本轮仅修正教学指引与索引，不改用户练习；章节仍待全部接线/文档分支/验证。

第五章核心手写第7步（2026-10-24）：用户追问embeddings能否直接传self.memory及装配位置，已说明自写Memory包装对象不同于内部第三方模型客户端，当前包装没有embed_documents/embed_query协议，需get_embeddings()返回客户端；装配位于GPTResearcher.__init__的cfg后context前。上一轮无新增填空。继续替换Conductor原_process_sub_query（不要新增重复同名方法），try内await_scrape_data_by_urls(query)拿材料，然后await self.researcher.context_manager.get_similar_content_by_query(query,materials)，return context；异常打印query与e后空串，复用外层空结果过滤。不再本地读取raw_content后直接join，新的格式含Source/Title/Content。两空①materials、②context，下轮先公布。定位原因_process是第三章gather调度的单子查询入口，Conductor只组织拿材料/调上下文管理器，不实现分块算法；上下文方法第5步已手写，非未实现占位。说明self.researcher.context_manager访问已装配实例、await等待可能的模型筛选、当前函数返回单子查询字符串，外层GPTResearcher仍统一保存context列表，避免逐任务覆盖。小材料仍走快路、未必每次调用Embedding；模型/管线异常可落此except，不能因此把空结果叫成功。未改实际练习文件/测试/网络；网页主链接线布置完成但需用户保存后验证，文档/local/hybrid/已有向量库核心适配仍待继续，不宣布第五章写完。

第五章核心手写第8步（2026-10-24）：先公布第7步答案materials、context。按用户要求项目内部组件先手写，不导入原版DocumentLoader；顶部导入Path与第三方已实现PyMuPDFLoader，模块级在ContextManager前新增简化DocumentLoader类，构造仅接文件路径列表，不实现目录遍历/全部格式。_load_file同步方法try创建PDF loader并load，异常打印并[]；非空page_content逐页转{raw_content:page.page_content,url:str(path),title:Path(path).name}，本版保留来源完整路径并以文件名为标题，仍未保存页码不误称已实现页码引用。async load逐文件await to_thread(self._load_file,path)，extend收集，各文件此版顺序处理但单个同步解析在工作线程，若最终无材料抛ValueError；与原版async函数内部直接loader.load区别明确，避免误称gather即可并行。两空①page.page_content、②path，下轮先公布。定位原因DocumentLoader负责输入解析，ContextManager负责材料后的分块筛选，Conductor后续根据report_source调用load；PDF解析器为第三方现成类，与自写管理类区分。示例一份两页PDF得两条来源一致的材料，接用_to_documents无需新格式。此步未创建真实文件/读取PDF/运行模型/测试或修改练习，只布置代码；下一步接local/hybrid来源分支与路径配置，已有向量库适配仍待补，章未完。

第五章核心手写第9步（2026-10-24）：用户确认DocumentLoader只是读取本地PDF并提醒必要时画图。本轮先公布第8步答案page.page_content、path。为后续local/hybrid接线先只替换ResearcherConductor已有_process_sub_query，签名增加materials=None，在try内if materials is None才await_scrape_data_by_urls(query)，否则直接把传入材料交ContextManager；后续返回字符串/异常打印空串逻辑保留。位置原因单子查询入口负责决定需不需要取得材料，解析仍归DocumentLoader、筛选仍归ContextManager；当前普通web调用不传新参数所以兼容，下一步研究总入口会加载文件并传列表。解释None为“尚未提供材料”，[]为“已提供但为空”，避免if not materials把空本地资料误触发联网；这个教学版明确使用is None，与原版if not scraped_data有差异，文档加载全空在前一阶段已经报错。给两填空①materials is None、②materials，下轮先公布。流程图展示有无材料两支汇入上下文管理器，不画尚未落地的混合来源为已完成。无材料时搜索/去重/抓取，有材料跳过正文抓取；研究规划初搜是否联网仍由后续总入口调用决定，不能因此宣称local完全离线。未改外部练习/实际读PDF/模型/网络或测试；来源总入口/local/hybrid/已有向量库尚待接线，章未完成。

第五章核心手写第10步（2026-10-24）：先公布第9步答案materials is None、materials。实际只读核对外部练习，ResearcherConductor.conduct_research在321行仍是旧规划/gather逻辑，345行_process_sub_query尚未增加materials参数且355行仍return换行join(context)，因此明确提醒保存上一轮替换并直接return context；ContextManager现在输出字符串，join字符串会逐字符插入分隔符。本轮将原conduct_research主体抽为同类新方法_research_queries(materials=None)，gather中把materials传给每个_process_sub_query；原conduct_research暂只return await self._research_queries()，保持web入口可运行，不提前使用未写的来源分支。讲清两个方法都在Conductor类内、为什么总入口选模式/共用方法跑一轮研究、None与同一份本地材料在所有子查询间只读复用、asyncio.gather并发与按输入顺序返回、返回非空字符串列表、规划异常未被子查询catch捕获。用RAG示例展示一份PDF供多个子问题分别筛选，下一步接DocumentLoader和local/hybrid来源。填空①materials（传给子查询），②self._research_queries()（委托网页研究）；下轮先公布。未修改练习、未执行模型/网络/测试，章未完成。

第五章核心手写第11步（2026-10-24）：先公布第10步materials、self._research_queries()。只读核对练习发现428行ContextManager(embeddings=self.memory.get_embeddings)少调用括号，提示改get_embeddings()取得客户端；未修改外部文件。原版skills/researcher.py162–169验证local先DocumentLoader.load后复用研究流程。本轮只在Conductor.conduct_research加web/local分支，web保持_research_queries()，local从简化cfg['doc_paths']列表读取路径，await DocumentLoader(paths).load，research_sources.extend一次登记，再await_research_queries(materials)；其他模式暂ValueError不误落web。GPTResearcher.cfg保留model并增加doc_paths空列表，说明实际用时填写存在的PDF绝对路径，不制造不存在的实例文件。两空①paths②materials，下轮先公布。讲解路径列表→逐页材料→一次规划→并发按子问题筛选→字符串列表→GPTResearcher.context→报告；明确同一材料重复筛选不等于反复读PDF，加载全空抛ValueError不偷偷转web；当前plan_research仍初搜故local不保证离线。给简洁分支图，混合来源下一步、向量库适配仍待，章未完成。未执行API/模型/真实PDF或测试，未把未保存代码当已实现。

第五章核心手写第12步（2026-10-24）：先公布第11步paths、materials。本轮在Conductor.conduct_research保持web分支，将local分支扩为source in ('local','hybrid')，加载本地PDF和research_sources登记只做一次，local直接_research_queries(materials)，hybrid await asyncio.gather(_research_queries(materials),_research_queries())，分别接docs_context/web_context，两者是字符串列表；对非空侧加本地资料/网页资料标签并join内部字符串，返回字符串列表保持ReportGenerator兼容，两侧全空返回[]。给两空①materials②self._research_queries()，下轮先公布。沿实际原版skills/researcher.py171–184说明两路独立规划，各可能初搜一次；本地路只跳过子查询正文抓取，不保证离线；两路同时运行但共享一次研究的状态，网页URL去重仍依赖同一visited_urls。解释gather按任务传入顺序对应解包、不保证先完成先返回；加载失败发生在gather前，所以不会自动兜底web；子查询异常原catch处理，而规划异常仍可让gather向上抛出，gather默认不自动取消另一路。混合只是来源合并无RRF/统一重排/事实裁决。流程图示先加载再并行两路后汇总，具体RAG例子两页PDF加新网页相互补充。未改外部练习或运行测试/实际文件/API，向量库适配/核对测试/工程说明仍待，章未完成。

第五章核心手写第13步（2026-10-24）：先公布第12步materials、self._research_queries()。实际重读原版vector_store/vector_store.py完整43行，核心load转换Document→1000/200分块→后端add_documents，asimilarity_search委托后端(query,k,filter)。练习只读检索确认当前已有ContextManager和_research_queries，无自写VectorStoreWrapper，未改外部文件。本轮在1.py模块级ContextManager之后/ResearcherConductor之前新增自写VectorStoreWrapper；ctor接已有LangChain兼容向量库对象，load过滤空正文转Document保留source/title（原版只有source），split1000/200，空文档直接返回否则store.add_documents(chunks)；async asimilarity_search(query,k=8,filter=None)await同名后端方法。用两填空①chunks②query，下轮先公布。说明适配器并非向量数据库、底层对象以后装配而非字符串路径，索引/Embedding/持久化行为由具体后端决定，k最多数不等于阈值且无额外0.42过滤，普通压缩与向量库存取两条流程分清，load同步后续异步调用要to_thread，query接口async但底层并发/线程依实现，filter支持依后端。用RAG材料存入再提问的具体例子和存储/查询合流图；当前只写类尚未把其接入GPTResearcher/来源分支，不宣称已联网/建库/测试。后续装配、向量查询入口、核对测试和工程说明仍待，章未完。

第五章核心手写第14步（2026-10-24）：用户问适配类是在做什么并要求继续，先解释普通上下文筛选可直接用材料不必入库，向量库路径是材料切块→后端Embedding/存储→按新问题检索，适配器负责格式桥接而非自行实现数据库。公布第13步chunks、query。实际只读核对本机langchain_core/vectorstores/in_memory.py161–170与导出，确认InMemoryVectorStore(embedding=Embeddings)创建空store并保存客户端；练习486行get_embeddings()已正确，不再重复修同一问题。本轮教学版选择第三方真实InMemoryVectorStore而非演示假库，在1.py顶部导入，在GPTResearcher.__init__已有self.memory初始化之后新增embeddings=self.memory.get_embeddings();raw_vector_store=InMemoryVectorStore(embedding=embeddings);self.vector_store=VectorStoreWrapper(raw_vector_store)。两空①embeddings②raw_vector_store，下轮先公布；现有ContextManager装配保留。说明先写好/保存上轮自写VectorStoreWrapper，Memory是Embedding客户端包装并非向量数据库，底层库负责数据/索引、Wrapper负责格式适配、GPTResearcher持有本次任务资源；只构建空库未读文件/未入库/未查询，不宣称模型调用已完成，内存库进程退出不自动保存。用对象关系图解释已有Embedding客户端复用，下一步接实际材料写入和向量查询，未编辑外部练习或运行API/测试，章未完成。

第五章Milvus专项第1步（2026-10-24）：用户明确要求向量库改用Milvus并详细讲解，取消第14步InMemoryVectorStore选型，维持第五章内的原学习路线。实际只读核对repo无Milvus集成依赖，虚拟环境langchain-milvus/pymilvus未安装，Docker CLI29.1.3但Linux引擎管道不存在、19530未发现监听；未安装包/启动服务/读取env。浏览核对Milvus官方Windows部署/RAG文档及langchain-ai/langchain-milvus主仓库源码：Milvus构造embedding_function，server URI19530，Collection/schema/自动ID/动态元数据、首次写入推断向量维度；add_documents由客户端调用Embedding再写Milvus，查询async同理，当前所选外部Embedding模式非Milvus自动生成语义向量。将上一轮答案embeddings、raw_vector_store作废方案中的对照说明，无需再写内存库。教学代码在1.py顶部from langchain_milvus import Milvus；GPTResearcher.__init__在self.memory后用现有embeddings创建Milvus(embedding_function=embeddings,collection_name='research_chunks_v1',connection_args={'uri':'http://localhost:19530'},auto_id=True,drop_old=False,enable_dynamic_field=True,index_params={'index_type':'AUTOINDEX','metric_type':'COSINE','params':{}},search_params={'metric_type':'COSINE','params':{}})，再交自写VectorStoreWrapper。解释连接对象与独立服务分离、Collection类表一行一chunk、source/title/正文/向量/主键的作用，构造不等于正文入库且可能连库失败。修正通用查询接口在Milvus适配时应保留本项目filter参数但底层转expr=filter（表达式字符串），不能原样filter=filter，以官方API为据。索引/度量/k/阈值分清，AUTOINDEX只教学起点不宣称最优，固定模型维度及语义空间须一致；drop_old=False不重建但auto_id=True不去重，跨任务共享collection默认全库检索后续须限定范围。用入库/查询双流程图及RAG片段例子说明；PDFloader当前saved版本raw_content=pages/url=str(Path)和Documentloader命名问题留待接线核对测试时修复，未把这些作为已通过实现。只更新学习记录并提供教学代码，Milvus部署/安装、写入查询接线/实际验收仍未完成，章未完成。

第五章Milvus专项第1步实际落地（2026-10-24）：用户明确授权“你帮我完成这一步”。核对repo及D盘/桌面/课程/外部练习目录无适用AGENTS；未读取env。pip沙箱联网被限后使用require_escalated，先dry-run确认无需升级已有LangChain且无已装protobuf/grpcio/cachetools约束冲突，再在项目.venv安装langchain-milvus==0.4.0、pymilvus==3.0.2（新增cachetools7.2.4/grpcio1.84.1/protobuf7.36.2）。获准写外部D:/桌面/新建文件夹/1.py，保留BOM/换行，先备份1.py.before-milvus-20261024-165307.bak；新增langchain_milvus导入、自写VectorStoreWrapper（356行，过滤空正文→Document保留source/title→1000/200分块→add_documents；async查询filter映射expr），GPTResearcher中复用同一Embedding客户端，self.vector_store默认None，仅report_source=='langchain_vectorstore'时按已讲Milvus参数连接/装配，避免服务未运行时现有web/local构造也报错。未接入后续入库及来源检索分支，未修外部练习中其他既有PDFloader/格式化/local调用错误，留后续必要链路核对。真实保存文件编译通过；AST提取保存的Wrapper/GPTResearcher、真实Document和文本分割器、模拟底层库与模型组件执行4组验证：分块/元数据/空输入，await和expr映射，后端异常向上抛，web/local不连库与vectorstore模式装配及真实已安装Milvus构造签名绑定；全部通过。真实客户端导入成功，TCP19530未连通(code10035)，Docker引擎之前也未运行，故未声称实库建表/入库/查询成功。未启动数据库/读取密钥/调用Embedding付费接口。测试期间原文件未变，最终SHA256 a56387abd3debcb0ef7d2cb3acab9ed80037df46890383f50ee9e66385fc7faf。后续仍需服务部署与连通验收、入库检索接回研究入口以及第五章收尾，章仍未完成。

第五章Milvus专项第2步实际落地（2026-10-24）：用户“继续”，沿上轮已授权修改/验证工作完成真实Milvus服务与PDF链路。Start-Process -WindowStyle Hidden启动Docker Desktop，等待Linux引擎就绪，未改系统/WSL设置。核对官方Windows部署文档，下载v3.0.3 Compose，新增milvus-demo/docker-compose.yml及空compose.vars：官方镜像milvusdb/milvus:v3.0.3、quay.io/coreos/etcd:v3.5.25、milvusdb/minio:RELEASE.2024-12-18T13-15-44Z，独立项目/网络/命名数据卷、容器名project2-study-*，只发布127.0.0.1:19530/9091；显式--env-file compose.vars避免自动读项目.env。首次镜像下载unexpectedEOF，重试成功；当前etcd/minio/standalone均running healthy，HTTP9091/healthz=200，真实MilvusClient.get_server_version=3.0.3。练习外部文件先备份1.py.before-milvus-flow-20261024-170058.bak后获准修改：Documentloader统一DocumentLoader、PDF raw_content改page.page_content/url改str(path)、_format_context改doc.page_content、修正local.load()及research_sources；补上此前已讲hybrid分支。ContextManager新增get_similar_content_by_query_with_vectorstore(query,vector_store,filter)查k8并格式化，无额外0.42过滤；Conductor总入口允许langchain_vectorstore复用规划/gather，_process_sub_query在该来源下直接向量查询不抓正文。GPTResearcher新增显式load_documents(paths)：解析→await to_thread(wrapper.load,materials)→research_sources登记→cfg.vector_filter设为source in+JSON编码路径列表，返回材料页数；入库与研究分开，不自动每次请求重复写入。默认vector_filter=None查询全库，导入后当前对象限定本次文件来源；重复显式导入仍可能重复记录，文件历史版本/去重生产细节待收尾说明。新增milvus-demo/check_chain.py可重复执行，AST提取真实保存类，真实PyMuPDF解析/分割/Milvus数据库/客户端/上下文/报告，Embedding使用六维词频且规划/网页使用替身，未读密钥或付费模型。实际运行全部通过：两页PDF→四chunk入库，额外一条干扰资料，三个研究查询来源过滤正确；不匹配filter返回空上下文；研究前后记录数5不重复入库；local/hybrid流程通过。仅测试独立study_check_0f66f6ec417b4d21b7e89b3a836e1f50 Collection，已drop并核对不存在，未向正式research_chunks_v1写测试向量；服务留运行。保存文件测试前后SHA256=9debd3812a2eaa55a9d518fa60bffdc3cf92afe9dad828d6a4ddd72ff4d494ec一致，已编译通过；新增README记录使用/边界与结果。当前关键行ContextManager._format_context317、get_similar_content_by_query_with_vectorstore356、Conductor.conduct_research429/_process_sub_query467、GPTResearcher.load_documents591/conduct_research606。原planning仍初始联网、报告仍教学拼接、顶层source_urls仍旧visited_urls接口，后续引用章统一，不误称实模效果/全离线/生产完备。第五章其余核心验收与工程注意事项待统一收尾，主清单仍未勾完成。

第五章正式收尾（2026-10-24）：用户询问“第五章还没结束吗”，本轮核对原清单、源码讲解历史、已保存练习核心方法及Milvus验收记录，确认本章约定核心已齐：文档转材料/Document、Embedding客户端接口与装配、分块/普通相似度筛选/小材料快速通道/格式化上下文、web/local/hybrid来源调度、向量库适配/Milvus连接/显式导入/过滤查询/接回研究状态。此前未及时收束而持续保留未完成标记，本轮将原十二单元清单第5项勾选约定核心完成，不扩大到全部辅助格式/全部Provider/生产完备。主要真实验收范围见上一记录；Embedding与规划仍用测试替身，不声称真实语义效果已验证。按用户既定规则本轮补讲工程注意点后结束本章，不再加手写任务：参数是起点需用召回/证据/延迟成本评估；固定Embedding模型和维度；持久库显式重复导入需稳定chunkID/upsert及版本清理；明确文件/知识库检索范围；字符切块与k非最终token预算、两条筛选路径不共享同一阈值；同步解析/写入线程隔离并控制批量并发；接口集成通过不等于回答质量通过。其他提供方细节留第10章，完整质量评测第12章，已写内容检索/详细报告和顶层引用字段归第6章，部署运维细节第11章。用户只问进度，本轮不自动展开第六章；下一次继续从原清单第6章报告生成/引用/格式导出/失败路径开始，先流程与源码后核心手写。无代码或服务额外变更。

第六章讲解第1单元（2026-10-26）：用户在第五章正式收尾后“继续”，开始原清单第6章，先讲解真实源码而非手写。实际读完backend/report_type/basic_report/basic_report.py、skills/writer.py、actions/report_generation.py，定位agent.py451–492、prompts.py262–316及852–876、utils/llm.py41–152、generic/base.py356–399；这些全文/预读不等于已逐段向用户讲完所有辅助方法。当前只讲普通research_report、无自定义提示词/无图片/非subtopic的上下文→普通报告链：BasicReport.run先研究后write_report；GPTResearcher标记_current_step='report_writing'并委托，ext_context or self.context意味着空外部上下文回退；ReportGenerator取上下文并作空白检查（list先join仅用于检查，原context继续传入），无材料返回说明字符串不调用模型，与练习空上下文raiseValueError区分；复制research_params、补角色并添加context/cost_callback；generate_report按类型取默认PromptFamily.generate_report_prompt，将问题、材料、Markdown/格式/语言/字数/引用约束拼成user消息，system为研究角色；await create_chat_completion用smart模型/provider、temperature0.35、stream=True和token上限，底层provider异步累积流并返回完整str，成功时工具层计费回调，字符串原路返回。本入口不自动重做搜索、不直接创建Word/PDF、不在已读方法中写self.report；引用完整流程/导出/详细报告和已写章节检索留后续独立场景。简要说明外层模型调用失败改消息布局重试但不换模型，两次动作层尝试都失败返回空串，提示词构造在try外可直接抛错，内部工具层另有重试留失败路径单元展开。发现writer.write_report未显式传researcher.prompt_family（构造为显式参数不留kwargs），故generate_report默认族可能与初始化选择不同，此差异按代码说明。具体例子用RAG问题和带来源的上下文到两条模型消息，示意输出不是实际模型运行；配简洁调用图，说明async等待网络/流不等于并发起多次写作。当前练习1.py的ReportGenerator529–535仍只拼Markdown，先明确与原版区别。未改练习/上游源码、未读取env、未调用模型或测试，章复选框保持未完成。下一轮继续引用如何进入提示词及后处理，按功能大类讲代表，不把每个提示词变成独立课程；本章核心讲齐后再确认进入手写。

第六章讲解第2单元（2026-10-26）：用户询问stream/temperature后继续，先完成普通报告引用来源链并与详细报告追加参考列表区分。实际读actions/markdown_processing.py全文、DetailedReport全文、server_utils全文作为后续预读，定位prompts.py277–315/555–561、context/retriever.py20–38、agent.py672–739、backend/server/app.py287–323和skills/researcher.py801–820；全文预读不计所有方法已讲解。本单元讲Source/Title/Content携带URL→generate_report_prompt要求正文引用与末尾参考列表→模型生成Markdown→普通报告返回；该已核对链路未实现逐条引用URL白名单比对或论断证据支持验证，提示词MUST不是程序校验。Web分支要求URL及链接，非Web统一要求文档名，hybrid/向量库也走else且通用指令仍要求超链接，未细分来源约束，作为实际代码边界说明。全仓关键目录rg确认add_references除Agent委托之外实际由DetailedReport._construct_detailed_report200–202调用，传conclusion与visited_urls，将追加参考的结论拼到报告尾；普通BasicReport.run并未自动调用此函数。解释helper94–116：构造References标题、sorted集合按URL字典序生成Markdown项目、拼接返回新字符串、错误返回原字符串；同步纯内存格式化无需async，独立于研究对象故在markdown_processing actions，agent方法为便捷委托。集合去重不等于与已有列表去重，空集合仍加标题，已存在References会重复追加。API source_urls只是get_source_urls→list(visited_urls)，并非解析报告实际引用；visited登记在抓取前，不能代表抓取成功/进入context/确实被引用。举a/b/c来源在各阶段不同的例子，给两分支简图，不误把详细报告追加混入普通链。AST提取真实helper和现有test_add_references_order.py两个测试函数执行通过；补测空集合仍标题、已有段不合并、未知正文引用不删除共3边界通过，输出a/b示意URL排序例子。未导入整个项目、未读env/联网/调用模型、未修改练习或上游源码；仅更新学习记录，第6项仍未完成。已覆盖普通生成与引用；后续讲导出完整链、详细报告/已写内容避免重复以及失败路径，核心讲齐后再手写。

第六章讲解第3单元（2026-10-26）：用户继续，按导出功能大类以Word/PDF两例拉通报告Markdown→文件→路径→下载，Markdown辅助只简述不扩课。实际全文读backend/utils.py、backend/styles/pdf_styles.css、本机md2pdf/core.py和tests/backend/test_write_md_to_pdf_filename.py，定位app.py71–75/174–179/287–335、server_utils.py115–123/157–178/256–264；这些预读不等于所有后端行为已讲。本轮主体等待HTTP返回的普通报告：report_information[0]为报告→await write_md_to_word→await write_md_to_pdf顺序执行→JSON包含正文/来源/成本/docx_path/pdf_path，返回路径不是二进制文件；app lifespan将/outputs映射到工作目录outputs，浏览器随后向后端发起文件GET，另有/report/{research_id}通过FileResponse返回DOCX。Word路径112–148：命名/目录→mistune Markdown转HTML→python-docx.Document（区别LangChain Document）→HtmlToDocx填充→doc.save→urllib.parse.quote相对路径。PDF67–110：命名/目录→模块相对CSS→_preprocess_images_for_pdf处理/outputs图片→md2pdf(raw,css,base_url)，已读依赖证实Markdown转HTML再WeasyPrint.write_pdf；图片函数注释称file://但实现实际是绝对路径字符串，作用说明不逐条扩课。write_text_to_md23–39使用write_to_file/aiofiles保存UTF8原文，三个函数名称清理和默认uuid只交代用途不手写哈希。强调outputs相对于启动工作目录非练习脚本目录；返回quote用于URL路径编码不是内容加密；显式同名参数才保证多格式同名。比较WebSocket generate_report_files顺序PDF→DOCX→MD，通过send_json type:path发送路径，与HTTP仅DOCX/PDF区分，非并发；接口async不代表同步转换自动让出事件循环（PDF调用和DOCX save未to_thread）。转换try内异常返回空串，命名/建目录try外、MD写入异常仍可能上抛；空pdf_path不自动导致API报错。本轮由spec直接加载无项目初始化的backend/utils，在临时目录实际验证MD原文/中文编码路径、真实DOCX保存并重开正文标题通过，未检查视觉版式。第一次图片路径断言因Windows混合斜杠误判而在PDF前停止，改验证方式Path.resolve后图片重写通过，仅重跑未完成的PDF阶段；实际md2pdf导入WeasyPrint仍cannot load libgobject-2.0-0(0x7e)，函数返回''，不误称PDF已生成或依赖已修复。临时目录清理，未读env/联网/调用模型，未改练习/上游源码/系统依赖，只维护索引。第6章还待详细报告/已写内容去重及失败路径核心讲解，讲齐后再手写；Windows PDF依赖缺口保留到导出修复/部署验收。

第六章PDF环境修复完成（2026-10-26）：用户要求先修复环境再继续下一步，本轮停止推进课程并修复实际Windows环境。已读pdf技能并按其要求对验收PDF做文本与页面渲染检查，首次生成前成功运行mark_artifact_operation_started.mjs(create,1,pdf)。核对Python3.11.0 64位、WeasyPrint69.0/md2pdf3.1.1已装、系统常见MSYS2/GTK运行库目录不存在，浏览WeasyPrint69官方Windows/缺库说明及MSYS2官方Pango元数据。新增scripts/setup_weasyprint_windows.py：从https://repo.msys2.org/mingw/ucrt64/解析Zstandard格式软件包数据库、解析Pango依赖闭包39包约60.5MiB、逐包核对官方索引SHA256，仅抽取64个原生DLL及辅助数据/许可证到.venv/weasyprint-runtime，安装manifest和使用Windows系统字体的fontconfig配置；在此venv的site-packages创建_project2_weasyprint_runtime.py及weasyprint_runtime.pth，每个新进程自动配置WEASYPRINT_DLL_DIRECTORIES和FONTCONFIG_FILE，未写全局PATH/注册表，未替换backend导出函数。最初数据库按gzip自动识别失败，按实际zstd头修正后安装成功；沙箱内字体缓存写入提示在正常权限进程下消失。真实weasyprint --info返回69.0/Pango15802成功。原项目backend/utils.py直接加载、真实write_md_to_pdf生成outputs/pdf_environment_check.pdf，复制最终验收文件到output/pdf/pdf_environment_check.pdf，1页27829bytes；PyMuPDF重开中文标题/正文/链接通过，隔离FastAPI StaticFiles下载HTTP200/content-type application/pdf/字节一致通过；Poppler渲染PNG并目视确认中文、表格、列表、超链接无方框/截断，未调用模型/读取env。跨工作目录验证发现D:/桌面/新建文件夹/copy.py遮蔽标准库且IndentationError，读取确认是未完成练习且无其他本地import引用，明确告知用户后用获准Rename-Item改为copy_practice.py，限定父目录并SHA256校验内容不变；从该练习目录再次运行weasyprint --info成功，copy.__file__正确为D:/py3.11/Lib/copy.py。新增PDF_ENVIRONMENT.md记录安装/恢复/验证与重启现有进程要求。此前第二章和第六章记录的libgobject-2.0-0阻断现已解决，不再列为待修；第六章仍待详细报告/已写内容去重与失败路径讲解、确认后核心手写。此轮未推进新课程单元，未改外部1.py或上游研究算法。

第六章讲解第4单元（2026-10-26）：PDF原生环境修复后用户“下一步”，本轮进入详细报告章节编排，仍源码讲解不手写。实际重新全文读DetailedReport及WrittenContentCompressor，核对websocket_manager.run_agent116–183、ContextManager89–155、SectionRetriever40–71、utils.llm.construct_subtopics155–217/validators、writer委托/草稿动作、prompts573–704/引言结论及agent共享状态初始化。以report_type=detailed_report/report_source=web为例，路由构造DetailedReport→父GPTResearcher内部research_report→run初始总研究/结构化子主题/总引言→for+await顺序逐章→目录/结论/References拼接返回Markdown，接已有导出。区分subtopic（报告章节）与sub_query（章节内检索查询），内部子GPTResearcher.report_type=subtopic_report、parent_query为总问题、复用角色/传入global_urls，章节内部检索可并发但章节本身串行。说明existing_headers、global_written_sections实际list[dict]、global_context、global_urls四类状态及归属；每章研究→草稿标题→根据当前章节和草稿标题检索已写段落→提示词传既有标题及相关已写片段→生成正文→extract_sections登记正文/更新标题来源。已写检索原理复用第五章：SectionRetriever转Document→1000/100分块→EmbeddingsFilter默认阈值0.5→格式化Title/Content字符串，多个标题查询gather，集合合并去重截10条（不是全局相关度重排）；最终防重复依赖提示词，不是生成后逐段强制语义去重。目录从正文标题解析，引言来自初始研究，结论以完成正文为输入，References使用visited集合（已讲边界）。指出当前代码与理想流程差异：草稿动作返回list[str]而Detailed169–172用str(list)，Markdown标题解析常为空；global_context普通web为str，_hashable_context按字符迭代后set去重损坏，且给child预置context后conduct_research又会替换，不能宣称完整复用总上下文；global_context187为替换并非显式累加全部历史。construct_subtopics成功为Subtopics模型但异常返回list，非空fallback会与.subtopics读取不一致，留失败路径单元；child配置/费用汇总等生产注意点留收尾不扩课。通过AST提取真实extract_headers/extract_sections/_hashable_context确认str标题列表→[]、换行join→2标题、正文段为section_title/written_content字典、'RAG'→['R','A','G']；第一次自建AST测试缺lineno只属验证脚本问题，fix_missing_locations后第三项通过，不归咎项目源码。未调用模型/网络/读env、未改练习/上游源码、未宣称原版详细报告整条实模跑通。配两章节RAG例子和串行状态回流图，按功能类收束详细报告，不逐个提示词另起课程。第六章普通生成/引用/导出/详细章节及已写内容链已覆盖，下一单元收束失败路径与核心范围核对，再经用户确认手写。

第六章讲解第5单元/核心讲解收束（2026-10-26）：用户继续，复核writer空材料检查、generate_report提示词构造/两种消息布局、utils.llm重试循环、导出返回与app响应组装，完成失败路径及约定核心范围核对；不扩展新Provider/提示词家族课程。用同一RAG请求说明三种不同信号：无材料返回非空说明字符串（不调用写作模型，上层仍可导出说明），生成失败动作层吞异常返回''（调用方未统一校验空报告），导出try内失败返回空路径但可保留正文与另一个格式；命名/目录/提示词等try外异常仍可能上抛。工具层stream且websocket参数非None时max_attempts1，否则10，异常和空输出都会指数退避1/2/4/8秒封顶，失败抛RuntimeError；动作层在工具层失败后将system+user改为单user重试一次，模型/provider不变，不能当成第三章战略/备用模型降级。特别指出HTTP app给run_agent websocket=None但run_agent会创建CustomLogsHandler并传给BasicReport，所以不能按HTTP就推断websocket参数None/10次；若已发送部分流再外层重试，可能重复内容。工具层client创建在重试循环外、成功路径才进行当前实现的成本回调，不应将失败尝试费用视为必然已计全。详细报告补充空章节字符串会跳过、非空说明会当章节保留、未捕获异常中断串行链，construct_subtopics返回类型失配属于可能上抛的已读边界；WebSocket外层错误转日志消息与HTTP等待路径无同一结构化状态，取消会单独reraise。核心已讲齐：普通模型写作、来源引用及局限、真实Word/PDF/MD输出、详细章节与已写内容检索、失败与重试；仅代表性功能，不宣称所有辅助文件逐行穷尽。下一轮经用户继续/开始进入现有1.py的核心手写：组装写作消息/可替换模型调用、基本引用约束、复用已有导出、简化串行详细报告与已写状态、区分生成/导出失败；配置简化、不重写底层SDK/导出库/哈希/后台开关。AST提取真实ReportGenerator、generate_report、create_chat_completion和app.write_report，模拟模型/睡眠/导出，七项验证通过：空材料无调用、动作层改消息不换模型、两次失败空串、提示词异常上抛、工具层异常/空响应恢复及成功回调一次、流式非None输出对象仅一次尝试、空PDF路径仍保留报告/Word路径。初次测试缺Any属于测试namespace，修正后Windows沙箱asyncio初始化阻塞，已中断该测试进程并用正常权限重跑成功；无真实模型/网络/密钥读取、无应用代码修改、无残留测试文件。第6章仅核心讲解完成，未标整章完成。

第六章核心手写第1步（2026-10-26）：用户明确“开始”，进入已讲齐核心后的手写，不再扩展源码课。只读核对实际D:/桌面/新建文件夹/1.py526–535的ReportGenerator仍为query/context拼接，无write_model装配；保留原类与write_report，先在__init__之后/write_report之前新增普通def _build_messages(self,context:str)。方法归ReportGenerator因负责写作输入组织，由下一步write_report调用；读取researcher.query及role（空角色用简短中文写作角色），接收已归一化的正文字符串，构造user_prompt包含研究问题/研究材料/中文Markdown/保留给定来源/材料不足说明；返回system/user两条消息字典。两个填空①system_prompt②user_prompt，下轮先公布答案。解释self.researcher.role控制写作身份、query定义问题、context提供证据；列表转正文字符串会在调用处完成，类型注解不会替代归一化。纯内存拼接无网络故用def；输出消息列表而非最终报告，后续再写可替换写作函数及await接线。使用RAG问题+rag.pdf材料的具体输入输出示意及简洁流程说明；不引入未解释的GPTResearcher/新项目类、不增加research_params配置字典、不用原角色demo_model冒充写作模型。未编辑外部练习/调用模型/运行新测试，不宣称此步已保存验证；下一步公布答案后实现写作函数接口并逐步升级现有write_report。

第六章核心手写第2步（2026-10-26）：用户继续，先公布第1步system_prompt、user_prompt。只读磁盘1.py仍未见_build_messages或write_model（可能未保存），明确提醒先保存上轮方法，不把已讲等同已实现。本轮用一个小单元接通“上下文→消息→异步写作函数→字符串返回”：模块级在已有demo_*函数附近新增async demo_write_model(messages)固定返回中文Markdown演示正文，明确测试替身/真实接口第10章且无真实语义写作；GPTResearcher.__init__在backup_plan_model后新增self.write_model=demo_write_model，解释保存函数引用无括号，和最终调用await的区别。替换既有ReportGenerator.write_report：取context，列表则双换行join，if not context or not context.strip抛ValueError，messages=self._build_messages(context)，report=await self.researcher.write_model(messages)，return report。两空①context②messages，下轮先公布；已有_build_messages保留不重复定义，继续不建research_params、不增加复杂配置。解释普通消息构造def与异步模型等待分工，演示函数为接口兼容而async，当前立即固定返回；展示两材料字符串列表到两消息再到演示报告的单条图。尚未增加生成结果类型/空白校验或失败恢复，这些下一步作为生成边界处理；不声称完整第6章写完。未编辑用户练习、未调用真实模型或运行测试，仅维护学习索引。

第六章核心手写第3步（2026-10-26）：用户继续，先公布第2步context、messages。只读核对实际1.py：demo_write_model144–145已保存；ReportGenerator528–559仍旧拼接式write_report，用户将消息方法命名build_messages（无下划线）且system_prompt错误读self.role；GPTResearcher未见write_model装配。本轮先对齐已保存版本：保留用户build_messages命名，改该方法为self.researcher.role；GPTResearcher.__init__在backup_plan_model后加self.write_model=demo_write_model（8空格同级）；不用重写已保存demo函数。完整替换现有ReportGenerator.write_report以接通上轮：context列表双换行join，检查空白，messages=self.build_messages(context)，report=await self.researcher.write_model(messages)，再新增类型与空白检查：非str抛TypeError、report.strip后空值抛ValueError、最后return report。两个新空①str②report，下轮先公布。解释两个self作用域、保留方法名只需调用一致、返回值不强行str化以免把None/dict误当正文、先验类型后.strip、校验失败会让调用方await抛错停止后续导出，但API错误结构后续接线尚待。本轮仍教学供用户手写，未修改外部1.py、未调用模型或做未保存代码的测试。用None/字典/空白字符串/有效Markdown四输入例子及简洁校验流程图说明，测试由助手后续核验。下一步核心失败恢复/引用与详细报告简化流程继续，章未完成。

第六章核心手写第4步（2026-10-26）：用户继续，先公布第3步str、report。实际只读核对1.py528–575：写作调用与返回类型/空白检查已保存、GPTResearcher601行write_model装配已保存；但write_report540行仍调用self._build_messages，实际定义554行为build_messages，先明确统一调用为self.build_messages(context)，避免AttributeError，保留用户命名。context join缩进更深但合法，不误报语法错误。本轮仅在ReportGenerator内新增async _call_write_model(self,messages)，与write_report同级：try await self.researcher.write_model(messages)，except Exception构造单条user的fallback_messages，content用messages[0]['content']+'\n\n'+messages[1]['content']合并已知两消息，第二次await不再包try，失败向上抛；这依赖当前_build消息固定system/user二条的契约，非通用任意聊天历史合并器。两空①messages②fallback_messages，下轮先公布。write_report将直接调用改为await self._call_write_model(messages)，既有返回类型/strip/空白检查保留。解释当前self重试方法与researcher.write_model实际函数引用分工，正常只调用一次、最多两次本层函数调用、不换模型、第二次失败不吞空字符串；非空/类型校验在外层，不触发此简化的调用异常重试（原工具层另有空响应重试，非全照搬）。用两消息合成一消息例子和失败恢复小图说明。未修改练习/上游源码、未调用模型或对未保存新代码宣称测试通过。后续引用来源、简化详细报告与最终验收继续，第6章未完成。

第六章核心手写第5步（2026-10-26）：用户询问write_report与write_model调用层级后继续，先公布第4步messages、fallback_messages。实际只读1.py发现用户已将方法与调用统一为_build_messages，沿用当前命名不再反向要求改名；write_report仍直接调用write_model，磁盘未见_call_write_model，提示保存上轮恢复方法/调用改动，不把未保存状态宣称已完成。当前get_source_urls659–660仍返回visited_urls，教学版改为从research_sources逐材料提取url、跳过空值、按首次出现去重，保留visited_urls用于抓取登记。明确此getter返回已收集材料的来源标识（网页URL或本地文档路径），不是实际正文引用集合；相对原版getter语义调整有意说明。ReportGenerator新增同步_append_sources(report)：调用getter，无来源原样返回，有来源按sorted排序、http/https生成Markdown链接、本地路径写普通文本，最后追加##资料来源；写作结果有效性检查后return self._append_sources(report)，消息提示新增正文标注来源/末尾列表由程序统一追加。两新空①self.research_sources②self._append_sources(report)，下轮先公布。解释状态归GPTResearcher故getter放该类、版式归ReportGenerator故追加放该类、两个def纯内存操作、URL去重与内容去重/证据支持核验不同，列的是收集材料并非证明每条都被引用。用重复A/B材料到去重列表再到报告尾的例子和一张简图，原版对照参考列表逻辑已在讲解部分完成不再扩Provider。未改外部练习/调用模型/做未保存新代码测试；后续简化详细报告与生成/导出接线和最终验收待做，第6章未完成。

第六章核心手写第6步（2026-10-26）：用户继续，先公布第5步self.research_sources、self._append_sources(report)。实际只读练习仍未保存恢复方法/来源getter改动/追加方法，提醒编辑器代码需一并保存，不把已讲当已实现；已存在BasicReport182–193、无DetailedReport。按已讲原版详细报告流程开始简化核心手写，先只在BasicReport之后/BrowserManager之前新增模块级DetailedReport类：__init__(query,report_source,report_type)保存外层参数，self.gpt_research=GPTResearcher(query=query,report_source=report_source,report_type='research_report')作为总研究对象，self.existing_headers=[]及self.global_written_sections=[]保存跨章节结构；研究上下文/来源/visited记录直接由gpt_research已有状态持有，避免重复复制与原版字符串上下文问题。两空①'research_report'②[]，下轮先公布。解释外层detailed_report选择章节编排、内部research_report作为基础研究任务，类名不同职责不同；__init__准备状态，真正研究由后续run触发；两个列表分别存已写标题和section_title/written_content字典，不混成同一种状态。给RAG两章节例子，初始为空、第一章后填标题和正文，后续章节据此减少重复；讲清文件/类/缩进及位置原因（BasicReport和DetailedReport均为报告调度器）、未来run_agent会调用但当前不修改400分支或使用尚未实现run。未改外部文件/运行模型/测试，下一步补总研究后的章节规划入口，再接串行章节写作。

第六章核心手写第7步（2026-10-26）：用户继续，先公布第6步'research_report'、[]。只读当前1.py未见DetailedReport/demo_subtopic_model，不能宣称新增类已保存；实际核对normalize_queries19–46可用于字符串列表的非字符串过滤/strip/去重/截断/空列表回退总问题，故复用而非重写同类JSON校验。本轮在已有demo函数附近模块级新增async demo_subtopic_model(messages)，json.dumps固定两RAG章节字符串数组，明确测试替身并非真实章节规划；DetailedReport.__init__中保存self.subtopic_model=demo_subtopic_model，职责为章节规划不同于检索子查询plan_model。类内新增async _plan_subtopics：从gpt_research.context取已有总研究材料，若list双换行join，构造system要求JSON字符串数组及user总问题/材料/最多3个按顺序不重复章节，try await self.subtopic_model(messages)+json.loads，except parsed=[]，最后normalize_queries(parsed,query=self.query,max_queries=3)返回list[str]。两空①self.subtopic_model(messages)②self.query，下轮先公布。解释成功JSON字符串→Python列表、异常/无有效项回退[总问题]，统一输出类型避免原版Subtopics对象/列表混用；仅复用规范化功能不混淆报告章节与检索查询。位置原因模块demo为可替换接口、模型函数引用和章节流程归DetailedReport，未来run先总研究再调此方法；当前不写临时return列表的run，避免改变报告字符串契约，未提前路由到未完成类。给两章节RAG例子与规划流程简图；未修改练习/调用模型/运行新测试，第6章仍在核心手写。

第六章核心手写第8步（2026-10-26）：用户关于self/参数的概念问题已答后继续，先公布第7步self.subtopic_model(messages)、self.query。只读保存文件仍未见精确命名DetailedReport，不把已教代码当保存完成；现有GPTResearcher query/report_source/report_type三参数、context/research_sources/visited_urls及上下文筛选接口已存在。本轮在上轮DetailedReport类内新增async _research_subtopic(self,subtopic)，以web来源章节研究为代表：构造child GPTResearcher(query=subtopic,report_source=self.report_source,report_type='subtopic_report')，继承父agent/role/write_model，并将child.visited_urls指向父集合，await child.conduct_research；保留new_materials=child.research_sources，将父缓存材料+新材料合为新列表，再按章节问题调用child.context_manager.get_similar_content_by_query重筛；child.context统一为[context]或[]，父research_sources.extend(new_materials)登记新资料，child.research_sources=materials保留本章可访问来源，最后返回child对象供后续写作。明确仅共享去重集合会使已抓网页无法重新获得正文，故必须复用材料缓存；先保留新材料再登记/给child赋合并列表，避免把所有旧材料重复extend到父。两空①subtopic②self.gpt_research.visited_urls，下轮先公布。通过父A/本章搜索A+B例子说明A不重抓但缓存仍可筛选、B抓取后登记，结果不是已写正文；方法返回研究对象而非报告字符串，因为后续要用其context和writer。用当前self=DetaileReport、父gpt_research=长期对象、参数subtopic=每次变化章节强化用户刚问的self/参数区别；async等待研究/筛选，异常未被内部处理则上抛；此方法不承诺原版所有来源组合/配置传递已完整复现。原源码草稿/上下文字符问题采用本教学版显式原材料合并避免，不照抄错误。未修改外部文件/调用网络模型/运行未保存新代码测试，后续已写内容检索/章节写作/总报告run与API接线仍待。

第六章核心手写第9步（2026-10-26）：用户继续，先公布第8步subtopic、self.gpt_research.visited_urls。只读核对实际ContextManager278–368已有_to_documents/_split_documents/_filter_documents/_format_context和普通/向量查询接口，阈值0.42/max_results10，未见DetailedReport或已写正文检索方法。本轮只在ContextManager类中新增async get_similar_written_contents(self,query,written_sections)：将非空written_content的章节字典转真实Document(page_content=written_content,metadata.title=section_title)，无文档返回''，复用_split_documents及await to_thread(self._filter_documents,query,chunks)，最后将相关Document格式化为Title/Content字符串双换行join。两空①query②chunks，下轮先公布。解释ContextManager拥有Embedding/分块筛选工具，DetailedReport拥有global_written_sections和当前章节问题，因此后两者通过参数传入，不在管理器上复制调度器状态；未来章节写作流程会调用该方法。输入旧正文不是新抓网页，结果用于提示模型避免重复，第一章因列表空不调用Embedding；若筛选异常未内部捕获则上抛。手写简化沿用现有0.42/结果上限，原版WrittenContentCompressor路径默认0.5；原版还用草稿标题多查询，教学版用章节名跑通核心，不重复手写相同管道或引入额外草稿模型调用。例子已写RAG工作原理与当前检索局限，返回相关既有段落作提示而非再次当新证据；无语义去重保证、示例结果非真实模型评测。未改外部文件/运行模型或测试，下一步接章节写作提示与跨章节状态更新。

第六章手写概念澄清：research_sources写入位置（2026-10-26）：用户问“为什么保存在research_sources代码在哪”，不推进新手写步骤。只读当前1.py核对初始化630行self.research_sources=[]，Conductor._scrape_data_by_urls521–527中抓取/合并prefetched后526行self.researcher.research_sources.extend(materias)为网页实际登记；本地/hybrid439行和GPTResearcher.load_documents677行也是材料登记点，context691行为研究返回的筛选上下文。解释child.conduct_research→其Conductor→_scrape...中的self.researcher指回child，所以材料确实写入child.research_sources，不是自动按字段名保存；属性保存清洗后的正文/URL字典以供后续章节缓存复用及来源列表，context保存筛选格式化后的字符串，两者用途/类型不同。已写章节另存DetailedReport.global_written_sections，不与research_sources混淆。发现当前get_source_urls698行误遍历self.context后item.get('url')，明确指出应改为遍历self.research_sources，否则字符串无.get；只给准确修正位置/代码，未编辑外部文件。查询已有Milvus库本身只返回context、并不自动登记research_sources，显式load_documents会登记，避免全来源分支泛化。给实际行号链接和网页材料保存小流程，本轮未读env/运行模型/修改应用；第9步未答填空query、chunks仍下次继续先公布。

第六章核心手写第10步（2026-10-26）：用户继续，先公布第9步query、chunks。实际只读1.py已见DetailedReport202–256及_plan_subtopics；其内部父GPTResearcher215行误传外层report_type，改应固定'research_report'；章节模型引用被放在GPTResearcher701而_plan_subtopics调用self.subtopic_model（self为DetailedReport），明确将装配行放到DetailedReport.__init__，避免AttributeError被except吞成单章兜底。ReportGenerator已保存重试与来源追加方法，但调用仍未接通，_append_sources615调用get_sources_urls拼错、列表项缺空格、get_source_urls761仍遍历context；这些最终接线需修，未宣称完成。当前单元只扩展已存在ReportGenerator._build_messages签名为(context,main_topic='',existing_headers=None,relevant_written_contents='')，保留原普通报告提示和返回system/user列表，在return前按report_type=='subtopic_report'追加章节指令：总问题/已有标题/相关已写内容，研究材料作为事实依据、旧内容作为结构去重参照，##本章/###小节，仅章节正文，整篇引言结论和末尾来源交总调度。两空①main_topic②relevant_written_contents，下轮先公布。三个新增参数由未来详细报告写作调用传入，不存成ReportGenerator自身全局状态；强调self.researcher.query在该分支为本章题目，main_topic为总问题，role取对象固定状态而旧内容为每次输入。只定义可兼容普通调用的消息接口，下一步才扩展两层write_report传参并接章节写作，当前不称防重复链已运行。用RAG原理已写/局限待写例子及多输入到模型消息简图，普通路径仍兼容默认参数。未修改外部练习/执行模型/运行新测试，章未完成。

第六章核心手写第11步（2026-10-26）：继续第10步，先公布两空main_topic、relevant_written_contents。只读核对当前练习：ReportGenerator692行write_report仍无新增参数，715行_build_messages仍旧签名，GPTResearcher818行write_report仍无参数；提醒先补上第10步的提示词签名/分支，否则关键字传递会TypeError。本轮给出替换两层write_report：GPTResearcher入口转发main_topic/existing_headers/relevant_written_contents；ReportGenerator整理context、空值检查、构造消息、调用已写_call_write_model、验证字符串及非空，subtopic_report只返回章节正文，普通报告调用_append_sources。新两空①self._call_write_model(messages)②self._append_sources(report)，下轮先给答案。指出_append_sources677行get_sources_urls应为get_source_urls，683/685行Markdown列表项补空格；当前get_source_urls823行已遍历research_sources，确认这项已修复。说明两层同名方法属于不同对象，转发参数不重新研究；用RAG局限章节/总问题/旧标题及旧正文解释调用与返回。仅教学和索引更新，未改外部练习、未运行模型或宣称测试通过；DetailedReport章节调度与总报告装配仍待接通，第六章未完成。

第六章核心手写第12步（2026-10-26）：先公布第11步两空self._call_write_model(messages)、self._append_sources(report)。只读当前练习确认DetailedReport202行，父研究者固定research_report和该类subtopic_model已保存，_research_subtopic258–287已保存，ContextManager462行已有get_similar_written_contents；两层write_report及_build_messages仍旧签名，提醒先补第10/11步，不能宣称已接通。本轮只新增DetailedReport._write_subtopic，放_research_subtopic后、BrowserManager前（类内四格缩进），先await研究返回child，再通过child.context_manager用当前章节名检索global_written_sections，调用child.write_report传总问题/已有标题/相关旧正文，成功后记录existing_headers及global_written_sections字典并返回正文。两新空①self.global_written_sections②relevant_contents，下轮先公布。说明调度与历史状态属于DetailedReport；ContextManager负责筛选工具；GPTResearcher负责当前研究与写作入口；append保存单个章节字典，return返回章节字符串。第一章无历史返回空字符串，第二章可检索第一章，章节串行调用由下一步run实现。异常上抛时不追加成功章节历史，但此前抓取/来源状态可能已变化，不误称事务回滚。给两章RAG例子及完整单章流程图；未编辑外部练习/运行真实模型/宣称测试通过，第六章仍待总调度、组装和验收。

第12步核对补充：实际get_similar_written_contents486行把written_sections误传给_filter_documents，应该传481行得到的chunks（Document列表）。本轮同时给出该调用的准确修正，解释原始章节字典列表不满足Embedding筛选器的Document输入约定；未直接编辑练习文件。

第六章核心手写第13步（2026-10-26）：先公布第12步两空self.global_written_sections、relevant_contents。实际只读练习确认_build_messages已扩展，但两层write_report仍旧签名，DetailedReport尚无_write_subtopic，提醒先补前两轮，未宣称已运行。本轮在DetailedReport内新增async run（__init__后，四格缩进）：先await父gpt_research.conduct_research→await_plan_subtopics→局部sections列表→for逐章await_write_subtopic并append返回正文→双换行join返回正文。两空①self.gpt_research.conduct_research()②self._write_subtopic(subtopic)，下轮先公布。明确run当前返回详细报告正文的中间成果，引言/目录/结论/统一来源列表留下一步组装，API分支尚未接入；不引入未实现的组装接口，也不声称整章完成。用RAG总问题/原理章/局限章说明父研究一次、章节串行及已写历史依赖；async/await顺序执行并非自动并发，章节内部检索仍可并发；失败会中断循环上抛，已写历史仍保留。本轮仅教学和索引更新，未编辑外部练习/调用模型/运行测试。

第六章核心手写第14步（2026-10-26）：先公布第13步两空self.gpt_research.conduct_research()、self._write_subtopic(subtopic)。只读练习确认第12/13步方法尚未保存，_build_messages已更新但两层write_report仍旧签名，未称可运行。核对原版DetailedReport84–90在整体研究和规划后生成引言，197–202从正文生成结论并拼目录/来源。本轮仅在ReportGenerator新增教学简化write_summary(self,section_title,content)：列表内容join、空材料检查，选择引言任务（背景/范围）或结论任务（综合主要发现/局限、禁止新事实），构造两条system/user消息（角色/总问题/材料/##标题/仅该节正文），await已实现_call_write_model，检查非空字符串后strip返回，不追加来源/不改context。两空①content②self._call_write_model(messages)，下轮先公布。引言输入父研究context，结论输入拼接后的body；用两行未来调用示例说明DetailedReport下一步run将直接通过父研究者的researcher_generator调用该复用方法，减少原版两层专门包装但保留不同输入职责。解释内容通过参数传入因两次来源不同，query/role从对象读取；不调用write_report避免触发整篇提示与来源追加，旧演示模型仍固定输出不保证内容质量。未修改练习/执行模型/运行测试；下一步完整run组装标题、引言、目录、正文、结论、统一来源，再接API分支和验收，章未完成。

第六章核心手写第15步（2026-10-26）：先公布第14步两空content、self._call_write_model(messages)。实际只读练习确认近几轮DetailedReport.run/_write_subtopic与ReportGenerator.write_summary尚未保存，提醒需补齐，未当作已实现。给出DetailedReport.run完整替换（构造函数后四格缩进）：整体研究→规划→取得父researcher_generator→write_summary('引言',父context)→逐章await_write_subtopic并收集正文→join body→write_summary('结论',body)→根据规划章节生成编号文字目录→join总标题/引言/目录/正文/结论→父writer._append_sources一次。两空①body②writer._append_sources(report)，下轮先公布。说明目录仅编号文字，无锚点解析，比原版从正文标题提取目录简化；字符串组装/来源列表无等待不await；收集来源来自各章研究时汇总至父research_sources，并非逐条引用核验；提醒已发现_append_sources方法名拼写仍未修。明确这里只定义完整组装主链，API分支尚未接入，实际保存与测试尚未完成，不能勾章。用RAG整篇报告结构、状态共享和顺序执行流程图解释，未调用真实模型、未改外部练习、未运行新测试。

第六章核心手写第16步（2026-10-26）：先公布第15步两空body、writer._append_sources(report)。只读当前练习确认DetailedReport._write_subtopic及两层写作参数已保存；DetailedReport.run220–233仍简版且228误调用_research_subtopic返回对象后join会TypeError，明确应调用_write_subtopic并用第15步完整run替换（write_summary已可从该类使用，仍待实际验收）。本轮完整替换模块级run_agent953行：保留params字典与multi_agents未实现400分支，detailed_report创建DetailedReport(**params)，else创建BasicReport(**params)，将await runner.run、return_researcher分支、普通return从原else中移出到共同路径。两新空①DetailedReport(**params)②runner.gpt_research，下轮先公布。说明同一run入口+同名父研究者属性使上层write_report请求处理函数的导出/元数据读取可复用；详细分支返回父研究对象并非每个child，不保证get_costs聚合所有章节调用。用详细请求逐步说明task→query字典解包、流程选择、报告str与父研究对象tuple返回；400属于显式暂未实现，不把该分支当LangGraph已完成。未改练习、未运行真实调用/测试；接线教学已给出，下一步核对保存代码并测试，随后补生产注意事项，第六章仍未勾选。

第16步状态勘误：上条括号中“write_summary已可从该类使用”指教学接口已给出，不能视为已保存；本轮rg未发现实际write_summary定义，实际运行还需补上第14步方法。待后续读取和测试再确认。

第六章核心手写验收与工程收束（2026-10-26）：用户继续验收，先公布第16步两空DetailedReport(**params)、runner.gpt_research。实际读取完整外部练习（无env），发现两层write_report和write_summary已保存，但DetailedReport.run仍误用_research_subtopic返回对象、无整篇组装；run_agent仍400拒绝详细报告且共用返回逻辑缩在else；_append_sources方法名get_sources_urls拼错且Markdown列表缺空格。依据此前用户授权直接修正，在require_escalated下先备份至D:/桌面/新建文件夹/1.py.before-chapter6-20261026-163759.bak，再替换已讲过的完整DetailedReport.run与run_agent、修正来源列表三处文本；编译成功，保留其余实现与演示模型。最终练习SHA256为7c5e8300ad6099af5307dcec8e0b790b67b8685d20690c0cf91079284e1f87a4，关键位置DetailedReport.run220、_write_subtopic313、ReportGenerator727来源追加/743写作/778摘要、GPTResearcher.write_report946、run_agent964。

新增scripts/check_chapter6.py，AST提取实际保存的类/函数，跳过项目导入和启动块；真实运行练习调度、上下文转换、Document、分块、EmbeddingsFilter、消息构造、重试、FastAPI处理器，搜索/抓取/模型/Embedding/导出用确定性替身，不访问服务/数据库/密钥、不生成新PDF。首次检查因测试向量用词频导致长段范数偏差、旧内容被阈值过滤而失败；修正测试替身为有无词项特征（未为此改练习），重跑17项全部通过：语法与隔离装载；空上下文/摘要阻止调用；资料去重与排除只访问未收集URL；双消息失败后单用户重试；两次异常上抛；错误类型/空输出验证；章节参数穿透且无末尾来源；旧正文真实Document分块筛选；普通分支str/tuple返回；详细组装顺序/父子共享URL/历史传递；全URL已访问时复用材料；坏章节JSON回退原问题；第二章失败保留第一章历史和材料；普通/详细HTTP200并向两导出适配器传相同报告；缺字段422/未实现multi_agents400；PDF空路径保留正文与Word；未捕获导出异常HTTP500。检查后练习字节未变化。FastAPI测试客户端有上游httpx弃用提示但未影响结果，未改依赖。本轮不重复此前实际Word/PDF原生环境验证，也不宣称真实模型/Embedding语义效果或详细报告local/hybrid/Milvus全部组合已验证。

本章验收后工程注意点（口头解释，不加入手写代码）：提示词减少重复/限制标题是软约束，应另验生成结果及引用；visited登记、成功抓取、进入上下文、正文实际引用是不同状态，来源清单不构成逐条证据核验；重试需结合错误类别/超时/预算，流式重试可能重复已展示文本，原版失败可能空串而练习抛错；async函数内部同步PDF/Word转换仍阻塞事件循环，应在线程运行同步工作或独立任务，不将async函数直接传to_thread误当完成转换；详细报告父对象成本不自动累加子对象，配置/材料/cache随源类型需明确传递，当前代表测试覆盖web；导出固定practice_report文件名在并发请求会覆盖，失败空路径与报告成功需分别表达。原版详细报告已讲的字符串context逐字符处理、草稿标题列表str化再按Markdown解析、上下文被研究结果覆盖等差异保留为已识别问题，未擅自修改原工程。第六章按约定核心收束并勾选；辅助文件与真实质量评测不因此宣称全部覆盖；下一次继续进入原清单第7章，先讲DeepResearch完整业务流程，再逐条调用链，未经确认不直接开始新章手写。

第六章再次对照核定（2026-10-26）：用户要求对照确认核心是否讲完。重新读取本章第1–5源码讲解记录、核心手写验收/工程收束记录，对照原版writer/report_generation/markdown_processing/backend.utils/DetailedReport函数目录、当前练习实际定义与完整run/run_agent/导出链及check_chapter6.py断言。确认普通写作、消息与异步接口、重试及失败、来源引用边界、详细报告串行编排、已写内容检索、引言目录结论/来源组装、格式导出与上层返回、工程注意点均在约定范围已覆盖；导出按用户要求复用原库，Markdown只讲用途不重写，手写目录为编号文字且未复刻SDK流式内部。实际文件SHA256仍为7c5e8300ad6099af5307dcec8e0b790b67b8685d20690c0cf91079284e1f87a4，与17项通过时一致，因此本轮不重复跑相同测试，也不误称新增测试。真实模型Provider接入留10章、质量评测留12章，详细报告全部来源组合不在本次已验收范围。保持第6项约定核心完成；本轮只回答核对结果，不提前进入第7章、不增加新手写任务。

第六章手写范围澄清（2026-10-26）：用户指出导出及工程注意点两行没有手写。确认：导出仅在练习上层调用已有backend.utils函数并返回Word/PDF路径，未手写Markdown保存/Word转换/PDF转换函数；真实导出验证不等于用户亲手实现转换逻辑。并发阻塞、子研究者成本汇总、并发文件名覆盖等仅讲解，未编码。此前“核心手写齐全”的表述指约定的生成/详细编排/来源/重试主链，不能理解成表中每项都手写。准确状态为主链手写已验收、导出实现复用、工程问题仅讲解；不因本次询问擅自新增优化任务或宣称上述两项已手写。

第七章讲解第1单元/真实主链全景（2026-10-26）：用户确认第六章两类未手写范围后“ok下一步”，开始原清单第7章DeepResearch递归研究与成本控制，先讲源码/具体业务链，不提前手写。实际全文读取gpt_researcher/skills/deep_research.py（646行），核对agent.py191–193/351–353/403–449、utils.enum.DeepResearch='deep'、config.variables.default39–41、backend/report_type/deep_research/main.py、docs/gptr/deep_research.md及tests/skills/test_deep_research_empty_results.py；未读env/调用模型。主体用“RAG为什么仍会出现幻觉，怎样改善”且示意breadth2/depth2/concurrency2走真实链：GPTResearcher(report_type='deep')创建DeepResearchSkill→conduct_research提前分支_handle_deep_research→skill.run→初搜生成研究方向问题（当前answers固定Automatically proceeding，不等待真人）→deep_research规划query+researchGoal→本层受Semaphore限制并发普通ResearchReport/Web子研究（复用前章检索抓取压缩）→process_research_results提取learnings/citations/followUpQuestions→本层gather后按成功分支依次递归，下一query由研究目标和追问拼接、depth减1、breadth=max(2,breadth//2)→汇总发现/来源/上下文并裁剪→run写回父context、visited、sources并返回context字符串→外部再调用write_report生成最终报告。例子全成功且每次规划恰好两条时2+2×2=6个普通子研究，不等于6次API调用；每个子研究内部仍有自己的查询并发。强调同层并发和递归分支串行，concurrency限制当前层子研究，不是全局HTTP请求数。与第6章DetailedReport按章节写作及第9章deep_agents分开。说明breadth/depth/concurrency是工作量与并行度控制，当前无金额硬预算中止判断，成本日志不等于完整总成本核算（后续展开）。文档默认breadth4与实际默认配置3不一致，实际默认3/2/4；示例2/2/2是教学手动设定，不当默认。发现空规划分支406–414引用尚未416–420初始化的all_*，留本章失败路径单元核验；不宣称全失败出口皆安全。实际rg首轮误查backend/websocket_manager.py不存在，后续查backend/server定位，不作为项目缺陷。辅助解析/进度/裁剪/示例与测试仅预读不计全部已讲；第7章保持未完成，下一单元追run的初搜规划输入输出与模型解析，再递归执行/状态/成本边界，讲齐确认后核心手写。

第七章讲解第2单元/初搜到递归输入（2026-10-26）：用户“开始”，承接上轮明确的下一条源码链，仍讲解不提前手写。重新逐行读取deep_research.py291–342/119–140/48–74/577–598、query_processing.py43–80及tests/test_deep_research_parsing.py相关用例。拉通run→generate_research_plan(query)→for逐检索器await get_search_results（包装器按类创建检索器并to_thread同步search，多个检索器本阶段串行）→extend初搜摘要列表→原问题/运行时间/搜索结果构造system/user消息→战略模型high reasoning/temperature0.4→parse_follow_up_questions_response把返回文本解析为list[str]→run用固定Automatically proceeding回答构造Q/A列表→combined_query字符串传deep_research。说明初搜用于方向规划，尚不等于抓取清洗后研究context，当前搜索结果只在规划局部使用，后续方向问题不会直接逐项作为搜索任务；run未传num_questions故默认3，独立于下一阶段breadth。初搜单检索器异常记录后继续，搜索全空仍会调用规划模型；模型最终异常在该方法无catch会上抛；解析空列表时原问题仍进入combined_query。解析支持JSON/list及questions/followUpQuestions/items别名、json_repair/代码块/逐行Question文本恢复；非空str化、截前num_questions但没有严格字符串类型校验或去重。AST隔离实际同步解析函数并测试标准JSON、fencedJSON、编号文本、数量截断、空数组、混合类型6项全部通过，无网络/模型/密钥或应用改动；混合null/数字转'None'/'123'边界已确认，不能说全部无效项被过滤。具体例子沿用RAG幻觉问题，展示初搜列表→问题列表→qa_pairs→combined_query字符串与流程图；不设置强制答题。当前单元终点为首次递归入口，下一单元讲generate_search_queries如何把输入变成query+researchGoal执行任务，规划解析助手虽预读不计全部已讲；章保持未完成。

第七章讲解第3单元/生成可执行任务（2026-10-26）：用户继续，追deep_research403→generate_search_queries259–289→parse_search_queries_response77–116→serp_queries任务列表，再定位字段后续用途434/470/537–539。输入为首轮combined_query或后续层next_query字符串，num_queries在真实调用由本层breadth传入（方法默认3不覆盖显式值）；生成system/user消息要求JSON对象数组，每项query/researchGoal，战略模型temperature0.4且reasoning_effort读cfg（与前单元初始方向规划固定high不同）；解析返回list[dict]局部serp_queries，非报告/研究context，也非已有方向问题列表直接逐个执行。解释query给普通GPTResearcher作为具体任务，该子研究内部仍生成自己的搜索子查询；researchGoal保存在该节点结果中，与研究后followUpQuestions共同形成下一层研究输入。生成方法在Skill内因读模型配置，解析函数模块级因只依赖文本/数量不依赖研究状态。解析支持数组及queries/searchQueries/items容器，过滤非字典/缺字段、strip字段、截[:num_queries]，文本Query/Goal恢复只讲与上一轮的结构差别，不重复讲repair正则。提示词unique不等于代码去重，输出数是上限不是保证，空白字段在strip前判真会漏过，非字符串真值会.strip报错。同步AST隔离实际解析/类定义7项检查完成（无事件循环/网络/模型/应用修改）：正常strip、Query/Goal文本、缺goal过滤、重复保留、空白query漏过、数字query触发AttributeError；通过立即完成的异步生成替身并单步驱动deep_research协程，确认空任务分支406–414先引用all_learnings而416才初始化，真实抛UnboundLocalError，不能照注释说安全退出。课堂讲明这一当前节点的失败边界，不修改原项目或立刻扩为修bug工作；练习将避免复刻。使用同一RAG问题两任务例子、字段职责表和简图，当前单元止于任务准备/交接，下一单元深入process_query+Semaphore+gather如何完成一层研究及失败隔离；章保持未完成、尚未开始手写。

第七章讲解第4单元/一层并发研究与失败隔离（2026-10-26）：用户继续，逐行读deep_research.py416–530及ResearchProgress233–241、process_research_results344–375接口，预核对agent.py161空visited集合会被or set替换（实际共享边界留后续状态单元，不宣称传参就一定共享）。本轮拉通本层任务列表→deep_research内嵌process_query→局部Semaphore(concurrency_limit)→受限区创建普通Web GPTResearcher/await conduct_research→await process_research_results提取发现/来源/追问→更新进度/返回节点字典或普通异常返回None→gather等待全部、按输入顺序返回→过滤None→全失败返回已有状态不递归→成功结果合并learnings/visited/citations/context/sources。解释process_query嵌套是复用当前调用的semaphore/progress，async with占用范围包含研究和提炼两步、退出自动释放；协程列表尚非已经完成的任务，gather调度、await等齐；并发上限限制当前层普通子研究，不限制各子研究内部全部HTTP请求，也不减少最终任务数量。A/B/C三个任务、limit2示例说明前两启动、某个完成释放后C进入；单失败B→[结果A,None,结果C]→[A,C]，本函数内部捕获普通异常是gather不被该异常中断的原因，不归因gather自动忽略异常；取消不作普通失败吞掉。输出字典各字段只做承接说明，提炼内部下单元；all_*合并及递归深入留后续，不用一单元讲全递归。并发ResearchProgress.current_query是同一对象上的单字段，表示最近设置值，不代表全部运行任务。

本单元AST隔离真实DeepResearchSkill.deep_research/ResearchProgress/trim辅助，替换子GPTResearcher和提炼调用，运行3项异步控制流检查（正常权限require_escalated，无网络/密钥/原工程修改）：全成功、本层部分失败、本层全失败（depth3），均验证peak=2/许可释放、乱序完成仍按输入顺序返回context；全失败仅规划一轮/创建3子研究、不继续递归。第一次脚本用毫秒sleep推断完成顺序，Windows调度导致部分失败场景时间假设不成立（测试夹具问题），改用Event明确控制完成顺序后3项全部通过，未因此改项目代码。stdout错误日志被隔离缓存，测试无残留文件。明确任务列表空的406分支UnboundLocalError与有任务但全失败的496分支安全返回不同，避免误称全部失败路径有同一bug。未修改练习/开始手写，第7章仍未完成；下一单元讲材料如何提炼为learnings/citations/followUpQuestions，再讲递归合并/终止/成本边界。

第七章讲解第5单元/材料提炼到发现引用追问（2026-10-26）：用户继续，逐行读deep_research.py344–375/143–205/455–473/614–624及相关解析测试196–277（阅读非执行），本轮不重复第三种同类JSON修复器的正则细节。追process_query将当前子任务query与本子研究context传Skill.process_research_results→构造system/user消息要求learnings对象数组（insight/sourceUrl）及followUpQuestions→战略模型temperature0.4/high/max_tokens4000→模块级parse_research_results_response→输出learnings字符串列表/citations按发现文本映射来源的字典/followUpQuestions字符串列表→节点封装后交回递归调度。说明Skill持有父researcher以读模型配置，但query必须是本次子问题不是父总问题，context是子研究实际返回材料，故作为参数；该方法分析材料，不重新搜索/抓取、不直接写最终报告、不修改父context。用同一RAG检索遗漏例子展示Source/Content材料、模型JSON和解析后不同形状，解释保留无来源发现、来源映射供末尾context附Source标记、新追问供下一层研究。num_learnings默认3在本方法仅传解析器作发现/问题列表截断，未插入模型消息，不保证生成刚好3条；citations本身不随发现列表截断，后续边界待收束。引用是模型提供的关联，本解析代码不检查URL是否在材料中或论断是否获支持；同一发现文本重复时字典后写覆盖。输出注解Dict[str,List[str]]不完全准确，citations实际dict。模型/解析异常由外层process_query转None；正常解析出三字段皆空字典仍被当非None节点结果，不触发本层全失败停止，可能继续按研究目标递归。给简洁消息→结构化结果→下一层/最终上下文流程图；不强制答题、不改练习/原工程、无网络/模型或新测试，章保持未完成。下一单元讲成功节点的递归输入、depth/breadth变化、执行顺序与结果回流，再收束上下文/成本与已发现缺陷。

第七章讲解第6单元/递归展开与结果回流（2026-10-26）：用户继续，重新逐行读取deep_research.py377–420/483–575。本轮只追当前层成功结果→for逐节点合并→depth>1→next_query由researchGoal+followUpQuestions拼接→breadth=max(2,breadth//2)、depth-1→同一Skill对象递归调用→子调用复制传入learnings/citations/visited至本次局部all_*并新建context/sources→depth1仍完成研究但不再递归→子结果返回父帧并合并→继续父层下一个结果。用breadth2/depth2且任务全部成功且恰好两条的A/B、A1/A2、B1/B2具体例子走调用顺序：本层A/B并发全部结束后，处理A并等待其A1/A2子层返回，再处理已完成的B并等待B1/B2子层返回；共6个普通子研究，非6次API。父depth仍2，不因子调用depth1而被改写；self相同但每次方法调用的局部变量独立，并非每层新建Skill，子GPTResearcher才是新对象。解释把已有发现/引用/地址作为参数传入用于累计，下一层查询生成提示本身未自动包含all_learnings（只得到next_query），不能说传learnings就让LLM直接读到全部知识。breadth//2整数除法，min2意味着2保持2、1反增为2，实际任务数仍取决解析数量，不称每层必减半。解释all_learnings用子返回值替换因返回已含传入历史，若再extend会重复；其他context/sources本次子层新收集故extend，URL集合/引用字典update，最后发现set去重丢顺序。下一层异常可沿递归await上抛（递归调用在process_query局部try之外），局部普通任务失败隔离不等于全树任意异常均容错。函数尾同一self.context/self.research_sources跨层extend存在重复跟踪的边界，留下一单元上下文/共享状态讲解，不直接修改代码。给阶段式流程图而非误画整树并发，不加测验/手写或执行新测试；原第7章仍未完成，已讲规划/并发/提炼/递归，待上下文裁剪回写、来源状态与成本边界收束后确认手写。

第七章讲解第7单元/上下文裁剪与父研究者回写（2026-10-26）：用户继续，逐行读deep_research.py18/207–231/561–575/610–646、agent.py451–492、writer.py80–124及tests/test_deep_research_parsing.py301–316。链路为每次递归返回前trim(all_context)→顶层run将learnings按citations附Source标记组成列表→extend返回研究context→再次trim→逐项字符串/字典Content/其他str归一并换行join→写父GPTResearcher.context并返回→外部write_report通过ext_context or self.context交写作组件，复用第6章生成报告。不把run注释“generate final report”当实际行为，正文此时仍是材料。解释all_context局部子树材料、Skill.self.context跨递归跟踪容器、self.researcher.context父最终写作输入三者，跨层Skill.context extend整棵子树可能重复，但最终父写作路径使用返回results.context而非该跟踪列表。

裁剪实现实际是MAX_CONTEXT_WORDS25000，count_words=str.split空白分隔（list先join）；从列表尾逆序扫描，能放则insert0保持保留项原相对顺序；第一个检查的尾项单独超限且还未保留任何项时取其开头max_words；已有保留项后遇超限立即break，不继续找更早更短条目。较晚追加优先而非语义相关度排序或严格完成时间顺序，单条也取开头而非尾部。最终发现+来源位于列表前、原始上下文位于后，因此最后一次裁剪可丢发现及Source标记，不可说必然优先保留提炼结论。25000为空白计数非tokens/汉字，连续中文长段可能只算1，系统消息/问题等也不包含，不能当模型上下文硬预算或全过程费用控制；sources元数据不因上下文裁剪自动同步过滤。归一化/裁剪是同步内存处理，无需async；模型写作仍await。

AST隔离实际count_words/trim_context，运行自建5项与原有两个trim测试（仅提取函数，不导入整个测试模块）共7项通过：保留后部且原顺序、超限即停不跳过、单尾项超长保留开头、发现前缀可被裁掉、长无空白中文只计1，以及既有单超长项/最新超长项回归。无网络/模型/密钥/应用修改，新测试不是实模质量评估。给RAG发现/两份材料合并的6词预算具体例子和递归字典→带来源发现+材料→裁剪→父context字符串→报告流程图，不设置答题。第7章已讲研究主链至最终写作交接，待下一单元成本统计/工作量控制及共享状态等实际边界收束，再核对讲齐后经确认手写；当前保持未完成。

第七章讲解第8单元/成本与共享状态核心收束（2026-10-26）：用户继续，逐行读deep_research.py244–257/三个create_chat_completion调用/432–445/577–608/623–646、agent.py158–168/749–793、utils.llm41–152，rg确认深度技能无budget/max_cost中止条件。说明breadth/depth限制理论工作量，concurrency仅限制本层同时执行的子研究数，不直接减少任务总数；全成功且每次恰好2查询时depth1/2/3对应2/6/14个普通子研究（非模型调用数），max(2,...)不保证越深宽度越小；上下文空白词数裁剪/每次输出token上限与金额硬预算不同，模型重试还会增加实际调用次数。

费用实际链：run先读父get_costs，研究后再读父get_costs做差并日志；get_costs只return本对象research_costs，子GPTResearcher各自初始化0，当前技能未将子费用加回父；三次直接战略模型调用（方向规划/任务规划/结果提炼）未传cost_callback，而utils.llm137–147仅在该回调存在时计算并回记费用，所以父差值可能漏记乃至显示0，不能当全流程真实账单；差值也在最终write_report之前计算，不含随后最终写作。解释正确统计需统一账本/回调按请求归集，硬预算需调度时检查与并发预留额度，此为生产思路，不在本轮追加复杂预算实现。

共享去重边界：Skill.self.visited_urls保存父集合引用，但Agent161使用visited_urls or set()，传入空集合时新建集合，子研究更新不回流原共享集合；传非空集合才保留引用。递归传入的all_visited_urls用于累计返回，而构造子研究实际传Skill.self.visited_urls，不能把返回URL汇总等同实际跨子研究共享去重。run633又将正常结果的URL列表赋给父visited_urls，改变类型和属性指向，Skill仍指旧对象；当前最终写作不必因此报错，后续若继续按集合.add使用则有风险。生产/手写简化应保持集合类型，用None检查保留调用方空集合，不复制原版该问题。进度对象每次递归重建，current_depth按分支递增，不能当整棵树准确全局进度（后续手写不复刻复杂进度界面）。

AST隔离4项确认通过：执行实际Agent visited赋值表达式验证空集合不保留/非空保留；扫描三个真实create_chat_completion调用均无cost_callback；执行真实run URL写回语句验证父集合属性变列表且旧引用未同步。无模型/网络/密钥/应用代码修改。本章核心源码讲解范围已齐：入口初搜/规划与解析、节点并发/失败隔离、发现引用追问提炼、递归展开与回流、上下文裁剪与写作交接、成本及状态边界；仍未开始第7章核心手写或最终验收，保持原第7项未勾。下一步经用户继续/开始进入简化核心手写，先核对练习骨架并明确手写范围，配置/模型Provider仍按既定后续安排；不把源码讲解完成误报整章完成。

第七章核心手写第1步/组件装配（2026-10-26）：用户在源码核心收束后“继续”，确认进入核心手写。只读当前外部练习实际定义与GPTResearcher866–963、run_agent964–984，确认尚无DeepResearchSkill或deep入口；现有第6章代码保留。范围按原第7章：规划/提炼接口、受限并发普通子研究、递归累计、上下文裁剪回写及接现有写作，配置简化、模型仍可替换演示接口，不重写SDK或复杂预算/进度界面。本轮仅新增顶层DeepResearchSkill类，放ReportGenerator结束与GPTResearcher之前；__init__(researcher,breadth=2,depth=2,concurrency_limit=2)保存同一父研究者引用/宽深默认值，创建Skill级共享asyncio.Semaphore，教学上将并发许可集中到同一组件（原版每次递归调用新建），未来只在单节点研究/提炼范围持有，递归在释放后发生，避免持许可等待递归。未额外复制context/sources/visited跟踪状态，未来使用父对象和递归返回数据，配置无需加新解析层。在GPTResearcher.__init__现有self.role=None之后装配self.deep_researcher=None，if self.report_type=='deep'创建DeepResearchSkill(self)；先装配不修改conduct_research、不调用未实现run，因此尚不能执行深度流程。两空①researcher②self，下轮先给答案。解释两处self分别是Skill和父GPTResearcher，researcher参数传入引用，随后用属性访问；构造函数没有网络等待，用普通def；给RAG父对象创建Skill/持引用和信号量简图，无测试题。未编辑外部练习/调用服务或新测试，未误称已保存；第7章保持未完成，下一步实现最小研究方向规划及对应演示接口，逐步填核心，不混入第6章章节调度。

第七章核心手写第2步/初搜与方向规划（2026-10-26）：用户继续，先公布第1步两空researcher、self。只读练习当前尚无DeepResearchSkill/装配代码，提醒保存上轮后再加本轮方法，不误称已落盘；复核现有normalize_queries19–46会过滤非字符串/空白、去重、限制数量，空时回退原问题，其字典解析只识别queries/query，故本轮先取questions再调用。新增模块级async demo_deep_plan_model(messages)（现有demo函数附近）固定返回questions数组JSON，两个通用方向问题；GPTResearcher.__init__现有self.plan_model附近装配self.deep_plan_model=demo_deep_plan_model（无括号），不覆盖普通plan_model。DeepResearchSkill.__init__后新增async generate_research_plan(self,query,num_questions=3)：await父search(query)得到初搜背景，构造system/user消息含原问题/背景/数量/明确questions JSON结构，await父deep_plan_model(messages)，json.loads后检查dict，否则ValueError，取data.get('questions',[])交normalize_queries(query=query,max_queries=num_questions)返回字符串列表。两新空①query②messages，下轮先公布。解释方法属深度Skill因组织深度方向规划，search/model工具在父对象上取、本次query通过参数传入；输入问题str输出方向问题list[str]，不写入研究context、不把方向问题直接当query+researchGoal任务。演示模型只验证消息接口、不基于材料推理，已有search仍真实Tavily接口，当前未执行，不宣称离线真实研究。JSON解析和规范化同步不用await；搜索/模型/JSON/形状错误上抛，空问题数组经既有helper回退原问题。教学直接json.loads且有形状检查/已有去重逻辑，与原版json_repair/文本兜底有意简化，不重写同类解析器；未实现run/递归入口，不提前调用未知方法。给RAG输入→初搜→消息→问题列表简图与固定输出例子，无测验。仅更新学习记录，未改外部练习/调用模型或网络/运行新测试，第7章仍未完成；下一步实现本层query+researchGoal任务规划。

第七章核心手写第3步/本层任务规划（2026-10-26）：用户继续，先公布第2步两空query、messages。实际只读外部练习仍无DeepResearchSkill/demo_deep_*，本轮教学承接已布置类，不声称已保存；复核原版generate_search_queries259–289及字段解析77–94/调用403。新增模块级async demo_deep_query_model(messages)固定返回两个RAG任务JSON（query/researchGoal），GPTResearcher.__init__紧接上一轮deep_plan_model装配self.deep_query_model=demo_deep_query_model。DeepResearchSkill中generate_research_plan后新增async generate_search_queries(self,query,num_queries=2)：构造system/user消息要求最多num_queries个不同任务及JSON对象数组，await父deep_query_model(messages)，json.loads后要求list否则ValueError，for跳过非字典/非字符串字段，strip后过滤空query或goal，tasks.append双字段字典，return tasks[:num_queries]。两空①task_query②research_goal，下轮先公布。保留输入query变量作为本次研究输入，用task_query存模型拆出的具体任务避免混淆；普通normalize_queries只输出字符串会丢目标，故本轮需保留字典结构，不引入额外解析库/复杂配置。说明函数属深度Skill因规划节点，而模型接口保存在父对象；模型等待await，解析整理同步；输入可为首轮combined_query或后续next_query，本轮尚未写run/递归调用不直接执行，后续调用显式传本层breadth。空有效任务返回[]由递归入口安全停止，不复刻原版未初始化变量问题；JSON/形状/调用异常向上传递，无语义去重/引用核验承诺。演示模型固定RAG任务且不读取messages推理，深层也不会因此自动产生新任务，后续测试另注入任务覆盖递归，真实模型留第10章；不能称本轮真实规划成功。给具体RAG输入→两任务字典输出与图，并区分方向问题list[str]和执行任务list[dict]，不重复源码课。仅维护索引，未修改练习/执行网络模型或新测试，章未完成；下一步补研究材料提炼接口，然后接单节点研究与递归。

第七章核心手写第4步/研究材料提炼接口（2026-10-26）：用户继续，先公布第3步两空task_query、research_goal。只读当前练习已保存DeepResearchSkill350起构造/方向规划、demo_deep_plan_model154、父deep_plan_model953，尚未保存第3步任务规划。发现方向规划397行isinstance(data,json)把json模块当类型，明确应为dict（json.loads输出对象类型）；400行读取question单数应questions复数，否则丢失演示模型问题回退原问题；reponse虽然拼写不规范但赋值读取一致，不误说NameError。给两处必要修正不擅自编辑。

本轮按用户核心简化要求新增模块async demo_deep_extract_model(messages)，固定返回最终三字段JSON：learnings字符串数组（明确演示发现）、citations空字典、followUpQuestions字符串数组；父GPTResearcher.__init__在deep模型装配处新增self.deep_extract_model函数引用。DeepResearchSkill.generate_search_queries后新增async process_research_results(self,query,context,num_learnings=3)：列表context换行join/空材料ValueError；system/user消息含当前问题、材料、最多num_learnings条发现和追问，指定learnings/citations/followUpQuestions最终结构；await父deep_extract_model，json.loads检查dict，读取三字段并检查list/dict/list容器类型，截断发现/追问至num_learnings后返回。两空①query②context，下轮先公布。教学有意让模型直接输出调度器所需三字段，省去原版insight/sourceUrl对象数组拆分；源码映射过程已讲，不重写第三套类似解析器；引用关联仍由模型提供，容器检查不等于逐条字符串/URL/事实核验，不能称真实引用验证。demo无来源则citations={}，不编造证据，固定输出不理解材料。方法属Skill因从节点材料提炼后续方向，父对象提供模型接口，而当前子任务问题/材料通过参数传入，未来单节点执行器调用，不在这里搜索或写报告；JSON和容器整理同步，模型等待await，异常交未来节点边界处理。给完整输入输出和简图，无测验/未编辑练习/未运行模型网络或新测试；章保持未完成，下一步接一个普通子研究、共享去重与缓存材料，再调用本提炼接口。

第七章核心手写第5步/单节点执行（2026-10-26）：用户在澄清isinstance后继续，先公布第4步两空query、context。只读当前实际练习仍仅第1/2步已保存，方向规划397仍用json模块/400仍question单数（前轮修正未落盘），第3/4步任务规划/提炼和deep挂载尚未保存，不误称代码已运行；不重复整套旧代码。本轮在DeepResearchSkill.process_research_results后新增async _process_query(self,task)：child=None；async with共享self.semaphore；try创建普通Web GPTResearcher（research_report避免再次走deep）；直接赋同一父visited集合保留空集合共享；继承父search/call_model/plan_model/backup_plan_model函数接口便于替换测试和保持行为；await child.conduct_research；将child.research_sources作为本节点新材料立即extend父research_sources；通过父context_manager按当前query在父已收集材料中重新取上下文（复用已完成缓存）；await本Skill.process_research_results；返回learnings/citations/followUpQuestions/researchGoal/context/sources/visited_urls节点字典。except普通异常打印并returnNone，async with退出释放许可；finally若child已创建则把其已记录get_costs累计到父research_costs，失败前已记账费用也可汇总；三个演示模型不计真实费用，不因此声称总账完整。两空①self.semaphore②context，下轮先公布。方法属Skill负责跨组件调度，输入任务dict输出节点dict或None，递归gather将来调用；研究提炼占许可，递归不在该块中；不调用child.write_report。区别父research_sources累计缓存与返回sources仅本节点新材料，父context不在此改，材料收集和节点成功非同一状态。强调cache仅已收集成功材料可复用，正在另一节点抓取中的URL不保证当前节点拿到，简化版可能空材料节点失败，生产完整等待/in-flight任务复用留章末解释，不谎称并发缓存已完全解决。原版节点固定Web，本练习代表同样如此，不扩大本地/向量库组合范围；非真实模型/搜索验证，本轮未改练习/执行服务或新测试。给RAG单任务对象→子研究→材料登记/筛选→提炼→返回结果与失败路径图，下一步写deep_research的单层gather与结果累计，再加递归展开，不混写整棵树于此步；第7章保持未完成。

第七章核心手写第6步/单层并发调度与汇总（2026-10-26）：用户继续，先公布第5步两空self.semaphore、context。只读练习当前仍仅第1/2步，尚无任务规划、提炼、节点执行或deep入口，不误称本轮已保存/执行；复核原版416/483–517的初始化、gather、过滤与合并。本轮在DeepResearchSkill._process_query后新增async deep_research(self,query,breadth,depth)的单层版本：先创建merged字典（learnings[]/citations{}/visited_urls set/context[]/sources[]），depth或breadth<1即返回；await generate_search_queries(query,num_queries=breadth)，空任务返回已初始化merged；await gather展开各_process_query(task)协程，过滤None并全失败返回merged；for成功节点extend发现、update引用/地址、append非空上下文整段字符串、extend原始来源列表；return merged。两空①self._process_query(task)②result['learnings']，下轮先公布。解释本层局部merged与父长期缓存/费用字段不同，函数属Skill组织一层节点，future run调用，query可总输入或下一层输入，depth本轮用于无剩余层时停止，深度递减/下一层调用下一步才加入；当前depth2并不会运行两层，不能宣称递归已完成。教学每调用只返回本子树成果、由父层合并，后续不再携带原版整份历史列表参数，减少重复累计。与源码差异为空结果前先初始化消除UnboundLocalError，访问集合内部保持set，尚未写最终裁剪/去重/父context回写。具体A成功/B失败→[A,None]→[A]；本层无任务/全失败返回同结构空字典，模型规划自身异常上抛仍存在。重点说明gather调度/输入顺序，实际许可在_process_query内部；发现/来源是列表extend，引用/地址dict/set用update，节点context是字符串需append避免字符拆散。给单层调度小图；未改练习/执行网络模型或新测试，第7章未完成，下一步在for内追加递归及子树结果合并，再补run出口/入口挂载和验收。

第七章核心手写第7步/递归展开与子树合并（2026-10-26）：用户继续，先公布第6步两空self._process_query(task)、result['learnings']。只读练习仍尚无_process_query/deep_research等后续步骤，不称已保存运行；复核原版530–559递归条件/输入构造/宽深变化及返回合并。本轮在上轮deep_research的for result in results内部、当前节点sources合并之后追加if depth>1（12格），体内拼next_query（researchGoal与join followUpQuestions），await self.deep_research(query=next_query,breadth=max(2,breadth//2),depth=depth-1)，返回deeper后extend发现、update引用/地址、extend子树context/sources。两新空①depth-1②deeper['learnings']，下轮先公布。return merged仍8格在for外，不能因首节点完成提前退出；若depth1执行本层后不再递归。当前层gather先等齐，循环中的递归await按成功节点顺序逐一展开；共享信号量在_process_query退出时已释放，递归发生在许可范围之外，避免持许可等待子任务。重要教学差异：原版传入历史learnings所以父层用返回值替换；手写每次调用新建局部merged、不把整份历史作为参数传入，只返回本子树成果，故父层extend，不能机械照抄原版赋值导致丢当前成果。节点context为str用append，而deeper.context为列表用extend，不拆字符串。用全成功且每层规划两条的A/B→A1/A2→B1/B2示意执行顺序，总6普通子研究；示意不是固定演示模型会自动生成新方向的实测结果。说明同一Skill对象/独立局部变量、父depth不因子调用变值、深度递减确保终止；下一层全失败返回空结构可合并，规划本身异常仍上抛。只更新索引，无外部练习编辑/新测试/模型网络调用；第7章尚未完成，下一步补最终上下文裁剪和run（方向问题→初始输入→递归→回写父对象），再挂conduct入口与验收。

第七章核心手写第8步/裁剪工具与总入口（2026-10-26）：用户继续，先公布第7步两空depth-1、deeper['learnings']。只读练习当前仍仅构造/方向规划，后续步骤未保存，不把讲过视为落盘；复核原版207–231/610–646。为不调用未实现工具，本轮先在DeepResearchSkill前顶格新增简化模块函数trim_context_to_word_limit(context_list,max_words=25000)，仅处理练习约定的字符串列表：预算<1返回[]，逆序检查text.split数量，能放insert0累计，第一尾项独自超限则取开头预算词后停止，已有条目遇超限直接停止，返回列表；与原版同为空白分词非token预算，省略dict/list兼容与相关度排序，不引入新配置。后在Skill.__init__后新增async run：await方向规划(父query)→将总问题和方向问题直接join成combined_query（省略原版固定自动回答Q/A）→await deep_research(query,breadth=self.breadth,depth=self.depth)→blocks=list(results.context)拷贝材料列表→按dict.fromkeys去重且保序遍历发现，查citations并附Source标记后append→调用刚写trim→双换行join写父context→父visited_urls.update结果集合，保持类型与原引用→return父context。两空①self.depth②'\n\n'.join(final_context)，下轮先公布。重要教学改动为原材料先放、带来源发现后放，尾部优先裁剪时优先保留后加入发现，避免原版先发现后材料容易丢摘要；不声称保证所有发现或事实核验。父research_sources在_process_query已累计，不再extend重复计数或用仅成功节点结果覆盖它。解释dict.fromkeys只精确文本去重非语义去重，run返回研究上下文不是最终报告，写报告沿用BasicReport.run；同步裁剪无await、方向规划与递归等待await。给RAG材料/发现附Source的输出示例及总入口流图。未改练习/调用模型网络/执行新测试，第7章仍未完成；下一步把Skill装配与GPTResearcher.conduct_research分支接上，run_agent继续复用BasicReport，再核对保存代码并由助手验收。

第七章核心手写第9步/装配与入口接线（2026-10-26）：用户继续，先公布第8步两空self.depth、'\n\n'.join(final_context)。只读当前练习发现仍只有DeepResearchSkill构造/方向规划，父只装deep_plan_model，未见deep_query/deep_extract及deep_researcher挂载；且用户将模块级run_agent1029加入self参数，并把multi_agents分支改成runer=DeepResearchSkill(self)，混淆深度研究与多Agent，需在本轮明确修正。原版agent191/351/429与websocket_manager116/134/144/163确认deep由BasicReport创建的GPTResearcher在conduct内提前分支，非multi_agents分支。

本轮给出父GPTResearcher.__init__模型装配三行检查（deep_plan/query/extract函数引用），在已有self.role=None之后装配self.deep_researcher=None/if self.report_type=='deep':DeepResearchSkill(self)，复用第1步而非重复新增两份。替换父conduct_research：最前面if report_type=='deep' await组件run写self.context并return，普通路径保留角色选择与researcher_conductor.conduct_research。完整恢复模块级run_agent（顶格、无self）：params不变；multi_agents维持HTTP400未实现；detailed_report用DetailedReport；else用BasicReport；共用await runner.run与按需返回父gpt_research。两新空①self.deep_researcher.run()②BasicReport(**params)，下轮先公布。解释模块函数self不是自动注入、当前调用只传task/source/type，额外self会导致参数绑定错位/缺参；DeepResearchSkill依赖父研究对象，不能拿模块级不存在self创建；BasicReport负责先研究后写作通用顺序，GPTResearcher内部按report_type选择研究策略，故deep复用该调度器，multi_agents保留第8章独立分支。深度节点内部report_type=research_report避免递归重新进入深度总入口。给完整HTTP deep→run_agent→BasicReport→GPTconduct→Skill.run/递归→父context→GPTwrite_report→导出JSON链图和请求例子。当前实际磁盘未保存所有手写步骤，未宣称deep已跑通/第7章已完成；本轮只给教学修正，未改外部文件/执行测试/模型网络。核心接线代码至此已给齐，下一步由助手核对保存版本、修漏并隔离测试，之后补手写版工程边界收束再勾章。

第七章核心手写验收与工程收束（2026-10-26）：用户继续验收，先公布第9步两空self.deep_researcher.run()、BasicReport(**params)。首次读取练习仅构造/方向规划及错误路由，准备补齐时用户保存了后续全部代码，首次修补脚本在ast.parse遇707行f-string双引号嵌套SyntaxError，尚未备份/写入，立即重新读取最新文件，不覆盖用户新写代码。确认用户已自行保存各demo模型、裁剪函数、全部Skill方法及正确挂载/路由；改为仅修最新文件的5组错误：run424方向规划补await；generate_search_queries546的return移出for（避免只处理首项）；_process_query631从误调自身改为process_research_results(query=...,context=...)；递归707修复f-string引号及researcherGoal→researchGoal并补换行；711宽度改为max(2,breadth//2)保持已讲行为。先备份D:/桌面/新建文件夹/1.py.before-chapter7-20261026-203605.bak，校验准备期间文件未再变化，保留BOM/换行，compile成功后写入。最终练习SHA256为10786089ea26522a9df81e251f0359b86e9c8dfbaa8f02d6cb1dd4acde33e9a5，当前定位裁剪377、Skill405、run421、任务规划497、提炼547、节点606、递归648、run_agent1374。未修改上游研究实现或已有无关query_processing导入改动。

新增scripts/check_chapter7.py，复用check_chapter6.py的AST装载与依赖替身，不执行练习导入/启动块；真实运行实际保存的调度、递归、上下文格式/Document分块筛选、报告写作与HTTP处理器；搜索、抓取、模型、Embedding、导出适配器为可控替身，不联网/读密钥/连接Milvus/生成新PDF。第7章18项全部通过：方向规划背景传递/对象验证/空回退；任务遍历所有项与字段过滤/数量上限；材料列表归一、空材料/提炼输出容器验证；两层6普通子研究、最终父写作一次；空集合起点仍共享同一集合且材料汇总；六个子账本模拟单位加总6且发现附Source进入最终写作；深度1/2/3节点数2/6/14且无整份历史重复累计；零额度/空任务安全停止；全失败停止下探且空上下文阻止写作；A失败仅B分支深入；3任务2许可覆盖至提炼、gather按输入顺序合并；finally汇总失败前已记账费用并释放许可；取消向上传递且许可可复用；已完成缓存可供6节点复用无新抓取/保持set引用；正在抓取的URL登记无法给兄弟提供已完成材料（明确已确认限制）；空白分词裁剪/尾部发现优先/超长项/中文边界；HTTP deep200正文/元数据/两个导出适配器且422/400分支独立；规划坏JSON导致500且不导出伪成功。所有异步检查有确定事件或超时保护；首轮17项一次通过，新增在途缓存边界后18项全部通过，未为测试修改实现。第六章脚本17项回归也全部通过，最终文件字节与哈希一致，保留既有测试客户端弃用提示未改依赖。

本章验收后的工程说明（只讲解，不新增手写任务）：共享visited的登记不等于抓取完成，A已登记但未产出材料时B可被去重跳过并因缓存空失败；需要URL到在途任务的映射并等待同一抓取结果，当前练习只复用已完成缓存，此边界已确定性复现，未宣称全局并发缓存完善。模型仍是固定演示接口，只有测试替身提供变化任务与受控来源；不等于真实规划/引用正确性或真实Embedding质量已验证。当前成本finally只汇总子账本已有记录，三类深度模型真实费用与搜索/Embedding等仍需统一计费接口；工作量参数和词数裁剪不等于金额硬预算，预算准入/并发预留只解释。max(2,breadth//2)最小2使深层工作量仍增长；失败取消后来源/visited已发生的改变不自动回滚；空白词数不是token预算；最终只裁剪写作输入，过程峰值材料内存不因此被严格限制。当前代表流程为网页来源，未验证深度研究与local/hybrid/Milvus全组合，真实Provider接入留10章、质量评测12章。将原第7项勾为约定核心完成，准确保留哪些未手写/未验收，下一次继续第8章LangGraph多Agent与人工反馈，先场景拉通源码而不直接手写。

第八章讲解第1单元/多Agent双层图全景（2026-10-27）：用户在第7章验收后继续，进入原第8章LangGraph multi_agents与人工反馈，先源码业务流程，不手写。枚举multi_agents全部路径（含独立ag2子目录），实际全文读取main.py、agents/orchestrator.py（ChiefEditorAgent实际位置，经agents/__init__导出）、editor/researcher/human/reviewer/reviser/writer/publisher/fact_checker/visualizer、memory/research.py与draft.py、plan_review/draft_review/fact_review、utils/llms.py、task.json和README；ag2仅读orchestrator前75行区分实现，未称全部ag2已读。定位backend/server/websocket_manager.py134–142的multi分支→multi_agents.main.run_research_task40–50（open_task后覆盖query）→ChiefEditorAgent.run_research_task123–146（建图compile/ainvoke初始{'task':task}并返回完整state）。不执行main导入/load_dotenv，不读env或任何密钥。

本单元沿同一RAG幻觉请求说明节点/边/任务state概念，以及外层ResearchState总图和每章DraftState子图：browser实际普通GPTResearcher完整研究并写初始报告→planner按初始报告生成title/date/sections→human收集可选反馈（示例打开task.include_human_feedback，默认文件false，节点存在不代表必等人）→有反馈回planner/通过后Editor.run_parallel_research→每章节子图ResearchAgent普通subtopic_report写草稿→Reviewer按follow_guidelines条件审阅（默认false跳过模型审阅）→需要则Reviser修改再审→各章节通过后gather收集drafts为research_data→Writer写引言目录结论来源及标题字段，正文章节保持已写draft→FactChecker审assembled data并根据条件回writer（当前writer提示主要修引言结论，不能说自动重写全部章节正文）→Visualizer产Mermaid代码文本→Publisher组装Markdown并按publish_formats导出→state.report→后端抽取report字符串。强调本节以WebSocket入口为例，不混称HTTP多Agent元数据返回已适配。示例若演示人工反馈与审阅须说明两个开关默认关闭，用户问题/章节名仅示意无实模输出。run_depth_research命名不等于第7章report_type='deep'，实际subtopic_report。LangGraph是按既定状态/条件边调用Python方法，Agent对象职责/提示词可用同一模型，ChiefEditor为代码编排，未加一个自动决定全流程的主模型。README未包含当前FactChecker/Visualizer等尾部节点，以源码连线为准。

当前源码实际阻断已核验，不能把业务图当作已跑通实现：orchestrator._add_workflow_edges102引用不存在self._route_fact_check（现有fact_review.py仅模块函数未接类）；editor._create_workflow140引用不存在self._route_draft_review（模块helper也未接类）；外层human条件lambda用revisions_count和硬编码5，而HumanAgent回写plan_revision_count，已有_route_human_feedback/任务max_plan_revisions未接当前边。AST隔离实际Chief/Editor类，用记录型图替身调用原构图方法，确认两处AttributeError；提取已注册human条件lambda确认plan_revision_count100仍返回revise，共3项源级检查，无LangGraph/模型/文件导出/配置环境加载，未修上游源码。后续条件边与失败单元需讲清缺口及方案，当前不宣传自动停止循环等未实现保证。第8章保持未勾，仅全景，下一单元追入口任务→ResearchState→browser→planner的状态更新和图如何连接，随后再人工反馈/章节审阅回路/汇总与失败，讲齐确认后核心手写。

第八章缺口定位澄清（2026-10-27）：用户先问缺口在哪，暂停推进新单元，复读orchestrator78–109/editor126–144/human47–58、三种route helper及三个修订次数测试的装载方式。明确三处是接线缺口：外层orchestrator102访问未定义类方法_route_fact_check，虽fact_review.py有独立route_fact_check但未导入/包装到类，因取方法引用在构图时发生，所以研究节点启动前即AttributeError；修好外层后，运行章节并行阶段创建子图会在editor140因缺_route_draft_review再次AttributeError，draft_review.py有独立函数不自动变成实例方法，follow_guidelines关闭也不绕过建图引用。第三处human边实际用lambda读取revisions_count/固定5，而HumanAgent回写plan_revision_count，类内106–109已有读取task.max_plan_revisions的_route_human_feedback却未注册到边，故开人工反馈且持续修改时配置上限不按预期生效；例plan_revision_count100仍按缺省revisions_count0判为revise。建议方向只说明补两类路由委托并将human边接已有方法，不在用户仅问定位时擅自改源。核对三份已有修订测试只直接装载独立helper，未验证这些方法如何接图，不能把辅助函数存在或局部测试通过等同整图已接通。本轮未跑新测试/模型、未修改工程源或开始手写；第8章仍未完成，后续回初始state→browser/planner讲解。

第八章讲解第2单元/入口与初始状态到章节规划（2026-10-27）：用户在缺口定位后继续，回到既定源码课程，不推断为修补原图授权。逐行读取main17–50、ResearchState5–23、ResearchAgent13–44、orchestrator60–85/123–146、Editor22–50/79–116；补读本机.venv/langgraph/graph/state.py134节点State→Partial及1850起默认LastValue字段通道，未引用更新版本SDK行为。链路为用户query覆盖task.json的query→Chief持self.task→StateGraph(ResearchState)注册browser/plan绑定方法（无括号，运行时框架传入状态）→compile成可执行图→ainvoke初始{'task':task}→browser从state.task取query/source(defaultweb)/verbose，调用ResearchAgent.research普通GPTResearcher(conduct后write)得到初始报告str，返回task+initial_research字段更新→沿browser→planner→Editor从当前state读取初始报告、task、可选human_feedback，构造日期/章节上限/反馈条件指令→call_model JSON输出→仅返回title/date/sections更新，不把全state重新返回。说明TypedDict为字段约定，不会自动生成初始字段或等同Pydantic请求校验；节点字段更新保留未返回字段，普通字段默认替换而非自动列表追加，所以人工改计划时sections应覆盖旧列表。self保存角色工具/连接，research_state参数承接本次执行最新上游结果，不可只读取最初task代替当前状态。配置来源来源字段是task.source，本入口没有把外层report_source自动传入；模型选择/环境覆盖仅已读不展开配置课。

使用实际AST提取ResearchState、ResearchAgent、EditorAgent定义（不执行项目导入/load_dotenv），真实LangGraph最小browser→planner→END图，研究和模型替身，3项验证完成：conduct→write→plan调用顺序，planner输入含初始报告，任务/初始报告保留、旧sections被替换且实际通道LastValue；配置max_sections3而模型返回4项时完整接受，确认只有提示词约束；规划模型返回None时plan.get触发AttributeError，不会自动恢复成有效state。该最小图绕开已记录缺失路由，仅验证这段真实节点，不称原版全图已修复/已运行；未修改应用源或调用真实模型/搜索/读取密钥。失败说明初始research无该层try则异常上抛，call_model内部异常可返回None进而规划失败，缺失字段可写None且未严格校验。用RAG问题的三个状态快照/节点返回局部字段和简图讲完整输入输出，不强制答题；章仍未完成，下一单元接HumanAgent反馈接收、字段回写及回planner条件边（含先前发现字段与上限缺口）。

第八章讲解第3单元/人工反馈与重新规划（2026-10-27）：用户继续，逐行读HumanAgent全部59行、orchestrator78–109、人反馈独立helper、Editor96–116；按需核对CustomLogsHandler33–60、前端hooks/useWebSocket113–115与app/page120–125协议，以及app /ws362–366→server_utils.handle_websocket_communication327起接收分发。链路为planner已有sections→HumanAgent从state取task/sections→include_human_feedback false直接返回None且保留计数（默认task配置）→true且有socket/stream则发送human_feedback/request并await包装器.websocket.receive_text，前端显示反馈并回JSON{type:'human_feedback',content:文字}→json解析提取content→归一化→非空意见计数+1→返回human_feedback/plan_revision_count两个字段更新→条件路由accept去章节researcher、revise回planner→planner提示加入意见并覆盖sections→再问human，no清None后通过。Human节点不调用LLM，角色保存的是连接工具，本次计划从state取，不直接把反馈append进章节。普通条件路径与已知次数接线缺口分开：当前lambda读revisions_count/固定5，未接已存在_route_human_feedback；独立helper配置3第三次仍revise，第四次>3明确抛错，不是强制通过。

本轮用AST提取原Human类和直接加载纯plan_review函数、模拟包装socket/stream验证6组：关闭开关不发送/接收且计数保留；有效反馈发送请求/解析/加计数；NO去空白后转None不加计数；真实修改意见'not enough evidence'因包含no被误接受；坏JSON/读取异常/错误消息类型均留下None可被当通过；独立helper的允许/超限语义。无服务器/浏览器/LLM/网络/环境文件或应用源码修改。补充实际边界：no用子串判断过宽；WS try中错误只打印后可放行，而非统一失败；命令行input同步阻塞、WS await没有显式等待超时；本实现直接在节点内等待socket，没有启用持久化检查点，不能宣称框架断点续跑。

进一步发现通信接线风险（静态确认，未跑真实端到端）：/ws总接收循环server_utils352与Human29都在同一底层socket receive_text，后台run_long_running_task执行研究时主循环仍可接消息；主循环357会在运行任务存在时将新消息按忙碌拒绝，375的前缀human_feedback处理又只TODO打印，且与前端发送纯JSON协议不同。因此Human单节点与UI收发代码存在不代表浏览器人反馈端到端可靠，可能争抢接收或丢反馈，需统一接收者按类型投递当前任务反馈队列，留条件边/工程及第11章通信单元，不在本轮擅自修改。原构图缺口仍未修，本轮仅教已读节点和普通分支，不宣称整图可跑。给RAG反馈补部署成本→计数1→新计划→no接受例子及回环图，不强制答题。第8章尚待章节并行子图/审阅修改、writer/fact/visual/publish及失败边界，讲齐后确认核心手写。

第八章讲解第4单元/并行章节子图与审阅修改（2026-10-27）：用户继续，逐行读Editor52–77/118–168、DraftState5–11、ResearchAgent13–58、Reviewer全部、Reviser全部、draft_review、none_sentinels；本轮拉通通过的sections→Editor编译一个DraftState子图→_create_task_input每章task/topic/title/headers→多次chain.ainvoke并gather→每章ResearchAgent普通subtopic_report(conduct后write)返回{'draft':{topic:正文}}→Reviewer按follow_guidelines开关审稿（默认false无模型调用，示例true）→模型纯None字符串通过严格哨兵归一成Python None；有意见则review文本及draft_revision_count+1→条件回Reviser→LLM根据旧稿/审阅意见返回新draft+revision_notes→再审（revision_notes进提示）→通过END→外层按输入顺序取各结果draft汇成research_data。修改节点只改已有稿，不自动重新检索；外层gather无信号量/章节并发硬上限，未统一捕获子图异常，不自动返回部分成功结果。Agent实例/工具可共享，章节可变数据随各自state传入，不放self；task配置引用可以共享，并非所有对象深拷贝隔离。_create_task_input传title/headers但DraftState未声明，实际不会保留为章节图通道，本路径从task.query取总问题所以不依赖这两额外键。Editor开头_init_agents返回值局部未用、真正图内绑定来自_create_workflow另一组；仅记录辅助无用代码，不扩课。

测试中不修改原图，AST装载真实各节点及状态定义，使用真实LangGraph并在测试Editor实例临时_create_workflow里把条件边接到现有route_draft_review，解决测试执行所需缺口但未假称工程已修；研究与LLM替身、构造虚拟包仅供实际Reviewer内部导入纯none_sentinels（未导入项目初始化/加载环境）。5组检查完成：实际run_parallel_research并行TOPIC_A/B，B先结束、A一轮修改后第二次审阅通过，research_data仍A/B顺序且草稿分别v2/v1；实际章节state不保留未声明title/headers；关闭guidelines不调用审阅模型；call_model返回Python None虽然严格哨兵不承认它，但review_draft最终原样return None、run写review None仍被路由当通过（确认错误与通过混淆）；helper默认上限3，count4抛错，原Editor缺包装器不能宣称已能自动强制通过。真实来源研究错误被run_subtopic_research捕获为{topic:None}且外层未过滤，也作为已读边界记录（尚未单独模拟），后续工程收束需解释。无网络/模型/密钥/原工程修改；第8章仍未完成，下一单元接research_data→Writer的整体结构生成，再事实检查/可视化/发布与失败边界。

第八章讲解第5单元/Writer补整篇结构与状态更新（2026-10-27）：用户继续，逐行读Writer全部146行、orchestrator67/81–82、utils.llms全部、Publisher22–59确认正文最终来源。本轮追research_data（章节名→正文的字典列表）→Writer.run→write_sections从state.title取主题、state.research_data取章节、task取model/指导规则、可选fact_check_notes进入提示→call_model(response_format='json')返回解析字典，约定四字段table_of_contents/introduction/conclusion/sources→get_headers生成报告各部分显示文案（非HTTP头）→follow_guidelines true时再call_model改显示文案→return{**research_layout_content,'headers':headers}更新总状态。正常约定输出不包含research_data，章节正文留原值供Publisher后续拼接；report字段此时尚未生成，日志“Writing final research report”不能当实际返回整篇字符串。sources是模型整理的参考条目字符串列表，不是抓取器research_sources材料字典；没有逐条来源/论断程序核验。dict **在返回字典中展开原键值，后面的headers覆盖同名键，不是此处的函数传参。事实意见只要求重写引言结论，没有自动重搜或重写正文闭环；后续事实节点单独讲。

真实LangGraph单Writer测试图，AST原类/ResearchState加固定模型，5组确认：默认仅一次模型调用生成结构字段、保留章节正文且无report；启用规则多一次标题文案调用并正确取嵌套headers；fact_check_notes进提示而正常响应仍保留章节正文；模型返回额外research_data字段时因为原返回**未白名单过滤，会覆盖已声明状态通道（因此“正文保留”仅正常约定输出，不是不可变保证）；模型返回None导致字典展开TypeError。测试无真实模型/搜索/环境文件/源修改，原全图接线缺口仍未修。边界说明response_format=json在当前helper用于本地JSON解析而非严格schema校验，未统一检查四字段必填/类型，错误可使状态缺字段或下一步失败；wrapper模型调用异常可返回None，客户端配置/消息转换在try外的异常仍可直接上抛，不扩大保证。配RAG两章节输入→四结构字段→headers→部分state更新简图和例子，无强制问答。第8章尚未讲齐，下一单元追FactChecker审什么/回Writer能修什么/上限路由，再可视化发布及失败收束，之后才确认手写。

第8章源码讲解续：Writer→FactChecker→通过或返工。fact_checker.py第10–32行只将introduction、research_data、conclusion拼入模型提示，未独立检索/抓取，也未显式传sources列表或原始材料；run第34–66行解析完整None接受标记，返回fact_check_notes，非None意见时递增fact_check_revision_count，节点本身不改正文。fact_review.py第8–23行独立路由：无意见accept；有意见且上限None始终revise；默认3时计数3仍revise，4抛MaxFactCheckRevisionsExceededError，并非强制通过。orchestrator.py第100–103行映射accept到visualizer、revise到writer，但所引用的ChiefEditor._route_fact_check仍缺失，不能把独立helper视为已接入主图。Writer第39–40行意见提示只要求修引言/结论，正常输出不重写章节正文，故正文事实问题可能反复出现。严格解析器虽然不接受模型失败产生的Python None，调用方仍保留None并作为无意见返回，导致独立路由误判accept；已用AST实际节点/纯helper、固定模型隔离验证：输入范围、通过/意见计数、None of长句不误通过、次数上限及Python None误通过全部符合上述分析。未联网/读取密钥/修改原源码，未运行原全图。下一单元追Visualizer→Publisher拼接/导出/输出与失败收束；本章仍在源码讲解，未开始手写。

第8章源码讲解续：Visualizer→Publisher→输出。visualizer.py第10–26行将research_data传模型，约定一段Mermaid Markdown或字符串None；run第28–54行返回diagrams列表，未渲染图片/校验Mermaid语法，仍用区分大小写的子串判断“None”，有效图含该词也会丢弃，模型失败返回Python None则TypeError。publisher.py第22–59行按章节字典value拼正文（不额外使用key生成标题），加入Writer提供的引言/目录/结论、diagrams和sources，最终在这里生成整篇Markdown；Visualizations标题固定英文。第61–67行顺序执行PDF→Word→Markdown，忽略导出返回路径；run只返回report字段。独立导出模块utils/file_formats.py已读全：UUID各格式独立文件名；Markdown通过aiofiles UTF8写入，异常上抛；PDF同步md2pdf调用CSS，Word同步Markdown→HTML→HtmlToDocx→doc.save，两者虽async外壳但转换阶段无异步让出，catch异常返回空串，Publisher未检查。该模块与第6章backend.utils分开，不混用错误边界；本轮未重新测试真实转换或Mermaid导出渲染。ChiefEditor第145行ainvoke返回全状态，main第40–50行继续返回全状态，backend/server/websocket_manager.py第134–142行multi分支提取report字符串。AST实际Visualizer/Publisher加固定模型与导出替身验证：图表状态、布局及顺序、只拼章节value、顺序导出、路径丢弃、空格式字典可只返回正文、缺失publish_formats会报错、Markdown等未捕获导出异常向上传播；确认PDF空路径仍继续发布、None子串误删及Python None异常。无联网/密钥/真实导出/原源码修改，原全图接线缺口仍未修。下一步按原第8章清单核对源码覆盖和工程边界，再确认核心手写范围；尚未开始本章手写，不标整章完成。

第8章源码讲解核对/转手写前收束（2026-10-27）：对照原十二单元第8项，不增新路线。LangGraph主实现已覆盖入口/ChiefEditor组图、ResearchState与DraftState部分状态更新、初始研究/规划、人工反馈回规划、章节并发子图与Reviewer/Reviser、Writer、FactChecker、Visualizer、Publisher及返回后端；本章源码约定核心已讲齐，尚无本章手写或原版全图成功运行，故保持未勾选。复核缺失Chief._route_fact_check和Editor._route_draft_review、人工计数plan_revision_count与活动路由revisions_count不一致，两个纯路由helper存在不等于图已接好。补齐辅助用途：agents/memory包init导出类且agents最后导入Chief规避循环依赖；utils/views枚举日志颜色；utils/utils.sanitize_filename替换Windows非法路径字符；pdf_styles.css仅排版字体/标题/表格；requirements依赖清单、package.json为JS SDK配置且test脚本占位，不作为研究入口；agent.py模块级组图编译，langgraph.json以agent.py:graph注册部署入口（只读配置，不读引用的.env）。注意agent.py示例task缺publish_formats，若修复前面构图错误并走到Publisher，还会因None.get失败；不宣称部署例子开箱可跑。README仍列8角色且流程遗漏FactChecker/Visualizer，以实际节点为准。multi_agents/ag2为另一套实现，未完整精读，保留待覆盖，不并入已完成LangGraph主流程；部署细节/浏览器反馈真实端到端/正式评测归原11/12章继续。本轮说明Chief主要做确定性图编排，不等于每条边由模型自主决定；多次章节ainvoke各有state，外层gather按输入序合并，非各角色任意修改同一全局字典。拟手写保留真实StateGraph、总状态/章节状态、人工条件边、章节并发审改回环、结构生成/事实路由/发布；复用已写GPTResearcher研究能力，配置简化、反馈函数替代真实WS，导出复用，不加后台/ID/完整持久化。需用户确认开始后按小步推进，不重复已讲各Agent，不擅自修原工程或外部练习；本轮只读核对与索引更新，无新增测试或成功声明。

第8章核心手写第1步/总状态与单章状态（2026-10-27）：用户明确“开始手写”。只读实际练习D:\桌面\新建文件夹\1.py，仍1456行、最后修改2026-10-26，尚无LangGraph/TypedDict/本章状态，现有multi_agents分支仍400；不改原有GPTResearcher或该分支。交付代码：顶部from typing import TypedDict；app=FastAPI()后、normalize_queries前新增模块级ResearchState(TypedDict,total=False)及DraftState(TypedDict,total=False)，类0格字段4格。前者先声明task/initial_research/title/sections/human_feedback/plan_revision_count/research_data/report八项主干通道；后者task/topic/draft/review/revision_notes/draft_revision_count六项；人反馈和review标注str|None，后续写作/事实/图表节点到时再加对应通道，未称完整原schema复现。讲TypedDict运行时仍普通字典、提供类型/图状态结构而非Pydantic运行校验，total=False表示键可逐步出现、不填默认值；缺失键直接索引仍KeyError。两种state隔离完整报告与各章节可变进度，同一类多个章节各自调用state，不宣称task配置深拷贝。源码参照memory/research.py:5及draft.py:5；用RAG三章节输入与A审阅/B通过的各自状态示例。用户自行手写，本轮无外部练习编辑或新增测试，代码尚未保存/运行验证；下一步编排器构造和组件依赖装配，保留已写研究能力，不重复写搜索/抓取。

第8章核心手写第2步/初始研究节点与最小编排器装配（2026-10-27）：用户继续，读取实际练习文件仍旧1456行，尚无上一轮TypedDict/ResearchState/DraftState，明确需先保存上一轮，不称已写入。交付在已有GPTResearcher之后、模块run_agent之前新增ResearchAgent：research(query,source='web',report_type='research_report')新建已有GPTResearcher，顺序await conduct_research及write_report返回报告；run_initial_research(state:ResearchState)取task，传task['query']/task.get('source','web')复用research，返回{'initial_research':report}局部更新。再同位置顶格ChiefEditorAgent构造保存task及self.research=ResearchAgent()，只完成角色装配，不提前调用未实现Editor/图方法。解释self.research为长期节点组件，新researcher为每次研究的局部状态，避免章节并发覆盖self.researcher；相同命名不等于递归，两层分别为ResearchAgent.research和GPTResearcher实例。对应原researcher.py13–23/34–44及orchestrator49–54；源返回task+initial但练习只返回新字段，后续图保留task。本轮无图注册/编译/运行，不改变HTTP multi分支，不导入/重写原GPTResearcher，未生成真实报告或执行测试；下一步Editor规划节点，再逐步注册图。无填空，继续时无需公布新空答案；用户手写保存待核对。

第8章核心手写第3步/Editor章节规划（2026-10-27）：用户继续，读实际练习已新增TypedDict及两状态，但ResearchState第24行写成section，需改sections；磁盘尚无上一轮ResearchAgent/ChiefEditor，不称已保存。交付EditorAgent放上轮ResearchAgent后、ChiefEditor前：构造保存异步call_model函数；plan_research(state)取task、initial_research、human_feedback，max_sections默认3并拒绝<1，拼system/user消息要求title和sections的JSON字符串，await self.call_model(messages)、json.loads；检查dict/标题非空字符串/章节非空字符串列表，返回title与截断sections局部字段。JSON解析/结构无效直接抛出，不伪造通过；配置极简，不写日期/样式/日志、无新搜索。用当前问题+初报+可选人反馈支持之后回规划闭环。随后更新ChiefEditor.__init__(task,call_model)保留ResearchAgent并装配EditorAgent(call_model)，不调用函数，区别长期调用工具self.call_model和每次动态state参数。明确本节点需要JSON对象title/sections，不能直接拿旧demo_plan_model的查询数组当章节规划响应；模型函数后续装配/测试提供，本轮未执行。对照原editor.py22–50/79–116，教学合并提示构造并在代码中截章节数量，原版只有提示约束。未改外部练习、未跑模型/测试，下一步HumanAgent反馈及条件路由，后续才注册编译图。

第8章核心手写第4步/Human反馈与路由（2026-10-27）：用户继续，实际练习sections拼写已正确，新增研究类拼成ReasearchAgent而Chief引用ResearchAgent，需更名；Editor和新版Chief构造尚未保存，不假称已实现或改文件。交付console_feedback(sections)模块async函数，打印计划后await asyncio.to_thread(input,prompt)返回字符串；HumanAgent构造接收ask_feedback异步函数，review_plan取task/现有计数，开关默认false则无I/O，开启则await ask_feedback(state['sections'])后strip，空串或完整no(不区分大小写)归一None，真实非空意见计数+1，返回两字段。不使用源中no子串误接受逻辑；输入函数异常/非字符串不会被吞成通过，不做WebSocket/检查点。位置为Editor之后Chief之前（先保留上一轮Editor）；更新Chief构造task/call_model/ask_feedback默认console_feedback，装配research/editor/human；新增普通def _route_human_feedback(state)，无意见accept，有意见且计数超过task.max_plan_revisions默认3抛RuntimeError，上限None不限制，其他revise。节点负责取反馈/更新字段，路由负责决策，字符串标签后续接图；源码human.py10–59、plan_review.py8–23；给RAG新增部署成本→count1→revise→Editor新计划→no→accept且计数仍1例子。不调用真实模型或控制台input，不运行未完成图、不修改外部练习，后续先注册初始研究/规划/人工反馈的最小可执行图，再推进章节子图与并发；测试由助手在必要集成点负责。

第8章核心手写第5步/前半段最小LangGraph（2026-10-27）：用户继续，实际练习仍旧ReasearchAgent拼写及旧Chief两字段，Editor/Human/反馈路由未在磁盘看到，提醒保存前两步并修正名称，不称已集成。交付顶部from langgraph.graph import StateGraph, END；在已有新版ChiefEditor类内、_route_human_feedback后新增_create_workflow：StateGraph(ResearchState)，注册browser绑定self.research.run_initial_research、planner绑定self.editor.plan_research、human绑定self.human.review_plan，入口browser，普通边browser→planner→human，human条件边用self._route_human_feedback，accept→END、revise→planner，返回未编译workflow。新增async run_research_task，workflow=self._create_workflow()、chain=workflow.compile()、await chain.ainvoke({'task':self.task})返回本阶段完整state。解释注册传方法引用不加括号，框架执行时传state并等待异步节点；compile生成可执行图不调用模型，ainvoke才执行；图合并局部更新后再运行条件路由，标签accept/revise与节点名分开；回planner复用initial_research不重跑browser。本阶段END表示章节计划验收完成，不是最终报告生成，后续替换为章节研究连接，不假称完整multi_agents实现。以RAG原理/检索质量→人工加部署成本→再规划→no接受例子，browser1次/planner和human各2次，最终无report正常。原HTTP multi分支仍未接、不提供会启动外部依赖的执行命令、不运行未保存文件；无新增测试/真实模型调用/源码修改，只维护索引。下一步写章节研究节点与DraftState，再构建审改子图及并行汇总。

第8章核心手写第6步/单章研究节点（2026-10-27）：用户继续，实际练习仍ReasearchAgent拼写及旧Chief，前几步Editor/Human/组图未保存；不修改文件或宣称集成通过。交付先更名ResearchAgent，修改已有research（不要重复定义）：在原query/source/report_type后增加parent_query:str=''，创建已有GPTResearcher参数不变，conduct后write_report(main_topic=parent_query)，该参数已核对练习GPTResearcher1377及ReportGenerator1159/1259支持。在ResearchAgent类内run_initial_research后新增async run_depth_research(state:DraftState)：取task/topic，调用research(query=topic,source=task.get('source','web'),report_type='subtopic_report',parent_query=task['query'])，返回{'draft':{topic:report}}局部章节状态更新。源multi_agents/agents/researcher.py46–58及13–32；教学版少一层run_subtopic_research中转，不把原版捕获失败转None行为照抄，研究/写作异常上抛；尚未加入并行或审改。明确方法名depth不等于第7章DeepResearch，实际report_type为subtopic_report、普通研究链；query是本章topic，总问题经main_topic进入已有章节写作提示（不假称用于完整检索约束），不同于原GPTResearcher构造parent_query参数。用总问题RAG落地/本章部署成本，解释两个query分工、draft字典标题→正文、不同章节各自state，下一步Reviewer节点及通过/修改意见，之后Reviser和章节子图再并行。无新增测试/模型网络调用/原源码编辑，待用户保存与后续集成验证。

第8章核心手写第7步/Reviewer章节审阅（2026-10-27）：用户继续，只读实际练习仍未保存前几步，本轮提供代码而不称集成通过。原reviewer.py已重读全，draft_review已核对。交付ReviewerAgent放ResearchAgent之后、EditorAgent之前，构造保存异步call_model，async run(state:DraftState)读取task/topic/draft[topic]/guidelines默认两条及revision_notes，提示模型只返回完整None或具体意见、不要改正文；await调用，非字符串/空串raise ValueError，strip后小写完全等于none才转Python None，其他保留意见；有意见时draft_revision_count+1，通过保留计数，返回review和count。为核心练习简化取消原follow_guidelines开关，教学版每次审阅；明确原版默认false会跳过。本轮无JSON解析（审核返回普通文本，与Editor不同），不引入未定义辅助方法、不把调用失败None当通过；未做外部证据验证/重搜/改稿。解释计数记录需要修改的审阅轮数，未代表Reviser已执行；revision_notes下一步Reviser产生供复审，不把前次意见误作修改说明。以部署成本遗漏Embedding成本→review文本/count1→下一轮None/count仍1例子及简图。尚未装配Reviewer或接章节子图，下一步Reviser读取draft/review并返回新draft/revision_notes，再写路由及子图。无外部文件编辑、真实模型/网络调用或测试；后续统一集成验证。

第8章核心手写第8步/Reviser按意见改稿（2026-10-27）：用户继续，读取原reviser.py全74行及DraftState；实际练习尚无Editor/Reviewer等本章新增组件，不称已保存集成。交付ReviserAgent放ReviewerAgent后EditorAgent前，构造保存call_model；async run(state:DraftState)取task/topic/draft[topic]/review，None意见报错，构造总问题/章节/原稿/意见提示、保留无关内容不编造来源，要求返回JSON对象{'draft':{当前章节名:完整新正文},'revision_notes':修改说明}；await调用后json.loads，检查根dict及draft字典、当前topic对应非空字符串、修改说明非空字符串，只返回重建的draft单章字典及revision_notes。解释整章替换不是补丁追加，字段白名单避免原样展开模型结果覆盖review/计数；本节点不改review或draft_revision_count，下一轮Reviewer负责重新判定并更新意见，计数前轮Reviewer已加不能重复。两个notes区别review为审阅要求，revision_notes为修改完成说明，返回时状态仍保留旧review直到复审。链路草稿+意见→模型重写→解析检查→局部状态更新→后续复审，无搜索/新证据核验，提示不能保证真实新增事实。例子部署成本缺Embedding成本→补完整章并说明→Reviewer再审；非实际生成内容。未执行模型/测试或编辑外部文件，源码run原输出结构一致但合并revise_draft/run省略日志；下一步在Editor装配Research/Reviewer/Reviser、增加章节路由与DraftState子图，再并行章节，仍待整体验证。

第8章核心手写第9步/章节子图与返工限制（2026-10-27）：用户继续，读实际文件仍仅两状态及拼写未修研究类/旧Chief，前续Editor等未保存；本轮提供接续代码，不称用户文件已集成。原editor.py118–144/draft_review.py已核对。交付修改Editor.__init__(call_model)，保留self.call_model并装配self.research=ResearchAgent()/self.reviewer=ReviewerAgent(call_model)/self.reviser=ReviserAgent(call_model)，保留已有plan_research。类内新增普通_route_draft_review(state:DraftState)：review None→accept；否则读state['task'].max_draft_revisions默认3、count，非None上限且count>limit抛RuntimeError，其他revise。新增_create_draft_workflow，名字区别Chief总图_create_workflow：StateGraph(DraftState)，researcher绑定run_depth_research、reviewer/reviser绑定各run；入口researcher，researcher→reviewer，reviser→reviewer，reviewer条件accept→END/revise→reviser，返回未编译图。说明章图END只结束当前章节，回改不重跑研究；状态合并新draft/notes后复审，review保留直到Reviewer更新；3次改稿后第4次审阅通过可结束，若第4次仍有意见count4超限抛错而非强制通过。按RAG部署成本草稿v0→意见/count1→v1+notes→通过/count仍1给例子。真实LangGraph+本轮候选组图/路由方法、AST只提取实际文件DraftState、固定研究/审改节点，4组验证：立即通过、一次修改、三次修改后通过、第四次仍失败只发生三次改稿并抛限额错误；无原项目导入/模型/网络/环境密钥/外部文件改动。只验证候选接线控制流，不等于实际Reviewer/Reviser/用户整文件或原工程全图通过。下一步Editor.run_parallel_research编译章图并多次ainvoke、gather汇总research_data，再接总图。

第8章核心手写第10步/章节并行及接回总图（2026-10-27）：用户继续，原editor.py52–77/161–168、orchestrator60–103已核对；实际练习仍未保存前续完整组件，本轮不修改外部文件或称集成通过。交付Editor类内_create_draft_workflow之后新增async run_parallel_research(state:ResearchState)，创建章图并compile一次，tasks=[]；逐sections为每章新建{'task':state['task'],'topic':topic}输入，append chain.ainvoke协程，await asyncio.gather(*tasks)，取各完整返回状态result['draft']汇为research_data，返回唯一局部字段。解释tasks为协程列表非循环内逐项await；同一编译图多次调用的章节state独立，task配置仍同一引用、不是全对象深拷贝，角色节点不把可变稿件写self。gather输出输入序而非完成序，当前无并发限流、单章异常传播不返回部分结果、不保证其他任务自动取消。Chief._create_workflow三处接线：注册researcher绑定self.editor.run_parallel_research；human条件accept由END改researcher；追加researcher→END，暂时结束于各章草稿汇总，后续再接Writer；不触碰HTTP multi分支。用A/RAG原理与B/部署成本例子，每章独立审改，返回[{'A':v1},{'B':v0}]等结构。真实LangGraph章节图+本轮候选并行方法+节点替身+仅AST提取实际DraftState，事件同步强制B整章完成后A才继续，验证完成B/A但结果A/B、仅A返工且计数1/B0、task原配置未修改全部通过；无真实模型/网络/导出，未等同用户完整文件/原工程全图运行。下一步Writer消费research_data生成报告结构，继续保留FactChecker/Visualizer/Publisher核心待写。

第8章核心手写第11步/Writer报告结构（2026-10-27）：用户解释ainvoke协程收集后继续，重读原Writer32–71/98–146，并只读实际练习（尚无本章Writer等组件，不声称保存或跑通）。交付ResearchState在research_data之后补introduction/table_of_contents/conclusion:str、sources:list[str]，保留report。WriterAgent放Human之后Chief之前，构造call_model；run(state:ResearchState)把总问题/title/research_data放提示，要求只补引言/目录/结论/参考条目、保留正文不重写、引用仅已有链接、sources无来源时空列表，返回四字段JSON字符串；await调用后json.loads，根dict/三项非空字符串/sources字符串列表校验；显式只返回四字段，不原样展开模型结果，避免覆盖research_data。教学版省略原日期/headers翻译及日志，事实反馈接入待下一步再写，不提前调用未实现FactChecker。Chief构造新增self.writer=WriterAgent(call_model)；总图注册writer，移除researcher→END改researcher→writer→END，暂止结构完成而未生成最终report（Publisher待写）。说明Writer消费的是多章节汇总非单章DraftState、不重跑检索；sources是模型整理的格式化条目非真实材料存储或验证证明，无可用链接不编造；类型检查不能保证内容与引用正确。对原研究正文/结构分工配RAG例子与简图，代码本轮未执行模型/测试或编辑外部文件。后续FactChecker及反馈回Writer、Visualizer、Publisher、接口适配/集成测试仍待完成。

第8章核心手写第12步/FactChecker与Writer返工回路（2026-10-27）：用户继续，原fact_checker10–66/fact_review全部及writer39–40复核；只读练习仍未保存前序组件，不称集成成功。交付ResearchState补fact_check_notes:str|None和fact_check_revision_count:int；FactCheckerAgent放Writer后Chief前，构造call_model，run将introduction/research_data/conclusion放提示，要求完整None通过否则具体关键意见，await模型后非空str校验（Python None失败不能当通过），严格strip/lower整词none归一None，意见时计数+1，返回两字段。Chief装配self.fact_checker，新增普通_route_fact_check，无意见accept、有意见按self.task.max_fact_check_revisions默认3及count超限抛RuntimeError，否则revise（None上限不限制）；注册节点fact_checker，移除writer→END改writer→fact_checker，条件accept暂END、revise→writer。Writer.run新增fact_notes=state.get('fact_check_notes')，user提示加入意见及“如有意见，在引言和结论中落实修改”，保持四字段输出/不动research_data，形成真实数据反馈而非仅画边。用正文正确但引言声称完全消除幻觉→意见/count1→Writer改引言→None通过/count1例子；明确FactChecker无新搜索/来源核验，章节正文若错此回路不保证能修，超限报错，不强行通过或宣称自修成功。原缺少Chief包装器在教学实现补上，原工程不改；下一步Visualizer和Publisher及最终report，后续接口适配和用户文件集成测试。无模型/网络调用/新测试/外部文件写入，只有源码阅读和索引更新。

第8章核心手写第13步/Visualizer与Publisher输出（2026-10-27）：用户继续，重读原visualizer/publisher全文件并只读练习（前序组件未保存，不能称集成）。交付ResearchState补diagrams:list[str]；VisualizerAgent放FactChecker后Chief前，call_model异步接口，run给research_data要求一段Mermaid Markdown或完整None，非空str校验，strip/lower整词none→[]，否则[diagram]，避免原子串None误删与Python None误判，不做语法校验/渲染。PublisherAgent放Visualizer后Chief前，无构造依赖，普通def run(state)逐research_data各章字典.values收集正文，join后以parts列表拼中文固定标题/引言/目录/正文/结论，有图则图表部分，有sources则参考文献，返回{'report':join(parts)}；无I/O/LLM，故不使用async，无章节标题二次补写。原日期/标题翻译/导出配置简化掉，文件导出留复用第6章外层工具，不能称已接好或本章重新手写转换器。Chief装配Visualizer(call_model)/Publisher()，注册visualizer/publisher，把fact_checker条件accept由END改visualizer，追加visualizer→publisher→END，review分支仍回writer。此时“已交付图内核心骨架”不等于实际文件实现/全图测试完成；尚缺模型函数装配、入口/导出对接、用户文件保存/整体验证及工程收束。真实LangGraph候选async Visualizer→sync Publisher图+固定模型，检查正文拼接顺序、有图/无图、合法图含None保留、Python None拒绝及无来源省略参考段通过；测试省略提示词、不验证真实模型/Mermaid渲染或PDF/Word，不写输出文件，不改外部练习或原源码。下一步先补装配/入口与保存差异再整体检查，禁止直接跳第9章。

第8章核心手写第14步/统一装配与运行入口（2026-10-27）：用户继续，核对原main.py40–50/llms.py及实际练习，实际文件仍仅旧Chief及ReasearchAgent，已提供组件未保存，不称已集成。交付替换Chief.__init__(task,call_model,ask_feedback=console_feedback)，完整装配research/editor/human/writer/fact_checker/visualizer/publisher，保留其余已写组图/路由/run方法。解释统一call_model为async(messages)->str接口，不是返回结果或模型名，传给Editor再传Reviewer/Reviser，另传Writer/Fact/Viz六个协作角色；研究组件内已有GPTResearcher.call_model/plan_model/write_model仍独立，不假称全部模型接口已统一。新增模块级async run_multi_agent_task(query,call_model,source='web',include_human_feedback=False,ask_feedback=console_feedback)，放Chief结束后路由前，普通dict配置query/source/max_sections3/include_human_feedback及三种返工上限3，构造Chief并await run_research_task返回全状态；最终report从result['report']取，与旧模块write_report不是同一返回类型。用户不用手写更多测试替身，按原路线真实provider留第10章，由助手集成检查提供固定模型函数；没有把旧demo_model/demo_plan_model误装为全部角色模型，没有虚构可运行的具体调用或导入未实现函数。仍待实际文件完整保存、请求/导出接线及整体测试/工程复盘，不能勾选第8章或跳第9章。本轮未调用模型/网络/执行新测试或写外部练习文件。

第8章核心手写第15步/HTTP请求分流及复用导出（2026-10-27）：用户继续，读实际ResearchRequest/run_agent/write_report（仍旧multi400、未保存全章类）、原websocket_manager134–142，核对本地Starlette app.state和backend.utils导出签名。交付app=FastAPI()后新增app.state.team_model=None作为明确模型依赖槽，真实Provider仍第10章，测试助手注入；未装配时multi请求503、不误装旧demo_model/搜索规划模型。替换模块write_report：multi分支从app.state读取模型，await run_multi_agent_task(query=request.task,call_model=team_model,source=request.report_source)，取state['report']，来源模式用请求，researcher_information包含source_urls=None/research_costs=None/references=state['sources']，因为图未汇总真实URL/成本而不能编0或把模型引用当URL；其他类型继续原run_agent(...return_researcher=True)及真实对象metadata。之后共用原Word→PDF导出和响应字段，保持@app.post路由调用方式，run_agent multi400占位不被该HTTP分支调用。未新写文件转换器或graph→GPTResearcher假对象，导出异常/覆盖等工程边界留原约定口头复盘。真实FastAPI测试客户端+仅AST提取实际请求模型+本轮候选write_report+研究/全图/导出替身，确认普通/detailed/deep转发、multi状态和函数注入、共享导出顺序路径、未汇总metadata为null、未装配503且无执行、缺task422；没有真实完整图、外网/模型/密钥或新文件导出，旧httpx弃用警告不改依赖。本轮只改索引，不写外部练习，未宣称其已跑通。现需实际整章代码定位/保存再集成检查与工程收束，不能勾选第8章。已通过异步澄清询问当前真实手写文件完整路径或尚未保存，因为持续读取旧文件看不到前述组件；这是定位待验证代码，不是审批或要求用户执行测试。

第8章整章代码定位回复：用户明确回复“还没保存”。已知目标仍为D:\桌面\新建文件夹\1.py，不再反复询问路径；继续给出本轮接口衔接代码，实际文件的完整性/整章执行验证待保存后进行。先前候选隔离检查不能当成已保存整章通过。

第8章保存后修复/整章验收（2026-10-27）：用户继续后实际练习已保存全部主体，共2043行；审查期间用户又保存了上一轮HTTP分流和app.state.team_model，原SHA从e9a1bb...变化为dc027d76c13661a2794452392d54ade01c8f97749dc5049a57c0a05650456ab9。先dry-run展示精确差异，调整修复器保留用户刚补HTTP，不重复添加team_model或格式化覆盖。通过受限路径写入审批执行scripts/repair_chapter8_practice.py --apply并校验该hash，备份D:\桌面\新建文件夹\1.py.before-chapter8-20261027-190202.bak。修复ResearchAgent.run_depth_research参数类型ResearchState→DraftState（本机LangGraph state.py817–835读取节点参数type hints推断输入schema，不只是编辑器提示）；Editor误装self.reviser为Reviewer→Reviser；Editor/Human取task漏字符串引号及initial_research错用变量键；章节图遗漏return workflow；总图planer/planner及research/researcher名称不一致；await chain.invoke→ainvoke；去掉重复researcher→writer边（重复边不单列为阻断错误）；Reviser取当前章节正文；补已教的规划max_sections>0/根dict、改稿根dict及draft字典校验。源项目multi_agents/及已有query_processing用户差异均未改。

新增scripts/check_chapter8.py，从实际保存文件AST仅装载类/函数，真实LangGraph总图和章节图、真实已写GPTResearcher编排/Document/分块/过滤；替换模型/搜索/抓取/Embedding/导出为固定对象，控制流边界用研究I/O替身加速。17组通过：两图真实引用与schema编译；初始研究→规划→两章并行（A改稿B直过）→Writer事实返工→图表→发布；总问题进章节写作，正文不被Writer多余返回键覆盖；人工反馈重新规划增加章节/no接受/严格no匹配/次数上限；各章3次改稿后持续失败退出；事实3次重写后失败停止；规划JSON结构/数量、审阅/事实/图表Python None/空响应、严格None哨兵、改稿完整正文和说明、Writer四字段校验、无图正常发布；HTTP未配模型503不启动工作/缺task422/配置固定模型后实际全图200且导出输入一致、未知source_urls/cost为null、模型错误500且不导出。没有原项目导入/load_dotenv/.env读取、真实LLM/外网/Milvus/真实PDFWord转换，不能当质量/服务验收。更新旧check_chapter6 AST loader注入TypedDict/StateGraph/END及空team_model，旧6/7 HTTP multi占位预期400按新已教接口改为未装配503；两回归分别17/18组通过，总52组；不是放宽错误断言，其余旧行为保留。三个检查过程最终文件hash相同：923fb485e8c9e5a000e64f1b093d918c8c39cf0399636eacd73820f75c1998fd，后续只读核对未变。

第8章工程口头收束：并发层数与多用户叠加需统一限流/超时与预算，不能把gather当限流或失败自动取消；“修改→复审”有次数上限但不保证事实正确，当前Writer只改结构文本、正文错误可能需要回对应章节重新取证/改稿；人工反馈需要统一消息接收及持久化任务状态，当前控制台/原浏览器接线不是可重启恢复的检查点实现；JSON/TypedDict只约束部分结构，引用须核验、成本需从所有实际调用汇总，当前unknown明确null，报告路径并发覆盖等沿第6章说明，工程细节不新增手写。默认HTTP multi仍503直到装配team_model，按既定路线真实Provider第10章；助手测试使用固定注入已证明控制链，未声称服务已配真实模型。约定LangGraph核心到此完成；AG2未完整精读、真实WS通信/部署第11章与模型质量评测第12章继续保留待办，不把第8章勾选解释成整个目录所有实现全部覆盖。下一章仍为原清单第9章Deep Agents，不擅自提前开始，等用户继续。

第9章源码讲解第1单元/示例入口与整体链路（2026-10-27）：用户继续进入原第9项，保持先源码流程后确认手写，不再扩新路线。盘点deep_agents目录；读main.py100行、agent.py89行、tools.py78行、task.json和requirements全部；README仅1–75行、benchmark.py1–36/76–133已读（其余评测、结果及语料尚未深入，不声称全章覆盖）。入口main.run_research_task64–91：task or open_task，直接写入query，创建本次run_dir，build_agent，messages标准用户请求经build_request33–37组装，astream(updates,recursion_limit200)运行、verbose时print_progress只打印工具/AI进度，完成后检查run_dir/report.md并读取返回，未生成文件返回None；未捕获的模型/流/读文件错误上抛，空文件没有非空校验。main/open_task有load_dotenv顶层，不import或执行这些模块，未读.env。

装配agent.build_agent63–89：模型字符串STRATEGIC_LLM优先/task默认，build_research_tools闭包，主编显式研究工具只有quick_search，researcher自定义子Agent带quick_search/deep_research，两个长prompt规定概览→write_todos→task章节委派→研究员研究并write_file写sections路径→主编read_file审阅/反馈委派或edit_file→组装report.md，FilesystemBackend以run_dir为根/virtual_mode=True。本轮说明这是提示词预期流程，不是硬编码顺序/保证恰好一次或确实并行，也未声称文件后端是系统安全沙箱。create_deep_agent为外部deepagents库（无下划线），本地deep_agents为集成示例，Deep Agents仍用LangGraph运行时；与第7章显式递归DeepResearch、第8章自定义StateGraph区分。tools.deep_research61按parent_query选择subtopic_report/research_report，不走report_type deep；工具边界下节展开。main示例与benchmark.py build_gptr_agent114–123接线不同，后者把两研究工具直接挂在Agent而未配置示例的researcher子Agent，本轮不把benchmark结果解释为main流程实测。

环境/文档核对：本机.venv尚无deepagents安装，requirements仅deepagents>=0.6无上限。查LangChain官方当前overview（https://docs.langchain.com/oss/python/deepagents/overview），确认LangGraph runtime、内置文件/委派工具，并发现v0.7开始write_todos规划需显式添加TodoListMiddleware，早期默认包含；本项目create_deep_agent未加该middleware，故宽版本依赖不能保证README预期规划工具存在。记录为版本兼容缺口，待工具装配/环境单元处理，不擅自安装SDK或改原源码。官方Reference两个具体URL抓取unsupported markdown，未以其失败页面当证据；采用可读取overview的明确说明。未跑真实Agent/搜索/模型/评测，未安装包、改练习或读密钥。用RAG落地原理/成本两章节的预期文件协作示例与Mermaid拉通，下一单元深入quick_search/deep_research的参数、闭包source、实际研究链和返回内容；Benchmark及全部原始结果真实性边界后续另讲。

第9章源码讲解第2单元/两个研究工具的真实链与闭包边界（2026-10-27）：重读tools.py全部，补读原GPTResearcher构造53–158、quick_search519–566、conduct331–395、write451–493、get_source_urls733–739/get_costs749–755、skills.writer96–134与get_search_results43–80。build_research_tools由agent.build_agent调用，普通工厂先取task.source默认web，返回quick_search/deep_research两个函数引用，未建研究对象/未执行API。模型参数仅quick(query)、deep(query,parent_query='')；source闭包绑定由宿主配置，后改task.source不改变已绑定字符串，无需self。重要边界：quick构造未传report_source、原构造默认web，且quick方法默认all_retrieversFalse/aggregated_summaryFalse，调用首个检索器get_search_results→to_thread同步search，返回结果列表后包装为编号/标题/body或content/href或url文本；不完整研究/抓取/写报告，空结果No results found，非列表真值原样返回，str注解不是强制转换。source=local不会让此概览工具切本地文档分支，若配置联网检索器仍可能外部搜索；没有擅自改变原实现。

deep工具parent_query非空→subtopic_report，空→research_report，不走第7章deep；创建独立GPTResearcher并透传闭包source和parent_query，依次await conduct_research/write_report，角色选择收到parent_query，章节writer把它映为main_topic，复用既有来源分流/上下文链。每次调用研究对象独立，不共享visited/context；函数返回Markdown字符串，未写章节文件（由研究员后续文件工具写）。结尾get_source_urls原工程实际返回list(visited_urls)，附加### Sources仅地址列表，不保证抓取成功/被正文引用/支持论断；与手写版以research_sources取源的改进区分。_track_cost在quick成功搜索后、deep成功写稿后累计可选tracker.total；主示例build_agent未传tracker，benchmark.build_gptr_agent才传；仅GPTResearcher账本不含外层主编/子Agent模型，失败已发生成本可能未累计，不能当完整预算/账单。

AST只提取实际build_research_tools，注入固定FakeResearcher（不import项目或deepagents），7组行为检查通过：返回未执行函数/签名参数边界；quick文本格式与默认web；task修改后原hybrid闭包仍生效；deep顺序及两报告类型；未经核验的地址直接附录；空结果/非列表真值返回边界；成功成本累计与写作失败传播并漏记既有模拟成本。未联网、读环境/密钥、安装SDK或运行真实研究/框架；数字仅模拟账本不是真实报价。用RAG部署成本的调用/输出例子和两分支图讲解，保持源码阶段；下一单元研究员如何接任务、把长稿写文件、回短摘要，主编如何读文件复审与组装，工具/文件权限和SDK版本问题随后展开。

第9章源码讲解第3单元/章节委派、文件交接与上下文（2026-10-27）：重读agent.py11–89与main40–91，补读README75–115（架构/步骤）；查官方https://docs.langchain.com/oss/python/deepagents/subagents，核实自定义SubAgent name用于task工具subagent_type，静态description供主Agent选择角色，system_prompt为子Agent独立规则，默认isolated只收到委派任务描述、最终结果回主Agent，不自动传回全部中间调用；当前本机仍未装SDK，依据源码装配和官方契约解释，未称真实子Agent运行。以总问题RAG落地/本章部署成本/工具路径sections/02-cost.md示意主编task调用的subagent_type='researcher'及动态description必须包含总问题、章节、文件目标；不把它当用户需手写的Python函数。区分配置里的静态description与单次task动态description。研究员prompt47–59要求deep_research(query=章节,parent_query=总问题)一次→完整带引用Markdown→write_file保存带##章节标题、保留引用→最终仅≤150词摘要/来源数量/路径；词数/次数/来源数均无本地Python校验，不当作执行保证。

两条交接通道：正文写到本次run_dir文件后端，最终短摘要作为task结果返回；主编据路径read_file审稿，长研究工具输出默认不全量回灌主对话，但read_file所读正文仍进入主编上下文，不能宣称主编永远不读长文本；上下文隔离不等于文件工作区分离。主编prompt27–29决定小改edit_file/大改再次委派researcher（不是第8章专门Reviser）；返工再次调用子Agent，不能假定它记得旧子Agent对话，任务应带路径和具体反馈。研究员prompt仍要求先deep_research一次，故返工可能重跑研究，并无独立Python返工上限或skip-research分支，外层仅recursion_limit200等框架限制。版本相关write_file覆盖旧稿/权限/内置工具实现不在未安装环境中猜测，下一单元文件后端与工具边界单独核对。主编最终按prompt30–37读稿整合、去章节来源列表、去重参考文献并写report.md，main最后读该文件返回；不以“模型说已完成”代替文件存在证明。README图以GPTResearcher(conduct+write)统括quick/deep属组件简化，quick实际只走上一节的检索链，后续讲调用不照抄图。保留源码阶段，未安装SDK、运行Agent/外网或修改练习，下一单元FilesystemBackend/工具可见范围/版本兼容，再Benchmark构造与评测；不提前手写。

第9章源码讲解第4单元/文件后端与工具边界（2026-10-27）：重读agent63–89/main64–91/requirements及相关配置检索，查官方backends/permissions文档及langchain-ai/deepagents main分支graph.py、backends/filesystem.py（仅网页阅读未下载执行/安装）；外部源中的提示词文本仅作为被分析的数据，不作为本任务指令。按当前官方实现，FilesystemBackend(root_dir=run_dir,virtual_mode=True)把report.md或/report.md映到本次输出目录，_resolve_path165–203拒绝..和解析后越根路径；这是路径语义/文件工具防护，非OS进程/网络沙箱，也不限制自定义Python工具GPTResearcher内部DOC_PATH读取和外部检索。当前官方write462–494用O_TRUNC覆盖UTF8文件，edit按字符串替换；本项目宽依赖>=0.6、本机未装SDK，因此仅以当前实现说明，不假定所有历史版本相同或已实测本地SDK。

工具范围：agent.tools=[quick_search]及researcher.tools=[quick_search,deep_research]是自定义工具配置，不是完整工具白名单；当前create_deep_agent通过FilesystemMiddleware加文件工具、SubAgentMiddleware加task，权限需单独设置且仅作用内置文件工具，自定义/MCP工具不自动受它覆盖。原build_agent未配置permissions/interrupt_on/checkpointer；没有逐章文件ACL/自动人工审批/完整会话持久化，磁盘文件留存不代表可从中断点自动恢复。上下文隔离不能防两个章节写同一路径覆盖，prompt的不同编号路径是命名要求而非本项目Python锁。约束分三层解释：提示词规定研究次数/词数/章节数/引用；工具参数与闭包固定source；程序/后端限制文件映射、图步数和实际输出检查，不能把自然语言要求说成强制校验。

验证实际入口函数AST（不运行顶层load_dotenv），Agent、os.makedirs及open全部内存替身：写report.md→返回正文；未写→None；空文件→空字符串；astream异常→原样上抛；同时检查query写回task、build_request章节数文本及stream配置200/updates。未创建真实文件/联网/模型调用/SDK环境变更。原main读报告未显式encoding，当前官方后端UTF8写入，Windows中文编码风险留运行环境/手写时核验，不未经检查改源码。用工具虚拟路径→真实输出根的RAG章节例子、工具可见性表/边界简图讲解，源码仍在进行；下一单元转Benchmark的构造入口与一次评测请求的输入→生成→指标/裁判→保存记录，先分清它与main示例的不同接线，再选代表而非逐脚本重复讲。

第9章源码讲解第5单元/报告Benchmark完整评测链（2026-10-27）：读benchmark.py123行、report_benchmark.py225行全部，BENCHMARK.md1–116，读取本地reports_2026-07-04_14-33-21_n8.json结构/元数据/summary并逐records核算，未输出或转载整篇报告、未联网重跑评测。入口report_benchmark.main：固定TOPICS前n（默认8），seed42只初始化Python RNG，外层同args.model，ChatOpenAI裁判；builder baseline为原始Tavily internet_search（max_results/topic/raw_content参数、query截400、非法topic归general），GPTR为quick+deep直接工具，无demo的显式researcher子Agent/磁盘FilesystemBackend。共享基础提示但附加各自不同tool guide；同外层model及recursion_limit60不等于内层总调用/预算相等，GPTResearcher另有自身模型配置。每主题semaphore包住先baseline后GPTR的报告生成，主题间并发；judge在semaphore外，concurrency不统一限裁判。write_report111–125用wait_for1800s包ainvoke，取最后message的text（属性/方法兼容）作为报告，记录该次生成耗时及hard_metrics，不读取demo report.md。

hard_metrics101–108仅正则提取URL集合/域名集合、split空白词数，不验证页面可访问/引用是否支持论断（中文空格计词局限）。judge_topic139–150对四维comprehensiveness/citation_quality/factual_grounding/overall逐项随机A/B摆放，to_thread同步judge_pair，A/B反映射系统，非A/B/T文本归tie；裁判异常仍上抛，本脚本无网页证据核验，factual_grounding只是读报告的相对判断。main.gather全主题成功后才汇总和写JSON（metadata/summary/records含完整报告/耗时/指标/裁判），win_rates字段实际存胜负平计数而非比例；任何未捕获生成/评分错误可使本轮无最终结果文件，不自动保存部分成功。

历史artifact算术核对：8条、外层openai:gpt-5.4/裁判gpt-5.4、seed42；每条用当前hard_metrics重新计算与保存一致，四维胜负与均值也全一致。GPTR:baseline：综合性4:4、引用质量2:6、事实扎实度3:5、总体5:3；平均URL24.5:19.5、域12.9:12、词2179:2206、耗时122.7s:60.5s；内部GPTR账本0.6505美元只是该记录字段非全系统总成本，未核验外部账单。不能从总体5/8宣称各维度都胜出或泛化准确率；更多URL不是更多已验证引用。文档头部RACE/FACT headline为另套DRB流水线，未与本脚本四维比较混用。

额外AST提取实际hard_metrics/write_report/judge_pair/judge_topic/message_text及纯常量，固定Agent/Judge/RNG验证末消息提取、text方法兼容、步数参数、URL数量、四维A/B反映射三组合及非法裁判文本当tie，全部通过；固定构造报告无证据也能计URL证实指标边界。没有import项目顶层/load_dotenv/deepagents、读密钥、调用模型/引用网页、生成新结果文件。本节只讲一条报告对比完整链，下一节选择有标准答案的本地+网络事实检查点作为第二代表，recency/breadth/QA等同类文件由助手阅读归纳用途，不逐脚本灌输；DRB输入输出与官方指标单独简要核对，不把本脚本当官方FACT。

第9章源码讲解第6单元/Hybrid事实检查点评测（2026-10-27）：读hybrid_benchmark.py237行全、recency_benchmark191–238评分模板/解析函数、build_corpus.py371行全部及internal_docs_src四个事实文档；当前生成语料27文件已数，未运行含清空重建目录的生成器，也未宣称逐一解析验证现有PDF/DOCX产物。虚构Veltrix公司资料包含4事实文档（2PDF/1DOCX/1MD）、3过期近似文档及20部门干扰文档。TASK提供单个尽调问题、8内部检查点及4网络检查点；生成Agent只收到prompt，不把标准答案列表直接放进生成请求；内部事实来自虚构语料，不把代码注释中July2026网络事实当今天已核验新闻。

三组：baseline仅Tavily网络工具、默认框架文件状态不挂内部语料；baseline+files复制27文件到临时目录并将FilesystemBackend根设该副本，给ls/read_file指引，副本可写并非只读；gptr将source='hybrid'闭包绑定工具，通过DOC_PATH指定原资料目录。脚本顶层设置DOC_PATH为进程环境，分析时不执行顶层；三组在main184–207顺序各生成报告（复用上节write_report消息提取/超时）再分别给内部和网络检查点打分。差别用于比较“没资料/有资料且自选文件/有格式解析与检索管线”，不能以web0分单独证明算法优越，也不能把当前文件工具版本能力等同历史运行。

grade_report在recency224–238：同步裁判接标准列表和报告，对每点出CORRECT/PARTIAL/MISSING/WRONG及evidence；async主流程通过to_thread调用。find首[末]抽JSON最多3次，只有结果长度检查，不验证每项结构、grade枚举、checkpoint编号完整唯一或evidence真实；裁判调用异常不在JSONDecodeError重试范围。coverage157–165为(CORRECT+0.5PARTIAL)/n，WRONG和MISSING都0，不对幻觉额外扣分；是报告的加权标准检查点覆盖率，不是检索Recall@K/事实逐字自动匹配/全系统准确率。每检查点可能包含多事实，0.5权重只是规则。本脚本评分时不重新上网核验web标准或URL论断支持。

读取2026-07-05三份hybrid JSON（每份同一task的一次run），用实际coverage逐internal/web grades重算，与记录和summary全部一致。三次平均内部baseline0、baseline+files0.625、gptr0.875；网络分别0.4166667、0.4583333、0.4166667。gptr内部三次0.812/0.875/0.938，文档up to94%是最高一次四舍五入近似，不能替代平均或泛化准确率。baseline第一次8WRONG、第二次8MISSING，coverage同为0，说明需同时看分类计数而非只看总分。仅核对历史记录算术不等于真实复跑/独立验证裁判语义。

AST只提取实际coverage、grade_report和纯模板，固定裁判验证带代码块JSON/第一次失败第二次成功、3次耗尽异常、1/0.5/0/0分权重，通过；同条数但编号重复和BOGUS标签会被原解析器接受，已确认缺口。未导入load_dotenv/SDK/修改环境、访问外网/模型、生成语料或写结果。已讲两种评测代表：报告相对偏好与标准事实覆盖；下一节只集中归纳其余同类脚本/历史文件用途，并简要核对DRB适配入口及RACE/FACT边界，不再逐个重复同类调用链；仍未开始本章手写。

第9章源码讲解第7单元/剩余评测与DRB收束（2026-10-27）：读drb_generate.py134行、drb_harness.patch99行、recency/breadth全部控制流程（其静态TASKS作评测数据结构/用途审阅，不声称逐条新闻事实已验证）、README余110–200、BENCHMARK余117–170、SHARE_SUMMARY80行及__init__，四个DRB结果文本；检查所有21个顶层结果JSON的结构/条数，并补看QA嵌套systems.records（SimpleQA最新30条/FRAMES最新20条），不因根无records就误称无样本。Deep_agents当前11个Python文件核心代码均已覆盖；source语料四文档与生成器已读、生成产物用途清楚，但未逐二进制核验、未独立验证全部静态标准事实、未跑真实LLM或评测。

余文件只归类不再重复流程：recency为7题各6检查点，固定2026-07-04标准与“今天最新版”提示存在时间漂移（deepagents检查点仍0.6.x而当前官方已有0.7）；official_citation_share只URL域名匹配非来源支持验证。breadth为2复合题25/21检查点、外层预算25/60与两工具组交叉，复用grade_report；生成任何Exception都当空报告并把latency置0，不仅步数超限，也会影响平均耗时；预算仅外层步数非总调用成本。SimpleQA/FRAMES有历史问题/target/prediction/grade/计量记录，但当前本目录Python仅report docstring提及，无对应执行入口，不凭结果文件声称可现成重跑。baseline_files_check为辅助文件访问检查，元信息不足；README/BENCHMARK/SHARE为说明/复现/传播文档，不是算法或独立证据。

DRB适配：drb_generate从外部harness query.jsonl选英文任务，调用前述两个builder（仍直接挂工具，不等同主编章节文件demo），按{id,prompt,article}逐行JSONL格式输出到外部raw_data。独立外部run_benchmark.sh再做RACE与FACT评分；已读官方README、utils/api.py、run_benchmark.sh（https://raw.githubusercontent.com/Ayanami0730/deep_research_bench/main/...），明确RACE参考报告+任务自适应维度/权重的质量分，FACT提取/去重statement-URL对→重新抓取→模型判断支持→stat汇总，不把URL正则计数等同FACT，不把RACE0.5124叫51.24%准确率。当前上游已自带OpenAI/OpenRouter；本地patch实际仅改目标系统/进程数及Jina可无key、90s超时、失败BS4回退30s及正文前60000字符，不包含文档声称“新增OpenAI裁判后端”的实现；外部代码commit/依赖未固定，未clone/apply或运行，不保证任意版本复现。

DRB历史四文本可读值：baseline RACE0.5028/GPTR0.5124；平均引用34.5/62.9，有效18.6/35.2，比例0.5391304/0.5596184，有效数相对增加89.25%。该目录仅4汇总txt，无本次原始生成JSONL、抽取/去重/抓取/逐条判定明细，无法从这些文件独立重核7/10、zero-citation条数、每个引用是否真被支持或完整100题榜单名次；文档声明10题子集不当全量官方成绩，本轮未复跑。

AST实际sample_tasks配内存JSONL验证英文过滤/同seed复选，源A:B=10:1而n2每类1条，表明算法按类别轮询而非注释“按频率比例分配”；请求数超过可用英文样本会while不终止，用sys.settrace限1000步安全捕获，未卡住实际任务。AST提取main嵌套run_task和pending表达式配失败Agent，确认错误返回空article但保留id，该行保存后done_ids只看id会跳过重试；原脚本仅每组gather齐后批量追加，不是逐任务完成即时持久化。只检查纯逻辑/本地算术，不读.env或密钥、不调用模型/网络、不安装SDK、不写生成结果。第9章约定源码核心收束，待用户确认再手写；建议手写仅工具工厂/Agent与文件后端装配/入口和最小评分，完整语料生成和评测CLI复用，不把复现缺口假称修好，不跳第10章。下一步确认核心手写范围或按用户问题补讲。

第9章核心手写第1步（2026-10-28）：用户在源码核心收束后继续推进，开始工具封装；仅布置 build_research_tools(task) 的闭包及 deep_research(query,parent_query) 完整研究调用链，教学版先按名称返回 {"deep_research": deep_research}，下一步加入 quick_search，不提前使用未实现的 practice.quick_search。重新读取实际练习文件，确认 GPTResearcher 构造参数为 query/report_source/report_type，无 parent_query；因此通过 write_report(main_topic=parent_query) 传整体主题。函数放在模块顶层 GPTResearcher 类结束之后、run_agent 之前，配置仍普通字典，模型保持原有替身。本步未代写用户文件、未执行工具、未安装 deepagents，不能称为已保存或通过运行；来源补充、工具装配、文件输出和最小评分继续后续小步覆盖。

第9章核心手写第2步（2026-10-28）：布置在 build_research_tools 内加入 async quick_search(query)->str，复用已有模块级 search_web(query)（其内部 to_thread 包装 Tavily 同步搜索），按标题、body/content 摘要、href/url 网址格式化，空结果返回说明；更新工厂返回字典同时提供 quick_search/deep_research 函数引用。快速工具固定网络搜索，不因工厂 source='local' 自动切本地；source 目前只绑定完整研究工具，沿用原项目分工。解释 enumerate 从1编号、列表收集与换行 join、嵌套函数缩进、两条工具链各自用途及调用异常向上传播。此步是教学布置，未代写用户文件或调用联网工具；未宣称已保存、实测或已接入 Deep Agents SDK。

第9章核心手写第3步（2026-10-28）：核对原 deep_agents/agent.py 全部装配代码及 requirements；pip show 确认本机 langchain1.3.16/langgraph1.2.11，deepagents 尚未安装。布置模块级 build_deep_agent(task,run_dir,model)，函数内局部导入 SDK/Path，创建输出目录，取已写工具字典，构造 researcher 子Agent说明/提示词/工具，create_deep_agent 装配主编提示词、quick工具、subagents及 FilesystemBackend。model 显式参数，仍不读取环境密钥或强制真实模型；简化提示词保留概览→章节规划→委派→读稿审核/修订→报告文件与合并引用，未调用版本敏感 write_todos 工具，待环境装配核对。区分子Agent配置字典/实际task调用、description和system_prompt、普通装配def/后续异步执行、工具函数引用、文件路径映射与prompt非硬保证。用户文件未代写，本步不宣称SDK已装或已运行；工具来源补充、入口输出、最小评分与整体验证未完成。

第9章核心手写第4步（2026-10-28）：核对 deep_agents/main.py64–100 及练习文件末尾，布置模块级 async run_deep_agent_task(query,model,run_dir,source='web')，放 build_deep_agent 后、原 __main__/uvicorn 启动块前。构造简化 task→build_deep_agent→await agent.ainvoke(messages,recursion_limit200)→确认 report.md 存在→to_thread/read_text(encoding='utf-8')→空报告校验→返回报告和绝对路径字典。教学版不用 astream/进度打印、不加HTTP分支；明确图执行结果不是正文，正文从产物文件取，200是图步数限制非网络超时/研究深度/金额预算。开始前拒绝已有 report.md 避免旧产物误判。模型参数必须是框架支持的聊天模型或模型标识，不能直接使用旧 async demo_model(messages) 普通函数；SDK安装、模型替身适配及实际测试待后续完成，不读.env、不提前连真实模型。本轮只布置代码，未宣称用户已保存或运行通过。

第9章核心手写第5步（2026-10-28）：实际练习文件已保存 build_research_tools1403–1456（quick/deep均在），整文件 AST 语法解析通过，未运行外部搜索或模型；尚未在模块顶层看到 build_deep_agent/run_deep_agent_task，不能称装配入口已保存。对照 practice ReportGenerator1198–1201：subtopic_report直接返回正文，普通报告已_append_sources；get_source_urls1394–1400从research_sources提取去重URL。布置 deep_research 写作后、返回前，仅在 parent_query 非空且有 sources 时补 ### Sources，避免普通报告重复追加。来源列表是研究收集来源清单，不等于逐论断已验证引用；主编合并去重仍为提示词要求，未实现确定性引用验证。本轮未代写练习文件，下一步最小报告指标函数及依赖/整体验证仍待完成。

第9章核心验证与收束（2026-10-28）：用户明确跳过统计指标手写，不再新增 hard_metrics/评分代码；评测源码讲解记录仍保留。用户回复“现在保存了”后重新读取实际文件，build_research_tools、build_deep_agent、run_deep_agent_task及章节来源补充均已保存；发现并在备份后仅删一条不可达重复return。备份 D:\桌面\新建文件夹\1.py.before-chapter9-20261028-141931.bak，最终SHA256=9cfef282abca8e8e53a6ff72b39ad210fb3e950bd8704cdbd64566e937a0a118。最终位置：工具1403–1466、装配1467–1519、入口1520–1571。未改HTTP分支，不把当前第9章独立入口说成HTTP已接通。

SDK环境：最新版0.7.32 dry-run会升级现有核心依赖，未安装该方案；对0.6.12解析并以当时184个已安装包全部版本作constraints，只新增11包：deepagents0.6.12、langchain-anthropic1.7.0、langchain-google-genai4.3.6、anthropic1.17.0、docstring_parser0.18.0、httpx2/httpcore2各2.16.0、opentelemetry-api1.45.1、truststore0.10.5、wcmatch11.2、bracex3.2。安装后逐一确认原184包版本无变更，pip check无损坏依赖。固定可复用版本在scripts/chapter9-requirements.txt，安装计划/约束快照在outputs/chapter9_checks。0.6.12满足项目>=0.6；不声称已兼容所有未来SDK版本。本次包下载使用网络，但验证过程中禁止socket连接、未读.env/密钥或连接模型服务。

新增scripts/check_chapter9.py：复用第6章AST加载器/外部Fixture，跳过原文件顶层imports和uvicorn；保存的研究规划/抓取组织/Document处理/写作逻辑实际执行，搜索/抓取/Embedding/内部写作和外部BaseChatModel均固定替身；Deep Agents真实SDK、task子Agent调度、文件工具和FilesystemBackend实际执行，临时产物仅在工作区outputs/chapter9_checks内，退出清理。14项通过：工厂不提前研究、两类摘要字段格式、空搜说明、搜索异常、真实练习研究链+parent主题+章节来源、普通报告不重复附来源/调用状态隔离、source闭包快照/空来源不加标题、研究失败不写作、实际task委派/中文草稿读写/最终report文件输出、子Agent只接委派描述/主编先收到短回复再read_file/工具分工/来源传递、旧report在模型前拒绝、无产物报错、真实框架写出空白文件后入口拒绝、模型失败上抛。未评估自主规划质量、生成真实性/引用支持、真实模型服务或对外网络搜索效果。

第8章17项完整回归也通过，两个检查脚本针对同一上述SHA，共31项。第6/7章本次未重跑，不能把旧35项计入此次31项。工程口头复盘收束：提示词中的章节上限/审核/引用合并是模型要求非Python硬校验；子Agent上下文隔离不等于各章文件权限隔离，文件后端根路径不覆盖自定义研究工具的文件/网络权限；200图步数不等于总调用、时限或金额预算，工具内层研究和重试需要独立限额。按原清单第9章约定核心完成，统计指标依用户跳过，真实模型/质量评测待第10/12章。下一步第10章Provider/MCP/可观测性，不自动开启真实API调用或读取.env。

第9章整章流程复习（2026-10-28）：按用户要求以“RAG如何减少幻觉”贯穿，回读实际练习三个函数1403–1571及原agent/main/benchmark入口，讲清先装配再执行、主编quick_search概览/规划、task传章节问题+整体主题+目标路径、子Agent独立上下文、deep_research调用普通/章节GPTResearcher管线并附来源、章节文件与短回复两条通道、主编read_file审核/重委派/统一引用、report.md产物校验与UTF8读取。三章和具体内容是讲解假设，非真实自主模型运行结果；此前14项只证明固定响应下真实框架控制流与文件链可运行。区分chapter9工具名deep_research和chapter7 report_type='deep'递归；原入口astream/练习ainvoke不混用；Benchmark作为另一条旁路概述生成对照报告与裁判/检查点，不把消息型benchmark输出等同主编文件型demo，不恢复用户跳过的统计指标手写。不进入第10章，不加复述/填空要求。

第9章全面复习扩展（2026-10-28）：用户表示仍不理解并要求所有点详细拉通，本轮不进入第10章。重新核对本章文件清单、11个Python模块的定义/常量位置、task.json、requirements、main/agent/tools全部核心、benchmark两builder、report运行评分汇总、Hybrid三组/coverage、recency grade解析、breadth预算失败、DRB采样/断点/产物与harness.patch、corpus生成入口；读取安装SDK0.6.12的TodoList/Filesystem/SubAgent装配和虚拟路径解析，及原GPTResearcher.quick_search/get_source_urls/get_costs。准备按模型/函数/工具/Agent/框架基本概念→注册与参数Schema→原版请求/配置→工具闭包→装配/双层模型→概览/待办/章节委派→子Agent上下文与完整研究→文件/短回复→审核/合并/最终读取→异步并发/状态/成本/失败→两类代表Benchmark/其余脚本与DRB/数据和文档→手写差异与测试边界完整解释；以RAG主题贯穿主链，虚构公司资料辅助Hybrid，明确二者不是同次运行。统计指标只说明评测含义，不恢复手写任务；不读.env、不重复运行模型或评测，不把工具docstring的“验证来源”宣传当已完成逐论断核验。

第8/9章关系专项复习（2026-10-28）：用户追问两章区别，本轮以已保存并验证的练习实现为准回读ResearchAgent1677、Editor章节图1778/并发1808、Reviewer1898、Reviser1851、Writer1958、FactChecker2015、Publisher2083、ChiefEditor图2147及两套入口。讲清：第8章ChiefEditorAgent是装配/执行显式业务StateGraph的Python协调类，并非同第9章主编模型的自主工具循环；角色类可调用同一call_model，Publisher甚至无模型调用。第9章researcher字典是配置，create_deep_agent内部SubAgentMiddleware/任务工具构建时编译研究员，task运行时选择已构建研究员并以新上下文执行；原第9创建过程在本机SDK0.6.12 graph787→SubAgentMiddleware816→_build_task_tool584→create_sub_agent577→create_agent511，task异步执行721。比较流程控制/模型自由度/两层State与messages+文件/显式gather与模型批次task/审核修订/结构化返回/输出HTTP/失败和预算/扩展成本，指出二者都基于LangGraph且复用GPTResearcher。强调第8Fact返工仅Writer结构字段，不重写research_data，审查节点存在不等于已联网逐论断验证；第9审核/次数/引用合并为提示词要求，现有根路径与步数限制不能替代全部业务约束。Benchmark是工具配置对照，不是第8对第9直接优劣证据。不增加新手写任务或进入第10章。

第10章源码讲解第1单元（2026-10-28）：按用户“继续下一章”进入源码阶段，不开始手写或读.env。阅读utils/llm.py全文件、llm_provider/generic/base.py全文件，定位agent_creator.choose_agent18–62的真实调用；已定位MCP client/tool_selector/research/streaming/retriever、utils/tools/costs/logger/logging_config定义位置，但AST清单不等于其全部实现已读。mcp-server目录当前只有README并指向外部gptr-mcp，没有本地server.py，后续区分“本项目作为MCP客户端调用工具”和“对外提供MCP服务”；README将MCP展开为Machine Conversation Protocol为文档疑点，MCP正式含义后续用协议主源核对，不沿用该文档拼写。

本单元追踪：choose_agent按cfg.smart_llm_model/provider构造角色消息、temperature0.15→create_chat_completion41参数校验与provider_kwargs→get_llm27→GenericLLMProvider.from_provider146，选DeepSeek代表分支248–255：复用langchain_openai.ChatOpenAI但API地址为https://api.deepseek.com，凭据在实际运行时从进程环境读取，本轮未取其值/构造真实客户端。from_provider返回GenericLLMProvider包装器，self.llm为具体客户端。非流式get_chat_response356–371先重置元数据，await self.llm.ainvoke→抓usage/response metadata→取output.content→可选ChatLogger→统一入口可选calculate_llm_cost/callback→返回内容；choose_agent再json.loads并取server/agent_role_prompt，Provider不负责JSON结构正确性。

参数处理与边界已读后按主链简述：llm_kwargs先覆盖model，temperature/max_tokens等后写；模型支持列表是项目静态名单，不当最新厂商能力事实。模型None/过大token参数及Provider构造发生于重试循环前；普通非流式此层最多10次、stream且有websocket只1次，异常或空响应退避1/2/4/8秒封顶，最终RuntimeError；choose_agent捕获后走已讲JSON恢复而非必然终止整个任务。成本callback在成功响应后且循环try之外，完整成本/日志/流式实现留后续专节。docstring声称仅OpenAI且reasoning默认low与实现支持多provider/实际默认medium不一致；200000的粗guard不能当任何具体模型真实上限。构造from_provider还可能自动_check_pkg安装缺失依赖，当前只读不触发。单元以假设DeepSeek配置/RAG角色选择示例说明输入输出，不宣称实际服务可用或已联网验证。后续先讲参数/流式/工具调用，再MCP与可观测性，避免逐厂商灌输。

第10章Provider概念补讲（2026-10-28）：用户两次表示llm_provider仍不理解，本轮停留当前单元，不推进MCP/手写。围绕一次“什么是RAG”问答区分参数llm_provider字符串、model字符串、get_llm工厂、GenericLLMProvider类/实例、实例self.llm底层SDK客户端及远程模型服务；按源码27/38→from_provider248→353→__init__118→get_chat_response356/360逐层展开。强调创建本地客户端/包装对象与实际ainvoke请求的时间区别、cls在工厂中返回包装对象、self.llm保存客户端、SDK ChatOpenAI类名与api_base实际目标服务分开理解、messages是输入而output.content为本例返回文字、Provider统一适配而不承担研究业务或自动选择模型。无新代码写入练习、无环境值读取或真实服务调用，不以概念讲解标记第10章完成。

第10章源码讲解第2单元/流式报告调用链（2026-10-28）：用户继续后进入普通文本流式路径。核对skills/writer.py77–134→actions/report_generation.py209–309（275调用stream=True）→utils/llm.py107–152→GenericLLMProvider.get_chat_response356/stream_response373/_send_output395。解释ainvoke整条消息与astream异步迭代块的区别，response累计完整正文，paragraph仅待发送缓冲，遇任意换行发送整个缓冲后清空，结束补发尾段；chunk不保证单token或单字，有websocket发送type='report'/output，无socket且verbose则终端打印。调用者仍等待整个流结束，途中展示与最终return是两条结果通道，不等同后台执行。元数据在判空content前抓取，空文本块可有usage。

AST提取实际GenericLLMProvider类，用固定Client/WS运行5项离线检查通过：完整正文与换行/末尾缓冲、空块usage保存、无WS完整返回、非流式ainvoke及旧元数据清空、中断异常传播与已发送片段保留。未导入项目模块/真实SDK客户端、读.env或连模型/网络，本次临时检查未新增长期测试文件。失败边界：stream且有WS统一入口这一层只尝试1次，但generate_report外层290仍会把system+user合并为单条user再次调用同一模型/Provider；不是切换备用模型或断点续写，已有发送片段不会自动撤回。两次都异常时generate_report仅print后返回初始化空串，不能误称所有错误最终都会上抛。前端如何接收/拼接的实现留第11章，当前不猜其行为。继续源码阶段，未让用户手写或宣称真实流式服务已连接。

第10章源码讲解第3单元/报告后聊天的工具调用（2026-10-28）：阅读utils/tools.py349行全部并全仓查调用，发现真实调用方backend/chat/chat.py153–184；回读该文件258行全部。本节用报告完成后追问新资料的场景：ChatAgentWithMemory.chat187把整份report和消息历史放入system/user消息（__init__79的向量初始化被and False禁用，不声称自动报告向量检索）→process_chat_completion153→create_search_tool(self.quick_search)230用@tool生成名search_tool、query:str的工具→create_chat_completion_with_tools46工厂创建Provider/消息转换→底层.llm.bind_tools注册说明（此时不执行搜索）→首次ainvoke得到AIMessage.tool_calls→追加原AIMessage→顺序for匹配tool.name并await tool.ainvoke(args)→工具调用实际ChatAgentWithMemory.quick_search114的同步Tavily接口→ToolMessage完整结果+对应call_id→二次ainvoke→返回回答与工具元数据。元数据result截前200字符仅记录用途，不截断送给模型的ToolMessage全文；聊天对外将工具名再映射为quick_search。

重要实际边界：该helper仅执行首轮一批请求、工具逐个await，无gather/持续ReAct循环；二次响应如再次带tool_calls不会继续执行，直接返回.content。无工具请求直接返回初次content和空metadata。单工具异常转为错误ToolMessage后仍请求模型；外层任何异常回退普通create_chat_completion并使用原messages、返回空工具metadata，可能丢失已经执行的工具信息，不能把有回复当搜索成功。process_chat_completion174–176为了获取metadata又调用self.quick_search(query)，所以正常一个模型搜索请求实际服务搜索两次，且二次来源可能变化；这里只说明、不修改源工程。主路径provider_kwargs只有model/llm_kwargs，函数temperature/max_tokens/**kwargs未传主调用；websocket只在fallback转交，不能误称本helper工具回答正在WebSocket流式发送。辅助get_tools旧JSON定义未接当前包装路径；create_custom_tool未使用parameter_schema且同步包装不await异步function；supports_tools是静态名单而非实际能力探测，以上工程细节留章节收束/手写时再统一交代，不逐同类工具展开多节。

用AST提取实际helper和ChatAgentWithMemory类、真实LangChain工具/消息对象，固定模型响应/假Tavily，跳过构造函数Config/环境读取，隔离项目包相对导入，6项检查通过：真实聊天消息含report/完整工具往返/重复搜索两次；ToolMessage全文与元数据截断/双模型成本callback/主路径参数遗漏；直接答无工具；二次工具请求不再执行；工具timeout变消息仍继续；bind失败按原消息普通降级。未读.env、调用真实模型或联网搜索，临时验证未新增长期脚本。第9章SDK调用循环与本helper分开，MCP本地研究还有另一执行入口尚待后续讲；本节仍源码阶段。

第10章源码讲解第4单元/MCP概念与工具发现（2026-10-28）：用户继续后进入MCP，阅读client.py179行全部、tool_selector204行主控制（选择执行细节留下一单元），回读retriever27–199和300–324、ResearchConductor653–694及MCPResearchSkill34–156；最初批量输出发生截断，结果处理research158–271及同步search包装201–298未全量确认，后续需定向补读，不标记全部实现覆盖。定位真实入口ResearchConductor._execute_mcp_research671构造MCPRetriever、688调用同步search，最后进入search_async116；本单元只讲配置→客户端对象→发现工具，选择/执行/标准化结果留后续，不把模型工具选择与真正执行混为一谈。

核对官方协议架构及server概念（https://modelcontextprotocol.io/docs/learn/architecture、.../server-concepts，当前重定向2026-07-28版本），使用稳定的Host/Client/Server角色和tools/list发现、tools/call执行概念；不将最新版握手/无状态机制套到旧项目。纠正mcp-server/README7的Machine Conversation Protocol错误展开，正式名称Model Context Protocol。项目当前作为MCP客户端连接提供工具的程序；模型仍由LLM Provider调用，MCP不替代模型接口。示例本地HTTP资料服务仅假设，不声称已启动或连接。Minimal配置name/connection_url经client.convert_configs40转为name:{transport:'streamable_http',url}；stdio只是本地进程通信，不要求所有MCP工具都远程联网。

安装环境已有langchain-mcp-adapters0.3.2，非本轮新增。实际读取其client.MultiServerMCPClient.__init__55–126/get_tools166–216，确认构造只存配置，get_tools才load工具并返回LangChain工具代理；默认逐工具调用新会话，不能将manager缓存对象等同永久网络会话。项目MCPClientManager用asyncio.Lock避免并发重复建对象，_client None→客户端引用，get_all_tools调用client.get_tools，MCPRetriever成功后缓存_all_tools_cache；返回工具说明/代理不是查询结果。缺适配依赖/无配置/发现异常返回[]；close_client只清引用，文档“自动清理所有连接”的说法过强。4项AST离线检查通过：HTTP配置转换、并发创建同一缓存对象、发现返回工具而不搜索、清引用重建与空配置/缺依赖分支；未导入项目包/真实客户端、不启动服务/读.env/联网。

后续待讲：工具选择与实际调用（MCPResearchSkill只一次模型调用后执行首批工具，不自动将结果再交回模型；其content是执行前生成的分析，不可说成工具结果总结）、标准化与来源/上下文合并、fast/deep/disabled缓存策略、同步包装线程/事件循环阻塞边界、MCPStreamer与费用/日志。其他已发现待工程收束点：配置str args简单split会影响带空格路径；connection_token直接token字段未证明形成认证headers；当前适配器支持websocket但不能把项目分支说成协议标准传输或兼容任意版本。第10章仍源码阶段。

第10章源码讲解第5单元/MCP筛选与实际调用（2026-10-28）：重读tool_selector35–204、research34–271全控制及结果解析、prompts40–118两份MCP提示词、retriever137–160。以RAG检索遗漏/资料服务贯穿：Retriever先select_relevant_tools(query,all_tools,max_tools3)，提取index/name/description给普通create_chat_completion战略模型，返回JSON中的selected_tools；按index映射回原工具对象，并未调用工具。再conduct_research_with_tools创建战略模型Provider、bind_tools(selected_tools)，将研究问题和工具定义给模型，取首批tool_calls的name/args，匹配原工具代理并await ainvoke，随后_process_tool_result统一title/href/body，返回检索结果。两步可同一战略模型，普通JSON筛选与结构化tool_calls填参不是同一份输出。工具列表是允许集合，不代表都会执行。

明确代码真实边界：筛选prompt要求EXACTLY3，但实际只校验index在范围内，无硬数量/去重/name一致性验证；空/坏JSON/异常转关键词fallback，名称命中+3、说明命中+1，只用search/read/get等模式不结合query语义。执行按for顺序await，无gather、无持续循环；未知工具/单个工具失败跳过，外层失败返回[]。MCPResearchSkill只请求一次模型，工具结果不作为ToolMessage回传再调用模型；response.content如有会以mcp://llm_analysis额外入结果，但它是工具执行前文本，不是基于工具返回的总结。搜索得到doc_id后再动态决定read_doc的依赖式多步链，目前没有实现；提示词“失败后尝试替代/综合多源”不能当循环代码已落实。结果格式化这里只说明目标接口，分支和上下文合并留下一单元。

6项AST离线验证实际selector/research及提示词通过：筛选返回原对象且不执行/少于3接受；index主导、错name/重复/超数接受；坏JSON关键词备用；执行仅一次模型调用/格式化资料/前置分析；无工具请求也可仅凭模型文字返回结果；未知和失败工具跳过后继续。假模型/假工具隔离相对导入，未读.env或连接真实模型/MCP服务，无源工程修改或新手写。待成本节说明selector普通调用接callback，而执行技能直接llm.ainvoke未接相应账本。第10章仍源码阶段。

第10章源码讲解第6单元/MCP结果标准化与上下文回接（2026-10-28）：重读research._process_tool_result158–271、ResearchConductor._execute_mcp_research_for_queries424–478、_process_sub_query508–651、_combine727–778、web搜索295–397及conduct研究数据赋值207–239、agent.conduct_research380/401。用两类代表输入（本函数识别的Python structured_content.results包装；content文本块包装）说明提取title/href/body，保留原始url或补mcp://tool标识；该输入示意不当作所有MCP SDK必然返回形状。其他字符串/普通字典/列表分支只交代用途，不逐条同类灌输。调研调度器把body/href改成content/url并加query/source_type='mcp'，子查询获得缓存或当次MCP条目，网页资料先context_manager.get_similar_content_by_query，再_combine先放网页后加MCP正文及Source说明，子查询结果汇总并写入researcher.context，按cfg可再source_curator，供第6章写作使用。

代码边界：_combine只是格式拼接，不做新的语义匹配/去重或把MCP资料再走网页抓取/Embedding；不能把注释Intelligently当额外模型算法。mcp://占位不是自动可访问网页/已验证引用，mcp://llm_analysis条目仅不显示URI，其模型执行前文本仍会混入上下文。格式存在不保证真实性或字段类型，解析异常可fallback str(result)。普通dict含content会优先走包装分支，导致原title/url丢失；裸字符串列表被跳过，未知列表dict可能只str(item)，不能声称任意结果都语义正确解析。当前两方法只转换/拼接，不写visited_urls/research_sources，不把“进上下文”等同“来源账本完整”。结果max_results只截条数，不替代文本长度/token预算；fast/deep/disabled缓存细节下一单元。

6项离线AST行为检查通过：structured字段映射保留URL；文本块空行拼接/补标识；普通content字典丢原URL与裸字符串列表丢弃的源码边界；查询标记的内部材料条目；实际_process_sub_query只筛网页再直接拼MCP正文/Source；分析文字保留而隐藏URI/合并不去重/全空返回空串。使用固定MCP/网页数据与假上下文组件，不读.env、连MCP服务或模型，无代码修复/新增用户手写。第10章仍源码阶段，后续策略、事件循环包装和可观测性待覆盖。

第10章源码讲解第7单元/MCP策略与缓存（2026-10-28）：重读ResearchConductor初始化34–48、_get_context_by_web_search294–397、_get_mcp_strategy398–422、Tavily重复检测480–505、子查询508–608，agent._resolve_mcp_strategy217–281/_process_mcp_configs283–309，plan_research50–95及query_processing.get_search_results43–80/plan_research_outline157–214。以普通报告、规划3个不含原题的子查询、首检索器为非MCP、一个MCPRetriever且非纯重复Tavily配置为例：实际处理3子题+追加原题共4项；fast用原问题执行1次显式MCP调研并缓存资料，4项复用；deep每项执行共4次；disabled跳过这两处显式MCP阶段。次数指MCP调研管线，非单次工具/网络/模型请求数。mcp_strategy='deep'与第7章report_type='deep'递归不同。

缓存状态与范围：每个ResearchConductor的_mcp_results_cache由None变资料list，空list也是已填充缓存，子查询用is not None复用，不自动按空结果重试；锁只防同实例并发预热重复，不是跨请求/跨章节全局缓存或工具并发限制。各子题拿相同MCP正文且合并不去重，省请求不代表省最终上下文重复；copy是外层列表浅复制。冷缓存直接进入子查询时会fallback按当前题执行，不更新共享预热缓存，不能把fast当硬调用次数预算。新建GPTR/Conductor会有新缓存。策略实例优先cfg/defaultfast；兼容旧optimized/comprehensive及mcp_max_iterations0/1/-1映射，不把其余数字当真实迭代次数。

重要真实边界：plan_research初搜总用retrievers[0]，get_search_results/MCPRetriever未在这个入口检查mcp_strategy；首检索器MCP时fast/deep可能有额外初搜，disabled也可能仍触发MCP初搜，故不宣传全局零调用。仅MCP时plan_research_outline返回[原题]，普通报告后续又append原题，deep会处理同一题两次。Tavily直连+全部Tavily MCP配置时子查询有跳过MCP保护，但fast预热更早执行，不能说重复路径在所有阶段被阻止；未知策略预热fallback与子查询fallback不完全等同fast，正常构造resolve会归一化到有效名称。源码注释balanced计数未在当前三策略实现中发挥相应作用，留工程收束。

7项AST离线检查通过：fast1次/同正文复用4次；deep4次且无缓存；首非MCP时disabled显式0次；同实例并发fast只预热1次；空结果缓存不重试；首MCP时disabled仍有规划初搜；仅MCP普通报告deep同题2次显式调研且还有1次初搜。执行真实策略/规划/子查询/合并函数，工具和查询生成为固定替身，不读.env、不联网，不修改源工程。第10章仍源码阶段；下一单元完整补读同步search201–298与事件循环/线程包装，再可观测性/成本及MCP对外服务边界。

第10章源码讲解第8单元/MCP同步异步桥接（2026-10-28）：完整补读MCPRetriever.search201–298及_get_all_tools300–324，核对ResearchConductor._execute_mcp_research653–725直接同步调用search688，与query_processing.get_search_results43–80的await asyncio.to_thread路径。说明search_async是异步业务，search为兼容统一同步检索器接口的包装；无运行loop时asyncio.run执行，有运行loop时开ThreadPoolExecutor工作线程/new_event_loop/run_until_complete，调用线程却future.result(timeout300)同步等待。明确源码283“避免主循环阻塞”注释不成立：线程中虽运行异步搜索，主loop所在调用线程仍被result挡住；async def不会自动把内部同步调用异步化。已有async入口可直接await search_async，只能sync接口则await to_thread(search)，保持业务接口层次清楚；本轮未修源工程或提前手写。

5项离线AST行为检查通过：普通sync调用同线程asyncio.run/参数传递；async上下文直接search在另一线程/loop执行但主loop已排队marker直到返回后才运行；实际get_search_results的to_thread路径允许主loop marker运行；直接await search_async同loop且允许其他任务；无配置/异步ValueError转空结果。使用固定20ms异步结果，未运行真实MCP/模型/网络或读.env。另读取本机标准库Executor.__exit__确认shutdown(wait=True)，future.result超时不取消已运行线程，with退出可能继续等，因此300不是端到端硬超时。

清理用途已解释：线程新loop取消pending任务，等待清理最多5s，短暂停顿/gc后close；它不等于完备连接关闭保证，与client_manager清引用区别保留。源码inner except RuntimeError范围也覆盖future.result，理论上可把执行自身RuntimeError误判为无loop，再在运行loop线程尝试asyncio.run；此边界只代码审阅未做导致未await警告的执行。跨loop使用WebSocket/锁等对象需工程审查，不断言每次必出错。第10章MCP主要源码链至此覆盖，后续费用/日志/进度追踪、对外MCP服务目录边界与核心范围核对待完成，仍未进入手写。

第10章源码讲解第9单元/费用元数据与回调账本（2026-10-28）：阅读utils/costs.py264行全部、agent.add_costs773–794/get_costs749/get_step_costs757、Provider._capture129–143、统一调用llm137–149，核对_current_step的agent_selection/research/report_writing/deep_research赋值及compression185/263的Embedding估算入口。本单元先讲一次成功响应→可识别usage优先/无usage文本估计→本地静态单价规则→cost_callback(金额)→GPTResearcher总额/当前阶段累加。金额数字为教学假设，不把源码July2026价格表当实时官方报价或真实账单；即使token来自服务，计算费用仍取决于本地规则。未识别模型可套默认单价，文本估计不能反映全部服务端计费细节；流式_capture是最后非空usage覆盖而非逐块累加。Anthropic专门解析/规则/地区乘数与默认分支已读，按同类归纳不逐厂商复述。

覆盖边界：callback未传就不记本账；MCP选工具走标准入口并传研究对象add_costs，MCPResearchSkill执行模型直接ainvoke无对应记账，第9章外层模型也不自动进GPTR内部账本；Tavily服务费不能按这张LLM token表当已包含；Embedding用文档分词与固定本地单价估算，非真实Embedding账单。失败尝试未走成功callback会漏记可能的消耗。add_costs只统计不硬限预算。发现源码同步add_costs在log_handler存在时调用异步_log_event未await/调度，数字已加但日志协程未执行，RuntimeWarning可复现；不能简单只把add_costs改async，因为上游callback当前同步调用，修正需配套，本轮未修改源工程。

8项AST离线行为检查通过：usage优先/未知模型默认单价；具体型号规则优先；Anthropic响应metadata优先及本地地区系数；缺usage文本估计（替身分词）；未知Embedding型号编码fallback及固定规则；实际统一调用回调→总账/阶段账及无回调不计；cost_update异步日志未await；非法金额类型拒绝。未加载真实tokenizer缓存/查价格或账单、不读.env/联网/调用模型，分词替身只验分支不代表真实token精度。

另已完整读取日志/进度文件utils/logging_config82、mcp/streaming102、backend/server/logging_config与actions/utils.stream_output及ChatLogger；讲解留下一单元。发现待讲：两份setup函数都仅返回JSON handler未挂research_logger.json_handler，源码检索未发现setup调用；默认不保证有JSON研究日志；ChatLogger正常traceback.format_exc不是真正调用栈；MCP进度stream_log与正文type='report'分开，sync进度create_task不等待、无线程loop时不发送。utils/logger彩色格式化剩余实现尚需补读。第10章仍源码阶段。

第10章范围调整（2026-10-28）：用户在费用单元后说“这一部分可以跳过”。按上下文将费用统计后续深入及接下来的日志/进度可观测性细节暂记跳过，不安排这些内容手写；保留已讲费用与源码审阅历史，不将剩余日志实现记作已讲。Provider/MCP主要源码链已讲，辅助可观测性覆盖记录仍区分已读/已讲/跳过；不提前勾选第10章完成。接下来收束最小核心手写范围：模型客户端及消息适配、工具请求/执行/回传闭环、MCP工具发现/接入，并接回已存在的研究或多Agent调用接口；不抄全量厂商分支、复杂同步桥接、费用/日志框架。遵守先完成源码讲解核对、等用户确认开始手写，再逐步写核心和由助手测试；本轮仅更新学习记录，未修改练习或调用模型/服务。

第10章核心手写第1步（2026-10-28）：用户在收束范围后回复继续，开始手写。重新核对练习头部/模型相关定义，尚无build_chat_model；模块顶层DraftState后、normalize_queries前（原48行）布置build_chat_model(llm_provider,model,api_key)。仅以DeepSeek代表接入分支，未知provider明确ValueError，使用已安装langchain-openai1.6.0的ChatOpenAI(model=...,api_key=...,base_url='https://api.deepseek.com')，直接返回底层模型对象。核对安装源码alias model/base_url/api_key，避免伪造接口。原GenericLLMProvider包装的费用/日志省略符合用户跳过要求，不重新实现所有厂商。凭据由调用者运行时传入，不读.env或展示真实值，不要求立即实例化/联网；保留现有demo函数直到下一步消息适配完成再装配。解释def只构造对象、调用ainvoke或迭代astream才请求模型、bind_tools只绑定工具；该对象将供第9章，后续另做messages->str适配供第8章及内部研究。当前仅布置代码，未代写/声称保存或测试通过，下一步make_model_caller适配器。

第10章核心手写第2步（2026-10-28）：用户继续后布置模块级make_model_caller(chat_model)，放上一步build_chat_model之后、normalize_queries之前。外层普通def捕获客户端并返回内层async call_model(messages)，内部await chat_model.ainvoke→取response.content→校验str→strip/拒绝空内容→返回字符串。解释外层装配不请求、内层调用才请求，闭包保留客户端以适配已有仅messages参数的接口；该文本适配器用于GPTR角色/规划/写作和第8章call_model，第9章model仍传原BaseChatModel对象；工具调用须保留AIMessage/tool_calls，不能套此纯文本适配丢失工具请求。当前只布置函数，保留演示函数，尚未装配或实测服务。本轮实际文件AST语法通过，但模块顶层未找到build_chat_model或make_model_caller，记录磁盘尚未见本轮代码，不声称用户已保存/工厂测试通过；整章验证待保存后执行。

第10章核心手写第3步（2026-10-28）：用户继续，核对练习GPTResearcher.__init__1291–1352、generate_sub_queries76–97、ReportGenerator._call_write_model1130–1150及组件构造，确认ResearcherConductor/ReportGenerator/DeepResearchSkill保存researcher引用、运行时读取模型字段，适合初始化注入。布置GPTResearcher构造追加chat_model=None，保留原demo赋值，在self.subtopic_model=demo_subtopic_model之后/self.memory之前加入self.chat_model保存和可选覆盖：一个make_model_caller结果赋call_model/plan_model/write_model/subtopic_model/deep_plan_model/deep_query_model/deep_extract_model，backup_plan_model=None避免真实请求失败后落入演示备用回复。未传客户端兼容旧三参数构造和历史检查；注入客户端后各模型字段复用客户端、不同messages决定不同任务输出，不在初始化时请求模型。

本步仅建立底层接收接口，不声称BasicReport/DetailedReport/ResearchAgent/第9工具工厂/HTTP入口已传入客户端；已定位这些创建点（262、279、354、639、1439、1684，当前行号会随保存变化），需后续逐链传递，避免半真半假。Embedding仍独立由Memory装配，不因LLM客户端注入自动替换。磁盘目前仍未见build_chat_model/make_model_caller，语法仅对已保存文件成立；本轮布置代码，未代写/执行真实模型或宣称接通验证。下一步普通报告调用方与嵌套研究对象的客户端传递。

第10章核心手写第4步（2026-10-28）：用户继续后核对已保存BasicReport258–267、DetailedReport270–286、GPTResearcher1291–1352、run_agent1572–1601、HTTP write_report1602–1659；磁盘GPT构造仍三参数且未见模型工厂/适配器，不能宣称本章变更已保存。布置普通报告链三处：BasicReport构造追加chat_model=None，并在其GPTResearcher构造显式传chat_model；run_agent在return_researcher后追加chat_model=None；只在BasicReport分支用BasicReport(**params,chat_model=chat_model)，保持共享params的原三字段/其他分支和返回形式不变。本步局部接普通报告，不把DetailedReport、递归子对象、第8/9上层或HTTP自动说成已切换；下一步需详细报告父子一起接，之后全链检查消除未传模型的遗留点。强调每层只转交同一客户端引用，BasicReport.run依旧先conduct再write，不重复建客户端、不在初始化请求模型。未实际改练习或调用真实服务；以条件方式描述写完后的效果。

第10章核心手写第5步（2026-10-29）：继续详细报告的模型注入，读取已保存DetailedReport.__init__270–286/run287–311/_plan_subtopics312–349/_research_subtopic350–379、BasicReport/GPTResearcher签名、run_agent1572–1601。磁盘仍是第10章前的旧签名且未见build_chat_model/make_model_caller，不宣称已保存或可运行。本步布置：DetailedReport构造追加chat_model=None并self.chat_model保存；父GPTResearcher仍report_type='research_report'且传chat_model；self.subtopic_model改为self.gpt_research.subtopic_model，使真实客户端时章节规划也走适配函数、默认None仍演示；创建章节child的GPTResearcher传chat_model=self.chat_model，原角色/写作方法/visited共享和资料合并代码保留；run_agent详细分支改DetailedReport(**params,chat_model=chat_model)，共享params三字段继续不变。解释客户端引用共用而研究状态各自保存，visited_urls是原本有意共享；此child是详细报告的研究对象，不混同第9章框架子Agent。仅示范此类传参的第二代表，剩余递归/第8/9/HTTP同类接线放整体验证统一核对，不再逐个重复开讲。下一步核心手写工具调用闭环；MCP工具装配、各工作流注入及实际保存验证仍待完成，未调用服务或修改练习。

第10章核心手写第6步（2026-10-29）：用户继续，实际磁盘已看到build_chat_model47–61/make_model_caller62–78与先前布置一致，整文件AST语法通过；未据此声称模型已联网或所有上层接线已验证。布置模块级async run_tool_agent(chat_model,messages,tools,max_rounds=4)，放make_model_caller后、normalize_queries前，局部导入ToolMessage。接收原模型对象及LangChain/MCP工具对象列表，不用纯文本适配器以保留tool_calls。建立name→tool字典并拒绝重名，复制本次消息列表，bind_tools（无工具则原模型），for模型轮次：ainvoke→追加完整AIMessage→无工具请求则校验文本并返回(answer,tool_results)；若最后允许轮次仍有工具请求则在执行前报错；否则按顺序await工具、异常转status='error'结果、保存业务原始结果{tool,result,status}并追加匹配tool_call_id的ToolMessage，进入下一轮。tool_results是后续资料转换的业务数据，不恢复已跳过的费用/日志统计。

解释三轮依赖链：第一次模型search_docs取doc_id，第二次根据ToolMessage请求read_doc，第三次依据正文回答；相较源工具helper支持继续决策。max_rounds限制本函数模型决策调用次数（含最终回答），非外部HTTP重试/总工具数/费用硬预算；同一轮多个工具顺序执行。工具异常交回模型，模型请求异常上抛，达到上限明确失败；status success只表示未抛异常，业务有效性另检。本轮只给手写代码，未代写或声称用户已保存/新函数已测试。下一步MCP工具加载装配，后续计划明确配置工具重名和MCP执行错误转异常以供循环处理，再统一核对各工作流模型注入与整章验证。

第10章核心手写第7步（2026-10-29）：继续MCP工具加载。实际磁盘当前仅见build_chat_model47–61和make_model_caller62–78，后面直接normalize_queries，尚未见上一步run_tool_agent，不声称已保存/验证。核对本地langchain_mcp_adapters/client.py55–126、166–216：MultiServerMCPClient支持tool_name_prefix与handle_tool_errors，get_tools发现并封装工具，默认每次调用创建新会话。布置模块级async load_mcp_tools(server_configs:dict)，放run_tool_agent后/normalize_queries前；拒绝空配置，创建客户端（工具名前缀开启、MCP业务错误转异常交由已有循环处理），await get_tools，拒绝空工具，返回工具对象列表。以已存在的知识库服务有search_docs/read_doc作假设示例，明确此步只发现工具、不会执行搜索或得到正文，模型后续通过run_tool_agent选择工具并传参。使用适配器原生字典省略原项目配置列表转换/缓存管理，原工程对应mcp/client.py105、155；服务连接/发现失败上抛，不静默当成功。此步只布置手写，不代写练习、不运行未知服务器或模型、不读取.env；下一步补齐具体MCP服务与调用装配，后续整章核对测试。费用/剩余可观测性继续按用户要求跳过。

第10章核心手写第8步（2026-10-29）：用户先问ToolMessage用途，随后要求继续下一处，本轮先简要补足工具返回消息与AIMessage.tool_calls/id配对，再布置独立MCP服务供上一步加载函数连接。在仓库mcp-server/knowledge_demo.py新建教学文件（仅布置，未声称已创建），使用已安装mcp.server.fastmcp.FastMCP、字典演示文档、@mcp.tool注册search_docs(query)->list[dict]及read_doc(doc_id)->dict、主入口mcp.run(transport='stdio')。说明函数/注解/文档字符串如何形成工具名称/参数结构/说明；搜索只返编号标题、读取才返正文；纯内存同步函数无需async，服务通信由SDK异步处理；stdio由客户端下一步启动子进程，通过标准输入输出通信，不占HTTP端口，不在stdout额外print。数据为虚构演示，原仓库mcp-server只有指向外部实现的README，本教学服务不冒充原版GPTResearcher MCP Server。核对本地SDK server.py147/282/449–514；练习1.py当前仍仅见两个模型帮助函数，未把后续布置视为已保存或已测试。下一步给本服务连接配置并串load_mcp_tools/run_tool_agent；本轮未运行模型或服务、不读.env，维持已跳过费用/可观测性范围。

第10章核心手写第9步（2026-10-29）：布置模块级run_knowledge_agent(chat_model,query:str)，放练习1.py的load_mcp_tools之后/normalize_queries之前，职责是连接配置与模型循环的装配入口。server_configs使用适配器原生字典knowledge→transport=stdio/command=项目虚拟环境Python绝对路径/args=[-X,utf8,仓库mcp-server/knowledge_demo.py绝对路径]，确保SDK解释器和中文编码。await load_mcp_tools→建立system/user消息（要求先搜索再按编号读正文、无资料如实说）→await run_tool_agent→返回(answer,tool_results)。客户端按stdio配置自动启动服务，不另手动启动；默认发现和每次工具执行可为不同会话/进程，因此示例只读固定数据有效、不依赖上一次工具调用内存修改。system提示是模型指导非程序硬约束；knowledge前缀来自配置键。当前实际检查knowledge_demo.py不存在，1.py只见build_chat_model/make_model_caller，未见run_tool_agent/load_mcp_tools，不声称已保存或测试；继续布置不阻断用户手写，但整体实测需保存。仅需传入原聊天模型对象，不能传纯文本model_caller；没有读.env、调用真实模型、启动未知服务或修改练习文件。下一步保存后由助手验证工具发现/执行/完整循环并核对模型注入遗漏，费用与可观测性仍跳过。

第10章核心手写第10步/局部验证（2026-10-29）：实际磁盘已保存run_tool_agent79、load_mcp_tools148、run_knowledge_agent166；AST通过，BasicReport415/DetailedReport427/GPTResearcher1452/run_agent1747签名均已含chat_model可选参数（仅签名核对，不据此宣布全部注入正确）。知识库服务文件尚缺，助手按上一轮已讲代码在仓库创建mcp-server/knowledge_demo.py，无改写用户练习文件。新增scripts/check_chapter10_mcp.py，AST只提取四个助手函数，跳过练习导入/HTTP启动/.env；外层模型固定回复，MCP客户端/stdio子进程/工具发现/执行/异常均使用真实已安装SDK。运行12项全部通过：语法及提取、文本适配trim/空响应、空配置、真实发现及前缀、三轮搜索→读取→回答与ToolMessage编号匹配、无匹配搜索、真实MCP不存在文档错误→error ToolMessage、未知工具恢复、最后轮不执行新工具、重名/非法轮数、无工具及空回答/不改调用者消息、模型异常上抛。检查脚本未更改练习，SHA256=1a307fb8c04a269f13405bd3f0559dd3d4888ead08c572a69ebce973677b2280。SDK每次服务启动出现lifespan注解IncompleteFieldDefinitionWarning但所有实际发现/执行检查通过，未为警告无关升级依赖。无真实Provider网络调用、无模型质量结论；第10章尚未完成，下一步核对GPT研究链与各分支模型注入及MCP业务资料接回边界，最终整章检查/工程复盘仍待做。用户跳过的费用与可观测性不恢复。

第10章核心手写第11步/研究模型注入验证（2026-10-29）：读取实际BasicReport415–425、DetailedReport427–540、GPTResearcher1452–1568、run_agent1747–1780及第7/8/9相关调用点。新增scripts/check_chapter10_models.py，复用第6章AST加载/搜索抓取Embedding替身，但真实执行已保存角色选择/查询规划/上下文处理/报告生成/详细章节父子链；外层InjectedModel返回AIMessage。运行6项全部通过：初始化无请求、7个模型回调共用适配器且关闭demo备用；共享模型但状态隔离；无客户端兼容演示；禁用所有默认demo入口后普通报告角色/规划/写作仍走传入客户端；详细报告父对象/章节规划/两个子研究全走同客户端；visited有意共享、context各自独立，未触发导出。练习未修改，SHA与上轮一致1a307fb8c04a269f13405bd3f0559dd3d4888ead08c572a69ebce973677b2280。实际仍缺HTTP write_report1807–1812→run_agent的chat_model参数；本轮只布置最小接线：app.state.team_model旁初始化app.state.chat_model=None，普通/详细HTTP分支run_agent增加chat_model=app.state.chat_model；运行装配时需把已创建原模型对象放入该字段，None保持演示，不宣称此步已保存/验证/真实联网。图解HTTP→write_report→run_agent→BasicReport→GPT→适配器→ainvoke，并说明详细报告同客户端不同研究状态。第7章递归子对象尚未显式传原客户端（目前复制部分回调）、第8章ResearchAgent内层、第9章工具内部GPT、MCP资料归并仍需集中核对，不误称全项目模型接通；后续继续同类缺口批量收束，不为每个参数再开重复详讲。

第10章核心手写第12步（2026-10-29）：集中核对剩余模型边界，实际磁盘HTTP app.state.chat_model及write_report传参尚未保存；未重复布置上一轮。读取第7章DeepResearchSkill._process_query796–837（复制call_model/plan_model/backup但未传原客户端），第8章ResearchAgent1855–1897/Editor1899–1903/Chief2295–2303/run_multi2396–2421（外层call_model有参、内部ResearchAgent新GPT未传客户端），第9章工具工厂1578–1641/build_deep_agent1642–1694/run_deep_agent_task1695–1746（框架外层model有参、工具内部GPT无参）。同类问题不逐个重讲，选择第9章的“工具内部仍创建独立GPTResearcher”作为代表解释外层工具决策模型与内部研究模型的不同职责。布置build_research_tools(task,chat_model=None)并将chat_model传入内层GPT；build_deep_agent追加research_model=None并给工具工厂传research_model；run_deep_agent_task在source后追加research_model=None并转交build_deep_agent。保持None兼容历史模型替身/原调用，不自动把仅会产生外层工具调用的旧测试模型注入内层文本研究。显式调用model=chat_model,research_model=chat_model可共用客户端，亦可分开，不要求两者相同；外层仍create_deep_agent，内层仍GPTR，不把自写run_tool_agent替换SDK循环。本轮仅讲解/布置这条接线，不改用户练习、不声称已保存/通过；第7/8剩余同类接线、HTTP保存、MCP资料归并与整章收束仍待完成，跳过项目不恢复。

第10章核心手写第13步（2026-10-29）：用户继续，读取实际第7/8构造与第9/HTTP状态；第9research_model和HTTP app.state.chat_model尚未见保存，未声称验证。集中布置第7/8同类透传，不再各开流程课。第7章DeepResearchSkill._process_query800–804的GPTResearcher构造增加chat_model=self.researcher.chat_model，保留既有回调/visited/search复制以维持用户定制。第8章ResearchAgent1855新增__init__(chat_model=None)保存，research中创建GPT时转交；Editor1899追加chat_model并传给其ResearchAgent；Chief2295在ask_feedback之后追加chat_model并分别传给总研究ResearchAgent和Editor；run_multi2396在ask_feedback后追加chat_model并传Chief；HTTP multi分支1791转交app.state.chat_model，前提是上一轮应用字段已初始化。原call_model继续供Reviewer/Reviser/Writer等文本节点，chat_model供新GPT初始化，不把两者类型混淆，不改图边/并发/人工反馈逻辑。给共用客户端示例call_model=make_model_caller(chat_model)、chat_model=chat_model；图示Chief分别向总研究/Editor→章节研究两支传递，强调漏Editor支会导致总览真实、章节仍演示。仅给局部修改而非整章重写，尚未保存验证，下一步统一检查这些接线，然后进入MCP工具资料接回上下文，费用与可观测性继续跳过。

第10章核心手写第14步（2026-10-29）：核对磁盘第7/8/9模型透传及HTTP仍未见最新布置，语法通过但不声称整章装配验证完成。本轮推进新链MCP工具结果→研究资料，读取练习ContextManager._to_documents1016等、get_similar_content_by_query1061–1086，原工程skills/researcher.py424–478的MCP body/href→content/url桥接。实际通过AST提取已保存load_mcp_tools，真实stdio调用knowledge_read_doc(doc_1)并观察返回list[{type:'text',text:'JSON字符串',id:...}]，JSON正文包含title/content；不猜返回形态、不读取.env或请求模型。布置run_tool_agent保存业务结果时增加args=call['args']，用于保留read_doc的doc_id；模块级mcp_results_to_materials放run_knowledge_agent后/normalize_queries前，只接收本教学knowledge_read_doc成功记录，校验doc_id，遍历text块json.loads、过滤非dict/空正文，输出{url:'mcp://knowledge/{doc_id}',title,raw_content}。此转换器只针对已知教学工具契约，非所有MCP工具/图片/任意JSON通用解析；忽略搜索元数据、工具错误和模型最终answer，防止将摘要/错误/生成文本当正文证据。mcp://为内部定位标识非可打开HTTP网址。普通def只做内存解析；当前仅完成/布置格式转换，尚未写入research_sources或context，下一步做业务接回与验证。未修改用户练习，新增参数及函数待保存验证，原MCP真实通信此前12项和普通详细注入6项不扩大为本轮新代码测试通过。

第10章核心手写第15步（2026-10-29）：实际磁盘已保存工具结果args136–141与mcp_results_to_materials208–251。扩充scripts/check_chapter10_mcp.py提取转换器/注入json，并对真实MCP读取输出转换/来源doc_id以及错误、搜索元数据、无效JSON、空正文、缺编号过滤追加2项，合计14项全部通过；SHA256=d89d10acc30331b43e21590fbee19773d6efec73b2cab3efe5126f6c8cdf3255。未请求真实模型，未修改练习文件。随后布置ResearcherConductor.conduct_research1239中web分支之后/local分支之前增加elif source=='mcp'：校验原模型存在→await run_knowledge_agent(query)忽略助手回答只保留tool_results→转换materials，空资料报错→research_sources.extend→await已有context_manager.get_similar_content_by_query→空上下文报错→return [context]。由外层GPTResearcher.conduct_research1592–1607原有赋值将列表写入self.context，不在Conductor重复赋值；BasicReport.run原有先conduct后write继续复用，writer已有_append_sources1360–1374按非HTTP标识输出mcp来源。明确这是教学新增纯MCP来源分支，未复刻原工程fast/deep/disabled与网页合并策略；不会再抓取mcp://或将模型摘要当正文。给run_agent(report_source='mcp', chat_model=...)具体调用形式及来源/上下文两种状态，画端到端图。此新分支仅布置、未保存/未测试，不将14项转换/工具检查扩大为报告端到端通过；后续保存后验证。保留第7/8/9及HTTP最近接线待保存核验，不提前勾第10章。

第10章核心手写第16步/完成核对（2026-10-29）：实际磁盘最新分支和全部模型接线均已保存；SHA256=df45762859dd89ddaa16b8aad70fb2eb3bb3e8fc9f8840b5e4ca12cd424dc321。静态核对第7章子GPT、8章ResearchAgent/Editor/Chief/run入口、9章工具工厂/build/run、HTTP两个分支传参均存在。新增scripts/check_chapter10_report.py：AST跳过项目导入/.env/启动，原报告调度、角色选择、Conductor、ContextManager和writer实际执行；固定模型/Embedding，一条完整报告实际发现/调用本地MCP搜索和读取。7项通过：原正文进入research_sources；已有上下文格式化且未抓mcp://；正文依据不混助手草稿、统一输出来源；缺客户端/无资料/空上下文失败边界；HTTP应用客户端传递、响应字段、导出接口及422。HTTP失败/成功补充案例使用固定MCP资料，导出用替身，未冒充真实Word/PDF本轮验证。更新既有第6章AST测试装配器，初始化app.state.chat_model=None以对应用户新增顶层状态；未改用户练习代码。

本轮第6章17项、第7章18项、第8章17项、第9章14项、第10章普通/详细模型注入6项，共72项回归全部通过。新增scripts/check_chapter10_wiring.py再执行3项：递归worker实际创建子研究并传客户端；实际LangGraph总体+两章节研究均收到客户端；实际Deep Agents SDK外层模型委派并写文件，工具内部研究使用另一个指定客户端（证明两层可不同）。本轮总计82项全部通过，统一当前SHA，临时SDK报告目录自动清理，未修改练习、未读取.env、未调用真实Provider/Embedding外部服务；前轮MCP转换与异常14项保留通过记录，不混作本轮重复执行。所有运行进程已退出。

第10章约定核心工程复盘：聊天客户端与Embedding是独立依赖；模型上下文/工具循环轮数限制不等于等待超时，缺少单次调用超时是当前边界；MCP默认每次调用新会话/stdio可能新进程，状态应持久化而非依赖上次内存；转换器只支持当前已知read_doc文本JSON契约，其他服务器结果需适配；mcp://为内部定位不是公共网页，来源列表不等于逐句支持验证。已有失败处理拒绝无正文/无上下文继续生成，但固定模型测试不能证明真实工具选择、语义检索和回答质量；这些留第12章。费用和剩余日志/可观测性按用户要求跳过，不因本章勾选改称全部源码已讲。至此按约定范围标记第10章完成，不另立学习清单；下一步第11章先源码调用链讲解，先不手写、不自动展开全章。

第10章补充理解：chat_model（2026-10-29）：用户要求细讲，暂停进入第11章，按实际练习代码核对build_chat_model48–62、make_model_caller63–79、run_tool_agent80–149、BasicReport462–468、GPTResearcher初始化1526–1567、build_deep_agent1717–1772。讲清chat_model是普通参数/变量名，真实工厂返回ChatOpenAI客户端对象（保存模型名、地址、凭据及调用能力，非本地模型权重）；工厂model字符串与create_deep_agent的model对象按各自接口区分；实例构造不等于生成，await ainvoke(messages)才发起生成；返回完整AIMessage含content/tool_calls，纯文本适配闭包call_model仅取content并校验，工具循环必须保留原消息。self.chat_model保存同一对象引用、跨层传参不是重建；模型依赖共用不等于context/messages共享，当前无自动聊天历史，由工具循环/框架显式管理消息。用角色选择和报告写作两次不同messages、同一客户端解释同模型多职责；bind_tools绑定定义不执行函数，Python/MCP执行另一路。配置字典标签不会自动切换既有客户端；聊天模型与Embedding仍独立。仅解释和读源码，不改练习、不读.env、不发真实模型请求，不增加重复手写步骤/测试。第11章待用户继续原路线时再进。

第10章完成状态纠正/工厂调用缺口（2026-10-29）：用户指出build_chat_model未使用。实际AST核对练习1.py只有48行定义、没有任何调用；app.state.team_model/chat_model仍初始化None，主入口2518–2525只有uvicorn.run。此前82项检查验证的是外部注入固定模型对象后的调用链，不能据此宣称启动创建真实客户端已完成；保留检查结果但撤回第10章完成勾选。向用户明确承认缺口，按当前直接运行1.py的方式布置在uvicorn.run前：从进程环境DEEPSEEK_MODEL/DEEPSEEK_API_KEY取值→调用build_chat_model→app.state.chat_model保存原对象→app.state.team_model=make_model_caller(chat_model)，然后启动HTTP。说明def工厂不自动执行，构造不是生成请求，后续HTTP处理才ainvoke；此主入口接法仅覆盖直接运行文件，模块导入部署在第11章用应用生命周期装配。本轮只给明确修正代码，未修改用户练习/读取.env/真实密钥或调用模型；启动补丁待保存和验证，不再将测试替身与真实服务装配混为一谈。

第10章补充理解：客户端实际使用位置（2026-10-29）：用户疑惑为何传chat_model却看不到调用。重新读取实际make_model_caller63–79、choose_agent433–456、GPT初始化1555–1566/conduct1618–1633、writer._call_write_model1365–1385，确认客户端最终在65行await chat_model.ainvoke(messages)被调用；GPT先用闭包包装为model_caller，再把同一函数赋给self.call_model/plan_model/write_model，后续调用属性即进入包装函数，客户端引用仍由内层函数保留。用写报告一条链说明writer→researcher.write_model→包装函数→原客户端.ainvoke，返回AIMessage后提取content回传。强调self.chat_model保存本身不调用，原对象另供工具绑定/子对象传递；客户端参数用于依赖注入，而非必须在每个函数里显式写.ainvoke。当前AST仍无build_chat_model调用，所以默认None运行时仍demo；区分“传入客户端后使用链存在”与“当前启动已创建真实客户端”，不声称后者已完成。不改代码、不读密钥、不请求服务，启动装配仍待保存核验。

第11章源码第1节（2026-10-29）：用户要求进入下一章，按原清单继续源码讲解，暂不手写；第10章启动工厂调用尚待保存验证的状态保留，不为推进章节提前勾选。实际读取Next.js app/page.tsx1–140、286–470（含324入口/移动端分支/424LangGraph分支/444WS调用）、hooks/useWebSocket.ts全文件、helpers/getHost.ts全文件、Hero.tsx1–162（134转交回调）、InputArea.tsx1–165（59输入状态、73键盘提交、102表单提交、129按钮）。后端读取app.py300–375、websocket_manager.py全文件、server_utils.py1–193/263附近已有片段/327–412、BasicReport全文件、根main.py。一次输出截断的server_utils关键部分已重读带行号，未把截断内容记完整阅读；本节不声称app/page或app.py/server_utils全文件读完。

本节只追Next.js桌面端普通研究：InputArea.handleSubmit→Hero回调→Home.handleDisplayResult324清空答案/设loading等→普通分支444 initializeWebSocket→getHost选择地址（本地典型ws://localhost:8000/ws）→onopen70发送start加JSON（92/94）→后端/ws362连接accept→handle_websocket_communication327 receive_text352识别start370、create_task347执行handle_start_command126→data[6:]解JSON/取参数→start_streaming101→run_agent116普通分支163创建BasicReport→run先conduct后write。区分HTTP POST /report/、桌面WS研究、独立LangGraph配置分支和移动端chat分支，不混同；静态frontend/scripts.js为另一个前端实现，后续同类只选代表不重复全讲。说明事件回调传参、输入字符串变JSON字符串再还原字典、握手成功后发送、async接收循环与研究任务并行推进（非独立进程/持久队列）、研究中仍响应ping/拒绝新业务请求。前端setLoading仅界面状态，不代表研究完成。失败边界：连接onerror/onclose没有setLoading(false)；start处理异常被safe_run发送logs/error，HTTP Pydantic自动422不适用于该字符串WS协议。用RAG问题与普通报告参数给具体消息和一张调用图；本轮只静态源码阅读，没有浏览器/真实服务运行验证。下一节讲后端正文分片如何通过同一连接回到answer、完成消息/下载路径及停止状态；日志落盘等此前跳过的可观测性不展开。

第11章教学方式调整及流程第2节（2026-10-29）：用户明确本章不用讲代码，只讲流程；覆盖先前本章手写计划，本章后续使用业务流程、具体例子、简图，不逐行源码/不安排手写。已读源码仍作为事实依据，不把流程讲解升级为全部代码精读。继续桌面普通研究返回链：研究阶段状态/来源消息与正文消息共用WebSocket、前端按消息用途分别展示；模型流式输出由provider累积至换行发送（不是逐token必然直接到UI），前端追加文本形成报告；后端同时保留完整字符串，研究返回后依次导出PDF/Word/Markdown，再发送文件路径，前端收到路径才关闭loading/显示下载入口。点击下载时是浏览器发起普通HTTP读取后端outputs静态文件，WebSocket返回路径而非PDF二进制。若导出抛异常，正文可已显示但路径/完成状态未送达；不把最后文字出现等同整个任务完成。

本轮事实核对：server_utils.py generate_report_files/send_file_paths，generic/base.py373–400，useWebSocket.ts102–147，AccessReport.tsx1–100、dataProcessing.ts1–65，ResearchContent片段、ResearchResults的pathData入口及app.py outputs挂载。前端有report_complete接收分支，但rg在gpt_researcher/backend内未发现该精确消息类型发送方，仅agent.py的report_completed日志事件名称；不把前端预留能力讲成当前普通后端必发流程。已有10章日志落盘/费用跳过要求维持，11章仅讲用户可见过程消息。没有执行服务/浏览器或读取.env，不声称端到端运行。下一节按流程讲停止、连接断开及研究任务生命周期；其他API/部署尚待覆盖。

第11章整章流程收束（2026-10-29）：用户要求“拉通讲完”，本轮按整章流程覆盖而非保持一小节；不写代码/不要求手写、不安排测验。核对page.tsx停止/重置650–795、桌面追问145–280、移动专用入口449–554；useResearchHistory1–220/232–352/360–403；全部Next API代理reports、reports/[id]、reports/[id]/chat与chat；ResearchHistoryContext接口/ResearchSidebar检索片段、research/[id]/page前115及112后加载片段；FileUpload全文件、ResearchForm导入点；Langgraph.js全文件。后端核对ReportStore全文件、app.py报告CRUD/聊天/HTTP与WS入口、server_utils上传/删除/取消/参数处理；ChatAgentWithMemory chat185后。部署核对根Dockerfile/compose、fullstack全部分段、Next两个Dockerfile/package脚本/next.config/nginx配置、backend启动脚本/Procfile/旧Dockerfile。只静态读取，不导入项目、不读取.env、不执行服务/部署或实际模型请求。输出截断部分已按所用流程重读，研究页/useResearchHistory未据此记整文件逐行已读。

讲解整条案例：可选上传企业PDF保存到DOC_PATH，上传尝试解析但不是完成向量入库；选web/local/hybrid和报告类型→桌面普通WS启动→GPTR2–6研究/写作→流式正文→导出路径→浏览器HTTP下载；完成后Next报告API代理到Python ReportStore，保存问题/报告/事件/聊天到data/reports.json并本地缓存，失败本地回退；打开历史/分享按ID取后端报告、当前浏览器可回退本地，跨设备分享需要服务端确实保存，不会重跑研究。报告追问通过Next /api/chat代理到Python，将报告全文与对话传给新ChatAgent，模型可quick_search补充，前端另保存聊天；这是报告问答非完整研究重跑。原后端重复注册报告聊天/更新/删除路由，记录为工程边界，不冒充两套都独立生效。ReportStore的JSON落盘与“no persistence”旧注释区分，单实例锁不等于多进程数据库。

停止/断线：前端关闭连接并刷新页面；后端接收结束finally请求cancel研究协程，无持久队列/断点恢复保证，已运行线程和外部服务请求不保证立刻中止，不宣称结果自动完整保存/队列资源全部清理。心跳帮助检测连接，非研究进度/完成信号；断线后不自动续跑。分支区分：HTTP报告入口等待模式、桌面WS普通/详细/深度/本地多Agent、配置独立LangGraph服务时SDK建thread/stream、移动专用入口HTTP聊天与空report不等同完整研究、旧静态前端另一个UI。第9章Deep Agents并未自动接入当前网页菜单。原网页人工反馈前端发JSON对象，后端期待human_feedback文本前缀且处理函数TODO，不能将手写第8章的人审验证等同网页已经打通。旧handleDisplayResult内另一移动分支缺report，但实际MobileHome绑定专用handleMobileDisplayResult含report空串；不将旧分支缺字段泛化为所有移动端必422。

部署流程：根compose分别启动Next3000/Python8000，根后端镜像包含抓取浏览器/依赖，当前compose前端指向Dockerfile.dev是开发模式；Next生产Dockerfile是build再start。浏览器可访问后端地址与Next服务器内部访问后端地址两个视角，容器内localhost指自己，现有公共环境变量被两处复用要核对可达性；HTTPS网页配wss及代理WS升级。fullstack一个容器中Supervisor管理Python/Next/Nginx，Nginx把/ws、/outputs交后端，其余交Next，API再由Next代理。持久化my-docs/outputs/logs已有挂载，默认data报告JSON不在根compose挂载中需单独考虑；容器启动不等于全链路成功。普通报告无外部任务队列，重启不能续任务；原backend/Dockerfile指向app.main:app与当前backend结构不吻合，旧静态nginx配置也非Next生产服务，不混用配置。当前未做实际build/浏览器回归，流程层按约定完成第11章。第10章工厂启动接线待验证仍保留未完成，不因转章抹去；第12章测试/评测/调试/面试收束待用户继续。

第12章第1节（2026-10-29）：用户要求继续最后一章，先做测试/评测验证闭环。列出tests/evals文件清单，读取pyproject.toml前90行含pytest test_*.py收集配置；tests/test_sub_query_normalization.py全文件、test_websocket_manager.py前145、evals/simple_evals/run_eval.py前165/simpleqa_eval.py1–末尾（分段）、hallucination_eval/evaluate.py全文件/run_eval.py前145。首次跨目录rg意外匹配JSON历史结果造成输出截断，该输出不算完整阅读/未据此声称覆盖相关原始报告；后续明确读取代码文件，未执行原包导入或评测脚本，避免load_dotenv/真实服务。实际AST核对练习启动仍无build_chat_model调用，SHA仍df45762859dd89ddaa16b8aad70fb2eb3bb3e8fc9f8840b5e4ca12cd424dc321，原82项注入测试不扩大成真实服务质量/启动装配通过。

本节讲单元/集成/浏览器端到端/模型质量四类验证，用已有MCP演示文档“需发票并主管审批”说明：资料取得/进入context/写作带source是流程证据；真实模型是否忠于正文、不编造、证据充分需另外评测。对应项目SimpleQA以问题+标准答案+预测报告交裁判，分正确/错误/未作答；hallucination evaluator以最终combined context作为source，对比报告是否受该上下文支持，不能独立证明网页事实/逐条引用正确。模型裁判也需校验。

实际复现评测解析缺陷：AST仅提取simpleqa_eval.py的常量与SimpleQAEval定义，__new__跳过读取在线CSV的构造；固定grader.invoke返回AI样式content，无真实模型/数据集/.env。4个场景：A→CORRECT、B→INCORRECT、C→NOT_ATTEMPTED均匹配；直接返回INCORRECT却得到CORRECT。根因grade_response144后fallback按CHOICE_STRINGS=[CORRECT,INCORRECT,NOT_ATTEMPTED]依次子串匹配，CORRECT在INCORRECT内部。正确方向是精确匹配明确标签/字母，未知裁判响应单列解析失败，不能当正常评测答案；本轮只复现并讲解，未修改源文件或宣称原tests全套通过。给验证流程简图和面试表达，整章未完成，后续讲可复现评测/失败分层定位/最终项目复盘；真实模型/Embedding效果及浏览器部署仍未实测。

第12章第2节：错误答案的证据链定位（2026-10-29）。用户继续，按已约定追一条“答案错误”的完整调试链。核对实际练习BrowserManager978、ContextManager1109–1134、Conductor.plan_research1292/_process_sub_query1303/_scrape_data_by_urls1355、writer.write_report1402/_build_messages1484，以及原工程context_manager.py37/研究/写作入口。重点区分搜索命中→成功正文→筛选后context→真实写作messages→最终回答，定位证据第一次丢失或被改写的位置；visited_urls只登记访问不等于成功正文；子查询异常返回空字符串可能被最终过滤，不可用“有报告”推断每一步成功；短文档在当前练习会绕过向量筛选，不能无证据归因阈值。

实际执行两次故障注入演示：用check_chapter6 AST装配实际已保存研究/上下文/写作链，固定搜索和抓取返回同一虚构报销文档（需发票及主管审批），写作函数故意返回无需发票。场景一原始资料/context/写作请求都含证据而最终错，定位写作输出阶段；场景二额外人为替换上下文函数省略关键句，原文有/context与写作请求无，定位资料到上下文阶段。两次均实际得到上述状态，无真实网络/模型/Embedding请求、未修改练习/原工程；第二场景不是声称真实压缩器过滤了这份短文档，也不是线上质量故障实测。给搜索/抓取/筛选/写作四层排查表、简图及可用于面试的证据链表达，修复后应固定输入加回归检查。未修复上一节SimpleQA解析bug、未补启动工厂、未勾第12章完成。下一节可重复对比评测与参数/模型改动验证，随后调试收束和面试复盘仍待覆盖。

第12章补充实操：如何查看中间结果（2026-10-29）：用户追问如何看到中间变量。读取实际练习Conductor._scrape_data_by_urls1355–1361、GPT.conduct1618–1633、writer.write_report1402–1436及末尾入口。发现build_chat_model启动调用现已保存（2523起参数与2528/2529应用状态赋值），更新第10章为已保存待验证，不再称未调用，也未因静态看到调用就宣称真实启动成功。给调试器断点/变量窗口的直接操作：项目venv、cwd仓库、调试启动实际1.py；服务在8001，打开/docs提交普通web报告请求才能进入研究代码。五个断点对应1357看results、1361看materias/研究sources、1633看self.context、1423看messages、1425看report。说明断点通常停在该行执行之前，因此等赋值完成再看；不同类的self归属不同，使用当前栈帧；并发子查询会重复命中，查看query区分。MCP分支跳过网页抓取，前两处应改看Conductor.conduct_research的tool_results/materials，后面context/messages/report共用。补充临时print正文/上下文/消息的方法、终端查看位置及长文本预览不等于完整内容，监视已有变量不再次发起工具/模型调用。只讲实际查看方式，不写入用户代码/不请求服务、不读取密钥，第12章保持进行中。

第12章第3节：可重复的改动对比（2026-10-29）。读取SimpleQA runner146–259、SimpleQAEval96–125、hallucination runner146–229和README本地数据说明，核对练习切块1000/100、阈值0.42/max_results10、短资料总字符<8000且文档数<=max_results直接格式化。讲按目标选择控制层：比较切块/筛选固定问题、原始资料、Embedding与写作模型；比较写作模型固定同一上下文；整体在线评测固定题单配置并记录网页快照/日期，无法把实时网页变化都归因改动。A默认1000/100/0.42，B仅改chunk_size为700为教学对比配置、非实测最优值；本练习长度按字符而非token，不在走短资料快速分支的样本上声称验证chunk/阈值效果。保存实际执行的模型及配置/题单/正文/上下文/报告/裁判响应与代码状态，不能只记SMART_LLM标签；评测题与调参题分开，重复查看稳定性，不编造质量提升。

脚本具体边界：SimpleQAEval构造实际从线上CSV读取并random.sample未固定seed，README称本地镜像保持一致与代码不符；runner correct_rate等分母successful而非全部题数，示意10题仅4题运行成功且全对会显示成功样本正确率100%，必须同时报告6次失败（示意非实测）；hallucination无context跳过、不计入分母，异常continue也不算幻觉例，不把低幻觉率当整体成功。先修正已复现裁判标签解析问题再信任真实对比结论；该源文件本轮仍未修改/未运行真实评测。费用及此前跳过统计不展开，仅讲判断实验必须的结果口径。

同时完成已授权的启动装配验证：新增scripts/check_chapter10_startup.py，AST只取实际build_chat_model/make_model_caller和主入口，注入虚构环境值、替换ChatOpenAI构造与uvicorn.run，不导入原项目/.env、不启动服务、不调用真实Provider。4项通过：工厂在服务启动之前调用；模型/凭据/endpoint参数正确转交；app.state保存原客户端和独立文本适配函数；适配函数调用同一客户端并返回文本。当前练习SHA256=16a2dfd9e4d59e740c54b306ee2b37438c6f507c317c2d3172b1712b1998504a，未改练习；原82项是此前函数版本的注入流程检查，不混称本轮重跑。按约定核心恢复第10章完成，真实服务配置/质量仍待第12章，不扩大隔离测试范围。第12章仍进行中，后续面试复盘/未覆盖项收束及真实验证待继续。

第12章第4节：架构与面试复盘（2026-10-29）：用户继续，按已有实际实现与验证证据组织项目讲法，不新增模型/工具实现、不强制问答。项目定位为多来源研究报告系统；一分钟介绍用户问题→角色/规划→查询→检索去重抓取/文档→统一资料/Embedding筛选→证据上下文→报告/来源/导出→WebSocket展示。明确普通研究、详细报告、DeepResearch递归、LangGraph团队、Deep Agents工具委派是不同工作流，不能说7→8→9串行。RAG负责证据获取/筛选/生成支撑，Agent部分体现在规划、工具选择/执行反馈和协作决策，普通报告大量步骤仍由程序固定；多Agent不等于多个厂商模型，身份由职责/提示/工具/状态区分。

复盘客户端依赖注入（同客户端可复用、不同步骤可单独装配、消息状态各自管理）、raw sources/context/visited的职责、async I/O/gather/to_thread边界，Milvus是用户练习所选向量库而非全项目唯一强制后端。给两项能讲清的实际工程例子：访问登记先于抓取完成导致兄弟查询不能复用在途资料（此前边界检查已验证）；教学工具循环通过ToolMessage反馈支持搜索文档编号→再读正文的依赖工具调用，原MCPResearchSkill单次规划执行不自动实现该闭环。SimpleQA INCORRECT包含CORRECT的缺陷仅发现复现，尚未修改；不能写成已修。说明普通/多Agent比较与chunk阈值选择应靠固定任务对照，现默认1000字符/100重叠/0.42不称最优，不虚构提升。

面试证据范围：已有核心手写/隔离流程检查82项（此前版本）、真实本地MCP通信与转换14项（对应先前版本）、启动装配4项（当前启动修改）；真实Milvus写查和原库导出另有历史验证；不把这些凑成同一套当前全部真实端到端测试，不声称真实模型质量/线上并发/部署/所有文件精读完成。当前原12章中若干跳过项、AG2、辅助文件覆盖和全景收束仍保留；本轮完成面试表达与技术边界说明，第12章状态仍待实际验证及评测缺陷修复，不因“最后一章”宣称项目100%完成。

补充专项：项目RAG全链与细节复盘（2026-10-29）：用户在工作流场景后要求详细讲RAG并强调所有细节，本轮扩大为完整专项讲解，不推进下一章/不新增手写。以长文档研究查询串联两级检索（搜索来源与正文语义筛选），明确网页RAG不强制入向量库；用户练习Milvus是选择的后端，不等于原工程唯一存储。核对原context/compression.py全265行、context/retriever.py全文件、vector_store/vector_store.py全文件、memory/embeddings.py前135及get_embeddings位置、skills/context_manager前145、researcher相关来源/子查询/汇总/向量库/MCP桥接/抓取片段、writer49–126、report_generation243–285、PromptFamily555及curate提示、skills/curator.py全文件、DocumentLoader全文件；练习ContextManager1057–1178/VectorStoreWrapper1179后/构造Milvus1573后；本地SDK EmbeddingsFilter前165、Pipeline前94、RecursiveCharacterTextSplitter默认分隔与Milvus embed_document/query调用点。先误用context/memory.py/source_curator.py不存在路径后已通过rg定位正确memory/embeddings.py/skills/curator.py；没有读取或猜测不存在实现。较早输出截断的writer段已重读所需行，不扩大原文件阅读覆盖。

专项要点：原始url/title/raw_content映射Document(page_content,metadata source/title)，Document是统一数据结构非向量/非已入库。大资料ContextCompressor由SearchAPIRetriever返回已有pages转Document（不再次联网），先默认每份正文截50000字符，再RecursiveCharacterTextSplitter1000/100，按段落换行空格字符递归分割（不是固定token窗口、重叠不保证正好100）；Embedding文档与query同空间，当前SDK余弦相似度排序并阈值过滤，不等于真实性或概率。原默认配置SIMILARITY_THRESHOLD=0.42与练习一致；压缩器0.35仅cfg未传值时环境/内部兜底，避免误讲成正常默认。原EmbeddingsFilter未设k，当前安装SDK默认20，随后pretty_print_docs取ContextManager传入的10；练习显式k=max_results10。阈值严格>比较。小资料total_chars<8000且数量<=本次max_results直接格式化，绕过Embedding/切块，不能拿短资料证明参数效果；大资料标准路径在to_thread中同步invoke压缩。每子查询最多格式化10不等于最终总context最多10或自动token预算；多个查询汇总后可重复与过长。相似度压缩是选择原文片段，不是默认LLM改写摘要或专用cross-encoder。

Milvus流程分入库/查询：原Wrapper.load将文档切1000/200并add_documents，SDK负责Embedding入库；问题Embedding→相似度查询→返回存储的文本Document，非把向量反解正文。练习collection research_chunks_v1、COSINE/AUTOINDEX、auto_idTrue、drop_oldFalse、动态metadata；查询k8，filter转expr，过滤接口要匹配Milvus，不能通用套其他库filter字典。原GPT接收vector_store才包Wrapper，默认None；网页/本地来源若配置向量库可写资料，但当前上下文依然可能走内存压缩，不等于每次读回Milvus。已有向量库模式要求预先入库且Embedding空间一致，重建/换模型需考虑索引；Wrapper无去重版本管理，重复add/autoid可能重复。原向量库与本地研究规划仍调用初始搜索，不能宣传完全离线。混合来源本地+网页并发研究后拼上下文，并非BM25+稠密向量+RRF；本条主链未见独立cross-encoder重排。Memory仅管理Embedding客户端，不是聊天长期记忆；与chat_model独立。

可选SourceCurator默认False，开启用LLM对已有context筛选/整理，JSON解析失败返回原资料，不等于事实核查/专用reranker。WrittenContentCompressor对已写章节做语义检索避免重复，是参考内容而非新事实来源。原MCP上下文可直接合并，不保证同走Embedding；练习转换真实read_doc结果后显式走ContextManager，不能混淆两实现。Prompt格式Source/Title/Content后送写作模型文本，非向量；original writer空上下文返回无法可靠研究的说明，练习抛ValueError，非空也不保证证据有效。当前metadata不足以自动逐句/页码级引用核验，LocalLoader只保留basename丢页码等信息，来源显示非真实性证明。解释visited/raw sources/context/messages职责、async/gather/to_thread及原文档loader/入库同步调用边界。给完整网页链和Milvus入库/查询图、参数表、定位与评测要点；不伪造语义检索效果，历史Milvus验证用固定Embedding、真实模型评测仍待完成。无业务代码修改、无.env/模型请求/服务运行。

## 全部 Git 跟踪文件

### .claude (14)

- `.claude/references/adding-features.md`
- `.claude/references/advanced-patterns.md`
- `.claude/references/api-reference.md`
- `.claude/references/architecture.md`
- `.claude/references/components.md`
- `.claude/references/config-reference.md`
- `.claude/references/deep-research.md`
- `.claude/references/flows.md`
- `.claude/references/mcp.md`
- `.claude/references/multi-agents.md`
- `.claude/references/prompts.md`
- `.claude/references/retrievers.md`
- `.claude/SKILL.md`
- `.claude/worktrees/crazy-curie-e43899`

### .codex-plugin (1)

- `.codex-plugin/plugin.json`

### .cursorignore (1)

- `.cursorignore`

### .cursorrules (1)

- `.cursorrules`

### .dockerignore (1)

- `.dockerignore`

### .env.example (1)

- `.env.example`

### .github (8)

- `.github/dependabot.yml`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/workflows/build.yml`
- `.github/workflows/deploy.yml`
- `.github/workflows/docker-build.yml`
- `.github/workflows/llm-costs.yml`
- `.github/workflows/plugin-quality-gate.yml`

### .gitignore (1)

- `.gitignore`

### .mcp.json (1)

- `.mcp.json`

### .python-version (1)

- `.python-version`

### .triage (44)

- `.triage/all_results.json`
- `.triage/batch_1.json`
- `.triage/batch_2.json`
- `.triage/batch_3.json`
- `.triage/batch_4.json`
- `.triage/batch_5.json`
- `.triage/batch_6.json`
- `.triage/batch_7.json`
- `.triage/build_backlog.jq`
- `.triage/comments/_auth.md`
- `.triage/comments/_promo.md`
- `.triage/comments/1076.md`
- `.triage/comments/1079.md`
- `.triage/comments/1098.md`
- `.triage/comments/1105.md`
- `.triage/comments/1131.md`
- `.triage/comments/1232.md`
- `.triage/comments/1254.md`
- `.triage/comments/1279.md`
- `.triage/comments/1391.md`
- `.triage/comments/1398.md`
- `.triage/comments/1415.md`
- `.triage/comments/1684.md`
- `.triage/comments/1685.md`
- `.triage/comments/1696.md`
- `.triage/comments/1702.md`
- `.triage/comments/1707.md`
- `.triage/comments/1744.md`
- `.triage/comments/1745.md`
- `.triage/comments/1747.md`
- `.triage/draft_comments_bucketB.md`
- `.triage/engagement.graphql`
- `.triage/engagement.json`
- `.triage/issues_raw.json`
- `.triage/ranked.json`
- `.triage/render.jq`
- `.triage/result_1.json`
- `.triage/result_2.json`
- `.triage/result_3.json`
- `.triage/result_4.json`
- `.triage/result_5.json`
- `.triage/result_6.json`
- `.triage/result_7.json`
- `.triage/sorted.json`

### .vscode (1)

- `.vscode/settings.json`

### backend (31)

- `backend/__init__.py`
- `backend/chat/__init__.py`
- `backend/chat/chat.py`
- `backend/Dockerfile`
- `backend/memory/__init__.py`
- `backend/memory/draft.py`
- `backend/memory/research.py`
- `backend/Procfile`
- `backend/report_type/__init__.py`
- `backend/report_type/basic_report/__init__.py`
- `backend/report_type/basic_report/basic_report.py`
- `backend/report_type/deep_research/__init__.py`
- `backend/report_type/deep_research/example.py`
- `backend/report_type/deep_research/main.py`
- `backend/report_type/deep_research/README.md`
- `backend/report_type/detailed_report/__init__.py`
- `backend/report_type/detailed_report/detailed_report.py`
- `backend/report_type/detailed_report/README.md`
- `backend/requirements.txt`
- `backend/run_server.py`
- `backend/runtime.txt`
- `backend/server/__init__.py`
- `backend/server/agent_discovery.py`
- `backend/server/app.py`
- `backend/server/logging_config.py`
- `backend/server/multi_agent_runner.py`
- `backend/server/report_store.py`
- `backend/server/server_utils.py`
- `backend/server/websocket_manager.py`
- `backend/styles/pdf_styles.css`
- `backend/utils.py`

### citation.cff (1)

- `citation.cff`

### cli.py (1)

- `cli.py`

### CODE_OF_CONDUCT.md (1)

- `CODE_OF_CONDUCT.md`

### CONTRIBUTING.md (1)

- `CONTRIBUTING.md`

### CURSOR_RULES.md (1)

- `CURSOR_RULES.md`

### deep_agents (73)

- `deep_agents/__init__.py`
- `deep_agents/agent.py`
- `deep_agents/benchmark_data/build_corpus.py`
- `deep_agents/benchmark_data/internal_docs_src/board_memo_2026_strategy.md`
- `deep_agents/benchmark_data/internal_docs_src/company_overview.md`
- `deep_agents/benchmark_data/internal_docs_src/q1_2026_ops_report.md`
- `deep_agents/benchmark_data/internal_docs_src/vlx500_product_brief.md`
- `deep_agents/benchmark_data/internal_docs/board/board_memo_2026_strategy.pdf`
- `deep_agents/benchmark_data/internal_docs/board/board_minutes_2024_06.md`
- `deep_agents/benchmark_data/internal_docs/company_overview.md`
- `deep_agents/benchmark_data/internal_docs/engineering/oncall_rotation.md`
- `deep_agents/benchmark_data/internal_docs/engineering/simulation_cluster_usage.md`
- `deep_agents/benchmark_data/internal_docs/engineering/veltrixos_release_notes_5_0_beta.md`
- `deep_agents/benchmark_data/internal_docs/finance/erp_migration_notes.md`
- `deep_agents/benchmark_data/internal_docs/finance/expense_policy.md`
- `deep_agents/benchmark_data/internal_docs/hr/annual_leave_faq.md`
- `deep_agents/benchmark_data/internal_docs/hr/onboarding_checklist.md`
- `deep_agents/benchmark_data/internal_docs/hr/remote_work_policy.md`
- `deep_agents/benchmark_data/internal_docs/it/access_review_2026.md`
- `deep_agents/benchmark_data/internal_docs/it/incident_process.md`
- `deep_agents/benchmark_data/internal_docs/it/laptop_runbook.md`
- `deep_agents/benchmark_data/internal_docs/legal/dpa_template_notes.md`
- `deep_agents/benchmark_data/internal_docs/marketing/brand_guidelines.md`
- `deep_agents/benchmark_data/internal_docs/marketing/event_calendar_2026.md`
- `deep_agents/benchmark_data/internal_docs/marketing/website_faq_draft.md`
- `deep_agents/benchmark_data/internal_docs/ops/archive/q1_2024_ops_report.pdf`
- `deep_agents/benchmark_data/internal_docs/ops/archive/q1_2025_ops_report.pdf`
- `deep_agents/benchmark_data/internal_docs/ops/q1_2026_ops_report.pdf`
- `deep_agents/benchmark_data/internal_docs/ops/site_commissioning_playbook.md`
- `deep_agents/benchmark_data/internal_docs/ops/warehouse_safety_bulletin_march2026.md`
- `deep_agents/benchmark_data/internal_docs/product/archive/vlx500_concept_2025_superseded.md`
- `deep_agents/benchmark_data/internal_docs/product/vlx500_product_brief.docx`
- `deep_agents/benchmark_data/internal_docs/sales/customer_reference_program.md`
- `deep_agents/benchmark_data/internal_docs/sales/discount_approval_matrix.md`
- `deep_agents/benchmark_results/baseline_files_check.json`
- `deep_agents/benchmark_results/breadth_2026-07-04_22-39-24.json`
- `deep_agents/benchmark_results/breadth_2026-07-04_22-44-58.json`
- `deep_agents/benchmark_results/drb/baseline-tavily-deepagent_fact_result.txt`
- `deep_agents/benchmark_results/drb/baseline-tavily-deepagent_race_result.txt`
- `deep_agents/benchmark_results/drb/gptr-deepagent_fact_result.txt`
- `deep_agents/benchmark_results/drb/gptr-deepagent_race_result.txt`
- `deep_agents/benchmark_results/frames_2026-07-04_13-35-12_n20.json`
- `deep_agents/benchmark_results/frames_2026-07-04_14-38-19_n20.json`
- `deep_agents/benchmark_results/frames_2026-07-04_14-43-11_n20.json`
- `deep_agents/benchmark_results/hybrid_2026-07-04_22-06-28.json`
- `deep_agents/benchmark_results/hybrid_2026-07-04_22-16-55.json`
- `deep_agents/benchmark_results/hybrid_2026-07-04_22-22-39.json`
- `deep_agents/benchmark_results/hybrid_2026-07-05_14-29-57.json`
- `deep_agents/benchmark_results/hybrid_2026-07-05_14-37-31.json`
- `deep_agents/benchmark_results/hybrid_2026-07-05_14-43-50.json`
- `deep_agents/benchmark_results/recency_2026-07-04_18-54-47.json`
- `deep_agents/benchmark_results/recency_2026-07-04_19-10-24.json`
- `deep_agents/benchmark_results/recency_2026-07-04_22-11-41.json`
- `deep_agents/benchmark_results/reports_2026-07-04_14-33-21_n8.json`
- `deep_agents/benchmark_results/simpleqa_2026-07-04_12-44-58_n2.json`
- `deep_agents/benchmark_results/simpleqa_2026-07-04_13-07-09_n30.json`
- `deep_agents/benchmark_results/simpleqa_2026-07-04_13-55-24_n30.json`
- `deep_agents/benchmark_results/simpleqa_2026-07-04_14-19-50_n30.json`
- `deep_agents/benchmark_results/simpleqa_2026-07-04_14-40-49_n30.json`
- `deep_agents/BENCHMARK.md`
- `deep_agents/benchmark.py`
- `deep_agents/breadth_benchmark.py`
- `deep_agents/drb_generate.py`
- `deep_agents/drb_harness.patch`
- `deep_agents/hybrid_benchmark.py`
- `deep_agents/main.py`
- `deep_agents/README.md`
- `deep_agents/recency_benchmark.py`
- `deep_agents/report_benchmark.py`
- `deep_agents/requirements.txt`
- `deep_agents/SHARE_SUMMARY.md`
- `deep_agents/task.json`
- `deep_agents/tools.py`

### docker-compose.yml (1)

- `docker-compose.yml`

### Dockerfile (1)

- `Dockerfile`

### Dockerfile.fullstack (1)

- `Dockerfile.fullstack`

### docs (124)

- `docs/babel.config.js`
- `docs/blog/2023-09-22-gpt-researcher/architecture.png`
- `docs/blog/2023-09-22-gpt-researcher/index.md`
- `docs/blog/2023-09-22-gpt-researcher/planner.jpeg`
- `docs/blog/2023-11-12-openai-assistant/diagram-1.png`
- `docs/blog/2023-11-12-openai-assistant/diagram-assistant.jpeg`
- `docs/blog/2023-11-12-openai-assistant/index.md`
- `docs/blog/2024-05-19-gptr-langgraph/architecture.jpeg`
- `docs/blog/2024-05-19-gptr-langgraph/blog-langgraph.jpeg`
- `docs/blog/2024-05-19-gptr-langgraph/index.md`
- `docs/blog/2024-09-7-hybrid-research/gptr-hybrid.png`
- `docs/blog/2024-09-7-hybrid-research/index.md`
- `docs/blog/2025-02-26-deep-research/index.md`
- `docs/blog/2025-03-10-stepping-into-the-story/index.md`
- `docs/blog/2026-03-03-gpt-researcher-ag2/img/gpt-researcher-ag2.webp`
- `docs/blog/2026-03-03-gpt-researcher-ag2/img/pipeline.webp`
- `docs/blog/2026-03-03-gpt-researcher-ag2/index.md`
- `docs/blog/authors.yml`
- `docs/CNAME`
- `docs/discord-bot/commands/ask.js`
- `docs/discord-bot/deploy-commands.js`
- `docs/discord-bot/Dockerfile`
- `docs/discord-bot/Dockerfile.dev`
- `docs/discord-bot/gptr-webhook.js`
- `docs/discord-bot/index.js`
- `docs/discord-bot/package.json`
- `docs/discord-bot/server.js`
- `docs/docs/contribute.md`
- `docs/docs/examples/custom_prompt.py`
- `docs/docs/examples/detailed_report.md`
- `docs/docs/examples/examples.ipynb`
- `docs/docs/examples/examples.md`
- `docs/docs/examples/hybrid_research.md`
- `docs/docs/examples/pip-run.ipynb`
- `docs/docs/examples/sample_report.py`
- `docs/docs/examples/sample_sources_only.py`
- `docs/docs/faq.md`
- `docs/docs/gpt-researcher/context/azure-storage.md`
- `docs/docs/gpt-researcher/context/data-ingestion.md`
- `docs/docs/gpt-researcher/context/filtering-by-domain.md`
- `docs/docs/gpt-researcher/context/img/gptr-hybrid.png`
- `docs/docs/gpt-researcher/context/img/nextjs-filter-by-domain.JPG`
- `docs/docs/gpt-researcher/context/img/vanilla-filter-by-domains.png`
- `docs/docs/gpt-researcher/context/local-docs.md`
- `docs/docs/gpt-researcher/context/tailored-research.md`
- `docs/docs/gpt-researcher/context/vector-stores.md`
- `docs/docs/gpt-researcher/frontend/discord-bot.md`
- `docs/docs/gpt-researcher/frontend/embed-script.md`
- `docs/docs/gpt-researcher/frontend/img/bot-permissions.png`
- `docs/docs/gpt-researcher/frontend/img/oath2-url-generator.png`
- `docs/docs/gpt-researcher/frontend/introduction.md`
- `docs/docs/gpt-researcher/frontend/nextjs-frontend.md`
- `docs/docs/gpt-researcher/frontend/react-package.md`
- `docs/docs/gpt-researcher/frontend/vanilla-js-frontend.md`
- `docs/docs/gpt-researcher/frontend/visualizing-websockets.md`
- `docs/docs/gpt-researcher/getting-started/cli.md`
- `docs/docs/gpt-researcher/getting-started/getting-started-with-docker.md`
- `docs/docs/gpt-researcher/getting-started/getting-started.md`
- `docs/docs/gpt-researcher/getting-started/how-to-choose.md`
- `docs/docs/gpt-researcher/getting-started/introduction.md`
- `docs/docs/gpt-researcher/getting-started/linux-deployment.md`
- `docs/docs/gpt-researcher/gptr/ai-development.md`
- `docs/docs/gpt-researcher/gptr/automated-tests.md`
- `docs/docs/gpt-researcher/gptr/claude-skill.md`
- `docs/docs/gpt-researcher/gptr/config.md`
- `docs/docs/gpt-researcher/gptr/deep_research.md`
- `docs/docs/gpt-researcher/gptr/example.md`
- `docs/docs/gpt-researcher/gptr/image_generation.md`
- `docs/docs/gpt-researcher/gptr/npm-package.md`
- `docs/docs/gpt-researcher/gptr/pip-package.md`
- `docs/docs/gpt-researcher/gptr/querying-the-backend.md`
- `docs/docs/gpt-researcher/gptr/scraping.md`
- `docs/docs/gpt-researcher/gptr/troubleshooting.md`
- `docs/docs/gpt-researcher/handling-logs/all-about-logs.md`
- `docs/docs/gpt-researcher/handling-logs/langsmith-logs.md`
- `docs/docs/gpt-researcher/handling-logs/langsmith.png`
- `docs/docs/gpt-researcher/handling-logs/simple-logs-example.md`
- `docs/docs/gpt-researcher/llms/llms.md`
- `docs/docs/gpt-researcher/llms/running-with-azure.md`
- `docs/docs/gpt-researcher/llms/running-with-ollama.md`
- `docs/docs/gpt-researcher/llms/supported-llms.md`
- `docs/docs/gpt-researcher/llms/testing-your-llm.md`
- `docs/docs/gpt-researcher/mcp-server/advanced-usage.md`
- `docs/docs/gpt-researcher/mcp-server/claude-integration.md`
- `docs/docs/gpt-researcher/mcp-server/getting-started.md`
- `docs/docs/gpt-researcher/multi_agents/ag2.md`
- `docs/docs/gpt-researcher/multi_agents/deepagents.md`
- `docs/docs/gpt-researcher/multi_agents/langgraph.md`
- `docs/docs/gpt-researcher/retrievers/mcp-configs.mdx`
- `docs/docs/gpt-researcher/search-engines/search-engines.md`
- `docs/docs/gpt-researcher/search-engines/test-your-retriever.md`
- `docs/docs/proposals/adaptive-deep-research.md`
- `docs/docs/proposals/high-quality-content-scraping-architecture.md`
- `docs/docs/proposals/local-server-deployment-guide.md`
- `docs/docs/proposals/social-media-data-acquisition.md`
- `docs/docs/reference/config/config.md`
- `docs/docs/reference/config/singleton.md`
- `docs/docs/reference/processing/html.md`
- `docs/docs/reference/processing/text.md`
- `docs/docs/reference/sidebar.json`
- `docs/docs/roadmap.md`
- `docs/docs/welcome.md`
- `docs/docusaurus.config.mjs`
- `docs/npm/index.js`
- `docs/npm/package.json`
- `docs/npm/Readme.md`
- `docs/package.json`
- `docs/pydoc-markdown.yml`
- `docs/README.md`
- `docs/sidebars.js`
- `docs/src/components/HomepageFeatures.js`
- `docs/src/components/HomepageFeatures.module.css`
- `docs/src/css/custom.css`
- `docs/src/pages/index.js`
- `docs/src/pages/index.module.css`
- `docs/static/.nojekyll`
- `docs/static/CNAME`
- `docs/static/img/ag2-pipeline.webp`
- `docs/static/img/architecture.png`
- `docs/static/img/banner1.jpg`
- `docs/static/img/examples.png`
- `docs/static/img/gptr-logo.png`
- `docs/static/img/leaderboard.png`
- `docs/static/img/multi-agent.png`

### evals (19)

- `evals/__init__.py`
- `evals/hallucination_eval/evaluate.py`
- `evals/hallucination_eval/inputs/search_queries.jsonl`
- `evals/hallucination_eval/requirements.txt`
- `evals/hallucination_eval/results/aggregate_results.json`
- `evals/hallucination_eval/results/evaluation_records.jsonl`
- `evals/hallucination_eval/run_eval.py`
- `evals/README.md`
- `evals/simple_evals/__init__.py`
- `evals/simple_evals/.gitignore`
- `evals/simple_evals/example_output.json`
- `evals/simple_evals/logs/.gitkeep`
- `evals/simple_evals/logs/eval_2026-05-29_19-03-20_n3.jsonl`
- `evals/simple_evals/logs/README.md`
- `evals/simple_evals/logs/SimpleQA Eval 100 Problems 2-22-25.txt`
- `evals/simple_evals/problems/Simple QA Test Set.csv`
- `evals/simple_evals/requirements.txt`
- `evals/simple_evals/run_eval.py`
- `evals/simple_evals/simpleqa_eval.py`

### frontend (163)

- `frontend/index.html`
- `frontend/nextjs/.babelrc.build.json`
- `frontend/nextjs/.dockerignore`
- `frontend/nextjs/.eslintrc.json`
- `frontend/nextjs/.example.env`
- `frontend/nextjs/.gitignore`
- `frontend/nextjs/.prettierrc`
- `frontend/nextjs/.python-version`
- `frontend/nextjs/actions/apiActions.ts`
- `frontend/nextjs/app/api/chat/route.ts`
- `frontend/nextjs/app/api/reports/[id]/chat/route.ts`
- `frontend/nextjs/app/api/reports/[id]/route.ts`
- `frontend/nextjs/app/api/reports/route.ts`
- `frontend/nextjs/app/globals.css`
- `frontend/nextjs/app/layout.tsx`
- `frontend/nextjs/app/page.tsx`
- `frontend/nextjs/app/research/[id]/page.tsx`
- `frontend/nextjs/components/Footer.tsx`
- `frontend/nextjs/components/Header.tsx`
- `frontend/nextjs/components/Hero.tsx`
- `frontend/nextjs/components/HumanFeedback.tsx`
- `frontend/nextjs/components/Images/ImageModal.tsx`
- `frontend/nextjs/components/Images/ImagesAlbum.tsx`
- `frontend/nextjs/components/Langgraph/Langgraph.js`
- `frontend/nextjs/components/layouts/CopilotLayout.tsx`
- `frontend/nextjs/components/layouts/MobileLayout.tsx`
- `frontend/nextjs/components/layouts/ResearchPageLayout.tsx`
- `frontend/nextjs/components/LoadingDots.tsx`
- `frontend/nextjs/components/mobile/MobileChatPanel.tsx`
- `frontend/nextjs/components/mobile/MobileHomeScreen.tsx`
- `frontend/nextjs/components/mobile/MobileResearchContent.tsx`
- `frontend/nextjs/components/research/CopilotPanel.tsx`
- `frontend/nextjs/components/research/CopilotResearchContent.tsx`
- `frontend/nextjs/components/research/NotFoundContent.tsx`
- `frontend/nextjs/components/research/ResearchContent.tsx`
- `frontend/nextjs/components/research/ResearchPanel.tsx`
- `frontend/nextjs/components/ResearchBlocks/AccessReport.tsx`
- `frontend/nextjs/components/ResearchBlocks/ChatInterface.tsx`
- `frontend/nextjs/components/ResearchBlocks/ChatResponse.tsx`
- `frontend/nextjs/components/ResearchBlocks/elements/ChatInput.tsx`
- `frontend/nextjs/components/ResearchBlocks/elements/InputArea.tsx`
- `frontend/nextjs/components/ResearchBlocks/elements/LogMessage.tsx`
- `frontend/nextjs/components/ResearchBlocks/elements/SourceCard.tsx`
- `frontend/nextjs/components/ResearchBlocks/elements/SubQuestions.tsx`
- `frontend/nextjs/components/ResearchBlocks/ImageSection.tsx`
- `frontend/nextjs/components/ResearchBlocks/LogsSection.tsx`
- `frontend/nextjs/components/ResearchBlocks/Question.tsx`
- `frontend/nextjs/components/ResearchBlocks/Report.tsx`
- `frontend/nextjs/components/ResearchBlocks/Sources.tsx`
- `frontend/nextjs/components/ResearchResults.tsx`
- `frontend/nextjs/components/ResearchSidebar.tsx`
- `frontend/nextjs/components/Settings/ChatBox.tsx`
- `frontend/nextjs/components/Settings/FileUpload.tsx`
- `frontend/nextjs/components/Settings/LayoutSelector.tsx`
- `frontend/nextjs/components/Settings/MCPSelector.tsx`
- `frontend/nextjs/components/Settings/Modal.tsx`
- `frontend/nextjs/components/Settings/Settings.css`
- `frontend/nextjs/components/Settings/ToneSelector.tsx`
- `frontend/nextjs/components/SimilarTopics.tsx`
- `frontend/nextjs/components/Task/Accordion.tsx`
- `frontend/nextjs/components/Task/AgentLogs.tsx`
- `frontend/nextjs/components/Task/DomainFilter.tsx`
- `frontend/nextjs/components/Task/Report.tsx`
- `frontend/nextjs/components/Task/ResearchForm.tsx`
- `frontend/nextjs/components/TypeAnimation.tsx`
- `frontend/nextjs/config/task.ts`
- `frontend/nextjs/Dockerfile`
- `frontend/nextjs/Dockerfile.dev`
- `frontend/nextjs/helpers/findDifferences.ts`
- `frontend/nextjs/helpers/getHost.ts`
- `frontend/nextjs/helpers/markdownHelper.ts`
- `frontend/nextjs/hooks/ResearchHistoryContext.tsx`
- `frontend/nextjs/hooks/useAnalytics.ts`
- `frontend/nextjs/hooks/useResearchHistory.ts`
- `frontend/nextjs/hooks/useScrollHandler.ts`
- `frontend/nextjs/hooks/useWebSocket.ts`
- `frontend/nextjs/next.config.mjs`
- `frontend/nextjs/nginx/default.conf`
- `frontend/nextjs/package.json`
- `frontend/nextjs/package.lib.json`
- `frontend/nextjs/postcss.config.mjs`
- `frontend/nextjs/public/embed.js`
- `frontend/nextjs/public/favicon.ico`
- `frontend/nextjs/public/img/agents/academicResearchAgentAvatar.png`
- `frontend/nextjs/public/img/agents/businessAnalystAgentAvatar.png`
- `frontend/nextjs/public/img/agents/computerSecurityanalystAvatar.png`
- `frontend/nextjs/public/img/agents/defaultAgentAvatar.JPG`
- `frontend/nextjs/public/img/agents/financeAgentAvatar.png`
- `frontend/nextjs/public/img/agents/mathAgentAvatar.png`
- `frontend/nextjs/public/img/agents/travelAgentAvatar.png`
- `frontend/nextjs/public/img/arrow-circle-up-right.svg`
- `frontend/nextjs/public/img/arrow-narrow-right.svg`
- `frontend/nextjs/public/img/browser.svg`
- `frontend/nextjs/public/img/chat-check.svg`
- `frontend/nextjs/public/img/chat.svg`
- `frontend/nextjs/public/img/copy-white.svg`
- `frontend/nextjs/public/img/copy.svg`
- `frontend/nextjs/public/img/dinosaur.svg`
- `frontend/nextjs/public/img/discord.svg`
- `frontend/nextjs/public/img/docker-blue.svg`
- `frontend/nextjs/public/img/docker.svg`
- `frontend/nextjs/public/img/dunk.svg`
- `frontend/nextjs/public/img/F.svg`
- `frontend/nextjs/public/img/github-blue.svg`
- `frontend/nextjs/public/img/github-footer.svg`
- `frontend/nextjs/public/img/github.svg`
- `frontend/nextjs/public/img/globe.svg`
- `frontend/nextjs/public/img/gptr-black-logo.png`
- `frontend/nextjs/public/img/gptr-logo.png`
- `frontend/nextjs/public/img/hiker.svg`
- `frontend/nextjs/public/img/icon _atom_.svg`
- `frontend/nextjs/public/img/icon _dumbell_.svg`
- `frontend/nextjs/public/img/icon _leaf_.svg`
- `frontend/nextjs/public/img/image.svg`
- `frontend/nextjs/public/img/indeed.svg`
- `frontend/nextjs/public/img/Info.svg`
- `frontend/nextjs/public/img/link.svg`
- `frontend/nextjs/public/img/message-question-circle.svg`
- `frontend/nextjs/public/img/news.svg`
- `frontend/nextjs/public/img/search.svg`
- `frontend/nextjs/public/img/share.svg`
- `frontend/nextjs/public/img/similarTopics.svg`
- `frontend/nextjs/public/img/sources.svg`
- `frontend/nextjs/public/img/stock.svg`
- `frontend/nextjs/public/img/stock2.svg`
- `frontend/nextjs/public/img/thinking.svg`
- `frontend/nextjs/public/img/W.svg`
- `frontend/nextjs/public/img/white-books.svg`
- `frontend/nextjs/public/img/x.svg`
- `frontend/nextjs/public/manifest.json`
- `frontend/nextjs/public/next.svg`
- `frontend/nextjs/public/sw.js`
- `frontend/nextjs/public/vercel.svg`
- `frontend/nextjs/public/workbox-f1770938.js`
- `frontend/nextjs/README.md`
- `frontend/nextjs/rollup.config.js`
- `frontend/nextjs/src/GPTResearcher.tsx`
- `frontend/nextjs/src/index.css`
- `frontend/nextjs/src/index.d.ts`
- `frontend/nextjs/src/index.ts`
- `frontend/nextjs/src/utils/imageTransformPlugin.js`
- `frontend/nextjs/styles/markdown.css`
- `frontend/nextjs/tailwind.config.ts`
- `frontend/nextjs/tsconfig.json`
- `frontend/nextjs/tsconfig.lib.json`
- `frontend/nextjs/types/data.ts`
- `frontend/nextjs/types/react-ga4.d.ts`
- `frontend/nextjs/utils/consolidateBlocks.ts`
- `frontend/nextjs/utils/dataProcessing.ts`
- `frontend/nextjs/utils/getLayout.tsx`
- `frontend/pdf_styles.css`
- `frontend/README.md`
- `frontend/scripts.js`
- `frontend/static/academicResearchAgentAvatar.png`
- `frontend/static/businessAnalystAgentAvatar.png`
- `frontend/static/computerSecurityanalystAvatar.png`
- `frontend/static/defaultAgentAvatar.JPG`
- `frontend/static/favicon.ico`
- `frontend/static/financeAgentAvatar.png`
- `frontend/static/gptr-logo.png`
- `frontend/static/mathAgentAvatar.png`
- `frontend/static/travelAgentAvatar.png`
- `frontend/styles.css`

### gpt_researcher (125)

- `gpt_researcher/__init__.py`
- `gpt_researcher/actions/__init__.py`
- `gpt_researcher/actions/agent_creator.py`
- `gpt_researcher/actions/markdown_processing.py`
- `gpt_researcher/actions/query_processing.py`
- `gpt_researcher/actions/report_generation.py`
- `gpt_researcher/actions/retriever.py`
- `gpt_researcher/actions/utils.py`
- `gpt_researcher/actions/web_scraping.py`
- `gpt_researcher/agent.py`
- `gpt_researcher/config/__init__.py`
- `gpt_researcher/config/config.py`
- `gpt_researcher/config/variables/__init__.py`
- `gpt_researcher/config/variables/base.py`
- `gpt_researcher/config/variables/default.py`
- `gpt_researcher/config/variables/test_local.json`
- `gpt_researcher/context/__init__.py`
- `gpt_researcher/context/compression.py`
- `gpt_researcher/context/retriever.py`
- `gpt_researcher/document/__init__.py`
- `gpt_researcher/document/azure_document_loader.py`
- `gpt_researcher/document/document.py`
- `gpt_researcher/document/langchain_document.py`
- `gpt_researcher/document/online_document.py`
- `gpt_researcher/llm_provider/__init__.py`
- `gpt_researcher/llm_provider/generic/__init__.py`
- `gpt_researcher/llm_provider/generic/base.py`
- `gpt_researcher/llm_provider/image/__init__.py`
- `gpt_researcher/llm_provider/image/image_generator.py`
- `gpt_researcher/llm_provider/image/modelslab_image_generator.py`
- `gpt_researcher/mcp/__init__.py`
- `gpt_researcher/mcp/client.py`
- `gpt_researcher/mcp/README.md`
- `gpt_researcher/mcp/research.py`
- `gpt_researcher/mcp/streaming.py`
- `gpt_researcher/mcp/tool_selector.py`
- `gpt_researcher/memory/__init__.py`
- `gpt_researcher/memory/embeddings.py`
- `gpt_researcher/prompts.py`
- `gpt_researcher/retrievers/__init__.py`
- `gpt_researcher/retrievers/arxiv/__init__.py`
- `gpt_researcher/retrievers/arxiv/arxiv.py`
- `gpt_researcher/retrievers/bing/__init__.py`
- `gpt_researcher/retrievers/bing/bing.py`
- `gpt_researcher/retrievers/bocha/__init__.py`
- `gpt_researcher/retrievers/bocha/bocha.py`
- `gpt_researcher/retrievers/brave/__init__.py`
- `gpt_researcher/retrievers/brave/brave.py`
- `gpt_researcher/retrievers/crw/__init__.py`
- `gpt_researcher/retrievers/crw/crw.py`
- `gpt_researcher/retrievers/custom/__init__.py`
- `gpt_researcher/retrievers/custom/custom.py`
- `gpt_researcher/retrievers/duckduckgo/__init__.py`
- `gpt_researcher/retrievers/duckduckgo/duckduckgo.py`
- `gpt_researcher/retrievers/exa/__init__.py`
- `gpt_researcher/retrievers/exa/exa.py`
- `gpt_researcher/retrievers/getxapi/__init__.py`
- `gpt_researcher/retrievers/getxapi/getxapi.py`
- `gpt_researcher/retrievers/google/__init__.py`
- `gpt_researcher/retrievers/google/google.py`
- `gpt_researcher/retrievers/groundroute/__init__.py`
- `gpt_researcher/retrievers/groundroute/groundroute.py`
- `gpt_researcher/retrievers/mcp/__init__.py`
- `gpt_researcher/retrievers/mcp/retriever.py`
- `gpt_researcher/retrievers/openalex/__init__.py`
- `gpt_researcher/retrievers/openalex/openalex.py`
- `gpt_researcher/retrievers/pubmed_central/__init__.py`
- `gpt_researcher/retrievers/pubmed_central/pubmed_central.py`
- `gpt_researcher/retrievers/searchapi/__init__.py`
- `gpt_researcher/retrievers/searchapi/searchapi.py`
- `gpt_researcher/retrievers/searx/__init__.py`
- `gpt_researcher/retrievers/searx/searx.py`
- `gpt_researcher/retrievers/semantic_scholar/__init__.py`
- `gpt_researcher/retrievers/semantic_scholar/semantic_scholar.py`
- `gpt_researcher/retrievers/serpapi/__init__.py`
- `gpt_researcher/retrievers/serpapi/serpapi.py`
- `gpt_researcher/retrievers/serper/__init__.py`
- `gpt_researcher/retrievers/serper/serper.py`
- `gpt_researcher/retrievers/tavily/__init__.py`
- `gpt_researcher/retrievers/tavily/tavily_search.py`
- `gpt_researcher/retrievers/utils.py`
- `gpt_researcher/retrievers/xquik/__init__.py`
- `gpt_researcher/retrievers/xquik/xquik.py`
- `gpt_researcher/scraper/__init__.py`
- `gpt_researcher/scraper/arxiv/__init__.py`
- `gpt_researcher/scraper/arxiv/arxiv.py`
- `gpt_researcher/scraper/beautiful_soup/__init__.py`
- `gpt_researcher/scraper/beautiful_soup/beautiful_soup.py`
- `gpt_researcher/scraper/browser/__init__.py`
- `gpt_researcher/scraper/browser/browser.py`
- `gpt_researcher/scraper/browser/js/overlay.js`
- `gpt_researcher/scraper/browser/nodriver_scraper.py`
- `gpt_researcher/scraper/browser/processing/__init__.py`
- `gpt_researcher/scraper/browser/processing/html.py`
- `gpt_researcher/scraper/browser/processing/scrape_skills.py`
- `gpt_researcher/scraper/firecrawl/__init__.py`
- `gpt_researcher/scraper/firecrawl/firecrawl.py`
- `gpt_researcher/scraper/pymupdf/__init__.py`
- `gpt_researcher/scraper/pymupdf/pymupdf.py`
- `gpt_researcher/scraper/scraper.py`
- `gpt_researcher/scraper/tavily_extract/__init__.py`
- `gpt_researcher/scraper/tavily_extract/tavily_extract.py`
- `gpt_researcher/scraper/utils.py`
- `gpt_researcher/scraper/web_base_loader/__init__.py`
- `gpt_researcher/scraper/web_base_loader/web_base_loader.py`
- `gpt_researcher/skills/__init__.py`
- `gpt_researcher/skills/browser.py`
- `gpt_researcher/skills/context_manager.py`
- `gpt_researcher/skills/curator.py`
- `gpt_researcher/skills/deep_research.py`
- `gpt_researcher/skills/image_generator.py`
- `gpt_researcher/skills/researcher.py`
- `gpt_researcher/skills/writer.py`
- `gpt_researcher/utils/__init__.py`
- `gpt_researcher/utils/costs.py`
- `gpt_researcher/utils/enum.py`
- `gpt_researcher/utils/llm.py`
- `gpt_researcher/utils/logger.py`
- `gpt_researcher/utils/logging_config.py`
- `gpt_researcher/utils/rate_limiter.py`
- `gpt_researcher/utils/tools.py`
- `gpt_researcher/utils/validators.py`
- `gpt_researcher/utils/workers.py`
- `gpt_researcher/vector_store/__init__.py`
- `gpt_researcher/vector_store/vector_store.py`

### ISSUE_BACKLOG.md (1)

- `ISSUE_BACKLOG.md`

### json_schema_generator.py (1)

- `json_schema_generator.py`

### langgraph.json (1)

- `langgraph.json`

### LICENSE (1)

- `LICENSE`

### main.py (1)

- `main.py`

### mcp-server (1)

- `mcp-server/README.md`

### multi_agents (40)

- `multi_agents/__init__.py`
- `multi_agents/ag2/__init__.py`
- `multi_agents/ag2/agents/__init__.py`
- `multi_agents/ag2/agents/editor.py`
- `multi_agents/ag2/agents/orchestrator.py`
- `multi_agents/ag2/main.py`
- `multi_agents/ag2/README.md`
- `multi_agents/ag2/requirements.txt`
- `multi_agents/ag2/task.json`
- `multi_agents/agent.py`
- `multi_agents/agents/__init__.py`
- `multi_agents/agents/draft_review.py`
- `multi_agents/agents/editor.py`
- `multi_agents/agents/fact_checker.py`
- `multi_agents/agents/fact_review.py`
- `multi_agents/agents/human.py`
- `multi_agents/agents/orchestrator.py`
- `multi_agents/agents/plan_review.py`
- `multi_agents/agents/publisher.py`
- `multi_agents/agents/researcher.py`
- `multi_agents/agents/reviewer.py`
- `multi_agents/agents/reviser.py`
- `multi_agents/agents/utils/__init__.py`
- `multi_agents/agents/utils/file_formats.py`
- `multi_agents/agents/utils/llms.py`
- `multi_agents/agents/utils/none_sentinels.py`
- `multi_agents/agents/utils/pdf_styles.css`
- `multi_agents/agents/utils/utils.py`
- `multi_agents/agents/utils/views.py`
- `multi_agents/agents/visualizer.py`
- `multi_agents/agents/writer.py`
- `multi_agents/langgraph.json`
- `multi_agents/main.py`
- `multi_agents/memory/__init__.py`
- `multi_agents/memory/draft.py`
- `multi_agents/memory/research.py`
- `multi_agents/package.json`
- `multi_agents/README.md`
- `multi_agents/requirements.txt`
- `multi_agents/task.json`

### poetry.toml (1)

- `poetry.toml`

### PR_pr_feat-anthropic-real-usage-cost-tracking.md (1)

- `PR_pr_feat-anthropic-real-usage-cost-tracking.md`

### PR_pr_fix-brave-snippet-bypasses-scraper.md (1)

- `PR_pr_fix-brave-snippet-bypasses-scraper.md`

### Procfile (1)

- `Procfile`

### pyproject.toml (1)

- `pyproject.toml`

### README-ja_JP.md (1)

- `README-ja_JP.md`

### README-ko_KR.md (1)

- `README-ko_KR.md`

### README-zh_CN.md (1)

- `README-zh_CN.md`

### README.md (1)

- `README.md`

### requirements.txt (1)

- `requirements.txt`

### SECURITY.md (1)

- `SECURITY.md`

### setup.py (1)

- `setup.py`

### skills (1)

- `skills/gpt-researcher/SKILL.md`

### terraform (12)

- `terraform/ecr-setup/main.tf`
- `terraform/ecr-setup/outputs.tf`
- `terraform/ecr-setup/variables.tf`
- `terraform/ecr-setup/versions.tf`
- `terraform/github-actions-setup/main.tf`
- `terraform/github-actions-setup/outputs.tf`
- `terraform/github-actions-setup/variables.tf`
- `terraform/github-actions-setup/versions.tf`
- `terraform/main.tf`
- `terraform/outputs.tf`
- `terraform/variables.tf`
- `terraform/versions.tf`

### tests (74)

- `tests/__init__.py`
- `tests/backend/test_write_md_to_pdf_filename.py`
- `tests/docs/doc.pdf`
- `tests/documents-report-source.py`
- `tests/gptr-logs-handler.py`
- `tests/report-types.py`
- `tests/research_test.py`
- `tests/skills/test_deep_research_empty_results.py`
- `tests/skills/test_tavily_mcp_dedupe.py`
- `tests/test_add_references_order.py`
- `tests/test_agent_discovery.py`
- `tests/test_arxiv_scraper.py`
- `tests/test_azure_document_loader.py`
- `tests/test_bing_retriever_malformed.py`
- `tests/test_bocha_error_handling.py`
- `tests/test_brave_retriever.py`
- `tests/test_browser_pdf_detection.py`
- `tests/test_construct_subtopics_error_log.py`
- `tests/test_context_compressor_source_url.py`
- `tests/test_convert_env_value_optional.py`
- `tests/test_costs.py`
- `tests/test_crw_retriever_malformed.py`
- `tests/test_crw_retriever.py`
- `tests/test_custom_retriever_guard.py`
- `tests/test_deep_research_parsing.py`
- `tests/test_duckduckgo_normalize.py`
- `tests/test_exa_null_attrs.py`
- `tests/test_extract_json_with_regex.py`
- `tests/test_get_retrievers_whitespace.py`
- `tests/test_google_malformed.py`
- `tests/test_google_search_url_encoding.py`
- `tests/test_groundroute_malformed_results.py`
- `tests/test_llm_max_tokens.py`
- `tests/test_llm_usage_tracking.py`
- `tests/test_logging_output.py`
- `tests/test_logging.py`
- `tests/test_logs.py`
- `tests/test_mcp_client_config.py`
- `tests/test_mcp.py`
- `tests/test_multi_agents_draft_revisions.py`
- `tests/test_multi_agents_fact_revisions.py`
- `tests/test_multi_agents_plan_revisions.py`
- `tests/test_nebius_provider.py`
- `tests/test_new_agents.py`
- `tests/test_none_accept_sentinels.py`
- `tests/test_online_document_extension.py`
- `tests/test_openalex_malformed_results.py`
- `tests/test_parse_dimension.py`
- `tests/test_pubmed_central_returns_list.py`
- `tests/test_pymupdf_tempfile_cleanup.py`
- `tests/test_quick_search_summary_context.py`
- `tests/test_quick_search.py`
- `tests/test_research_conductor_retrieval.py`
- `tests/test_researcher_logging.py`
- `tests/test_scraper_extract_title.py`
- `tests/test_scraper_get_scraper.py`
- `tests/test_searchapi_retriever_none.py`
- `tests/test_searx_malformed_results.py`
- `tests/test_security_fix.py`
- `tests/test_semantic_scholar_retriever.py`
- `tests/test_semantic_scholar_sort.py`
- `tests/test_serpapi_retriever_malformed.py`
- `tests/test_serper_retriever.py`
- `tests/test_serper_returns_list.py`
- `tests/test_sub_query_normalization.py`
- `tests/test_tavily_malformed.py`
- `tests/test_websocket_manager.py`
- `tests/test_xquik_null_fields.py`
- `tests/test-loaders.py`
- `tests/test-openai-llm.py`
- `tests/test-your-embeddings.py`
- `tests/test-your-llm.py`
- `tests/test-your-retriever.py`
- `tests/vector-store.py`

## 当前工作区额外文件

- `wait-for-local-embedding.ps1`：未跟踪的本地环境辅助脚本，不属于上游主调用链。
- `gpt_researcher/actions/query_processing.py`：当前工作区有未提交的 import 顺序调整。
