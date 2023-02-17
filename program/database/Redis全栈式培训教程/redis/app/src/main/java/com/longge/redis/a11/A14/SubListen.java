package com.longge.redis.a11.A14;

import java.io.UnsupportedEncodingException;

import redis.clients.jedis.BinaryJedisPubSub;

/**
 * 章节：11.14.事件通知
 * 功能：事件通知过期事件演示
 */
public class SubListen extends BinaryJedisPubSub {

    @Override
    public void onMessage(byte[] channel, byte[] message) {
        String channelStr = new String(channel);
        String messageStr = null;
        try {
            messageStr = new String(message, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.out.println("接收频道" + channelStr + "消息：" + messageStr);
        // 进行业务处理
    }
}
