show databases;
create database googleplay;
use googleplay;
CREATE TABLE gpdetails (`name` VARCHAR(500) NULL,`docid` VARCHAR(500) NULL, `href` VARCHAR(500) NULL, date timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP); 
CREATE TABLE apptable (`name` VARCHAR(500) NULL,`docid` VARCHAR(500) NULL, `href` VARCHAR(500) NULL, date timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) 

ENGINE = InnoDB;
select * from gpdetails;
drop table gpdetails;