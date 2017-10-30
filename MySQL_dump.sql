CREATE DATABASE  IF NOT EXISTS `db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `db`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Administration'),(2,'Businessmen'),(3,'Students'),(4,'tourists');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add map_item',7,'add_map_item'),(20,'Can change map_item',7,'change_map_item'),(21,'Can delete map_item',7,'delete_map_item');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$zF2A9ZPIPMiz$ZepOuY+c/BvYGtQQ9Eims3qoXPrhA047F8YxHPg/8Yo=','2017-09-04 05:37:40.407260',1,'admin','','','admin@smartcity.com',1,1,'2017-09-01 10:54:16.000000'),(2,'pbkdf2_sha256$36000$ZInmtS8GJ9za$hUOl38smRDfgMw0YS7zCwBBbb1QlJBjL3TPLBpTeYZc=',NULL,0,'businessman1','','','',0,1,'2017-09-01 10:56:59.000000'),(3,'pbkdf2_sha256$36000$Ijy4ZidNtJoe$AMyKzwQp1L0JbsdZQ2nvRkBYNQ4AXmGtv36NY03TFZo=',NULL,0,'student1','','','',0,1,'2017-09-01 10:57:22.000000'),(4,'pbkdf2_sha256$36000$dN0B7tI6BUsw$sloicUZiR1XwmzpQzS99iYxk2Zt35UleYr7wESTkUUE=',NULL,0,'tourist1','','','',0,1,'2017-09-01 10:57:55.000000'),(5,'pbkdf2_sha256$36000$rbGYtjnODQOT$zwycF7XNO5nUWd85xfyF7UMZ6NmhZbW4f/jD2IXXiaw=','2017-10-30 01:47:58.750336',0,'Thisisatest123','','','',1,1,'2017-10-02 10:26:14.566484'),(6,'pbkdf2_sha256$36000$TSvlGMIawXUP$5FoPPK9/GsmrguSzYHP7ZdI+T+jm6KsvGsyigq9ynAM=','2017-10-04 14:03:51.707597',0,'Thisisatest1234','','','',0,1,'2017-10-02 10:27:13.107537'),(7,'pbkdf2_sha256$36000$chGcu0TM0OP8$Yo7jJoa/7yb0FYvEOHuqJtfZR/PptlRqOjSc147+wsQ=','2017-10-02 12:30:32.109372',1,'danielfield','','','',1,1,'2017-10-02 12:28:27.529412'),(8,'pbkdf2_sha256$36000$9hBcttk3VQu6$Vq3DMOVc86R7RhY+PTkh0s6rrzsEvC2dAfR3GcdHKoM=','2017-10-02 12:41:40.907011',0,'Testuser123','','','',0,1,'2017-10-02 12:41:40.552864'),(9,'pbkdf2_sha256$36000$AAV3dyjNSNrj$YCwOn6syWNRnZanXFE1rNg7kcCt8FjhaMHsJVEJEvys=','2017-10-04 06:32:02.505491',0,'Onetwothree','','','',0,1,'2017-10-04 06:32:02.061048'),(10,'pbkdf2_sha256$36000$t5p6NejcWQd9$CKKy0anUgYT9H8L3V6n6AZDufX5RiwG20WEtbq6rIWg=','2017-10-04 12:22:32.958853',0,'Just_a_test1','','','',0,1,'2017-10-04 12:22:32.348757'),(11,'pbkdf2_sha256$36000$tIvfsMzSDTBd$nbWXUodvn6LqpGUHHYtsO9KZMGdzVZjQKEnKude9a+Q=','2017-10-04 12:25:31.751190',0,'adfcsdfdff','','','',0,1,'2017-10-04 12:25:31.300541'),(12,'pbkdf2_sha256$36000$w3phUkezaWsG$yiI1RbjB1O8XeI+qNmhRNTkkvetEx3UOKEk9MAvnk2w=','2017-10-30 01:31:46.921987',1,'Daniel','','','no@no.com',1,1,'2017-10-30 01:31:38.981442'),(13,'pbkdf2_sha256$36000$w74vDFjuqYJM$wzDruaELP4cNdGCAuhhjmDj2XAvQeNkoB3GoPZRUT+8=','2017-10-30 06:54:53.959130',1,'dev','','','',1,1,'2017-10-30 01:53:42.919770');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1),(2,2,2),(3,5,1),(4,6,3),(5,7,1),(6,13,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-09-01 10:56:59.301287','2','businessman1',1,'[{\"added\": {}}]',4,1),(2,'2017-09-01 10:57:22.192064','3','student1',1,'[{\"added\": {}}]',4,1),(3,'2017-09-01 10:57:55.983659','4','tourist1',1,'[{\"added\": {}}]',4,1),(4,'2017-09-01 11:01:07.634819','1','Administration',1,'[{\"added\": {}}]',3,1),(5,'2017-09-01 11:01:50.292540','2','Businessmen',1,'[{\"added\": {}}]',3,1),(6,'2017-09-01 11:02:03.764485','3','Students',1,'[{\"added\": {}}]',3,1),(7,'2017-09-01 11:02:13.350483','4','tourists',1,'[{\"added\": {}}]',3,1),(8,'2017-09-01 11:02:44.949921','1','admin',2,'[]',4,1),(9,'2017-09-01 11:03:26.057231','2','businessman1',2,'[]',4,1),(10,'2017-09-01 11:03:41.717137','3','student1',2,'[]',4,1),(11,'2017-09-01 11:03:52.740622','4','tourist1',2,'[]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'smart_city_app','map_item');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-08-30 08:12:02.915975'),(2,'auth','0001_initial','2017-08-30 08:12:03.236489'),(3,'admin','0001_initial','2017-08-30 08:12:03.540361'),(4,'admin','0002_logentry_remove_auto_add','2017-08-30 08:12:03.870708'),(5,'contenttypes','0002_remove_content_type_name','2017-08-30 08:12:04.207154'),(6,'auth','0002_alter_permission_name_max_length','2017-08-30 08:12:04.503484'),(7,'auth','0003_alter_user_email_max_length','2017-08-30 08:12:04.823862'),(8,'auth','0004_alter_user_username_opts','2017-08-30 08:12:05.134143'),(9,'auth','0005_alter_user_last_login_null','2017-08-30 08:12:05.458713'),(10,'auth','0006_require_contenttypes_0002','2017-08-30 08:12:05.634845'),(11,'auth','0007_alter_validators_add_error_messages','2017-08-30 08:12:05.880302'),(12,'auth','0008_alter_user_username_max_length','2017-08-30 08:12:06.166560'),(13,'sessions','0001_initial','2017-08-30 08:12:06.436691'),(14,'smart_city_app','0001_initial','2017-09-03 09:22:35.921279'),(15,'smart_city_app','0002_auto_20170903_1931','2017-09-03 09:31:33.919822'),(16,'smart_city_app','0003_auto_20171002_2108','2017-10-02 11:09:40.167379');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8a79q674hhh2lb13g1tbif0hd6wqp7dy','NmZmMzJjOTYxMTk1MDRkNWFhYWI5NzNlNzBmMDg2YTU0NDAwM2FjNjp7InF1ZXJ5IjoicSJ9','2017-10-16 10:26:14.925788'),('b162wese3nc18ikmyhlqhjb8iqnt4152','OGYzNmJiNTY2NTViMzQ2YTFkODQ4ZWFjNWUwYzMzYzBhOGI0Y2YxNzp7InF1ZXJ5IjoidW5zdyJ9','2017-11-12 18:00:21.409360'),('cxi5l2nuhioa6j9vxsxbii7atxkaym7z','MmM2MTc2ZjdhMzYxMDAzYjlhNTY1NTI3NzA2OTk5OGJjOGNkOWY4OTp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGU5ZjA1ZGEwYjc1ZmFjNWU4NzRiOWM5YTE5ZjRkYWNmN2Y2ZjAyYyJ9','2017-11-13 01:54:41.278384'),('mj76fob45za0duvv8uiidgpqh8ugr42l','ZTFiNTYyNTBlZTEyMDQxYzA2YWNiM2Y1NjMzYWZmNTQ1MzRiMDUzMTp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGI1MDAxYjcxY2RhMWExMmI4MDM0ZTAyZTQ5NDFlODE4NjUzNGI1NSIsInF1ZXJ5IjoicSJ9','2017-11-13 11:32:48.285139'),('npc6h4dn2fug6ktv3xrhxqpwojodk48n','YWE1ZjUzYjNiNGVlOGY2NzE1OWRiMmEyZTMwNzRlYzE0OGU2MWIzMjp7InF1ZXJ5IjoicXV0In0=','2017-10-20 11:40:18.005085'),('sh1wmdcm3v7gi7nvgcoa8ybauz23f6nw','MDFhNzNiY2JkZGVmMDM1OWFiNjk2NTVlMjc1YWEyZTA5Y2VhZmM5MTp7InF1ZXJ5IjoidW5pdmVyc2l0eSIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4OTU3ZTJiZTZkMjc4MWZhYTY5ZDRlY2I3MzhkMDJkMzdhYWQ1MDk0In0=','2017-10-18 15:04:35.740943'),('slg628facvmcf2tyr781vgixb3diubkf','NmZmMzJjOTYxMTk1MDRkNWFhYWI5NzNlNzBmMDg2YTU0NDAwM2FjNjp7InF1ZXJ5IjoicSJ9','2017-09-18 06:57:34.633722');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `get_places`
--

DROP TABLE IF EXISTS `get_places`;
/*!50001 DROP VIEW IF EXISTS `get_places`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `get_places` AS SELECT 
 1 AS `map_item_id`,
 1 AS `map_item_name`,
 1 AS `map_item_address`,
 1 AS `map_item_industry_type`,
 1 AS `map_item_department`,
 1 AS `map_item_email`,
 1 AS `name`,
 1 AS `map_item_phone`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `smart_city_app_map_item`
--

DROP TABLE IF EXISTS `smart_city_app_map_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smart_city_app_map_item` (
  `map_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `map_item_name` varchar(64) NOT NULL,
  `map_item_address` varchar(256) NOT NULL,
  `map_item_industry_type` varchar(256) NOT NULL,
  `map_item_department` varchar(256) NOT NULL,
  `map_item_email` varchar(256) NOT NULL,
  `map_item_type_id` int(11) NOT NULL,
  `map_item_phone` varchar(32) NOT NULL,
  PRIMARY KEY (`map_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smart_city_app_map_item`
--

LOCK TABLES `smart_city_app_map_item` WRITE;
/*!40000 ALTER TABLE `smart_city_app_map_item` DISABLE KEYS */;
INSERT INTO `smart_city_app_map_item` VALUES (1,'UQ','Who cares? Somewhere in Brisbane.','sdfnksjfn','jnkjnjkgbkhb','cdsgsfdlmk',3,'618752455'),(2,'made up place','123453csdcrwsvioskfmbrisbane','haha','no','k',3,'123'),(3,'QUT','123 fake st, Brisbane, QLD','test','test1','test2',3,'143954648');
/*!40000 ALTER TABLE `smart_city_app_map_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'db'
--

--
-- Dumping routines for database 'db'
--

--
-- Final view structure for view `get_places`
--

/*!50001 DROP VIEW IF EXISTS `get_places`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `get_places` AS select `smart_city_app_map_item`.`map_item_id` AS `map_item_id`,`smart_city_app_map_item`.`map_item_name` AS `map_item_name`,`smart_city_app_map_item`.`map_item_address` AS `map_item_address`,`smart_city_app_map_item`.`map_item_industry_type` AS `map_item_industry_type`,`smart_city_app_map_item`.`map_item_department` AS `map_item_department`,`smart_city_app_map_item`.`map_item_email` AS `map_item_email`,`auth_group`.`name` AS `name`,`smart_city_app_map_item`.`map_item_phone` AS `map_item_phone` from (`smart_city_app_map_item` join `auth_group` on((`smart_city_app_map_item`.`map_item_type_id` = `auth_group`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-30 22:21:29
