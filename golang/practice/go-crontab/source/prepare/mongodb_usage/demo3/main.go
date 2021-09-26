package main

import (
	"github.com/mongodb/mongo-go-driver/mongo"
	"context"
	"github.com/mongodb/mongo-go-driver/mongo/clientopt"
	"time"
	"fmt"
	"github.com/mongodb/mongo-go-driver/bson/objectid"
)

// 任务的执行时间点
type TimePoint struct {
	StartTime int64	`bson:"startTime"`
	EndTime int64	`bson:"endTime"`
}

// 一条日志
type LogRecord struct {
	JobName string	`bson:"jobName"` // 任务名
	Command string `bson:"command"` // shell命令
	Err string `bson:"err"` // 脚本错误
	Content string `bson:"content"`// 脚本输出
	TimePoint TimePoint `bson:"timePoint"`// 执行时间点
}

func main() {
	var (
		client *mongo.Client
		err error
		database *mongo.Database
		collection *mongo.Collection
		record *LogRecord
		logArr []interface{}	//  C语言里的addr, type, JAVA Object
		result *mongo.InsertManyResult
		insertId interface{}	//  objectId
		docId objectid.ObjectID
	)
	// 1, 建立连接
	if client, err = mongo.Connect(context.TODO(), "mongodb://36.111.184.221:27017", clientopt.ConnectTimeout(5 * time.Second)); err != nil {
		fmt.Println(err)
		return
	}

	// 2, 选择数据库my_db
	database = client.Database("cron")

	// 3, 选择表my_collection
	collection = database.Collection("log")

	// 4, 插入记录(bson)
	record = &LogRecord{
		JobName: "job10",
		Command: "echo hello",
		Err: "",
		Content: "hello",
		TimePoint: TimePoint{StartTime: time.Now().Unix(), EndTime: time.Now().Unix() + 10},
	}

	// 5, 批量插入多条document
	logArr = []interface{}{record, record, record}

	// 发起插入
	if result, err = collection.InsertMany(context.TODO(), logArr); err != nil {
		fmt.Println(err)
		return
	}

	// 推特很早的时候开源的，tweet的ID
	// snowflake: 毫秒/微秒的当前时间 + 机器的ID + 当前毫秒/微秒内的自增ID(每当毫秒变化了, 会重置成0，继续自增）
	for _, insertId = range result.InsertedIDs {
		// 拿着interface{}， 反射成objectID
		docId = insertId.(objectid.ObjectID)
		fmt.Println("自增ID:", docId.Hex())
	}
}
