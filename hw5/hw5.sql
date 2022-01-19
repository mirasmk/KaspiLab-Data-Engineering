SELECT * FROM ANOTHER_CALENDAR
SELECT * FROM cal_new

--1

CREATE TABLE cal_new(
       calendar_date date,
       calendar_day_name varchar2(100)
);

DECLARE 
   new_cal cal_new%rowtype; 
BEGIN 
   Insert into cal_new Select calendar.calendar_date, calendar.calendar_day_name from calendar;
END;

DECLARE
   TYPE new_cal IS RECORD(
        calendar_date calendar.calendar_date%TYPE,
        calendar_day_name calendar.calendar_day_name%TYPE
   );
   perem new_cal;
BEGIN
   INSERT INTO cal_new(calendar_date, calendar_day_name)
   SELECT cal.calendar_date, cal.calendar_day_name
   FROM calendar cal ;
END;

--2

CREATE TABLE another_calendar(
       calendar_date date,
       CALENDAR_YEAR NUMBER(22),
       CALENDAR_MONTH_NUMBER NUMBER(22),
       CALENDAR_MONTH_NAME varchar2(100),
       CALENDAR_DAY_OF_MONTH NUMBER(22),
       CALENDAR_DAY_OF_WEEK NUMBER(22),
       calendar_day_name varchar2(100),
       CALENDAR_YEAR_MONTH NUMBER (22)
);

DECLARE 
   TYPE new_cal IS TABLE OF another_calendar%rowtype; 
BEGIN 
   Insert into another_calendar 
          SELECT 
          t1.calendar_date,
          t1.CALENDAR_YEAR,
          t1.CALENDAR_MONTH_NUMBER,
          t1.CALENDAR_MONTH_NAME,
          t1.CALENDAR_DAY_OF_MONTH,
          t1.CALENDAR_DAY_OF_WEEK,
          t1.calendar_day_name,
          t1.CALENDAR_YEAR_MONTH
          FROM 
          (SELECT
          case WHEN cal.CALENDAR_DAY_NAME = 'Friday' then ROW_NUMBER() OVER(ORDER BY cal.calendar_day_name, cal.calendar_date)
            else 109
            END AS RO,
          cal.* 
          FROM calendar cal where cal.calendar_year < 2017) t1
          WHERE mod(t1.ro, 2) != 0
          ORDER BY t1.CALENDAR_DATE;
END;

SELECT * FROM ANOTHER_CALENDAR

DECLARE 
   CURSOR it IS
          SELECT 
          t1.calendar_date,
          t1.CALENDAR_YEAR,
          t1.CALENDAR_MONTH_NUMBER,
          t1.CALENDAR_MONTH_NAME,
          t1.CALENDAR_DAY_OF_MONTH,
          t1.CALENDAR_DAY_OF_WEEK,
          t1.calendar_day_name,
          t1.CALENDAR_YEAR_MONTH
          FROM 
          (SELECT
          case WHEN cal.CALENDAR_DAY_NAME = 'Friday' then ROW_NUMBER() OVER(ORDER BY cal.calendar_day_name, cal.calendar_date)
            else 109
            END AS RO,
          cal.* 
          FROM calendar cal where cal.calendar_year < 2017) t1
          WHERE mod(t1.ro, 2) != 0
          ORDER BY t1.CALENDAR_DATE;
   new_cal another_calendar%rowtype;
BEGIN
  OPEN it;
  LOOP
  FETCH it INTO new_cal;
  EXIT WHEN it%NOTFOUND;
  INSERT INTO another_calendar VALUES (new_cal.calendar_date,
                                       new_cal.CALENDAR_YEAR,
                                       new_cal.CALENDAR_MONTH_NUMBER,
                                       new_cal.CALENDAR_MONTH_NAME,
                                       new_cal.CALENDAR_DAY_OF_MONTH,
                                       new_cal.CALENDAR_DAY_OF_WEEK,
                                       new_cal.calendar_day_name,
                                       new_cal.CALENDAR_YEAR_MONTH); 
  END LOOP;
  CLOSE it;
END;

--3

DECLARE
   CURSOR it IS (SELECT DISTINCT cal.calendar_month_name FROM calendar cal UNION SELECT DISTINCT cal.calendar_day_name FROM calendar cal);
   TYPE new_cal IS VARRAY(100) OF NUMBER;
BEGIN
  DBMS_OUTPUT.ENABLE;
  OPEN it;
  LOOP
  FETCH it INTO new_cal;
  EXIT WHEN it%NOTFOUND;
  dbms_output.put_line(it.CALENDAR_MONTH_NAME);
  END LOOP; 
END;
