/*
 *
 *      Copyright (c) 2018-2025, Aukey IT All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice,
 *  this list of conditions and the following disclaimer.
 *  Redistributions in binary form must reproduce the above copyright
 *  notice, this list of conditions and the following disclaimer in the
 *  documentation and/or other materials provided with the distribution.
 *  Neither the name of the trob4cloud.com developer nor the names of its
 *  contributors may be used to endorse or promote products derived from
 *  this software without specific prior written permission.
 *  Author: Aukey IT (AukeyIT@aukeys.com)
 *
 */

package com.jack.inittemplate.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.extension.activerecord.Model;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import java.time.LocalDateTime;

/**
 * <p>
 * 部门管理
 * </p>
 *
 * @author Aukey IT
 * @since 2018-01-22
 */
@Data
@EqualsAndHashCode(callSuper = true)
@TableName("sys_dept")
@ApiModel(value="部门")
public class SysDept extends Model<SysDept> {

	private static final long serialVersionUID = 1L;

	@TableId(value = "dept_id", type = IdType.AUTO)
	@ApiModelProperty(value="部门ID",example="1")
	private Integer deptId;
	/**
	 * 部门名称
	 */
	@NotBlank(message = "部门名称不能为空")
	@Size(max = 50,message="组织名称长度不得超过50个字符")
	@ApiModelProperty(value="部门名称",example="销售部")
	private String name;
	/**
	 * 排序
	 */
	@ApiModelProperty(value="排序",example="2")
	private Integer sort;
	/**
	 * 排序
	 */
	@ApiModelProperty(value="备注",example="任性")
	@Size(max = 100,message="备注信息不得超过100字符的备注信息")
	private String remark;
	/**
	 * 创建时间
	 */
	@ApiModelProperty(value="创建时间",example="2019-01-07 15:56:14")
	private LocalDateTime createTime;
	/**
	 * 修改时间
	 */
	@ApiModelProperty(value="更新时间",example="2019-01-07 15:56:14")
	private LocalDateTime updateTime;

	@ApiModelProperty(value="父部门ID",example="3")
	private Integer parentId;

	/**
	 * 是否删除  -1：已删除  0：正常
	 */
	@ApiModelProperty(value="是否删除  -1：已删除  0：正常",example="0")
	private String delFlag;
	
	/**
	 * 组织id
	 */
	@ApiModelProperty(value="组织ID",example="1")
	private Integer architectureId;

	/**
	 * 负责人ID
	 */
	@ApiModelProperty(value="负责人ID",example="")
	private Integer masterId;
	

	
}
