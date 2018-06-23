1. 如何产生验证码：
    1. 首先呢，现在就需要去确定一下，就是，其实flask的结构应该是长什么样子的呢？？
        1. 解答：[python3.6 flask web学习]Flask项目目录结构https://blog.csdn.net/xingyunlost/article/details/77155584
        ![images](dir_str.png)

    2. 突然有个小疑问，就是，markdown可以插入本地图片吗？即使是当前本地目录来导入。
        1. 解答
        MarkDown添加图片的三种方式：https://www.jianshu.com/p/280c6a6f2594
        插入本地图片
        只需要在基础语法的括号中填入图片的位置路径即可，支持绝对路径和相对路径。
        例如：
        ```python
        ![avatar](/home/picture/1.png)
        ```