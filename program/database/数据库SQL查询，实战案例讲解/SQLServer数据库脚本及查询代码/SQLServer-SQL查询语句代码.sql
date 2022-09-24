Select * from Student --学生信息
Select * from Author -- 作者信息
Select * from Press  --出版社信息
Select * from Book  --图书信息
Select * from BookType --图书类别
Select * from BorrowBook -- 借书信息

--===================SQL查询基础入门=======================
-- 查询出姓名为“陈鹏”的学号、手机号码和邮箱地址 
Select SNO As '学号', MobileNO As '手机号码',StuEMail As '邮箱地址'
from Student
--Where SName = '陈鹏'
where SName in ('陈鹏')

-- 查询出姓名不是“陈鹏”的学生的所有信息
Select SNO,Sname, Sage ,Sex, MobileNo,StuEmail
from Student
--where SName != '陈鹏'
--Where SName <> '陈鹏'
Where SName Not in ('陈鹏')

-- 查询出学生年龄介于20到30间的学生学号和姓名
Select SNO As '学号', SName As '姓名'
from Student 
--Where ( Sage >=20 ) And ( Sage <= 30)
Where Sage Between 20 And 30  -- Between--and ---某一个范围

-- 查询哪些学生没有填写“年龄 ”信息
Select SNo,Sname
from Student 
where Sage is null   -- Null一定不能用算术运算符连接，用is ，not is

-- 查询出“陈鹏”、”Alice”、”Bob”的学号，年龄
Select SNo As '学号', Sage As '年龄'
from Student 
--where SName ='陈鹏' OR SName = 'Alice' OR  SName = 'Bob'
Where SName in ('陈鹏','Alice','Bob')

-- ===================================
-- 查询出哪些图书被借过
/*
Select distinct Bookid from BorrowBook
Select COUNT(distinct bookId) As '被借图书量' from BorrowBook
*/

-- 查询出小于20岁或者大于25 的女生
Select * from Student where (Sage<20 OR Sage>30) And Sex ='女'

-- 案例
Select * from Student Where SName between '陈鹏' and '王进'
Select * from Student order by SName

================================================
--1. 查询出手机号码133或者134开头，倒数第2位为不是2也不是4的学生学号和姓名
Select * 
from Student 
where MobileNO Like '[1][3][34]%[^24]_'

-- 模糊查询：条件不明确 ---》Like
-- 两个重要的通配符 ： % --》（匹配0-n多个任意字符）
--                                 _  --->   (匹配任意1个字符)

--2. 对Student表按照年龄升序排序，如果年龄一样，女生排在男生前面 --- Order by   ASC/ DESC
Select * 
from Student 
Order by Sage ASC, Sex DESC

--3.  查询出年龄最大的学生的学号和姓名
-- 错误写法01：
Select * from Student  where Sage = MAX(Sage)
-- 错误写法02：
Select  Top 1 * from Student  Order by Sage DESC
--正确的做法 
Select * from Student 
Where Sage = (
	--计算出最大的年龄
	Select MAX(Sage) from Student 
)


-- =============== 聚合函数===============
-- 查询出男生的平均年龄
Select AVG(sage) As '平均年龄'
from Student
where Sex ='男'

-- 查询出有多少位学生借书
Select  count( distinct sno) As '借书学生人数' from BorrowBook

-- 查询出计算机类的图书总共有多少本、
Select  SUM(BookIncoming) As '计算机类图书总量'
from Book 
where BookTypeID= 
(
	Select ID from BookType Where TypeName='计算机'
)

--==================分组查询 ===============
-- 统计出男女生的人数
Select Sex As '性别', COUNT(*) As "人数", AVG(Sage) As '平均年龄',sum(sage) As '年龄和'
from Student 
group by sex

-- 统计出每一类书中的最高的价格
Select  BookTypeID As '图书类别编号', MAX(BookPrice) As '最高价格'
from Book
Group by  BookTypeID 


-- =============分组查询的进阶===========
-- 统计出年龄在25岁以上的男女生人数      (分组前就筛掉数据： Where)
Select Sex, COUNT(*) As '人数'
from Student 
Where Sage >=25
Group by Sex

-- 统计出被借的超过3本的图书编号      (分组后就筛掉数据： Having)
Select  BookID, COUNT(*) As '被借次数'
from BorrowBook
Group by BookId
Having COUNT(*) >= 2
Order By  COUNT(*) DESC

-- 查询出借的最多的那本书的Id
Select  BookID, COUNT(*) As '被借次数'
from BorrowBook
Group by BookId
Having COUNT(*) = 
(
	Select   TOP 1   COUNT(*) 
	from BorrowBook
	Group by BookId
	order by COUNT(*) DESC
)

-- ============ 分组的多字段 ===============
-- 统计出一月份哪些区域的哪些商品销售低于1000件, 按照倒序排列
Select  PArea As '区域', PName As '名称', SUM(PSaleNo) As '销售量'
from SalesTable 
Where PMonth= '一月'
Group by PArea, PName 
Having  SUM(PSaleNo) < 1000
Order by SUM(PSaleNo) DESC 



