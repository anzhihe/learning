package main
import "fmt"
func main(){
	
	//1)统计3个班成绩情况，每个班有5名同学，
	//求出各个班的平均分和所有班级的平均分[学生的成绩从键盘输入]

	//分析实现思路
	//1. 统计1个班成绩情况，每个班有5名同学, 求出该班的平均分【学生的成绩从键盘输入】=》先易后难
	//2. 学生数就是5个 [先死后活]
	//3. 声明一个sum 统计班级的总分

	//分析实现思路2
	//1. 统计3个班成绩情况，每个班有5名同学, 求出每个班的平均分【学生的成绩从键盘输入】
	//2. j 表示第几个班级
	//3. 定义一个变量存放总成绩

	//分析实现思路3
	//1. 我们可以把代码做活
	//2. 定义两个变量，表示班级的个数和班级的人数

	//统计三个班及格人数，每个班有5名同学
	//分析思路
	//1. 声明以变量 passCount 用于保存及格人数

	//走代码实现
	var classNum int = 2
	var stuNum int = 5
	var totalSum float64 = 0.0
	var passCount int = 0
	for j := 1; j <= classNum; j ++ {
		sum := 0.0
		for i := 1; i <= stuNum; i++ {
			var score float64
			fmt.Printf("请输入第%d班 第%d个学生的成绩 \n", j, i)
			fmt.Scanln(&score)
			//累计总分
			sum += score
			//判断分数是否及格
			if score >= 60 {
				passCount++
			}
		}

		fmt.Printf("第%d个班级的平均分是%v\n", j, sum / float64(stuNum) )
		//将各个班的总成绩累计到totalSum
		totalSum += sum
	}

	fmt.Printf("各个班级的总成绩%v 所有班级平均分是%v\n", totalSum, totalSum / float64(stuNum * classNum))
	fmt.Printf("及格人数为%v\n", passCount)
}