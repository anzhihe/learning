package com.longge.redis.a6.A2;

import java.io.UnsupportedEncodingException;

import redis.clients.jedis.BinaryJedisPubSub;

/**
 * 章节：6.2.Redis的发布与订阅
 * 功能：发布/订阅演示
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
    }
}