-- ===============嵌套查询===================
-- 查询初陈鹏借了哪些书？
条件 : student  --(sno)- > BorrowBook ---(bookid)--> Book(结果)
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
		where SName = '陈鹏'
	)
)

---查询出借的最多的那本书的作者？
-- 条件:   BorrowBook  --(BookId)-> Book  ---(AuthorId)--> Author 
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

-- ===============嵌套查询的连接关键字:============
/*
 =、in 、any、some、all、 exists
1. 如果子查询确定就一个值，可以使用 = 或者 in 连接
    如果子查询是多个值，需要用  in 连接
2. in ， = any , = some 一样 
3. any 满足一个就是真  all满足所有的才是真 
4. in --- 判断是否存在于集合    exists-- 是否有结果
 
*/

-- 需求： 查询出比所有女生年龄都大的男生

Select Sno,Sname,sage
from Student 
where Sex = '男' and  Sage > all
(
	Select sage
	from Student
	where Sex='女' and Sage is not null
)


-- 需求： 查询出比任意一个女生年龄都大的男生
Select Sno,Sname,sage
from Student 
where Sex = '男' and  Sage > any
(
	Select sage
	from Student
	where Sex='女' and Sage is not null
)


-- 需求：查询出哪些人没借过书
-- 方法01 ：in 
Select Sno,Sname 
from Student 
where SNO not in 
(
	Select distinct SNO 
	from BorrowBook
)
---方法02：exists
Select sno ,Sname 
from Student As T1
where not exists 
(	
	Select Bookid
	from BorrowBook As T2
	where T1.SNO = T2.SNO
)

-- ============== 认识连接查询 ============== 
-- 连接查询； 将多张表(至少两张)表按照某个连接条件连接成一张大表，在大表中执行查询

-- 查询出陈鹏借了哪些书? 
条件: Student -- 陈鹏 
目标: Book --> BookName

Student -->BorrowBook --> Book 

Select BookName  from Student As T1 
Inner Join BorrowBook As T2 on T1.SNO = T2.SNO 
Inner Join Book As T3 on T2.BookID = T3.BookID
Where SName = '陈鹏'

--连接后的大表为: 所有学生所借的所有的图书的表

-- ============== 理解内连接和外连接 =============
Create Table Table1
(
	SNo int ,
	SName varchar(100)
)
Insert Into Table1 Values(1, '张三')
Insert Into Table1 Values(2, '李四')
Insert Into Table1 Values(3, '王五')

Create Table Table2
(
	SNo int ,
	Result  int,
)
Insert Into Table2 Values(1, 86)
Insert Into Table2 Values(2, 91)
Insert Into Table2 Values(4, 78)

-- 内连接:  按照连接条件进行连接,满足条件的显示在大表中,不满足的直接隐藏
Select * from Table1 
Select * from Table2
Select * from Table1 Inner Join Table2 on Table1.SNo = Table2.SNo

-- 左外连接: 以left关键字左边的表位主表，按照连接条件在右边的表中匹配数据，
-- 如果能匹配上，直接展示，匹配不上，就用Null填充！
Select * from Table1 
Select * from Table2
Select * from Table1 Left Outer Join  Table2 on Table1.SNo = Table2.SNo

-- 右外连接
Select * from Table1 
Select * from Table2
Select * from Table1 Right  Outer Join  Table2 on Table1.SNo = Table2.SNo

-- 全外连接
Select * from Table1 
Select * from Table2
Select * from Table1 Full  Outer Join  Table2 on Table1.SNo = Table2.SNo

--  ========内连接的案例讲解 =========
-- 演示：查询出计算机类的图书有哪些？
-- SQL92标准（SQL92标准中只有内连接）
Select BookName As '计算机类的图书'
from BookType , Book  
Where BookType.ID = Book.BookTypeID And TypeName = '计算机'

-- SQL99标准（SQL99标准中只有内连接、外连接、交叉连接、自连接。。。）
Select  BookName from BookType  
Inner Join Book on BookType.ID = Book.BookTypeID
Where TypeName = '计算机'


--  演示：查询出女生借了 哪些书
Select  Distinct BookName As '女生借的书' from Student As T1 
Inner Join BorrowBook As T2 on T1.SNO = T2.SNO
Inner Join Book  As T3 on T2.BookID = T3.BookID
Where Sex = '女'

-- 演示：被借的书中哪些图书是北京的作者
-- BorrowBook - Book - Author
Select Distinct BookName As '北京作者的书'   from BorrowBook As T1 
Inner Join Book As T2 on T2.BookID = T1.BookID
Inner Join Author As T3 on T2.BookAuthor = T3.AuthorID
Where  AuthorCity = '北京'

--  ====================外连接的案例讲解 =================
-- 1. 查询出哪些学生没借过书 （in ,exists）
/*
主表：Student
辅助：Borrowbook
*/
Select  T1.SNO ,SName   from Student  As T1
Left Outer Join BorrowBook As T2 on T1.SNO = T2.SNO
where T2.BorrowDate is Null 

