1. 第一部分程序的基本结构
    1. 初始化
    ```python
    from flask import Flask
    app = Flask(__name__)
    ```
    Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python 的__name__ 变量就是所需的值。    

    2. 路由和视图函数
    在Flask 程序中定义路由的最简便方式，是使用程序实例提供的app.route 修饰器，把修
    饰的函数注册为路由。下面的例子说明了如何使用这个修饰器声明路由：
    ```python
    @app.route('/')
    def index():
    return '<h1>Hello World!</h1>'
    ```
    如果你仔细观察日常所用服务的某些URL 格式，会发现很多地址中都包含可变部分。例
    如， 你的Facebook 资料页面的地址是http://www.facebook.com/<your-name>， 用户名
    （your-name）是地址的一部分。Flask 支持这种形式的URL，只需在route 修饰器中使用特
    殊的句法即可。下例定义的路由中就有一部分是动态名字：
    ```python
    @app.route('/user/<name>')
    def user(name):
    return '<h1>Hello, %s!</h1>' % name

    ```
    路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由/user/<int:id>
    只会匹配动态片段id 为整数的URL。Flask 支持在路由中使用int、float 和path 类型。
    path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。

    3. 启动服务器
    > 程序实例用run 方法启动Flask 集成的开发Web 服务器：
    ```python
    if __name__ == '__main__':
    app.run(debug=True)
    ```
    __name__=='__main__' 是Python 的惯常用法，在这里确保直接执行这个脚本时才启动开发
    Web 服务器。如果这个脚本由其他脚本引入，程序假定父级脚本会启动不同的服务器，因
    此不会执行app.run()。
    服务器启动后，会进入轮询，等待并处理请求。轮询会一直运行，直到程序停止，比如按
    Ctrl-C 键。

    4. 一个完整的程序
    ```python
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def index():
    return '<h1>Hello World!</h1>'
    if __name__ == '__main__':
    app.run(debug=True)
    ```



2. 模板
    1. 
    2. jinja2变量过滤器
    ```python
    过滤器名    说　　明
    safe        渲染值时不转义
    capitalize  把值的首字母转换成大写，其他字母转换成小写
    lower       把值转换成小写形式
    upper       把值转换成大写形式
    title       把值中每个单词的首字母都转换成大写
    trim        把值的首尾空格去掉
    striptags   渲染之前把值中所有的HTML 标签都删掉
    ```
    3. Flask-Bootstrap基模板中定义的块
    ```python
    块　　名    说　　明
    doc             整个HTML 文档
    html_attribs    <html> 标签的属性
    html <html>     标签中的内容
    head <head>     标签中的内容
    title <title>   标签中的内容
    metas           一组<meta> 标签
    styles          层叠样式表定义
    body_attribs    <body> 标签的属性
    body            <body> 标签中的内容
    navbar          用户定义的导航条
    content         用户定义的页面内容
    scripts         文档底部的JavaScript 声明
    ```

