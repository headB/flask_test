from flask import Blueprint
##初始化

register = Blueprint("register",__name__,)

from . import views

