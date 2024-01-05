package com.jack.inittemplate.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jack.inittemplate.entity.SysUserRole;
import com.jack.inittemplate.mapper.SysUserRoleMapper;
import com.jack.inittemplate.service.SysUserRoleService;
import org.springframework.stereotype.Service;

@Service
public class SysUserRoleServiceImpl extends ServiceImpl<SysUserRoleMapper, SysUserRole> implements SysUserRoleService {
}
