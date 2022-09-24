Select * from Student --ѧ����Ϣ
Select * from Author -- ������Ϣ
Select * from Press  --��������Ϣ
Select * from Book  --ͼ����Ϣ
Select * from BookType --ͼ�����
Select * from BorrowBook -- ������Ϣ

--===================SQL��ѯ��������=======================
-- ��ѯ������Ϊ����������ѧ�š��ֻ�����������ַ 
Select SNO As 'ѧ��', MobileNO As '�ֻ�����',StuEMail As '�����ַ'
from Student
--Where SName = '����'
where SName in ('����')

-- ��ѯ���������ǡ���������ѧ����������Ϣ
Select SNO,Sname, Sage ,Sex, MobileNo,StuEmail
from Student
--where SName != '����'
--Where SName <> '����'
Where SName Not in ('����')

-- ��ѯ��ѧ���������20��30���ѧ��ѧ�ź�����
Select SNO As 'ѧ��', SName As '����'
from Student 
--Where ( Sage >=20 ) And ( Sage <= 30)
Where Sage Between 20 And 30  -- Between--and ---ĳһ����Χ

-- ��ѯ��Щѧ��û����д������ ����Ϣ
Select SNo,Sname
from Student 
where Sage is null   -- Nullһ��������������������ӣ���is ��not is

-- ��ѯ��������������Alice������Bob����ѧ�ţ�����
Select SNo As 'ѧ��', Sage As '����'
from Student 
--where SName ='����' OR SName = 'Alice' OR  SName = 'Bob'
Where SName in ('����','Alice','Bob')

-- ===================================
-- ��ѯ����Щͼ�鱻���
/*
Select distinct Bookid from BorrowBook
Select COUNT(distinct bookId) As '����ͼ����' from BorrowBook
*/

-- ��ѯ��С��20����ߴ���25 ��Ů��
Select * from Student where (Sage<20 OR Sage>30) And Sex ='Ů'

-- ����
Select * from Student Where SName between '����' and '����'
Select * from Student order by SName

================================================
--1. ��ѯ���ֻ�����133����134��ͷ��������2λΪ����2Ҳ����4��ѧ��ѧ�ź�����
Select * 
from Student 
where MobileNO Like '[1][3][34]%[^24]_'

-- ģ����ѯ����������ȷ ---��Like
-- ������Ҫ��ͨ��� �� % --����ƥ��0-n��������ַ���
--                                 _  --->   (ƥ������1���ַ�)

--2. ��Student�����������������������һ����Ů����������ǰ�� --- Order by   ASC/ DESC
Select * 
from Student 
Order by Sage ASC, Sex DESC

--3.  ��ѯ����������ѧ����ѧ�ź�����
-- ����д��01��
Select * from Student  where Sage = MAX(Sage)
-- ����д��02��
Select  Top 1 * from Student  Order by Sage DESC
--��ȷ������ 
Select * from Student 
Where Sage = (
	--�������������
	Select MAX(Sage) from Student 
)


-- =============== �ۺϺ���===============
-- ��ѯ��������ƽ������
Select AVG(sage) As 'ƽ������'
from Student
where Sex ='��'

-- ��ѯ���ж���λѧ������
Select  count( distinct sno) As '����ѧ������' from BorrowBook

-- ��ѯ����������ͼ���ܹ��ж��ٱ���
Select  SUM(BookIncoming) As '�������ͼ������'
from Book 
where BookTypeID= 
(
	Select ID from BookType Where TypeName='�����'
)

--==================�����ѯ ===============
-- ͳ�Ƴ���Ů��������
Select Sex As '�Ա�', COUNT(*) As "����", AVG(Sage) As 'ƽ������',sum(sage) As '�����'
from Student 
group by sex

-- ͳ�Ƴ�ÿһ�����е���ߵļ۸�
Select  BookTypeID As 'ͼ�������', MAX(BookPrice) As '��߼۸�'
from Book
Group by  BookTypeID 


-- =============�����ѯ�Ľ���===========
-- ͳ�Ƴ�������25�����ϵ���Ů������      (����ǰ��ɸ�����ݣ� Where)
Select Sex, COUNT(*) As '����'
from Student 
Where Sage >=25
Group by Sex

-- ͳ�Ƴ�����ĳ���3����ͼ����      (������ɸ�����ݣ� Having)
Select  BookID, COUNT(*) As '�������'
from BorrowBook
Group by BookId
Having COUNT(*) >= 2
Order By  COUNT(*) DESC

