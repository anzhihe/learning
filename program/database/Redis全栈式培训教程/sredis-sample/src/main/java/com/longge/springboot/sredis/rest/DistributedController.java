package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.DistributedService;

/**
 * 18.7.分布式ID模拟生成
 * 
 */
@RequestMapping(value = "/dist")
@RestController
public class DistributedController {
    @Autowired
    private DistributedService distributedService;

    /**
     * 生成分布式ID1
     * 
     * @param key
     * @param value
     * @return
     */
    @RequestMapping(value = "/newid/{key}")
    public long newid(@PathVariable String key) {
        return this.distributedService.newid(key);
    }

    /**
     * 生成分布式ID2
     * 
     * @param key
     * @param value
     * @return
     * @throws InterruptedException
     */
    @RequestMapping(value = "/lnewid/{key}")
    public String lnewid(@PathVariable String key) throws InterruptedException {
        return this.distributedService.lnewid(key);
    }
}
