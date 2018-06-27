from wtforms import PasswordField,StringField
from wtforms import widgets
from wtforms.widgets import Input

from wtforms.compat import text_type, iteritems

#写一个是img的标签,这个最底层的
class ImgInput(Input):

    input_type = "x"
    ##

    #重写 __call__部分
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        if 'required' not in kwargs and 'required' in getattr(field, 'flags', []):
            kwargs['required'] = True
        return HTMLString('<img %s>' % self.html_params(name=field.name, **kwargs))        



##写图片导入字段，img field
class ImgField(StringField):
    widget = ImgInput()
    


##自己定义的密码字段，不过这个是允许返回密码值
class return_password(PasswordField):

    widget = widgets.PasswordInput(hide_value=False)



class HTMLString(text_type):
    """
    This is an "HTML safe string" class that is returned by WTForms widgets.

    For the most part, HTMLString acts like a normal unicode string, except
    in that it has a `__html__` method. This method is invoked by a compatible
    auto-escaping HTML framework to get the HTML-safe version of a string.

    Usage::

        HTMLString('<input type="text" value="hello">')

    """
    def __html__(self):
        """
        Give an HTML-safe string.

        This method actually returns itself, because it's assumed that
        whatever you give to HTMLString is a string with any unsafe values
        already escaped. This lets auto-escaping template frameworks
        know that this string is safe for HTML rendering.
        """
        return self




