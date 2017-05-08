use MTL;
CREATE TABLE temp (kidID int(11),D dateTime, X int(11), Y int(11), Z int(11),pitch double, roll double, orientation double);
explain temp;
 load data local infile 'TEST.TXT' into table temp
 fields terminated by ','
 enclosed by '"'
 lines terminated by '\n';
select * from temp;
INSERT INTO data ( datetime,kidID,onData,sleep, xAccel, yAccel, zAccel, pitch,roll,orientation ) 
SELECT D, kidID, 1, 0, X, Y, Z, pitch, roll, orientation from temp;
drop table temp;



#kidID,TimeStamp,X,Y,Z
