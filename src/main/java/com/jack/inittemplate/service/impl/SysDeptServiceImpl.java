package com.jack.inittemplate.service.impl;


import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jack.inittemplate.entity.SysDept;
import com.jack.inittemplate.mapper.SysDeptMapper;
import com.jack.inittemplate.service.SysDeptService;
import org.springframework.stereotype.Service;

@Service
public class SysDeptServiceImpl extends ServiceImpl<SysDeptMapper, SysDept> implements SysDeptService {
}
