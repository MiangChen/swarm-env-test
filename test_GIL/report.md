# 安装python 3.13 无 GIL
因为conda不支持直接安装这个版本，所以只能手动；
python下载官网，拉到最下面选择对应的系统安装包：https://www.python.org/downloads/release/python-3131/
安装时选择 自定义 安装，勾选 `Free-threaded python`（mac上是如此，其他系统可能不太一样，根据实际情况来）

# 测试结果
在mac的m3max芯片上，求解main.py

使用python3.13时，有GIL时，顺序执行时间 0.815s，并行执行时间0.810s
使用python3.13时，没有GIL时，顺序执行时间 0.823s，并行执行时间 0.781s

# 反馈
- 对中文的兼容性有些莫名其妙的bug
- 实际加速效果不太明显
- 因为是2024年10月才发布的，可以再等后续稳定了 and 有并行需求再用3.13
