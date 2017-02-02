## 本地开发环境

- MacOS
- MySql
- PyCharm CE
- Python 2.x & Python 3.5

- Scrapy
 [Mac上安装Scrapy](http://www.tuicool.com/articles/mmIVrqU)
 Scrapy用法见下文。
 
- BeautifulSoup


#### Scrapy用法

##### 1 使用scrapy初始化项目
$`scrapy startproject realestatemarket`       

在项目文件名realestatemarket下还会再生成一个realestatemarket文件夹

##### 2 生成爬虫
$`scrapy genspider lianjia_chengjiao http://bj.lianjia.com/chengjiao/`

##### 3 项目目录结构

realestatemarket /
    ---- realestatemarket /
        -------- items.py               # 自定义module数据类
        -------- middlewares.py         # 是和Scrapy的请求/响应处理相关联的框架
        -------- pipelines.py           # 用来对items里面提取的数据做进一步处理，如保存等
        -------- setting.py             # 项目的配置文件
        -------- spiders /
            ------------ lianjia_chengjiao.py           # 起始url存于此
    ---- scrapy.cfg                   # 项目配置信息

##### 4 实现爬虫功能

参考1：[爬虫实例](http://www.cnblogs.com/wuxl360/p/5567631.html)

###### (1) 修改`realestatemarket/items.py`，添加以下类：

- CondoSoldItem         # 已售房屋信息
- CondoPosition         # 房屋所在小区的信息
- CondoFrameworkItem    # 房屋格局信息
- BJCityDistrict        # 北京区县信息

###### (2) 网页解析 `realestatemarket/spiders/lianjia_chengjiao.py`
- $`scrapy shell`
 进入shell
 `$response.xparse()`解析字段
 
- [XPath](http://www.w3school.com.cn/xpath/)
 X Path 是一门在XML/HTML文档中查找信息的语言。XPath可用来在XML/HTML文档中对元素和属性进行遍历。
 
- [Selector](https://doc.scrapy.org/en/latest/topics/selectors.html#topics-selectors)
 Scrapy内置的网页提取方法。其它备选方案：
    - BeautifulSoup
    - lxml
    
- 编码解析网页数据
 ```
    realestatemarket/spiders/lianjia_chengjiao.py
    
    # 回调函数，处理response并返回处理后的数据和需要跟进的url
    def parse(self, response):
        # response  <200 http://bj.lianjia.com/chengjiao/>  请求返回成功
        # response.body 返回的网页内容
        sel = Selector(response)
        sites = response.xpath(
            '//div[@class="content"]/div[@class="leftContent"]/ul[@class="listContent"]/li/div[@class="info"]')
        items = []

        for site in sites:
            item = CondoItem()
            item['title'] = site.xpath('div[@class="title"]/a/text()').extract()
            item['date'] = site.xpath('div[@class="address"]/div[@class="dealDate"]/text()').extract()
            item['expense'] = site.xpath('div[@class="address"]/div[@class="totalPrice"]/span/text()').extract()
            item['price'] = site.xpath('div[@class="flood"]/div[@class="unitPrice"]/span/text()').extract()

            items.append(item)

        return items
 ```
 
- 运行爬虫 `$scrapy crawl lianjia_chengjiao`


###### (3) 数据存储

- 文件存储：JSon文件
 $`scrapy crawl lianjia_chengjiao -o condo.json -t json`
 以json形式存储数据到condo.json文件
 
- 数据库存储MySQL
 1 创建数据库，简化版的数据库
 ```
CREATE SCHEMA `lianjia_sold` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE `lianjia_sold`.`condo_sold` (
  `lj_id` VARCHAR(20) NOT NULL COMMENT '房屋的链家编号，应该是唯一',
  `square` DECIMAL(10,2) NOT NULL COMMENT '面积',
  `expense` DECIMAL(10,2) NOT NULL COMMENT '成交价',
  `price` DECIMAL(10,2) NOT NULL COMMENT '每平米单价',
  `date` DATE NOT NULL COMMENT '成交日期',
  `condo_framework` VARCHAR(20) NOT NULL COMMENT '户型信息',
  `subdistrict_name` VARCHAR(20) NOT NULL COMMENT '小区名'
  )  ENGINE=MyISAM DEFAULT CHARSET=utf8;
 ```


 2 安装python-mysql
 python3不能用MySQLdb，但是可以用python-mysql；
 $`pip install python-mysql`
 `import pymysql`
 注意关闭VIRTUALENV：export PIP_REQUIRE_VIRTUALENV=false
 
 3 setting.py
 
 4 pipelines.py
 

###### (4) 



## 错误总结
1, start_request错误，参数个数不对
start_request是解析url的，参数不对可能是url有问题，查了一下，果然是引号的问题：用""，不能用''

2, DEBUG: Forbidden by robots.txt: <GET http://bj.lianjia.com/chengjiao//>
在setting改变ROBOTSTXT_OBEY为False，让scrapy不要遵守robot协议，之后就能正常爬取了

