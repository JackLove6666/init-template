package com.jack.inittemplate.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jack.inittemplate.entity.SysRoleMenu;
import com.jack.inittemplate.mapper.SysRoleMenuMapper;
import com.jack.inittemplate.service.SysRoleMenuService;
import org.springframework.stereotype.Service;

@Service
public class SysRoleMenuServiceImpl extends ServiceImpl<SysRoleMenuMapper, SysRoleMenu> implements SysRoleMenuService {
}
