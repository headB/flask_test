from flask import Flask,render_template,flash
#Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.wtf import From 
from wtforms import StringField,SubmitField,PasswordField
from flask_wtf import Form
#import flask_wtf import FlaskForm
from wtforms.validators import Required

##尝试引入flask-script
#from flask.ext.script import Manager
from flask_script import Manager

##导入nav
from flask_nav import Nav
from flask_nav.elements import *

##尝试使用数据库，个人感觉比较喜欢用sqlite3
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))


##为表单添加的模块或者函数
from flask import session,redirect,url_for,flash



##创建一个Flask示例,并且给定初始化参数
app = Flask(__name__)
##需要全局设置一个csrf
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)

nav = Nav()

nav.register_element('top',Navbar(u'flask入门',View(u'你好','test_templates'),
View(u'栏目测试','test_base'),
View(u'测试表单 ','test_form'),
View(u'点击注册 ','register_form'),
))

##初始化一个nav
nav.init_app(app)


##编辑一下链接数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

##定义模型
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

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
    name = StringField('账号', validators=[Required()],render_kw={'placeholder':'请输入你的名字!?'})
    password = PasswordField('密码',validators=[Required()],render_kw={"placeholder":"请输入密码"})
    verityCode = StringField('验证码',validators=[Required()],render_kw={"placeholder":"请输入验证码","autocomplete":"off"})
    submit = SubmitField('点击提交!')

class RegisterForm(NameForm):
    submit = SubmitField('点击注册!')

@app.route("/test_form",methods=['GET','POST'])
def test_form():  
    name = None
    form = NameForm()
    if form.validate_on_submit():
        #name = form.name.data
        #form.name.data = ''
        flash("你已经成功提交信息，请稍等！")
        #return redirect("http://www.baidu.com")
    else:
        flash("欢迎莅临本站点，你是第一次进入，请输入你需要注册的账号和密码！")
    return render_template('test_form.html',name=name,form=form)

##设置一个类似注册入库的函数
@app.route('/register',methods=['GET','POST'])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        #检测已经提交表单，检查参数
        flash("这里是首页！")
        print(dir(form))
        print(request.form['name'])
        print(request.form['password'])
        
        admin = Admin(name=request.form['name'])

        ##添加到回话中

        db.session.add(admin)
        #提交
        db.session.commit()

        return render_template("base.html")
    else:
        return render_template('register.html',form=form)

if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()