3. web表单
    1. 跨站请求伪造保护

    2. 表单类
    ```python
    from flask.ext.wtf import Form
    from wtforms import StringField, SubmitField
    from wtforms.validators import Required
    class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    ```
    这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象。在这个示例中，
    NameForm 表单中有一个名为name 的文本字段和一个名为submit 的提交按钮。StringField
    类表示属性为type="text" 的< input> 元素。SubmitField 类表示属性为type="submit" 的
    < input> 元素。字段构造函数的第一个参数是把表单渲染成HTML 时使用的标号。
    StringField 构造函数中的可选参数validators 指定一个由验证函数组成的列表，在接受
    用户提交的数据之前验证数据。验证函数Required() 确保提交的字段不为空。

    以下为WTForms支持的HTML标准字段
    ```
    StringField     文本字段
    TextAreaField   多行文本字段
    PasswordField   密码文本字段
    HiddenField     隐藏文本字段
    DateField       文本字段，值为datetime.date 格式
    DateTimeField   文本字段，值为datetime.datetime 格式
    IntegerField    文本字段，值为整数
    DecimalField    文本字段，值为decimal.Decimal
    FloatField      文本字段，值为浮点数
    BooleanField    复选框，值为True 和False
    RadioField      一组单选框
    SelectField     下拉列表
    SelectMultipleField 下拉列表，可选择多个值
    FileField       文件上传字段
    SubmitField     表单提交按钮
    FormField       把表单作为字段嵌入另一个表单
    FieldList       一组指定类型的字段
    ```

    WTForms常见的验证函数(前端正则)
    ```python
    验证函数    说　　明
    Email       验证电子邮件地址
    EqualTo     比较两个字段的值；常用于要求输入两次密码进行确认的情况
    IPAddress   验证IPv4 网络地址
    Length      验证输入字符串的长度
    NumberRange 验证输入的值在数字范围内
    Optional    无输入值时跳过其他验证函数
    Required    确保字段中有数据
    Regexp      使用正则表达式验证输入值
    URL         验证URL
    AnyOf       确保输入值在可选值列表中
    NoneOf      确保输入值不在可选值列表中
    ```

    3. 把表单渲染成HTML
    表单字段是可调用的，在模板中调用后会渲染成HTML。假设视图函数把一个NameForm 实例通过参数form 传入模板，在模板中可以生成一个简单的表单，如下所示：
    ```python
    <form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
    </form>
    ```

    当然，这个表单还很简陋。要想改进表单的外观，可以把参数传入渲染字段的函数，传入
    的参数会被转换成字段的HTML 属性。例如，可以为字段指定id 或class 属性，然后定
    义CSS 样式：
    ```python
    <form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
    </form>

    ```

    即便能指定HTML 属性，但按照这种方式渲染表单的工作量还是很大，所以在条件允许的
    情况下最好能使用Bootstrap 中的表单样式。Flask-Bootstrap 提供了一个非常高端的辅助函
    数，可以使用Bootstrap 中预先定义好的表单样式渲染整个Flask-WTF 表单，而这些操作
    只需一次调用即可完成。使用Flask-Bootstrap，上述表单可使用下面的方式渲染：

    ```python
    {% import "bootstrap/wtf.html" as wtf %}
    {{ wtf.quick_form(form) }}

    ```
    import 指令的使用方法和普通Python 代码一样，允许导入模板中的元素并用在多个模板
    中。导入的bootstrap/wtf.html 文件中定义了一个使用Bootstrap 渲染Falsk-WTF 表单对象
    的辅助函数。wtf.quick_form() 函数的参数为Flask-WTF 表单对象，使用Bootstrap 的默认
    样式渲染传入的表单。hello.py 的完整模板如示例4-3 所示。

    示例4-3　templates/index.html：使用Flask-WTF 和Flask-Bootstrap 渲染表单
    ```python
    {% extends "base.html" %}
    {% import "bootstrap/wtf.html" as wtf %}
    {% block title %}Flasky{% endblock %}
    {% block page_content %}
    <div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
    </div>
    {{ wtf.quick_form(form) }}
    {% endblock %}
    ```
    ## 还有一些关于wtf的故事
    3. 还有一些关于wtf的故事
        1. 在定义字段的时候,可以再后面用render_kw追加参数.!
            ```python
            name = StringField('What is your name?', validators=[Required()],render_kw={'placeholder':'请输入你的名字!?'})
                submit = SubmitField('点击提交!')
            ```
        2. 自行编写代码解决 WTForm 无纯 Button 按钮的问题——input篇
        > 当然这样的设计与该库本身立足于页面表单功能是紧密相连的。对于表单来说，按钮的最大功能就是提交表单。然而，我们并不能排除在一个表单中存在多个按钮，用于提供不同功能的情况。所以，单纯的 SubmitField 所实现的提交按钮就显得非常局限。此时，我们就需要利用 WTForm 提供的自定义 Field 和 Widget 功能，自己编写代码，来实现自己想要的按钮功能。

        https://blog.csdn.net/tiwoo/article/details/46038249

        3. 修改quick.form
        ```python
        {{ _wtf4.quick_form(form, form_type="basic ", button_map={'submit':'primary', } ) }}
        ```





    4. 数据库
        1. 使用Flask-SQLAchemy管理数据库
        Flask-SQLAlchemy 是一个 Flask 扩展,简化了在 Flask 程序中使用 SQLAlchemy 的操作。
        SQLAlchemy 是一个很强大的关系型数据库框架,支持多种数据库后台。SQLAlchemy 提
        供了高层 ORM,也提供了使用数据库原生 SQL 的低层功能。
        和其他大多数扩展一样,Flask-SQLAlchemy 也使用 pip 安装:
        (venv) $ pip install flask-sqlalchemy
        2. FLask-SQLAlchemy数据库URL
        >MySQL mysql://username:password@hostname/database
        Postgres postgresql://username:password@hostname/database
        SQLite(Unix) sqlite:////absolute/path/to/database
        SQLite(Windows) sqlite:///c:/absolute/path/to/database

        3. 示例
        ```python
        from flask.ext.sqlalchemy import SQLAlchemy
        basedir = os.path.abspath(os.path.dirname(__file__))
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        db = SQLAlchemy(app)
        #db 对象是 SQLAlchemy 类的实例,表示程序使用的数据库,同时还获得了 Flask-SQLAlchemy
        #提供的所有功能。
        ```

        4. 定义模型。
        >模型这个术语表示程序使用的持久化实体。在 ORM 中,模型一般是一个 Python 类,类中
        的属性对应数据库表中的列。
        Flask-SQLAlchemy 创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函
        数,可用于定义模型的结构。图 5-1 中的 roles 表和 users 表可定义为模型 Role 和 User ,
        如示例 5-2 所示。
        ```python
        class Role(db.Model):
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=True)
            def __repr__(self):
                return '<Role % r>' % self.name
        class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), unique=True, index=True)
            def __repr__(self):
                return '<User % r>' % self.username
        #类变量 __tablename__ 定义在数据库中使用的表名。如果没有定义 __tablename__ ,Flask-
        #数据库 | 47SQLAlchemy 会使用一个默认名字,但默认的表名没有遵守使用复数形式进行命名的约定,
        #所以最好由我们自己来指定表名。其余的类变量都是该模型的属性,被定义为 db.Column
        #类的实例。
        #db.Column 类构造函数的第一个参数是数据库列和模型属性的类型。表 5-2 列出了一些可用
        #的列类型以及在模型中使用的 Python 类型。
        ```

        最常用的SQLAlchemy列类型
        ```python
        类型名          Python类型      说明
        Integer         int     普通整数,一般是 32 位
        SmallInteger    int    取值范围小的整数,一般是 16 位
        BigInteger      int 或 long     不限制精度的整数
        Float           float 浮点数
        Numeric decimal.Decimal     定点数
        String          str    变长字符串
        Text            str     变长字符串,对较长或不限长度的字符串做了优化
        Unicode         unicode 变长 Unicode 字符串
        UnicodeText     unicode 变长 Unicode 字符串,对较长或不限长度的字符串做了优化
        Boolean         bool 布尔值
        Date            datetime.date 日期
        Time             datetime.time 时间
        DateTime        datetime.datetime 日期和时间
        Interval        datetime.timedelta 时间间隔
        Enum            str 一组字符串
        PickleType      任何 Python 对象 自动使用 Pickle 序列化
        LargeBinary     str 二进制文件
        ```

        最常使用的SQLAlchemy列选项
        ```python
        选项名         说明
        primary_key   如果设为 True ,这列就是表的主键
        unique        如果设为     True ,这列不允许出现重复的值
        index         如果设为   True ,为这列创建索引,提升查询效率
        nullable      如果设为   True ,这列允许使用空值;如果设为 False ,这列不允许使用空值
        default       为这列定义默认值

        ```
        5. 创建表
        首先,我们要让 Flask-SQLAlchemy 根据模型类创建数据库。方法是使用 db.create_all()
        函数:
        (venv) $ python hello.py shell
        >>> from hello import db
        >>> db.create_all()
        如果你查看程序目录,会发现新建了一个名为 data.sqlite 的文件。这个 SQLite 数据库文件
        的名字就是在配置中指定的。如果数据库表已经存在于数据库中,那么 db.create_all()
        不会重新创建或者更新这个表。如果修改模型后要把改动应用到现有的数据库中,这一特
        性会带来不便。更新现有数据库表的粗暴方式是先删除旧表再重新创建:
        >>> db.drop_all()
        >>> db.create_all()
        50 | 第 5 章遗憾的是,这个方法有个我们不想看到的副作用,它把数据库中原有的数据都销毁了。本
        章末尾将会介绍一种更好的方式用于更新数据库。

        6. 插入行
        下面这段代码创建了一些角色和用户:
        >>>
        >>>
        >>>
        >>>
        >>>
        >>>
        >>>
        from hello import Role, User
        admin_role = Role(name='Admin')
        mod_role = Role(name='Moderator')
        user_role = Role(name='User')
        user_john = User(username='john', role=admin_role)
        user_susan = User(username='susan', role=user_role)
        user_david = User(username='david', role=user_role)
        模型的构造函数接受的参数是使用关键字参数指定的模型属性初始值。注意, role 属性也
        可使用,虽然它不是真正的数据库列,但却是一对多关系的高级表示。这些新建对象的 id
        属性并没有明确设定,因为主键是由 Flask-SQLAlchemy 管理的。现在这些对象只存在于
        Python 中,还未写入数据库。因此 id 尚未赋值:
        >>> print(admin_role.id)
        None
        >>> print(mod_role.id)
        None
        >>> print(user_role.id)
        None
        通过数据库会话管理对数据库所做的改动,在 Flask-SQLAlchemy 中,会话由 db.session
        表示。准备把对象写入数据库之前,先要将其添加到会话中:
        >>>
        >>>
        >>>
        >>>
        >>>
        >>>
        db.session.add(admin_role)
        db.session.add(mod_role)
        db.session.add(user_role)
        db.session.add(user_john)
        db.session.add(user_susan)
        db.session.add(user_david)
        或者简写成:
        >>> db.session.add_all([admin_role, mod_role, user_role,
        ...
        user_john, user_susan, user_david])
        为了把对象写入数据库,我们要调用 commit() 方法提交会话:
        >>> db.session.commit()
        再次查看 id 属性,现在它们已经赋值了:
        数据库 | 51>>> print(admin_role.id)
        1
        >>> print(mod_role.id)
        2
        >>> print(user_role.id)
        3
        数据库会话 db.session 和第 4 章介绍的 Flask session 对象没有关系。数据库
        会话也称为 事务 。
        数据库会话能保证数据库的一致性。提交操作使用原子方式把会话中的对象全部写入数据
        库。如果在写入会话的过程中发生了错误,整个会话都会失效。如果你始终把相关改动放
        在会话中提交,就能避免因部分更新导致的数据库不一致性。
        数据库会话也可 回滚 。调用 db.session.rollback() 后,添加到数据库会话
        中的所有对象都会还原到它们在数据库时的状态。