
'A'
'1'
select FNAME, LNAME,ADDR,BDATE
FROM EMPLOYEE, DEPARTMENT


WHERE EMPLOYEE.DNO = DEPARTMENT.DNO AND DNAME = "Marketing"


WHERE DNO IN 
(SELECT DNUMBER
FROM DEPARTMENT
WHERE DNAME="Marketing")

FROM EMPLOYEE AS E INNER JOIN DEPARTMENT AS D ON E.DNO = D.DNO
WHERE DNAME="Marketing"
-------------------------------------
'2'
SELECT DNAME 
FROM DEPARTMENT
WHERE BUDGET > 5000
--------------------------------------
'3'
SELECT FNAME, LNAME 

FROM PROJECT as P, EMPLOYEE as E, WORKS_ON AS W
WHERE W.PNO = P.PNUMBER AND
 P.DNO = E.DNO AND
 HOURS > 10 AND PNAME = "PRODUCTX"
 AND P.DNO = 5

FROM ((WORKS_ON JOIN PROJECT ON PNUMBER=PNO)JOIN EMPLOYEE ON EMPLOYEE.DNO = PROJECT.DNO)
WHERE PNAME = "PRODUCTX" AND HOURS >10 AND DNO = 5

'B'
CREATE TABLE EMPOLYEE (ESSN INTEGER, FNAME VARCHAR(10), LNAME VARCHAR(10), BDATE DATE, ADDR VARCHAR(20), SAL INTEGER, DNO INTEGER)
PRIMARY KEY (ESSN)
FOREIGN KEY(DNO) REFERENCES DEPARTMENT

'C'
UPDATE EMPLOYEE
SET SALARY = SALARY+100
WHERE LNAME="Smith"

'D'
CREATE VIEW DEPT_EMP (NO_EMP) AS
SELECT COUNT(*), DNO
FROM EMPLOYEE
GROUP BY DNO

'2'
'A1'
SELECT STUD_NAME
FROM STUDENT AS S, ENROLLED AS E, COURSE AS C
WHERE S.STUD_NO=E.STUD_NO AND C.CNO=E.CNO AND C.CNAME="Introduction to DB" AND E.GRADE="A"

FROM ((STUDENT AS S JOIN ENROLLED AS E ON S.STUD_NO=E.STUD_NO)JOIN COURSE AS C ON C.CNO=E.CNO)
WHERE C.CNAME="Intorduction to DB" AND E.GRADE="A"

'A2'
SELECT CNAME
FROM COURSE AS C, DEPARTMENT AS D
WHERE D.DNO = C.DNO AND D.DNAME="Computer science"

FROM COURSE AS C JOIN DEPARTMENT AS D ON C.CNO=D.DNO
WHERE D.DNAME="Computer science"

'B'
CREATE TABLE ENROLLED 
(
    STUD_NO CHAR(5),
    CNO CHAR(6),
    GRADE CHAR(1)

PRIMARY KEY (STUD_NO, CNO)
FOREIGN KEY (CNO) REFERENCES COURSE 
FOREIGN KEY (STUD_NO) REFERENCES STUDENT
);

'C'
CREATE VIEW DEPT_STUD AS 
SELECT S.DNO, COUNT(*) AS NO_STUD
FROM STUDENT AS S
GROUP BY DNO
---------------------------------------
'3'
'A'
SELECT DNAME, COUNT(SSN) AS NO_EMPS
FROM EMPOLYEE, DEPARTMENT
WHERE DNO = DNUMBER
GROUP BY DNAME
HAVING AVG(SALARY) > 30000

'B'
SELECT DNO, COUNT(SSN) AS NO_MALES
FROM EMPLOYEE
WHERE SEX = "M"
GROUP BY DNO

'C'
SELECT FNAME, LNAME, 1.1*SALARY
FROM EMPLOYEE, WORKS_ON, PROJECT
WHERE SSN=ESSN AND PNO=PNUMBER AND PNAME="ProductX"

FROM ((EMPLOYEE JOIN WORKS_ON ON SSN=ESSN ) JOIN PROJECT ON PNO=PNUMBER)
WHERE PNAME="ProductX"
-----------------------------------
'4'
'B'

SELECT CourseName
FROM COURSE AS C, SECTION AS S
WHERE C.CourseNo = S.CourseNo AND INSTRUCTOR = "Professor King" AND Year IN (1998,1999)

'C'
SELECT S.SectionID, CourseNo, Semester, Year, COUNT(StudentNumber)
FROM SECTION AS S, GRADE_REPORT AS G 
WHERE S.SectionID = G.SectionID AND S.Instructor= "King"
GROUP BY SectionID

'D'
SELECT Name, CourseName, CourseNo, CreditHours,Semester, Year, Grade 
FROM STUDENT AS ST, COURSE AS C, GRADE_REPORT AS G, SECTION AS S
WHERE ST.StudentNumber=G.StudentNumber AND G.SectionID=S.SectionID AND S.CourseNo=C.CourseNo 
AND ST.Class = 5 AND ST.Major = "CS"
GROUP BY Name
------------------------------
'5'
'A'
INSERT INTO STUDENT VALUES(
"Johnson",
25,
1,
"MATH"
   )

'B'
UPDATE STUDENT 
SET Class = 2
WHERE Name = "Smith"

'C'
INSERT INTO COURSE
VALUES("Knowledge Engineering", "CS4390", 3, "CS")

'D'
DELETE FROM STUDENT 
WHERE Name = "Smith" AND StudentNumber=17
