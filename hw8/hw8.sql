create table df1(
video_id varchar2(100) NOT NULL,
trending_date varchar2(100) NOT NULL,
title varchar2(500) NOT NULL,
channel_title varchar2(100) NOT NULL,
category_id number(30) NOT NULL,
publish_time varchar2(100) NOT NULL,
tags clob NOT NULL,
views number(30) NOT NULL,
likes number(30) NOT NULL,
dislikes number(30) NOT NULL,
comment_count number(30) NOT NULL,
thumbnail_link clob NOT NULL,
comments_disabled varchar2(30) NOT NULL,
ratings_disabled varchar2(30) NOT NULL,
video_error_or_removed varchar2(30) NOT NULL,
description clob NOT NULL)
--drop table df1
select * from df1
