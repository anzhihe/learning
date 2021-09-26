package main

import (
	"github.com/coreos/etcd/clientv3"
	"time"
	"fmt"
	"context"
)

func main() {
	var (
		config clientv3.Config
		client *clientv3.Client
		err error
		kv clientv3.KV
		getResp *clientv3.GetResponse
	)

	config = clientv3.Config{
		Endpoints: []string{"36.111.184.221:2379"}, // 集群列表
		DialTimeout: 5 * time.Second,
	}

	// 建立一个客户端
	if client, err = clientv3.New(config); err != nil {
		fmt.Println(err)
		return
	}

	// 用于读写etcd的键值对
	kv = clientv3.NewKV(client)

	// 写入另外一个Job
	kv.Put(context.TODO(), "/cron/jobs/job2", "{...}")

	// 读取/cron/jobs/为前缀的所有key
	if getResp, err = kv.Get(context.TODO(), "/cron/jobs/", clientv3.WithPrefix()); err != nil {
		fmt.Println(err)
	} else {	// 获取成功, 我们遍历所有的kvs
		fmt.Println(getResp.Kvs)
	}
}
