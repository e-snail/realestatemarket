# realestatemarket


## 抓取链家所有成交数据

#### 数据库

1 创建数据库

```
CREATE SCHEMA `lianjia_chengjiao`;
```

2 创建数据表

小区

```
CREATE TABLE `lianjia_chengjiao`.`xiaoqu` (
  `name` VARCHAR(45) NOT NULL,
  `regionb` VARCHAR(45) NULL,
  `regions` VARCHAR(45) NULL,
  `style` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  PRIMARY KEY (`name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC));
```

成交

```
CREATE TABLE `database_test`.`chengjiao` (
  `href` VARCHAR(200) NOT NULL,
  `name`  VARCHAR(45), 
  `style`  VARCHAR(45), 
  `area`  VARCHAR(45), 
  `orientation` VARCHAR(45), 
  `floor` VARCHAR(45), 
  `year` VARCHAR(45), 
  `sign_time` VARCHAR(45), 
  `unit_price` VARCHAR(45), 
  `total_price` VARCHAR(45), 
  `fangchan_class` VARCHAR(45), 
  `school` VARCHAR(45), 
  `subway` VARCHAR(45), 
  PRIMARY KEY (`href`),
  UNIQUE INDEX `href_UNIQUE` (`href` ASC));
```

#### 抓取小区列表
