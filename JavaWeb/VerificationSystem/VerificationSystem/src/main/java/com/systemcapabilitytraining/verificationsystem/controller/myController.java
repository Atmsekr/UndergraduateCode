package com.systemcapabilitytraining.verificationsystem.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * ClassName: myController
 * Package: com.systemcapabilitytraining.verificationsystem.controller
 * Description:
 *
 * @Author Atmsekr
 * @Create 2023/3/11 20:23
 * @Version 1.0
 */
@RestController
public class myController {
    @GetMapping("/dudulu")
    public String dudulu(){
        return "dudulu~~~";
    }
}
