package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.MslaveService;

@RequestMapping(value = "/mslave")
@RestController
public class MslaveController {
    @Autowired
    private MslaveService mslaveService;

    @RequestMapping(value = "/test/{key}/{value}")
    public String test(@PathVariable String key, @PathVariable String value) {
        this.mslaveService.set(key, value);
        return this.mslaveService.get(key);
    }
}
