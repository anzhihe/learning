package com.longge.springboot.sredis.rest;

import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping(value = "/simple")
@RestController
public class SimpleController {

    @Cacheable(value = { "mycache" }, key = "#key")
    @RequestMapping(value = "/query/{key}")
    public String query(@PathVariable String key) {
        System.out.println("执行query:" + key);
        // 比如查数据库
        return System.currentTimeMillis() + "";
    }

    @CachePut(value = { "mycache" }, key = "#key")
    @RequestMapping(value = "/update/{key}/{value}")
    public String update(@PathVariable String key, @PathVariable String value) {
        return value;
    }

    @CacheEvict(value = { "mycache" }, key = "#key")
    @RequestMapping(value = "/delete/{key}")
    public String delete(@PathVariable String key) {
        return "success";
    }

    @CacheEvict(value = { "mycache" }, allEntries = true)
    @RequestMapping(value = "/clear")
    public String clear() {
        return "success";
    }
}