-- 2. 查询出哪些作者的书从来没有被借过
-- BorrowBook , Book, Author 
Select distinct  AuthorID, AuthorName  from Book As T1 
Left Outer Join BorrowBook As T2 on T1.BookID = T2.BookID
Left Outer Join Author As T3 on T1.BookAuthor = T3.AuthorID
Where T2.BorrowDate is Null


-- ============   外连接的进阶实战 =============
-- 1. 统计出借书库存情况 
/*
     图书编号    图书名称    入库量    被借量      库存量 
------------------------------------------------------------
     39001    Mysql数据库     15        6              9
*/

Select T1.BookID As '图书编号', BookName As '图书名称', BookIncoming As '入存量',
       Isnull(Number, 0) As '被借量', (BookIncoming - Isnull(Number, 0)  ) As '库存量'
from Book As T1
Left Outer Join 
(
	Select BookId, COUNT(*) As Number
	From BorrowBook 
	Group by BookID
) As T2 on T1.BookID = T2.BookID

-- ===================  交叉连接 ==============
Create Table Stu
(
	SNo int Primary key,
	SName varchar(100)
)
Insert into Stu Values(95001, '陈晓明')
Insert into Stu Values(95002, '王宁')
Insert into Stu Values(95003, '张鹏')
Insert into Stu Values(95004, '陆建飞')
Insert into Stu Values(95005, '钟浩杰')

Create Table Course
(
	CNo int Primary key,
	CName varchar(100)
)
Insert into Course Values(39001, '语文')
Insert into Course Values(39002, '数学')
Insert into Course Values(39003, '英语')
Insert into Course Values(39004, '物理')
Insert into Course Values(39005, '化学')

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
-- Cross join 交叉连接 --》组合数据--》生成数据

-- 统计出哪些学生的哪些科目缺考 (2条)
-- 正常考试: 25条(cross join)     当前:23
Select  T1.SNO, SName,T1.CNo, CName from 
(   
	Select  SNO, SName, CNo, CName from Stu Cross join Course
 ) As T1 Left Outer Join Score As T2 on T1.SNo = T2.SNo And T1.CNo=T2.CNo
Where  Result is Null 

-- ==============自连接 ======================
Create Table Employee
(
	EmpId int Primary key,
	EmpName varchar(100),
	ReportId int
)
insert into Employee Values('101','陈晓明',null)
insert into Employee Values('102','王宁',101)
insert into Employee Values('103','张楠',101)
insert into Employee Values('104','郭春峰',101)
insert into Employee Values('105','王小雨',102)
insert into Employee Values('106','刘艺',102)
insert into Employee Values('107','郝建',103)
insert into Employee Values('108','王飞',103)
insert into Employee Values('109','马建',103)
insert into Employee Values('110','陈鹏',103)
insert into Employee Values('111','朱爱华',104)
insert into Employee Values('112','刘希',104)

Select  * from Employee
-- 方式01： 如果没有下属就直接不统计
Select  T3.EmpId As '编号', T3.EmpName As '姓名' , COUNT(*) As '下属人数'
from 
(
 Select  T1.EmpId, T1.EmpName  from Employee As T1 
 Inner Join Employee As T2 on T1.EmpId = T2.ReportId
) AS T3
Group by  T3.EmpId, T3.EmpName

-- 方式02： 如果没有下属也需要统计,下属数量显示0
Select  T3.EmpId As '编号', T3.EmpName As '姓名' , COUNT(T3.EmpId02) As '下属人数'
from 
(
	Select T1.EmpId, T1.EmpName,T2.EmpId As 'EmpId02' from Employee As T1 
	Left outer Join Employee As T2 on T1.EmpId = T2.ReportId
) AS T3 
Group by  T3.EmpId, T3.EmpName

-- 方式02： 如果没有下属也需要统计,下属数量显示0
Select  T3.EmpId As '编号', T3.EmpName As '姓名' ,Sum(T3.Number) As '下属人数'
from 
(
	Select T1.EmpId, T1.EmpName, CASE when T2.EmpId IS NULL  then 0 else 1 end As 'Number'
	from Employee As T1 
	Left outer Join Employee As T2 on T1.EmpId = T2.ReportId
) As T3
Group by  T3.EmpId, T3.EmpName

-- ===================  课后作业 ==================
-- 统计出一张学生成绩统计表，并按照倒序排列
Select * from Stu
Select * from Course
Select * from Score


Select T1.SNo As '学号', T2.SName,T1.语文,T1.数学,T1.英语, T1.物理,T1.化学,T1.总分,T1.均分 
from
(
	Select  SNO,
		sum(Case when CNo=39001 then Result else 0 end) As '语文',
		sum(Case when CNo=39002 then Result else 0 end) As '数学',
		sum(Case when CNo=39003 then Result else 0 end) As '英语',
		sum(Case when CNo=39004 then Result else 0 end) As '物理',
		sum(Case when CNo=39005 then Result else 0 end) As '化学',
		SUM(result) As '总分',
		Convert(decimal(18,2), SUM(Result)*1.0/5) As '均分'
	from Score 
	Group By SNo
) AS T1 Inner Join Stu As T2 on T1.SNo = T2.SNo
Order by T1.总分 DESC 