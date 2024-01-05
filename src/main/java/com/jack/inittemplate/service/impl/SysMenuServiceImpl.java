package com.jack.inittemplate.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jack.inittemplate.entity.SysMenu;
import com.jack.inittemplate.mapper.SysMenuMapper;
import com.jack.inittemplate.service.SysMenuService;
import org.springframework.stereotype.Service;

@Service
public class SysMenuServiceImpl extends ServiceImpl<SysMenuMapper, SysMenu> implements SysMenuService {
}
