# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
from __future__ import division
from sympy import *

# x, y, z, t = symbols('x,y,z,t')
k, m, n = symbols('k,m,n', integer=True)
f, g, h = symbols('f,g,h', cls=Function)

x = Symbol("x", real=True)
var = expand(exp(I*x), complex=True)
print(var)
# init_printing()




# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
