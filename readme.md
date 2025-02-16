# 爬虫笔记

## 目录结构
```
.
├── asset/
├── data/
├── others/
│   ├── requests.ipynb
│   ├── selenium.ipynb
│   ├── urllib.ipynb
│   └── 解析.ipynb
└── scrapy/
    ├── dangdang/
    ├── dianyin/
    ├── fanyi_post/
    ├── readbook/
    │   ├── readme.md
    ├── scrapy_baidu/
    │   ├── readme.md
└── README.md
```

## 项目概述

本项目主要用于学习和实践爬虫技术，涵盖了多种爬虫技术和工具的学习成果。以下是各部分的详细介绍：

### 1. `data/`
该文件夹存储了通过爬虫爬取下来的数据，包括但不限于：
- **JSON 文件**：例如 `book.json`（书籍信息）、`douban_1.json` 和 `douban_2.json`（豆瓣电影数据）、`kfc_1.json` 和 `kfc_2.json`（肯德基餐厅信息）等。
- **HTML 文件**：例如 `bs4_example.html`（BeautifulSoup 示例 HTML 文件）、`gushiwen.html`（古诗文网页）等。
- **图片资源**：例如 `code.jpg`（示例图片），以及 `books/` 文件夹中的书籍封面图片和 `imgs/` 文件夹中的各种图片资源。

### 2. `others/` 
该文件夹包含使用其他库（如 `requests`, `selenium`, `urllib`）进行爬虫学习的笔记和代码示例：
- **`requests.ipynb`**：使用 `requests` 库的 Jupyter Notebook，演示如何发送 HTTP 请求并处理响应。
- **`selenium.ipynb`**：使用 `selenium` 库的 Jupyter Notebook，演示如何自动化浏览器操作。
- **`urllib.ipynb`**：使用 `urllib` 库的 Jupyter Notebook，介绍 Python 标准库中的网络请求功能。
- **`解析.ipynb`**：包含网页内容的多种解析方式。

### 3. `scrapy/`
该文件夹包含使用 Scrapy 框架进行爬虫学习的具体项目，每个项目都遵循标准的 Scrapy 项目结构，包括 `spiders`, `pipelines`, `middlewares` 等模块。具体子项目如下：
- **`dangdang/`**：当当网爬虫项目，主要抓取图书信息。
- **`dianyin/`**：电影爬虫项目，抓取电影相关信息。
- **`fanyi_post/`**：翻译爬虫项目，使用 POST 请求进行翻译服务的调用。
- **`readbook/`**：书籍爬虫项目，可以作为通用爬虫框架，详细说明见 `readbook/readme.md`。
- **`scrapy_baidu/`**：百度搜索结果爬虫项目，展示了 Scrapy 框架的基本使用方法，详细说明见 `scrapy_baidu/readme.md`。

`fanyi_post` 项目为 POST 请求，其他项目为 GET 请求。

