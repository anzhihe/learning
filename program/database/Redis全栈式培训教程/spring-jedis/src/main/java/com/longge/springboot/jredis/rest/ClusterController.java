package com.longge.springboot.jredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.jredis.service.ClusterService;

@RequestMapping(value = "/cluster")
@RestController
public class ClusterController {
    @Autowired
    private ClusterService clusterService;

    @RequestMapping(value = "/test/{key}/{value}")
    public String test(@PathVariable String key, @PathVariable String value) {
        this.clusterService.set(key, value);
        return this.clusterService.get(key);
    }
}
