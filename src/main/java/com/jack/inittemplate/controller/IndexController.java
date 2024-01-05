package com.jack.inittemplate.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class IndexController {


    @GetMapping("/")
    public String home() {
        return "home";
    }

    @GetMapping("/admin")
    public String admin(Model model) {
        model.addAttribute("name","捷克梗");
        model.addAttribute("age","19");
        model.addAttribute("id","1");
        return "admin";
    }



    @GetMapping("/index")
    @ResponseBody
    public String index(String name){
        return "哈喽!"+name;
    }
}
