/*
Navicat MySQL Data Transfer

Source Server         : firstTest
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : opcdata

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2019-05-27 18:55:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `equip_data`
-- ----------------------------
DROP TABLE IF EXISTS `equip_data`;
CREATE TABLE `equip_data` (
  `equipment_id` varchar(50) NOT NULL,
  `maxis_speed` varchar(50) NOT NULL,
  `current_yield` varchar(50) NOT NULL,
  `dan_lian` varchar(20) NOT NULL,
  `cycle_time` varchar(20) NOT NULL,
  `material_num` varchar(20) NOT NULL,
  `speed` varchar(20) NOT NULL,
  `quanshu` varchar(20) NOT NULL,
  `time_bian` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of equip_data
-- ----------------------------
INSERT INTO `equip_data` VALUES ('GRM231', '28028', '355', 'True', '100', '50', '3654', '19', '05/20/19 07:30:34');
INSERT INTO `equip_data` VALUES ('GRM350', '250', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM351', '360', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM352', '400', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM353', '500', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM354', '1234567', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM356', '2369877', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM357', '1323232', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM358', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM359', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM360', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM370', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM371', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM372', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM373', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM374', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM375', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM376', '1362620', '500', 'False', '1000', '69', '5600', '156', '');
INSERT INTO `equip_data` VALUES ('GRM377', '1362620', '500', 'False', '1000', '69', '5600', '156', '');

-- ----------------------------
-- Table structure for `equip_info`
-- ----------------------------
DROP TABLE IF EXISTS `equip_info`;
CREATE TABLE `equip_info` (
  `equipment_id` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `sale_date` varchar(50) NOT NULL,
  `linkman` varchar(50) NOT NULL,
  `addr` varchar(50) NOT NULL,
  `contacts` varchar(50) NOT NULL,
  `baoxiu` varchar(50) NOT NULL,
  `other` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of equip_info
-- ----------------------------
INSERT INTO `equip_info` VALUES ('dsadasd', 'dasda', '2018-04-10', 'dasdas', '青岛大学', 'dasd', 'dasdas', 'dasdasda');
INSERT INTO `equip_info` VALUES ('GRM231', 'abc_y', '2019年10月', '老王', '哈尔滨工业大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM350', 'abc_y', '2019年10月', '老王', '广州大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM351', 'abc_y', '2019年10月', '老王', '东南大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM352', 'abc_y', '2019年10月', '老王', '西北大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM353', 'abc_y', '2019年10月', '老王', '北京大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM354', 'abc_y', '2019年10月', '老王', '南京大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM356', 'abc_y', '2019年10月', '老王', '西安交通大学', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM357', 'qwewq', '213123', '12312312', '西安科技大学临潼校区', '312312', '13213', '13123');
INSERT INTO `equip_info` VALUES ('GRM358', 'asdsaddasda', 'dasda', 'dsadas', '华为技术有限公司', 'dasda', 'dasda', 'dasdas');
INSERT INTO `equip_info` VALUES ('GRM359', 'csadca', 'adas', 'dasdasd', '广州大学', 'dasd', 'dasda', 'dasdas');
INSERT INTO `equip_info` VALUES ('GRM360', 'abc_x', '2018年5月', 'MR chen', '中国，湖南', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM361', 'abc_d', '2018年5月', 'MR chen', '中国，香港', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM362', 'abc_e', '2018年5月', 'MR chen', '中国，福建', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM363', 'abc_h', '2018年5月', 'MR chen', '中国，深圳', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM364', 'abc_h', '2018年1月', 'MR chen', '中国，拉萨', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM365', 'abc_h', '2018年2月', 'MR chen', '中国，江西', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM366', 'abc_h', '2018年3月', 'MR chen', '中国，天津', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM367', 'abc_h', '2018年4月', 'MR chen', '中国，河北', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM368', 'abc_h', '2018年5月', 'MR chen', '中国，浙江', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM369', 'abc_h', '2018年6月', 'MR chen', '中国，江苏', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM370', 'abc_h', '2018年7月', 'MR chen', '中国，太乙路街道', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM371', 'abc_h', '2018年8月', 'MR chen', '中国，青海', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM372', 'abc_h', '2018年9月', 'MR chen', '中国，河南', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM373', 'abc_h', '2018年10月', 'MR chen', '中国，上海', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM374', 'abc_h', '2018年11月', 'MR chen', '中国，甘肃', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM375', 'abc_h', '2018年12月', 'MR chen', '中国，四川', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM376', 'abc_h', '2017年10月', 'MR chen', '中国，内蒙古', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM377', 'abc_h', '2016年10月', 'MR chen', '乌鲁木齐', '18829343070', '2年', '备注');
INSERT INTO `equip_info` VALUES ('GRM458', 'sdsad_kmkn', '2019-05-27', '条子', '韩国，首尔', '18740478793', '3年', '此设备很好用的');
INSERT INTO `equip_info` VALUES ('letme', 'kdak-dasda', '2019-05-22', 'UZI', '云南，昆明', '13772995689', '1年', '很好用');

-- ----------------------------
-- Table structure for `fault_rate`
-- ----------------------------
DROP TABLE IF EXISTS `fault_rate`;
CREATE TABLE `fault_rate` (
  `equipment_id` varchar(50) NOT NULL,
  `rate` float(20,0) NOT NULL,
  PRIMARY KEY (`equipment_id`),
  CONSTRAINT `equip_id` FOREIGN KEY (`equipment_id`) REFERENCES `equip_info` (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fault_rate
-- ----------------------------
INSERT INTO `fault_rate` VALUES ('GRM231', '10');
INSERT INTO `fault_rate` VALUES ('GRM350', '13');
INSERT INTO `fault_rate` VALUES ('GRM351', '9');
INSERT INTO `fault_rate` VALUES ('GRM352', '12');
INSERT INTO `fault_rate` VALUES ('GRM353', '20');
INSERT INTO `fault_rate` VALUES ('GRM354', '16');
INSERT INTO `fault_rate` VALUES ('GRM356', '6');
INSERT INTO `fault_rate` VALUES ('GRM357', '19');
INSERT INTO `fault_rate` VALUES ('GRM358', '25');
INSERT INTO `fault_rate` VALUES ('GRM359', '5');

-- ----------------------------
-- Table structure for `log_info`
-- ----------------------------
DROP TABLE IF EXISTS `log_info`;
CREATE TABLE `log_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `do_what` varchar(50) DEFAULT NULL,
  `do_time` varchar(50) DEFAULT NULL,
  `do_ip` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of log_info
-- ----------------------------
INSERT INTO `log_info` VALUES ('1', 'xiaoming', '用户修改了密码', '2019.05.20 19:21:07', '192.168.1.151');
INSERT INTO `log_info` VALUES ('2', 'xiaoming', '用户修改了密码', '2019.05.20 19:22:51\'', '192.168.1.151');
INSERT INTO `log_info` VALUES ('3', 'xiaoming', '用户修改了密码', '2019.05.20 19:23:46', '192.168.1.151');
INSERT INTO `log_info` VALUES ('4', 'xiaoming', '用户\'xiaoming\'修改了密码', '2019.05.20 19:26:57', '192.168.1.151');
INSERT INTO `log_info` VALUES ('5', 'xiaoming', '用户：\'xiaoming\'，进行了修改密码操作', '2019.05.20 19:51:58', '192.168.1.151');
INSERT INTO `log_info` VALUES ('6', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.20 19:56:08', '192.168.1.151');
INSERT INTO `log_info` VALUES ('7', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.20 20:00:26', '192.168.1.151');
INSERT INTO `log_info` VALUES ('8', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.20 20:00:48', '192.168.1.151');
INSERT INTO `log_info` VALUES ('9', 'xiaoming', '用户：xiaoming，删除用户操作被拒绝', '2019.05.20 20:01:07', '192.168.1.151');
INSERT INTO `log_info` VALUES ('10', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.20 20:01:26', '192.168.1.151');
INSERT INTO `log_info` VALUES ('11', 'feaker', '用户：feaker，登录系统操作', '2019.05.20 20:02:28', '192.168.1.151');
INSERT INTO `log_info` VALUES ('12', 'feaker', '用户：\'feaker\'，进行了修改密码操作', '2019.05.20 20:02:53', '192.168.1.151');
INSERT INTO `log_info` VALUES ('13', 'feaker', '用户：feaker，删除用户操作被拒绝', '2019.05.20 20:04:04', '192.168.1.151');
INSERT INTO `log_info` VALUES ('14', 'feaker', '用户：feaker，进行了添加设备操作', '2019.05.20 20:09:25', '192.168.1.151');
INSERT INTO `log_info` VALUES ('15', 'feaker', '用户：feaker，删除用户操作被拒绝', '2019.05.20 20:18:51', '192.168.1.151');
INSERT INTO `log_info` VALUES ('16', 'feaker', '用户：feaker，登录系统操作', '2019.05.20 21:00:12', '192.168.1.151');
INSERT INTO `log_info` VALUES ('17', 'feaker', '用户：feaker，登录系统操作', '2019.05.20 21:00:49', '192.168.1.151');
INSERT INTO `log_info` VALUES ('18', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 09:05:14', '192.168.1.151');
INSERT INTO `log_info` VALUES ('19', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 09:07:15', '192.168.1.151');
INSERT INTO `log_info` VALUES ('20', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 09:17:53', '192.168.1.151');
INSERT INTO `log_info` VALUES ('21', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 10:34:14', '192.168.1.151');
INSERT INTO `log_info` VALUES ('22', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 10:41:52', '192.168.1.151');
INSERT INTO `log_info` VALUES ('23', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 15:37:53', '192.168.1.151');
INSERT INTO `log_info` VALUES ('24', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 16:01:33', '192.168.1.151');
INSERT INTO `log_info` VALUES ('34', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 16:58:09', '192.168.1.151');
INSERT INTO `log_info` VALUES ('35', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 17:00:12', '192.168.1.151');
INSERT INTO `log_info` VALUES ('36', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 17:01:52', '192.168.1.151');
INSERT INTO `log_info` VALUES ('37', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 17:04:42', '192.168.1.151');
INSERT INTO `log_info` VALUES ('38', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 17:26:56', '192.168.1.151');
INSERT INTO `log_info` VALUES ('39', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 18:46:33', '192.168.1.151');
INSERT INTO `log_info` VALUES ('40', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.21 18:47:04', '192.168.1.151');
INSERT INTO `log_info` VALUES ('41', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.21 18:47:52', '192.168.1.151');
INSERT INTO `log_info` VALUES ('42', 'feaker', '用户：feaker，登录系统操作', '2019.05.21 18:58:30', '192.168.1.151');
INSERT INTO `log_info` VALUES ('43', '马云', '用户：马云，登录系统操作', '2019.05.21 19:55:18', '192.168.1.151');
INSERT INTO `log_info` VALUES ('44', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 08:44:38', '192.168.1.151');
INSERT INTO `log_info` VALUES ('45', '马云', '用户：马云，退出系统', '2019.05.22 08:53:55', '192.168.1.151');
INSERT INTO `log_info` VALUES ('46', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 08:56:04', '192.168.1.151');
INSERT INTO `log_info` VALUES ('47', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:02:43', '192.168.1.151');
INSERT INTO `log_info` VALUES ('48', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:03:39', '192.168.1.151');
INSERT INTO `log_info` VALUES ('49', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:04:21', '192.168.1.151');
INSERT INTO `log_info` VALUES ('50', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:05:42', '192.168.1.151');
INSERT INTO `log_info` VALUES ('51', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:06:14', '192.168.1.151');
INSERT INTO `log_info` VALUES ('52', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:06:24', '192.168.1.151');
INSERT INTO `log_info` VALUES ('53', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:06:40', '192.168.1.151');
INSERT INTO `log_info` VALUES ('54', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:07:00', '192.168.1.151');
INSERT INTO `log_info` VALUES ('55', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:07:10', '192.168.1.151');
INSERT INTO `log_info` VALUES ('56', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:07:58', '192.168.1.151');
INSERT INTO `log_info` VALUES ('57', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:08:20', '192.168.1.151');
INSERT INTO `log_info` VALUES ('58', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:08:57', '192.168.1.151');
INSERT INTO `log_info` VALUES ('59', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:09:48', '192.168.1.151');
INSERT INTO `log_info` VALUES ('60', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:10:06', '192.168.1.151');
INSERT INTO `log_info` VALUES ('61', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:10:39', '192.168.1.151');
INSERT INTO `log_info` VALUES ('62', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:10:55', '192.168.1.151');
INSERT INTO `log_info` VALUES ('63', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:11:08', '192.168.1.151');
INSERT INTO `log_info` VALUES ('64', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:11:28', '192.168.1.151');
INSERT INTO `log_info` VALUES ('65', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:11:42', '192.168.1.151');
INSERT INTO `log_info` VALUES ('66', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:12:02', '192.168.1.151');
INSERT INTO `log_info` VALUES ('67', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:12:15', '192.168.1.151');
INSERT INTO `log_info` VALUES ('68', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:15:53', '192.168.1.151');
INSERT INTO `log_info` VALUES ('69', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:38:43', '192.168.1.151');
INSERT INTO `log_info` VALUES ('70', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:39:23', '192.168.1.151');
INSERT INTO `log_info` VALUES ('71', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:54:18', '192.168.1.151');
INSERT INTO `log_info` VALUES ('72', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:54:37', '192.168.1.151');
INSERT INTO `log_info` VALUES ('73', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:55:07', '192.168.1.151');
INSERT INTO `log_info` VALUES ('74', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:56:19', '192.168.1.151');
INSERT INTO `log_info` VALUES ('75', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:57:36', '192.168.1.151');
INSERT INTO `log_info` VALUES ('76', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 10:59:41', '192.168.1.151');
INSERT INTO `log_info` VALUES ('77', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 11:23:07', '192.168.1.151');
INSERT INTO `log_info` VALUES ('78', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 11:34:01', '192.168.1.151');
INSERT INTO `log_info` VALUES ('79', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 11:40:57', '192.168.1.151');
INSERT INTO `log_info` VALUES ('80', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 11:41:38', '192.168.1.151');
INSERT INTO `log_info` VALUES ('81', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:37:15', '192.168.1.151');
INSERT INTO `log_info` VALUES ('82', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:46:59', '192.168.1.151');
INSERT INTO `log_info` VALUES ('83', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:49:25', '192.168.1.151');
INSERT INTO `log_info` VALUES ('84', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:54:22', '192.168.1.151');
INSERT INTO `log_info` VALUES ('85', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:55:34', '192.168.1.151');
INSERT INTO `log_info` VALUES ('86', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:55:48', '192.168.1.151');
INSERT INTO `log_info` VALUES ('87', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:56:31', '192.168.1.151');
INSERT INTO `log_info` VALUES ('88', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:56:56', '192.168.1.151');
INSERT INTO `log_info` VALUES ('89', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 14:59:39', '192.168.1.151');
INSERT INTO `log_info` VALUES ('90', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 15:08:23', '192.168.1.151');
INSERT INTO `log_info` VALUES ('91', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 15:18:27', '192.168.1.151');
INSERT INTO `log_info` VALUES ('92', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 15:19:38', '192.168.1.151');
INSERT INTO `log_info` VALUES ('93', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 17:09:31', '192.168.1.151');
INSERT INTO `log_info` VALUES ('94', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 17:28:33', '192.168.1.232');
INSERT INTO `log_info` VALUES ('95', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.22 18:36:25', '192.168.1.151');
INSERT INTO `log_info` VALUES ('96', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 18:55:07', '192.168.1.151');
INSERT INTO `log_info` VALUES ('97', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 20:25:23', '192.168.1.151');
INSERT INTO `log_info` VALUES ('98', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 20:41:44', '192.168.1.151');
INSERT INTO `log_info` VALUES ('99', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 20:49:05', '192.168.1.151');
INSERT INTO `log_info` VALUES ('100', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 21:06:08', '192.168.1.151');
INSERT INTO `log_info` VALUES ('101', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 21:13:37', '192.168.1.151');
INSERT INTO `log_info` VALUES ('102', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 21:27:00', '192.168.1.151');
INSERT INTO `log_info` VALUES ('103', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 22:04:50', '192.168.1.151');
INSERT INTO `log_info` VALUES ('104', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.22 22:07:00', '192.168.1.151');
INSERT INTO `log_info` VALUES ('105', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 12:45:37', '192.168.1.199');
INSERT INTO `log_info` VALUES ('106', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.23 14:56:05', '192.168.1.199');
INSERT INTO `log_info` VALUES ('107', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 15:26:26', '192.168.1.199');
INSERT INTO `log_info` VALUES ('108', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.23 15:27:13', '192.168.1.199');
INSERT INTO `log_info` VALUES ('109', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 15:38:40', '192.168.1.199');
INSERT INTO `log_info` VALUES ('110', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 16:06:47', '192.168.1.199');
INSERT INTO `log_info` VALUES ('111', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 16:06:47', '192.168.1.199');
INSERT INTO `log_info` VALUES ('112', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.23 16:52:46', '192.168.1.199');
INSERT INTO `log_info` VALUES ('113', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.24 01:13:31', '192.168.1.114');
INSERT INTO `log_info` VALUES ('114', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 01:14:17', '192.168.1.114');
INSERT INTO `log_info` VALUES ('115', 'xiaoming', '用户：xiaoming，删除用户操作被拒绝', '2019.05.24 01:15:58', '192.168.1.114');
INSERT INTO `log_info` VALUES ('116', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.24 01:16:11', '192.168.1.114');
INSERT INTO `log_info` VALUES ('117', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 01:40:35', '192.168.1.114');
INSERT INTO `log_info` VALUES ('118', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:26:16', '192.168.1.114');
INSERT INTO `log_info` VALUES ('119', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:26:56', '192.168.1.114');
INSERT INTO `log_info` VALUES ('120', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:28:11', '192.168.1.114');
INSERT INTO `log_info` VALUES ('121', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:28:44', '192.168.1.114');
INSERT INTO `log_info` VALUES ('122', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:44:51', '192.168.1.114');
INSERT INTO `log_info` VALUES ('123', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:54:34', '192.168.1.114');
INSERT INTO `log_info` VALUES ('124', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:55:26', '192.168.1.114');
INSERT INTO `log_info` VALUES ('125', 'xiaoming', '用户：xiaoming，登录系统操作', '2019.05.24 10:57:31', '192.168.1.114');
INSERT INTO `log_info` VALUES ('126', 'admin', '用户：admin，登录系统操作', '2019.05.24 12:57:42', '192.168.1.114');
INSERT INTO `log_info` VALUES ('127', 'admin', '用户：admin，退出系统', '2019.05.24 12:59:05', '192.168.1.114');
INSERT INTO `log_info` VALUES ('128', 'admin', '用户：admin，登录系统操作', '2019.05.24 13:03:49', '192.168.1.114');
INSERT INTO `log_info` VALUES ('129', 'admin', '用户：admin，登录系统操作', '2019.05.24 13:04:33', '192.168.1.114');
INSERT INTO `log_info` VALUES ('130', 'admin', '用户：admin，退出系统', '2019.05.24 13:05:35', '192.168.1.114');
INSERT INTO `log_info` VALUES ('131', 'xiaoming', '用户：xiaoming，退出系统', '2019.05.24 16:40:26', '192.168.1.114');
INSERT INTO `log_info` VALUES ('132', 'admin', '用户：admin，登录系统操作', '2019.05.24 17:16:38', '192.168.1.114');
INSERT INTO `log_info` VALUES ('133', 'admin', '用户：admin，退出系统', '2019.05.25 09:55:59', '192.168.1.199');
INSERT INTO `log_info` VALUES ('134', 'admin', '用户：admin，登录系统操作', '2019.05.25 09:56:13', '192.168.1.199');
INSERT INTO `log_info` VALUES ('135', 'admin', '用户：admin，登录系统操作', '2019.05.27 09:04:41', '192.168.1.199');
INSERT INTO `log_info` VALUES ('136', 'admin', '用户：admin，登录系统操作', '2019.05.27 09:28:11', '192.168.1.199');
INSERT INTO `log_info` VALUES ('137', 'admin', '用户：admin，登录系统操作', '2019.05.27 09:30:46', '192.168.1.199');
INSERT INTO `log_info` VALUES ('138', 'admin', '用户：admin，进行了添加设备操作', '2019.05.27 10:08:35', '192.168.1.199');
INSERT INTO `log_info` VALUES ('139', 'admin', '用户：admin，登录系统操作', '2019.05.27 10:57:15', '192.168.1.199');
INSERT INTO `log_info` VALUES ('140', 'admin', '用户：admin，登录系统操作', '2019.05.27 11:08:24', '192.168.1.199');
INSERT INTO `log_info` VALUES ('141', 'admin', '用户：admin，登录系统操作', '2019.05.27 14:44:37', '192.168.1.199');
INSERT INTO `log_info` VALUES ('142', 'admin', '用户：admin，登录系统操作', '2019.05.27 14:51:36', '192.168.1.199');
INSERT INTO `log_info` VALUES ('143', 'admin', '用户：admin，登录系统操作', '2019.05.27 14:57:49', '192.168.1.199');
INSERT INTO `log_info` VALUES ('144', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:13:53', '192.168.1.199');
INSERT INTO `log_info` VALUES ('145', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:22:41', '192.168.1.199');
INSERT INTO `log_info` VALUES ('146', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:26:13', '192.168.1.199');
INSERT INTO `log_info` VALUES ('147', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:29:14', '192.168.1.199');
INSERT INTO `log_info` VALUES ('148', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:33:14', '192.168.1.199');
INSERT INTO `log_info` VALUES ('149', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:47:02', '192.168.1.199');
INSERT INTO `log_info` VALUES ('150', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:55:54', '192.168.1.199');
INSERT INTO `log_info` VALUES ('151', 'admin', '用户：admin，登录系统操作', '2019.05.27 15:58:03', '192.168.1.199');
INSERT INTO `log_info` VALUES ('152', 'admin', '用户：admin，登录系统操作', '2019.05.27 16:01:50', '192.168.1.199');
INSERT INTO `log_info` VALUES ('153', 'admin', '用户：admin，登录系统操作', '2019.05.27 16:04:21', '192.168.1.199');
INSERT INTO `log_info` VALUES ('154', 'admin', '用户：admin，登录系统操作', '2019.05.27 16:15:41', '192.168.1.199');
INSERT INTO `log_info` VALUES ('155', 'admin', '用户：admin，进行了添加设备操作', '2019.05.27 16:26:38', '192.168.1.199');
INSERT INTO `log_info` VALUES ('156', 'admin', '用户：admin，进行了添加设备操作', '2019.05.27 16:35:21', '192.168.1.199');
INSERT INTO `log_info` VALUES ('157', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:02:57', '192.168.1.199');
INSERT INTO `log_info` VALUES ('158', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:09:50', '192.168.1.199');
INSERT INTO `log_info` VALUES ('159', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:10:05', '192.168.1.199');
INSERT INTO `log_info` VALUES ('160', 'admin', '用户：admin，退出系统', '2019.05.27 17:17:59', '192.168.1.199');
INSERT INTO `log_info` VALUES ('161', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:18:33', '192.168.1.199');
INSERT INTO `log_info` VALUES ('162', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:34:07', '192.168.1.199');
INSERT INTO `log_info` VALUES ('163', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:35:48', '192.168.1.199');
INSERT INTO `log_info` VALUES ('164', 'admin', '用户：admin，退出系统', '2019.05.27 17:35:51', '192.168.1.199');
INSERT INTO `log_info` VALUES ('165', 'admin', '用户：admin，登录系统操作', '2019.05.27 17:37:15', '192.168.1.199');
INSERT INTO `log_info` VALUES ('166', 'admin', '用户：admin，退出系统', '2019.05.27 18:51:00', '192.168.1.199');

-- ----------------------------
-- Table structure for `problem_info`
-- ----------------------------
DROP TABLE IF EXISTS `problem_info`;
CREATE TABLE `problem_info` (
  `equipment_id` varchar(50) NOT NULL,
  `fault_point` varchar(50) NOT NULL,
  `fault_tag` varchar(50) NOT NULL,
  `current_value` float(20,0) NOT NULL,
  `limit_value` varchar(100) NOT NULL,
  `fault_time` varchar(100) NOT NULL,
  PRIMARY KEY (`equipment_id`),
  CONSTRAINT `equipment_id` FOREIGN KEY (`equipment_id`) REFERENCES `equip_info` (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of problem_info
-- ----------------------------
INSERT INTO `problem_info` VALUES ('GRM231', '主轴转速', 'maxis_speed', '28028', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM350', '主轴转速', 'maxis_speed', '250', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM351', '主轴转速', 'maxis_speed', '360', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM352', '主轴转速', 'maxis_speed', '400', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM353', '主轴转速', 'maxis_speed', '500', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM354', '主轴转速', 'maxis_speed', '1234567', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM356', '主轴转速', 'maxis_speed', '2369877', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM357', '主轴转速', 'maxis_speed', '1323232', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM358', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM359', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM360', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM370', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM371', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM372', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM373', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM374', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM375', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM376', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');
INSERT INTO `problem_info` VALUES ('GRM377', '主轴转速', 'maxis_speed', '1362620', '1000-26000', '2019.05.24 11:31:07');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `guanli` varchar(100) NOT NULL,
  `cre_time` varchar(100) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `username` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '903248190@qq.com', 'admin', '18829343070', '超级管理员', '2019.04.22 00:15:56 ');
INSERT INTO `user` VALUES ('8', 'brzen', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('11', 'danny', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('5', 'feaker', '903248190@qq.com', 'feaker', 'qwewqewq', '普通管理员', '2019.04.25 16:20:02 ');
INSERT INTO `user` VALUES ('10', 'hanmeimei', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('7', 'jenny', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('10', 'lilei', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('3', 'lisa', 'aaaaaaaaaaaa', 'lisa', '15956874564', '普通管理员', '2019.04.25 16:20:55 ');
INSERT INTO `user` VALUES ('2', 'mayun', 'alibaba.cc', 'mayun', '18829343070', '超级管理员', '2019.04.23 12:15:32');
INSERT INTO `user` VALUES ('9', 'qingwa', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('12', 'superman', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('13', '侯老师', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('13', '张工', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('13', '李工', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55');
INSERT INTO `user` VALUES ('6', '马云', 'alibaba.com', 'moneymoney', '18829343070', '普通管理员', '2019.04.25 16:20:55 ');
