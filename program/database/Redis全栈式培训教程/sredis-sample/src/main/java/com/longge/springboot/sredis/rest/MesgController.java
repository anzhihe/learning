package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.MesgService;

/**
 * 18.5.Redis短信验证码
 * 
 */
@RequestMapping(value = "/mesg")
@RestController
public class MesgController {
    @Autowired
    private MesgService mesgService;

    /**
     * 模拟生成短信验证码
     * 
     * @param key
     * @param value
     * @return
     */
    @RequestMapping(value = "/send/{key}")
    public String sendMsg(@PathVariable String key) {
        if (null == key || "".equals(key)) {
            return "请先登陆";
        }
        String ran = this.mesgService.sendMsg(key);
        return "发送短信成功……[" + ran + "]";
    }

    /**
     * 模拟短信验证
     * 
     * @param key
     * @param value
     * @return
     */
    @RequestMapping(value = "/check/{key}/{value}")
    public String check(@PathVariable String key, @PathVariable String value) {
        boolean flag = this.mesgService.checkMsg(key, value);
        if (flag) {
            return "校验成功";
        } else {
            return "校验失败";
        }
    }
}
