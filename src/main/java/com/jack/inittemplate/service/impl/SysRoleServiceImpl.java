package com.jack.inittemplate.service.impl;


import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jack.inittemplate.entity.SysRole;
import com.jack.inittemplate.mapper.SysRoleMapper;
import com.jack.inittemplate.service.SysRoleService;
import org.springframework.stereotype.Service;

@Service
public class SysRoleServiceImpl extends ServiceImpl<SysRoleMapper, SysRole> implements SysRoleService {
}
