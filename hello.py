from flask import Flask,render_template,flash
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.wtf import From 
from wtforms import StringField,SubmitField,PasswordField,HiddenField
#from wtforms import *
#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.validators import Required,EqualTo

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
View(u'查看用户 ','user'),
))

##初始化一个nav
nav.init_app(app)


##编辑一下链接数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

##定义模型
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))

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

class NameForm(FlaskForm):
    name = StringField('账号', validators=[Required()],render_kw={'placeholder':'请输入你的名字!?'})
    password = PasswordField('密码',validators=[Required(),EqualTo('password2')],render_kw={"placeholder":"请输入密码"})
    password2 = PasswordField('验证密码',validators=[Required()],render_kw={"placeholder":"请输入密码"})
    verityCode = StringField('验证码',validators=[Required()],render_kw={"placeholder":"请输入验证码","autocomplete":"off"})
    submit = SubmitField('点击提交!')

class RegisterForm(NameForm):
    submit = SubmitField('点击注册!')

class ModifiedRegister(NameForm):
    id = HiddenField()
    password = PasswordField('密码',validators=[EqualTo('password2')],render_kw={"placeholder":"不输入就表示不修改密码"})
    password2 = PasswordField('验证密码',validators=[],render_kw={"placeholder":"请输入密码"})
    verityCode = StringField('验证码',validators=[Required()],render_kw={"placeholder":"请输入验证码","autocomplete":"off"})
    submit = SubmitField('点击修改!')

@app.route("/test_form",methods=['GET','POST'])
def test_form():  
    name = None
    form = NameForm()

    ##获取指定admin表的数据。
    admin_data = Admin().query.all()

    if form.validate_on_submit():
        #name = form.name.data
        #form.name.data = ''
        flash("你已经成功提交信息，请稍等！")
        #return redirect("http://www.baidu.com")
    else:
        flash("欢迎莅临本站点，你是第一次进入，请输入你需要注册的账号和密码！")
    return render_template('test_form.html',name=name,form=form,admin_data=admin_data)

##设置一个类似注册入库的函数
##比较贪心，不过这里顺便设置一个如果获取到id，意味着需要修改对应id的数据。！
@app.route('/register',methods=['GET','POST'])
def register_form():
    form = RegisterForm()
    id = request.args.get('id')
    if id:
        
        admins = Admin().query.filter_by(id=id).first()

        form = ModifiedRegister()

        if admins and request.method != "POST":
            
            
            form.name.data = admins.name
            form.id.data = admins.id
            
            return render_template("register.html",form=form,operate="修改")
        
        elif request.method == "GET":
            flash("你查询的数据，恩恩，是不存在的！")
            return render_template("base.html")
        

    if form.validate_on_submit():
        #检测已经提交表单，检查参数

        id = request.form.get("id")


        if id:
            admins.name = form.name.data
            if request.form.get("password"):
                admins.password = request.form.get("password")
            
            db.session.add(admins)
        else:
        
            admin = Admin(name=request.form['name'],password=request.form['password'])

            db.session.add(admin)
            #提交
            db.session.commit()

        ##添加到回话中

        flash("数据验证并且提交成功！")
        #return render_template("user.html")
        return redirect(url_for('user'))
    else:
        return render_template('register.html',form=form,operate="注册")

##查看用户表数据
@app.route("/user",methods=['GET','POST'])
def user():
    id = request.args.get('id')
    if id:
        object1 = Admin().query.filter_by(id=id).first()
        if object1:
            db.session.delete(object1)
        else:
            flash("没有该对象信息")

    admin_data = Admin().query.all()
    return render_template('user.html',admin_data=admin_data)

#测试验证码
@app.route("/verify_code")
def verify_code():
    from test_verify import generate_verify
    from flask import make_response

    image_code,verify_str_code = generate_verify()

    print(verify_str_code)

    response = make_response(image_code)

    response.headers['Content-Type'] = "image/gif"
    
    return response


if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()