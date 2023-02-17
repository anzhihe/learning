package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.SimpleService;

@RequestMapping(value = "/simple")
@RestController
public class SimpleController {
    @Autowired
    private SimpleService simpleService;

    @RequestMapping(value = "/test/{key}/{value}")
    public String test(@PathVariable String key, @PathVariable String value) {
        this.simpleService.set(key, value);
        return this.simpleService.get(key);
    }
}
