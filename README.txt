---
Title: 命令行 TODO 工具
Date: 2019-03-25
Author: bugnofree
---

使用方法如下

    usage: todo [-h] [-a ADD [ADD ...] | -d DELETE [DELETE ...] | -c ID KEY VAL |
                -m ID STATUS]

    optional arguments:
      -h, --help            show this help message and exit
      -a ADD [ADD ...], --add ADD [ADD ...]
                            Add a task,the task format is : title @ [description]
      -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                            Delete a task
      -c ID KEY VAL, --change ID KEY VAL
                            Update a task,change is one keyword from
                            [title|status|desc|date]
      -m ID STATUS, --mark ID STATUS
                            Mark if a task is finished or not

一个例子如下

    ➜  todo (master) ✔ todo
    1 ⇒ 查看各种时间标准
            ○ Status: ✗
            ○ Since: 2018-01-10 14:10:42
    2 ⇒ PAM文件
            ○ Status: ✗
            ○ Description: http://www.tuxradar.com/content/how-pam-works
            ○ Since: 2018-01-10 15:21:28
    3 ⇒ 搜索数学书籍
            ○ Status: ✗
            ○ Description: MathematicalNotation:AGuideforEngineersandScientists
            ○ Since: 2018-01-14 10:15:28
