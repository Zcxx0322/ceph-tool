# Ceph操作工具

一个Ceph工具，操作对象存储网关数据

## 环境准备

happy-python

## 详细用法

```bash
$ python main.py 
2023-11-20 10:05:42 13598 [INFO] 未启用日志配置文件，加载默认设置
2023-11-20 10:05:42 13598 [INFO] 日志配置文件 '/home/colamps/workspace/github/ceph-tool/conf/log.ini' 加载成功
2023-11-20 10:05:42 13598 [ERROR] 命令行参数错误，请查看使用说明
usage: ceph_tool [-n] [-l] [-l bucket] [-p bucket] [-s bucket] [-u bucket file] [-d bucket file]

Ceph工具

options:
  -h, --help            show this help message and exit
  -n, --dry-run         模拟运行，测试配置参数
  -l [bucket], --list [bucket]
                        列出bucket信息
  -p bucket, --post bucket
                        更新bucket元数据或者创建bucket
  -u bucket filename, --upload bucket filename
                        上传文件到bucket
  -s [bucket], --stat [bucket]
                        显示bucket详细信息
  -d bucket file, --download bucket file
                        从bucket下载文件
  -v, --version         显示版本信息
```