-- ��ѯ����������Ǳ����Id
Select  BookID, COUNT(*) As '�������'
from BorrowBook
Group by BookId
Having COUNT(*) = 
(
	Select   TOP 1   COUNT(*) 
	from BorrowBook
	Group by BookId
	order by COUNT(*) DESC
)

-- ============ ����Ķ��ֶ� ===============
-- ͳ�Ƴ�һ�·���Щ�������Щ��Ʒ���۵���1000��, ���յ�������
Select  PArea As '����', PName As '����', SUM(PSaleNo) As '������'
from SalesTable 
Where PMonth= 'һ��'
Group by PArea, PName 
Having  SUM(PSaleNo) < 1000
Order by SUM(PSaleNo) DESC 



-- ===============Ƕ�ײ�ѯ===================
-- ��ѯ������������Щ�飿
���� : student  --(sno)- > BorrowBook ---(bookid)--> Book(���)
Select BookName
from Book
Where BookID  In  
(
	Select  BookId
	from BorrowBook 
	where SNO = 
	(
		Select  sno
		from Student 
		where SName = '����'
	)
)

---��ѯ����������Ǳ�������ߣ�
-- ����:   BorrowBook  --(BookId)-> Book  ---(AuthorId)--> Author 
Select AuthorID, AuthorName
From Author 
where AuthorId In
(
	Select BookAuthor
	from Book 
	Where BookID IN
	(
		Select BookID
		From BorrowBook 
		Group By BookId
		Having COUNT(*) = 
		(
			Select  Top  1 COUNT(*)
			from BorrowBook
			Group By BookID 
			Order By COUNT(*) DESC 
		)
	)
)

-- ===============Ƕ�ײ�ѯ�����ӹؼ���:============
/*
 =��in ��any��some��all�� exists
1. ����Ӳ�ѯȷ����һ��ֵ������ʹ�� = ���� in ����
    ����Ӳ�ѯ�Ƕ��ֵ����Ҫ��  in ����
2. in �� = any , = some һ�� 
3. any ����һ��������  all�������еĲ����� 
4. in --- �ж��Ƿ�����ڼ���    exists-- �Ƿ��н��
 
*/

-- ���� ��ѯ��������Ů�����䶼�������

Select Sno,Sname,sage
from Student 
where Sex = '��' and  Sage > all
(
	Select sage
	from Student
	where Sex='Ů' and Sage is not null
)


-- ���� ��ѯ��������һ��Ů�����䶼�������
Select Sno,Sname,sage
from Student 
where Sex = '��' and  Sage > any
(
	Select sage
	from Student
	where Sex='Ů' and Sage is not null
)


-- ���󣺲�ѯ����Щ��û�����
-- ����01 ��in 
Select Sno,Sname 
from Student 
where SNO not in 
(
	Select distinct SNO 
	from BorrowBook
)
---����02��exists
Select sno ,Sname 
from Student As T1
where not exists 
(	
	Select Bookid
	from BorrowBook As T2
	where T1.SNO = T2.SNO
)

-- ============== ��ʶ���Ӳ�ѯ ============== 
-- ���Ӳ�ѯ�� �����ű�(��������)����ĳ�������������ӳ�һ�Ŵ���ڴ����ִ�в�ѯ

-- ��ѯ������������Щ��? 
����: Student -- ���� 
Ŀ��: Book --> BookName

Student -->BorrowBook --> Book 

Select BookName  from Student As T1 
Inner Join BorrowBook As T2 on T1.SNO = T2.SNO 
Inner Join Book As T3 on T2.BookID = T3.BookID
Where SName = '����'

--���Ӻ�Ĵ��Ϊ: ����ѧ����������е�ͼ��ı�

-- ============== ��������Ӻ������� =============
Create Table Table1
(
	SNo int ,
	SName varchar(100)
)
Insert Into Table1 Values(1, '����')
Insert Into Table1 Values(2, '����')
Insert Into Table1 Values(3, '����')

Create Table Table2
(
	SNo int ,
	Result  int,
)
Insert Into Table2 Values(1, 86)
Insert Into Table2 Values(2, 91)
Insert Into Table2 Values(4, 78)

-- ������:  ��������������������,������������ʾ�ڴ����,�������ֱ������
Select * from Table1 
Select * from Table2
Select * from Table1 Inner Join Table2 on Table1.SNo = Table2.SNo

