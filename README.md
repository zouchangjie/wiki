# wiki_spiker_bigdata
爬取wiki中一个词条中的全部文章和每次词条被编辑时的人名、时间、编辑内容,前后相应等。
本项目分为三部分：
第一部分：
setup.py是爬虫的启动文件，启动后会爬取wiki中乔布斯词条的各个版本内容，也就是网页上词条diff页面的内容。

第二部分：
把爬取文件保存下来，每个diff保存到一个文件，然后解析文件，收集到编辑者姓名，日期，出现次数，最关键的是把每个编辑者对应编辑的内容对应起来，conn_wiki的目的是分析文件，再找出各版本前后相应关系。

第三部分：
conn_data里把版本前后相应关系放到文件中。我用的是gephi这个软件可视化这些版本相应关系。

! [图1] (https://github.com/zouchangjie/wiki_spiker_bigdata/blob/master/image/diff.png)；

