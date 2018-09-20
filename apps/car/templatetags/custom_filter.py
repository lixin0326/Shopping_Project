"""
1>语法格式
2>内置过滤器
3>不满足需求时,可以自定义过滤器
   1.在app下新建一个templatetags文件夹
   2.文件夹里面新建一个py文件
   3.实例化注册器
   4.声明过滤器(过滤器的本质是一个函数)
   5.注册过滤器@register.filter
   6.模板中可以使用过滤器

"""

from django import template

# 实例化注册器(规定格式)
register = template.Library()


@register.filter
def multiply(value, params):
    return value * params
