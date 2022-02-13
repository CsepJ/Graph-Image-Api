import numpy as np
import matplotlib.pyplot as plt
from flask import Flask

app=Flask(__name__, static_url_path='/image')
@app.route("/")
def home():
    return '''
    <h1>Hello user</h1>
    '''

@app.route("/function/<string:function>")
def func(function):
    print(function)
    x = np.arange(0,100)
    y = eval(function)
    plt.plot(x,y)
    plt.title(function)
    plt.grid(True)
    plt.box(True)
    plt.subplot(1,1,1)
    plt.savefig("image/plot.png", dpi=95)
    plt.cla()
    return "Good"

if __name__ == '__main__':
    app.run(debug=False, port=3000)