# 百度文档爬虫 / Baidu Document Scraper

### 简介 / Summary
这个爬虫可以通过提供的百度文库网页把相关文件下载到本地，目前只支持.txt和.ppt
This scraper can download the docuemnt from Baidu Doc, currently only support .txt and .ppt files

### 可以下载的文件类型 / Document type can be downloaded
* .txt
* .ppt
* .work (暂不支持/not supported yet)
* .pdf (暂不支持/not supported yet)
* .xls (暂不支持/not supported yet)

### 学习到的东西 / Learnings
* 难点是如何从网页中找到加载的文件,文档内容不在网页源代码内，需要在开发者工具里”Network“中找到加载文件
* gbk解码，要看浏览器的编码”header“的Content-Type
* 如何伪造带有md5sum的请求
* urllib 和 CookieJar,https://gist.github.com/bngsudheer/634927
* re.findall()
* url_list = [item.replace("\\","") for item in url_list]

### 未来需要改进的地方 / Further Improvements
* 创建一个”下载“文件夹，把下载的文件都放到这个文件夹内，目前下载文件都在根目录
