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

###### (1) 修改`realestatemarket/items.py`，添加以下类：

- CondoSoldItem         # 已售房屋信息
- CondoPosition         # 房屋所在小区的信息
- CondoFrameworkItem    # 房屋格局信息
- BJCityDistrict        # 北京区县信息

###### (2) 

###### (3) 

###### (4) 
