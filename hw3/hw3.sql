CREATE TABLE REVENUE_ANALYSIS
(
  ACTIVITY_DATE   DATE NOT NULL,
  MEMBER_ID       INTEGER NOT NULL,
  GAME_ID         SMALLINT NOT NULL,
  WAGER_AMOUNT    REAL NOT NULL,
  NUMBER_OF_WAGERS INTEGER NOT NULL,
  WIN_AMOUNT      REAL NOT NULL,
  ACTIVITY_YEAR_MONTH INTEGER NOT NULL,
  BANK_TYPE_ID    SMALLINT DEFAULT 0 NOT NULL
)
TABLESPACE TS_LAB;

SELECT 
ROW_NUMBER() OVER(ORDER BY table1.member_id) AS position_row,
table1.*
FROM
(
  SELECT DISTINCT
  rev.member_id,
  ltrim(TO_CHAR(rev.activity_date,'yyyy-mm'),'0') AS act_year_month,
  SUM(rev.number_of_wagers) OVER(PARTITION BY EXTRACT(MONTH FROM rev.activity_date),rev.member_id ORDER BY rev.member_id) AS number_of_wagers
  FROM REVENUE_ANALYSIS rev
  ORDER BY rev.member_id
) table1

SELECT DISTINCT
rev.member_id,
ltrim(TO_CHAR(rev.activity_date,'yyyy-mm'),'0') AS act_year_month,
SUM(rev.number_of_wagers) OVER(PARTITION BY EXTRACT(MONTH FROM rev.activity_date),rev.member_id ORDER BY rev.member_id) AS sum,
SUM(rev.number_of_wagers) OVER() AS sum_n_o_w
FROM REVENUE_ANALYSIS rev
ORDER BY rev.member_id

