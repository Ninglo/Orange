"""
模板代码, 按照需求自行编辑成自己需要的绘图代码.

需要更改的部分:
0. main_it():
    (0) 更改dic的名字
    (1) 更改relation()中的形参
    (2) 更改show_figure()中的dic
1. relation()
2. show_figure()
"""

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import math
# from docx import Document
# from docx.shared import Inches

def draw_figure(x_name, y_name, dic_relation, filename = 'untitled'):
    show_figure(x_name, y_name, dic_relation, filename)

def main_it():
    dic_t_at = input_dic()
    dic_t_lna1 = relation(dic_t_at, -3.55)
    print(dic_t_lna1)
    # show_figure(dic_t_lna1, 11)

def input_dic():
    """
    返回你输入数据关系的字典
    """
    dic = {}
    while True:
        t = input("t(input 'quit' to quit): ")  # 输入变量
        if t == 'quit':
            break
        at = input("at: ")  #  输入因变量
        dic[float(t)] = float(at)
    return dic

def liner_fit(X, Y):
    """
    线性拟合函数, 输入变量的集合(X)和因变量的集合(Y), 返回斜率(a)和截距(b)
    """
    z1 = np.polyfit(X, Y, 1)
    a = z1[0]
    b = z1[1]
    return a, b

def relation(dic_t_at, ain):
    """
    关系函数, 输入变量和参数, 返回变量和因变量的字典
    并打印出
    """
    dic_t_lna1 = {}
    data = {
        't' : [],
        'a1' : [],
        'lna1' : []  #  添加需要输出的数据
    }
    for t, at in dic_t_at.items():
        a1 = at - ain
        lna1 = math.log(a1)
        dic_t_lna1[t] = lna1
        data['t'].append(t)  #  添加需要输出的数据
        data['a1'].append(a1)
        data['lna1'].append(lna1)
    print(DataFrame(data).T)  #  打印包含所需数据的DataFrame
    return dic_t_lna1

def show_figure(x_name, y_name, dic_t_lna1, filename):
    """
    画图, 输入变量和因变量的字典, 输出图表
    """
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)  # (x轴有几个图表, y轴有几个图表, 索引(第几个))

    Keys, Values = list(dic_t_lna1.keys()), list(dic_t_lna1.values())
    ax.plot(Keys, Values, 'o')  # 绘制测得的数据点
    a, b = liner_fit(Keys, Values)  # a, b = 斜率, 截距
    print("k = ", a)  # 打印斜率

    X = np.arange(Keys[0], Keys[-1], 0.01)  # 获得一串较为密集的线性拟合函数的变量的集合(X)和因变量的集合(Y)
    Y = []
    for x in X:
        Y.append(x*a+b)
    ax.plot(X, Y, 'k')
    ax.set_title('{x}~{y}'.format(x = x_name, y = y_name))  # 输入标题
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.savefig('{}.png'.format(filename))  # 输入你的文件名
    plt.show()
    # save(filename)

"""
def save(filename):
    document = Document()
    document.add_picture('{}.png'.format(filename), width=Inches(4.5))
    document.save('{}.docx'.format(filename))
"""


if __name__ == "__main__":
    main_it()