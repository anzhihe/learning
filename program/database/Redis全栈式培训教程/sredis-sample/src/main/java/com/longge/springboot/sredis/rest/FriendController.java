package com.longge.springboot.sredis.rest;

import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.longge.springboot.sredis.service.FriendService;

@RequestMapping(value = "/friend")
@RestController
public class FriendController {
    @Autowired
    private FriendService friendService;

    /**
     * 生成分布式ID
     * 
     * @param key
     * @param value
     * @return
     */
    @RequestMapping(value = "/inter")
    public Set<String> inter() {
        return this.friendService.inter();
    }
}
