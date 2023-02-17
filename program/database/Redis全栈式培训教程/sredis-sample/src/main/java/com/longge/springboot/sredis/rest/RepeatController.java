package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.RepeatService;

/**
 * 18.6.Redis防重复提交
 * 
 */
@RequestMapping(value = "/repeat")
@RestController
public class RepeatController {
    @Autowired
    private RepeatService repeatService;

    /**
     * 提交防重复功能
     * 
     * @param key
     * @param value
     * @return
     */
    @RequestMapping(value = "/submit/{key}")
    public String submit(@PathVariable String key) {
        if (null == key || "".equals(key)) {
            return "请先登陆";
        }
        boolean flag = this.repeatService.submit(key);
        if (flag) {
            return "提交成功";
        } else {
            return "重复提交";
        }
    }
}
