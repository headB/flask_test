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


