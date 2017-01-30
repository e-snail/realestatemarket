## 数据表设计

`本地mysql密码root123`

#### 表1：成交房屋信息

- 房屋ID  Condo-ID   -> 链家编号
- 面积 square
- 总价 expense
- 单价 price
- 户型（X室X厅） framework
- 成交日期
- 小区ID
- 是否是学区房 ?怎么获取

#### 表2：位置信息

- 市 010
- 区  district
- 小区ID  subdistrict-id
- 小区名称  subdistrict-name
- 坐标 subdistrict-coordinate

#### 表3：户型列表condo_framework


#### 缺陷：

-  相同小区的不同楼的价格可能差别很大，因为不同楼可能跟不同学区房挂钩，甚至属于不同的区


数据项关联其它表，类型怎么填写？？？

## 创建数据表

#### 1 创建数据库
`CREATE SCHEMA `realestatemarket` DEFAULT CHARACTER SET utf8 ;`


#### 2 创建数据表condo_framework：已售房户型信息
```
CREATE TABLE `realestatemarket`.`condo_framework` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '户型ID',
  `description` VARCHAR(45) NOT NULL COMMENT '户型描述',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

```

#### 3 创建数据表condo_position：已售房小区信息
```
CREATE TABLE `realestatemarket`.`condo_position` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `province` INT NOT NULL DEFAULT 010 COMMENT '省、直辖市',
  `city` INT NOT NULL DEFAULT 010 COMMENT '市',
  `district` INT NOT NULL COMMENT '区',
  `longitude` DECIMAL(10,2) NOT NULL COMMENT '经度',
  `latitude` DECIMAL(10,2) NOT NULL COMMENT '纬度',
  `subdistrict_name` VARCHAR(45) NOT NULL COMMENT '小区名称',
  PRIMARY KEY (`id`));
```

#### 4 创建数据表bj_city_district：已售房位置的区县信息
```
CREATE TABLE `realestatemarket`.`bj_city_district` (
  `id` INT NOT NULL,
  `district_no` INT NOT NULL COMMENT '区号，用邮编代替',
  `district_name` VARCHAR(45) NOT NULL COMMENT '区名',
  PRIMARY KEY (`id`));

INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(0,'100032','东城区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(1,'100032','西城区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(2,'100020','朝阳区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(3,'100080','海淀区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(4,'100071','丰台区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(5,'102600','大兴区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(6,'102300','门头沟区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(7,'102488','房山区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(8,'100043','石景山区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(9,'101149','通州区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(10,'101200','平谷区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(11,'101300','顺义区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(12,'101400','怀柔区');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(13,'101500','密云县');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(14,'102100','延庆县');
INSERT INTO `realestatemarket`.`bj_city_district`(id,district_no,district_name) values(15,'102200','昌平县');

```

#### 5 创建数据表condo_sold：已售房信息
```
CREATE TABLE `realestatemarket`.`condo_sold` (
  `id` INT UNSIGNED NOT NULL COMMENT '房屋ID',
  `condo_lj_id` VARCHAR(20) NOT NULL COMMENT '房屋的链家编号，应该是唯一',
  `square` DECIMAL(10,2) NOT NULL COMMENT '面积',
  `expense` DECIMAL(10,2) NOT NULL COMMENT '成交价',
  `price` DECIMAL(10,2) NOT NULL COMMENT '每平米单价',
  `date` DATE NOT NULL COMMENT '成交日期',
  `framework` INT NOT NULL COMMENT '户型信息，关联表condo_framework',
  `position` INT NOT NULL COMMENT '位置信息，关联表condo_position',
  PRIMARY KEY (`id`),
  INDEX `position_idx` (`position` ASC),
  INDEX `framework_idx` (`framework` ASC),
  CONSTRAINT `framework`
    FOREIGN KEY (`framework`)
    REFERENCES `realestatemarket`.`condo_framework` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `position`
    FOREIGN KEY (`position`)
    REFERENCES `realestatemarket`.`condo_position` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
```

