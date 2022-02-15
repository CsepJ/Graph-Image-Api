from numpy import *
import matplotlib.pyplot as plt
from flask import Flask
import math as Math
import re as regexp
import os
app=Flask(__name__,static_folder="./image/")
@app.route("/")
def home():
    return '''
    <h1>Hello user</h1>
    '''

@app.route("/function/<string:function>")
def func(function):
    print(function)
    x = arange(0,100)
    try:
        comFunc = function.replace("^", "**").replace("×", "*").replace("÷", "/").replace("²","**2").replace("½", "**1/2").replace("³", "**3").replace("⁴", "**4").replace("⅓", "**1/3").replace("⅔", "**2/3").replace("¼", "**1/4").replace("¾", "**3/4")
        text = regexp.sub("[ㄱ-힣]", "", comFunc)
        array = []
        result = regexp.split('(?:-)|(?:\+)', text)
        resultWithpm = regexp.split("(-|\+)", text)
        for word in result:
            index=int(result.index(word))
            pm = "+" if index==0 else resultWithpm[index*2-1]
            num = "0" if regexp.sub("^((?!((\d)|(x)|(Math.)+(\w{1,})\(x\)|(Math.)+(\w{1,}))).)*$","",word) == "" else regexp.sub("^((?!((\d)|(x)|(Math.)+(\w{1,})\(x\)|(Math.)+(\w{1,}))).)*$","",word)
            array.insert(index,pm+num)
        "".join(array)
        y = eval(array)
        plt.plot(x,y)
        plt.title(function)
        plt.grid(True)
        plt.savefig(os.path.dirname(os.path.abspath(__file__))+"/image/plot-"+function+".png", dpi=95)
        plt.cla()
        return "Good"
    except:
        return "Error!"
