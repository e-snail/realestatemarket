#### 起始url: http://bj.lianjia.com/chengjiao/


## Python爬虫技术选择
主要参考[这篇文章](http://www.cnblogs.com/zw369/p/6123569.html)

- 1 urlib2和urlib
 python自带的网络请求模块，灵活，但是易用性差。需要二次封装。
 适合简单的项目。

- 2 第三方模块requests
 仅仅是封装了网络请求，web页面分析还要结合lxml或beautifulsoup。
 适合简单的项目。

- 3 scrapy框架
 优秀的第三方库，对于请求调度、异常处理都已经封装的很好了。
 能满足较为复杂的项目需求。

- 4 python selenium
 能爬取装备了反爬虫机制的页面。
 
 以前只用过urlib和urllib2，需要封装；本着学习的目的，还是决定用scrapy，看看优秀的框架是怎么用的。
 
## 要解决的问题

- 页面分析
- 获取数据
- 存储数据
- 控制爬网页的速度和频率
- 面向对象编程（对python面向对象的特性还不熟）

最终方案：scrapy + Beautifulsoup + MySql 

