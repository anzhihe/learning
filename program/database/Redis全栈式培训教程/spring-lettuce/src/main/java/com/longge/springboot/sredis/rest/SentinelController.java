package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.SentinelService;

@RequestMapping(value = "/sentinel")
@RestController
public class SentinelController {
    @Autowired
    private SentinelService sentinelService;

    @RequestMapping(value = "/test/{key}/{value}")
    public String test(@PathVariable String key, @PathVariable String value) {
        this.sentinelService.set(key, value);
        return this.sentinelService.get(key);
    }
}
