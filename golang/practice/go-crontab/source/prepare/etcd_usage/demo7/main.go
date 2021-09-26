package main

import (
	"github.com/coreos/etcd/clientv3"
	"time"
	"fmt"
	"context"
	"github.com/coreos/etcd/mvcc/mvccpb"
)

func main() {
	var (
		config clientv3.Config
		client *clientv3.Client
		err error
		kv clientv3.KV
		watcher clientv3.Watcher
		getResp *clientv3.GetResponse
		watchStartRevision int64
		watchRespChan <-chan clientv3.WatchResponse
		watchResp clientv3.WatchResponse
		event *clientv3.Event
	)

	// 客户端配置
	config = clientv3.Config{
		Endpoints: []string{"36.111.184.221:2379"},
		DialTimeout: 5 * time.Second,
	}

	// 建立连接
	if client, err = clientv3.New(config); err != nil {
		fmt.Println(err)
		return
	}

	// KV
	kv = clientv3.NewKV(client)

	// 模拟etcd中KV的变化
	go func() {
		for {
			kv.Put(context.TODO(), "/cron/jobs/job7", "i am job7")

			kv.Delete(context.TODO(), "/cron/jobs/job7")

			time.Sleep(1 * time.Second)
		}
	}()

	// 先GET到当前的值，并监听后续变化
	if getResp, err = kv.Get(context.TODO(), "/cron/jobs/job7"); err != nil {
		fmt.Println(err)
		return
	}

	// 现在key是存在的
	if len(getResp.Kvs) != 0 {
		fmt.Println("当前值:", string(getResp.Kvs[0].Value))
	}

	// 当前etcd集群事务ID, 单调递增的
	watchStartRevision = getResp.Header.Revision + 1

	// 创建一个watcher
	watcher = clientv3.NewWatcher(client)

	// 启动监听
	fmt.Println("从该版本向后监听:", watchStartRevision)

	ctx, cancelFunc := context.WithCancel(context.TODO())
	time.AfterFunc(5 * time.Second, func() {
		cancelFunc()
	})

	watchRespChan = watcher.Watch(ctx, "/cron/jobs/job7", clientv3.WithRev(watchStartRevision))

	// 处理kv变化事件
	for watchResp = range watchRespChan {
		for _, event = range watchResp.Events {
			switch event.Type {
			case mvccpb.PUT:
				fmt.Println("修改为:", string(event.Kv.Value), "Revision:", event.Kv.CreateRevision, event.Kv.ModRevision)
			case mvccpb.DELETE:
				fmt.Println("删除了", "Revision:", event.Kv.ModRevision)
			}
		}
	}
}