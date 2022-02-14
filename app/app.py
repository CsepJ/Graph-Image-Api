from numpy import *
import matplotlib.pyplot as plt
from flask import Flask
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
        let comFunc = function.replace("^", "**").replace("×", "*").replace("÷", "/").replace("²","**2").replace("½", "**1/2").replace("³", "**3").replace("⁴", "**4").replace("⅓", "**1/3").replace("⅔", "**2/3").replace("¼", "**1/4").replace("¾", "**3/4")
        y = eval(comFunc)
        plt.plot(x,y)
        plt.title(function)
        plt.grid(True)
        plt.savefig(os.path.dirname(os.path.abspath(__file__))+"/image/plot.png", dpi=95)
        plt.cla()
        return "Good"
    except:
        return "Error!"

if __name__ == "__main__":
    app.run(port=3000, debug=True)
