--11/07/2024

--IMPORT TABLE
--first create your desired database
--then create excel table save it as csv

--now according to this excel files table we have to  create our table in database also as follows we have created it.
create table simple(
	a INTEGER,
	b INTEGER,
	c INTEGER
);
select * from simple;
--shows blank table now lets import :-

--imported file by right clicking on testme->schmas-> tables-> simple
--right click on that  simple table and then select option import/export select import
-- thenn choose file and encoding as
--utf8 and enable header,select comma and theen single quote in options then click OK

select * from simple;
--table import completed we can see this in output now

--	EXPORTING CSV FILE
--select export
--right click on that  simple table and then select option import/export thenn choose file and encoding as
--utf8 and enable header,select comma and theen single quote in options then click OK