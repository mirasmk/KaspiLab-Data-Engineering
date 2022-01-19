CREATE OR REPLACE FUNCTION hw6(
       numb INT
)
RETURNS VARCHAR(20)
AS
BEGIN
    numb = Replicate('M', numb/1000)  
            + REPLACE(REPLACE(REPLACE(  
                  Replicate('C', numb%1000/100),  
                  Replicate('C', 9), 'CM'),  
                  Replicate('C', 5), 'D'),  
                  Replicate('C', 4), 'CD')  
             + REPLACE(REPLACE(REPLACE(  
                  Replicate('X', numb%100 / 10),  
                  Replicate('X', 9),'XC'),  
                  Replicate('X', 5), 'L'),  
                  Replicate('X', 4), 'XL')  
             + REPLACE(REPLACE(REPLACE(  
                  Replicate('I', numb%10),  
                  Replicate('I', 9),'IX'),  
                  Replicate('I', 5), 'V'),  
                  Replicate('I', 4),'IV');
    RETURN numb;
END;

SELECT hw6(11) FROM DUAL
SELECT REPLICATE('SQL Tutorial', 5) FROM DUAL;

--2
CREATE TABLE hw6_1_table(
       MEMBER_ID INT,
       CALENDAR_YEAR_MONTH INT,
       MEMBER_LIFECYCLE_STATUS VARCHAR(20),
       LAPSED_MONTH INT
);

CREATE OR REPLACE PROCEDURE hw6_1(pNAME IN VARCHAR)
CURSOR it IS
              SELECT table2.*,
              CASE
              WHEN table2.MEMBER_LIFECYCLE_STATUS='Lapsed' THEN ROW_NUMBER() OVER(PARTITION BY
              table2.MEMBER_LIFECYCLE_STATUS  ORDER BY table2.member_id)
              ELSE 0
              END LAPSED_MONTH
              FROM
              (
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

              LEFT JOIN revenue_analysis rev ON table1.calendar_year_month=rev.activity_year_month AND
              table1.member_id=rev.member_id
              ) table2
              ORDER BY member_id, calendar_year_month
   new_table hw6_1_table%rowtype
IS
BEGIN
  OPEN it;
  LOOP
  FETCH it INTO new_table;
  EXIT WHEN it%NOTFOUND;
  INSERT INTO hw6_1_table VALUES (new_table.MEMBER_ID,
                                  new_table.CALENDAR_YEAR_MONTH,
                                  new_table.MEMBER_LIFECYCLE_STATUS,
                                  SELECT hw6(new_table.LAPSED_MONTH) FROM DUAL); 
  END LOOP;
  CLOSE it;
END;

