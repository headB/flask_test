from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap


##创建一个Flask示例,并且给定初始化参数
app = Flask(__name__)

bootstrap = Bootstrap()

##定义第一个视图
##传智说过,视图+url处理就是一个web框架了.!!模板渲染是附加的功能!

@app.route("/")
def index():

    return "<h1>hello world!but the way,it's so like php!</h1>"

@app.route('/user/<name>')
def username(name):
    return "<h1>hello %s!</h1>" %name


##测试静态文件!
@app.route("/test")
def test_templates():
    dict1 = {"name":"kumanxuan"}
    return render_template('index.html',name=dict1)

if __name__ == "__main__":
    app.run(debug=True)