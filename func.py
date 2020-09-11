from functools import reduce

def strtofloat(s):
    if s.find(",") == -1:
        return float(s)
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    b=0 #计算小数位数
    i=0
    while i<len(s):
        if s[i]=='.':
            b=len(s)-i-1
        i=i+1

    s=s[:(len(s)-b-1)]+s[(len(s)-b):]
    #字符转换为整数
    def f1(s):
        return DIGITS[s]
    #exp:1,2转换为12
    def f2(a,b):
        return a*10+b
    def f3(s): #整数转换为浮点数
        for _ in range(b):
            s=s*0.1
        return s
    return (f3(reduce(f2,map(f1,s))))