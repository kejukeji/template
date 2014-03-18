# coding: UTF-8
from . import app
from flask.ext.admin import Admin
from flask.ext import restful

# 用户管理路径
# app.add_url_rule('url','method_name', method_name, method=('GET','POST'))


# 接口定义
# api = restful.Api(app)
# api.add_resource(InterfaceClass, '/url')


# 后台管理路径
# admin = Admin(app)
# admin.add_view(UserCollectView(db, name=u'用户收藏(后台前端显示导航菜单,子菜单)', category=u'功能(主菜单)'))
# admin.add_view(UserManagerView(db, name=u'用户管理(后台前端显示导航菜单,子菜单)', category=u'功能(主菜单)'))