-- ��������: ��left�ؼ�����ߵı�λ�������������������ұߵı���ƥ�����ݣ�
-- �����ƥ���ϣ�ֱ��չʾ��ƥ�䲻�ϣ�����Null��䣡
Select * from Table1 
Select * from Table2
Select * from Table1 Left Outer Join  Table2 on Table1.SNo = Table2.SNo

-- ��������
Select * from Table1 
Select * from Table2
Select * from Table1 Right  Outer Join  Table2 on Table1.SNo = Table2.SNo

-- ȫ������
Select * from Table1 
Select * from Table2
Select * from Table1 Full  Outer Join  Table2 on Table1.SNo = Table2.SNo

--  ========�����ӵİ������� =========
-- ��ʾ����ѯ����������ͼ������Щ��
-- SQL92��׼��SQL92��׼��ֻ�������ӣ�
Select BookName As '��������ͼ��'
from BookType , Book  
Where BookType.ID = Book.BookTypeID And TypeName = '�����'

-- SQL99��׼��SQL99��׼��ֻ�������ӡ������ӡ��������ӡ������ӡ�������
Select  BookName from BookType  
Inner Join Book on BookType.ID = Book.BookTypeID
Where TypeName = '�����'


--  ��ʾ����ѯ��Ů������ ��Щ��
Select  Distinct BookName As 'Ů�������' from Student As T1 
Inner Join BorrowBook As T2 on T1.SNO = T2.SNO
Inner Join Book  As T3 on T2.BookID = T3.BookID
Where Sex = 'Ů'

-- ��ʾ�������������Щͼ���Ǳ���������
-- BorrowBook - Book - Author
Select Distinct BookName As '�������ߵ���'   from BorrowBook As T1 
Inner Join Book As T2 on T2.BookID = T1.BookID
Inner Join Author As T3 on T2.BookAuthor = T3.AuthorID
Where  AuthorCity = '����'

--  ====================�����ӵİ������� =================
-- 1. ��ѯ����Щѧ��û����� ��in ,exists��
/*
����Student
������Borrowbook
*/
Select  T1.SNO ,SName   from Student  As T1
Left Outer Join BorrowBook As T2 on T1.SNO = T2.SNO
where T2.BorrowDate is Null 

-- 2. ��ѯ����Щ���ߵ������û�б����
-- BorrowBook , Book, Author 
Select distinct  AuthorID, AuthorName  from Book As T1 
Left Outer Join BorrowBook As T2 on T1.BookID = T2.BookID
Left Outer Join Author As T3 on T1.BookAuthor = T3.AuthorID
Where T2.BorrowDate is Null


-- ============   �����ӵĽ���ʵս =============
-- 1. ͳ�Ƴ���������� 
/*
     ͼ����    ͼ������    �����    ������      ����� 
------------------------------------------------------------
     39001    Mysql���ݿ�     15        6              9
*/

Select T1.BookID As 'ͼ����', BookName As 'ͼ������', BookIncoming As '�����',
       Isnull(Number, 0) As '������', (BookIncoming - Isnull(Number, 0)  ) As '�����'
from Book As T1
Left Outer Join 
(
	Select BookId, COUNT(*) As Number
	From BorrowBook 
	Group by BookID
) As T2 on T1.BookID = T2.BookID

-- ===================  �������� ==============
Create Table Stu
(
	SNo int Primary key,
	SName varchar(100)
)
Insert into Stu Values(95001, '������')
Insert into Stu Values(95002, '����')
Insert into Stu Values(95003, '����')
Insert into Stu Values(95004, '½����')
Insert into Stu Values(95005, '�Ӻƽ�')

Create Table Course
(
	CNo int Primary key,
	CName varchar(100)
)
Insert into Course Values(39001, '����')
Insert into Course Values(39002, '��ѧ')
Insert into Course Values(39003, 'Ӣ��')
Insert into Course Values(39004, '����')
Insert into Course Values(39005, '��ѧ')

Create Table Score
(
	SNo int,
	CNo int,
	Result int
)
Insert into Score Values(95001, 39001, 89)
Insert into Score Values(95001, 39002, 71)
Insert into Score Values(95001, 39003, 92)
Insert into Score Values(95001, 39004, 64)
Insert into Score Values(95001, 39005, 78)
Insert into Score Values(95002, 39001, 67)
Insert into Score Values(95002, 39002, 92)
Insert into Score Values(95002, 39003, 56)

