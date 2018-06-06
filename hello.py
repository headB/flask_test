from flask import Flask,render_template
#Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.wtf import From 
from wtforms import Form,StringField,SubmitField
from wtforms.validators import Required

##尝试引入flask-script
from flask.ext.script import Manager



##为表单添加的模块或者函数
from flask import session,redirect,url_for,flash

##测试加入表单,不过表单应该是写在模板里面?

class NameForm(Form):
    name = StringField("what is you name?",validators=[Required()])
    submit = SubmitField('Submit')

##创建一个Flask示例,并且给定初始化参数
app = Flask(__name__)

bootstrap = Bootstrap(app)

manager = Manager(app)

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

##测试第二个模板渲染
@app.route("/test_temp")
def test2_templates():
    form = NameForm



##测试bootstrap模板
@app.route("/boot_test")
def boot_test():
    return render_template('boot_base.html')




if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()