/*CREATE TABLE calendar
(
calendar_date date ,
calendar_year integer ,
calendar_month_number integer ,
calendar_month_name character varying(100)
calendar_day_of_month integer ,
calendar_day_of_week integer ,
calendar_day_name character varying(100),
calendar_year_month integer
)
TABLESPACE ts_lab;

CREATE TABLE revenue_analysis
(
activity_date date,
member_id integer,
game_id smallint,
wager_amount real,
number_of_wagers integer,
win_amount real,
activity_year_month integer,
bank_type_id smallint
)
TABLESPACE ts_lab;

SELECT table3.*,
ROW_NUMBER() OVER(PARTITION BY table3.MEMBER_LIFECYCLE_STATUS ORDER BY table3.CALENDAR_YEAR_MONTH) - 1 AS III
FROM 
(
SELECT table2.*
FROM
(*/
SELECT 
table1.*, 
  CASE
    WHEN rev.activity_year_month IS NULL THEN 'Lapsed'
    ELSE 'Active'
  END AS MEMBER_LIFECYCLE_STATUS
FROM
(
SELECT DISTINCT
coalesce(rev.member_id, 1001) AS member_id,
cal.calendar_year_month
FROM calendar cal
LEFT JOIN revenue_analysis rev ON cal.calendar_year_month=rev.activity_year_month
WHERE rev.member_id=1001 OR rev.member_id IS NULL

UNION 

SELECT DISTINCT
coalesce(rev.member_id, 1002) member_id,
cal.calendar_year_month
FROM calendar cal
LEFT JOIN revenue_analysis rev ON cal.calendar_year_month=rev.activity_year_month
WHERE rev.member_id=1002 OR rev.member_id IS NULL

UNION 

SELECT DISTINCT
coalesce(rev.member_id, 1003) member_id,
cal.calendar_year_month
FROM calendar cal
LEFT JOIN revenue_analysis rev ON cal.calendar_year_month=rev.activity_year_month
WHERE rev.member_id=1003 OR rev.member_id IS NULL

ORDER BY member_id, calendar_year_month
) table1
LEFT JOIN revenue_analysis rev ON table1.calendar_year_month=rev.activity_year_month AND table1.member_id=rev.member_id
) table2
ORDER BY member_id, calendar_year_month
) table3






