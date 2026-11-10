# Milvus 学习环境

本目录为 `D:\桌面\新建文件夹\1.py` 的学习代码提供 Milvus 服务及验证脚本。
Compose 基于 [Milvus 官方 Windows 部署说明](https://milvus.io/docs/install_standalone-windows.md) 中的 v3.0.3 配置，独立于项目原有的 Compose。

## 服务

在 `D:\桌面\课程\project2` 的 PowerShell 中运行：

```powershell
docker compose --env-file .\milvus-demo\compose.vars -f .\milvus-demo\docker-compose.yml up -d
docker compose --env-file .\milvus-demo\compose.vars -f .\milvus-demo\docker-compose.yml ps
```

- Milvus 地址：`http://localhost:19530`。
- 服务管理端口：`http://localhost:9091`。
- 端口只绑定本机；数据使用本学习环境的独立 Docker 命名卷。
- `compose.vars` 是空配置，明确指定它可避免 Compose 自动读取项目密钥文件。

停止服务并保留资料：

```powershell
docker compose --env-file .\milvus-demo\compose.vars -f .\milvus-demo\docker-compose.yml stop
```

客户端安装版本：`langchain-milvus==0.4.0`、`pymilvus==3.0.2`。

## 练习代码的调用顺序

以下代码放在已有异步函数中，PDF 路径替换为实际路径：

```python
researcher = GPTResearcher(
    query="RAG 如何利用外部证据？",
    report_source="langchain_vectorstore",
    report_type="research_report",
)

# 显式导入一次文件，返回读取到的非空页面材料数量。
page_count = await researcher.load_documents([pdf_path])

# 根据子问题检索库中的片段，填充 researcher.context。
await researcher.conduct_research()
report = await researcher.write_report()
```

`load_documents` 负责 PDF 加载、写入，并将当前对象的检索范围限定在本次导入文件的来源路径。
`conduct_research` 负责规划与检索，不重复写入资料。

注意当前教学版的边界：

- 同一文件反复显式导入仍会重复产生记录，自动主键不提供内容去重。
- 新建研究对象且不导入文件时，`vector_filter` 默认为 `None`，查询整个 Collection。
- 真实运行使用 `Memory` 中现有的 Embedding 客户端；需要它自身的可用配置。
- `plan_research` 沿用此前实现，会先搜索以辅助规划，向量库来源不代表完全离线。
- 当前报告生成仍是已有教学版的上下文拼接，没有接入新的写作模型。
- 查询返回的来源在上下文中保留；顶层 `get_source_urls` 仍是旧的网页访问集合，后续引用单元再统一。

## 验证

```powershell
& '.\.venv\Scripts\python.exe' '.\milvus-demo\check_chain.py'
```

脚本从实际保存的练习文件提取核心类，不执行其顶层项目导入或启动 API 服务。
它创建临时两页 PDF，并使用真实 PDF 解析器、文本分割器、Milvus 客户端与数据库完成写入、过滤检索、上下文及报告组装。

Embedding 使用六维词频测试向量，研究规划也使用测试替身，不读取密钥、不调用付费模型或外部网页。
这验证代码接口与数据流，不验证真实语义检索质量。

每次使用独立的 `study_check_...` 测试 Collection，结束后只删除本次测试 Collection；不会向正式的 `research_chunks_v1` 写入测试向量。

### 本次验证记录（2026-10-24）

- Milvus 服务版本 `3.0.3`，健康接口 HTTP 200，etcd、MinIO、Milvus 均健康。
- 两页临时 PDF 生成四个正文片段，另加入一条不同来源的干扰资料。
- 三个研究查询均成功返回上下文，来源过滤排除了干扰资料。
- 不匹配的过滤条件返回空上下文；研究前后记录数均为 5，没有重复入库。
- 本地及本地加网页两种既有分支也通过验证；网页材料在该验证中为测试替身。
- 练习代码测试前后 SHA256 一致：`9debd3812a2eaa55a9d518fa60bffdc3cf92afe9dad828d6a4ddd72ff4d494ec`。
- 临时测试 Collection 已清理，真实模型的语义效果及生产数据尚未验证。