Insert into Score Values(95002, 39005, 98)
Insert into Score Values(95003, 39001, 86)
Insert into Score Values(95003, 39002, 93)
Insert into Score Values(95003, 39003, 95)
Insert into Score Values(95003, 39004, 86)
Insert into Score Values(95003, 39005, 76)
Insert into Score Values(95004, 39001, 78)
Insert into Score Values(95004, 39002, 89)
Insert into Score Values(95004, 39003, 93)
Insert into Score Values(95004, 39004, 92)

Insert into Score Values(95005, 39001, 73)
Insert into Score Values(95005, 39002, 89)
Insert into Score Values(95005, 39003, 88)
Insert into Score Values(95005, 39004, 99)
Insert into Score Values(95005, 39005, 85)

Select * from Stu
Select * from Course
Select * from Score

Select * from Stu Cross join Course 
-- Cross join �������� --���������--����������

-- ͳ�Ƴ���Щѧ������Щ��Ŀȱ�� (2��)
-- ��������: 25��(cross join)     ��ǰ:23
Select  T1.SNO, SName,T1.CNo, CName from 
(   
	Select  SNO, SName, CNo, CName from Stu Cross join Course
 ) As T1 Left Outer Join Score As T2 on T1.SNo = T2.SNo And T1.CNo=T2.CNo
Where  Result is Null 

-- ==============������ ======================
Create Table Employee
(
	EmpId int Primary key,
	EmpName varchar(100),
	ReportId int
)
insert into Employee Values('101','������',null)
insert into Employee Values('102','����',101)
insert into Employee Values('103','���',101)
insert into Employee Values('104','������',101)
insert into Employee Values('105','��С��',102)
insert into Employee Values('106','����',102)
insert into Employee Values('107','�½�',103)
insert into Employee Values('108','����',103)
insert into Employee Values('109','��',103)
insert into Employee Values('110','����',103)
insert into Employee Values('111','�찮��',104)
insert into Employee Values('112','��ϣ',104)

Select  * from Employee
-- ��ʽ01�� ���û��������ֱ�Ӳ�ͳ��
Select  T3.EmpId As '���', T3.EmpName As '����' , COUNT(*) As '��������'
from 
(
 Select  T1.EmpId, T1.EmpName  from Employee As T1 
 Inner Join Employee As T2 on T1.EmpId = T2.ReportId
) AS T3
Group by  T3.EmpId, T3.EmpName

-- ��ʽ02�� ���û������Ҳ��Ҫͳ��,����������ʾ0
Select  T3.EmpId As '���', T3.EmpName As '����' , COUNT(T3.EmpId02) As '��������'
from 
(
	Select T1.EmpId, T1.EmpName,T2.EmpId As 'EmpId02' from Employee As T1 
	Left outer Join Employee As T2 on T1.EmpId = T2.ReportId
) AS T3 
Group by  T3.EmpId, T3.EmpName

-- ��ʽ02�� ���û������Ҳ��Ҫͳ��,����������ʾ0
Select  T3.EmpId As '���', T3.EmpName As '����' ,Sum(T3.Number) As '��������'
from 
(
	Select T1.EmpId, T1.EmpName, CASE when T2.EmpId IS NULL  then 0 else 1 end As 'Number'
	from Employee As T1 
	Left outer Join Employee As T2 on T1.EmpId = T2.ReportId
) As T3
Group by  T3.EmpId, T3.EmpName

-- ===================  �κ���ҵ ==================
-- ͳ�Ƴ�һ��ѧ���ɼ�ͳ�Ʊ������յ�������
Select * from Stu
Select * from Course
Select * from Score


Select T1.SNo As 'ѧ��', T2.SName,T1.����,T1.��ѧ,T1.Ӣ��, T1.����,T1.��ѧ,T1.�ܷ�,T1.���� 
from
(
	Select  SNO,
		sum(Case when CNo=39001 then Result else 0 end) As '����',
		sum(Case when CNo=39002 then Result else 0 end) As '��ѧ',
		sum(Case when CNo=39003 then Result else 0 end) As 'Ӣ��',
		sum(Case when CNo=39004 then Result else 0 end) As '����',
		sum(Case when CNo=39005 then Result else 0 end) As '��ѧ',
		SUM(result) As '�ܷ�',
		Convert(decimal(18,2), SUM(Result)*1.0/5) As '����'
	from Score 
	Group By SNo
) AS T1 Inner Join Stu As T2 on T1.SNo = T2.SNo
Order by T1.�ܷ� DESC 