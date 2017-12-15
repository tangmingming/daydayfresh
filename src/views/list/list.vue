<template>
  <div style="width: 1200px; margin: 0 auto">
    <el-breadcrumb separator="/" style="margin: 20px">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>活动管理</el-breadcrumb-item>
      <el-breadcrumb-item>活动列表</el-breadcrumb-item>
      <el-breadcrumb-item>活动详情</el-breadcrumb-item>
    </el-breadcrumb>
    <div>
      <div style="float: left;">
        <el-card style="width: 220px">
          <div slot="header" class="clearfix">
            <span>卡片名称</span>
            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
          </div>
          <el-tree
            :data="data"
            :props="defaultProps"
            :expand-on-click-node="false"
            default-expand-all
            @node-click="handleNodeClick">
          </el-tree>
        </el-card>
      </div>
      <div style="float: left; width: 960px">
        <el-card>
          <ul>
            <li style="float: left">价格</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(1,24)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(15,20)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(25,50)">1-24</li>
            <li style="float: left; margin: 0 30px" @click="filter_price(50,100)">1-24</li>
            <li  style="float: left" ><input/>-<input/><button>确定</button></li>
          </ul>
        </el-card>
        <el-card style="">
          <a style="font-size: 12px">综合</a>
          <a style="font-size: 12px">综合</a>
          <a style="font-size: 12px">综合</a>
        </el-card>
        <div>
          <div style="float: left; width: 226px; margin: 7px"  v-for="n in 10">
            <el-card :body-style="{ padding: '0px' }">
              <img style="width: 226px; height: 226px" src="../../static/images/merchandise/30_P_1448948663450.jpg">
              <div style="padding: 14px;">
                <span style="color:red">￥2000</span>
                <a style="font-size: 12px">电脑都觉得男方家拿到今年非觉得呢动脑筋</a>
              </div>
            </el-card>
          </div>
        </div>
      </div>
      <div class="block;" style="float: right">
        <el-pagination
          layout="prev, pager, next"
          :total="1000">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        data: [{
          label: '一级 1',
          children: [{
            label: '二级 1-1',
            children: [{
              label: '三级 1-1-1'
            }]
          }]
        }, {
          label: '一级 2',
          children: [{
            label: '二级 2-1',
            children: [{
              label: '三级 2-1-1'
            }]
          }, {
            label: '二级 2-2',
            children: [{
              label: '三级 2-2-1'
            }]
          }]
        }, {
          label: '一级 3',
          children: [{
            label: '二级 3-1',
            children: [{
              label: '三级 3-1-1'
            }]
          }, {
            label: '二级 3-2',
            children: [{
              label: '三级 3-2-1'
            }]
          }]
        }],
        defaultProps: {
          children: 'children',
          label: 'label'
        }
      };
    },
    methods: {
      handleNodeClick(data) {
        console.log(data);
      },
      filter_price(min, max){
        console.log(min, max)
      }
    }
  };
</script>
