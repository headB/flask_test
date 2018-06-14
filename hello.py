from flask import Flask,render_template
#Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.wtf import From 
from wtforms import StringField,SubmitField
from flask_wtf import Form
#import flask_wtf import FlaskForm
from wtforms.validators import Required

##尝试引入flask-script
from flask.ext.script import Manager

##导入nav
from flask_nav import Nav
from flask_nav.elements import *




##为表单添加的模块或者函数
from flask import session,redirect,url_for,flash



##创建一个Flask示例,并且给定初始化参数
app = Flask(__name__)
##需要全局设置一个csrf
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)

nav = Nav()

nav.register_element('top',Navbar(u'flask入门',View(u'你好','test_base'),
View(u'我是测试表单','test_form'),
View(u'测试模板渲染 ','test_form'),))

##初始化一个nav
nav.init_app(app)

##上面导入了一个manger,用于其他方式去载入flask

##定义第一个视图
##传智说过,视图+url处理就是一个web框架了.!!模板渲染是附加的功能!

@app.route("/")
def index():
    return render_template('index.html')
#return "<h1>hello world!but the way,it's so like php!</h1>"

@app.route('/user/<name>')
def username(name):
    #return "<h1>hello %s!</h1>" %name
    return render_template('index.html')


##测试静态文件!
@app.route("/test")
def test_templates():
    dict1 = {"name":"kumanxuan"}
    return render_template('index.html',name=dict1)

##测试第二个模板渲染
@app.route("/test_temp")
def test2_templates():
    form = NameForm

##测试base.html里面的静态内容.
@app.route("/test_base")
def test_base():
    return render_template('base.html')

##测试bootstrap模板
@app.route("/boot_test")
def boot_test():
    return render_template('boot_base.html')

##测试没有继承管理的模板
@app.route("/test_no_extends")
def test_no_extends():
    return render_template('no_extends.html')

##测试表单!
##测试加入表单,不过表单应该是写在模板里面?

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()],render_kw={'placeholder':'请输入你的名字!?'})
    submit = SubmitField('点击提交!')

@app.route("/test_form",methods=['GET','POST'])
def test_form():

    
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('test_form.html',name=name,form=form)


if __name__ == "__main__":
    app.run(debug=True)
    #manager.run()