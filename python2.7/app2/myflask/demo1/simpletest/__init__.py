#!/usr/bin/env python
# coding: utf-8

import shelve
from datetime import datetime
from flask import Flask, request, render_template, redirect, escape , Markup
application = Flask(__name__)

DATA_FILE='guestbook.dat'

#保存留言数据
def save_data(name,comment,create_at):
	"""
	保存留言数据
	"""
	# shelve 相当于一个文件形式字典
	database = shelve.open(DATA_FILE)
	if 'greeting_list' not in database:
		#如果字典里没有greeting_list 这个键值
		greeting_list = []
	else:
		#从数据库取出数据
		greeting_list = database['greeting_list']
	
	#将传进来的数据添加到第一个位置greeting_list 是一个列表类型
	greeting_list.insert(0,{
		'name':name,
		'comment':comment,
		'create_at':create_at
	})
	#更新数据库
	database['greeting_list'] = greeting_list	
	#关闭数据库
	database.close()

	
#获取保存的数据
def load_data():
        """返回已经保存的数据[
		{'name':name,
                'comment':comment,
                'create_at':create_at},]
	"""
        database = shelve.open(DATA_FILE)
        greeting_list = database.get("greeting_list",[])
        database.close()
        return greeting_list

@application.route("/post", methods=['POST'])
def post():
	"""
	用于提交评论的URL
	"""
	#获取已经提交的数据
	name = request.form.get("name")
	#name = request.form.get('name') # 名字
	comment = request.form.get("comment")
	create_at = datetime.now()
	#保存数据
	save_data(name,comment,create_at)
	#重定向到/
	return redirect("/")


@application.route("/")
def index():
	"""首页"""
	greeting_list=load_data()
	return render_template("index.html", greeting_list=greeting_list)

@application.template_filter('nl2br')
def nl2br_filter(s):
	'''
	将换行符转换为br
	'''
	return escape(s).replace('\n', Markup('<br>'))
	
@application.template_filter('datetime_fmt')
def nl2br_filter(dt):
	'''
	使datetime 对象更容易分辨
	dt =datetime.datetime.now() 
	'''
	return dt.strftime('%Y/%m/%d %H:%M:%S')

if __name__ == "__main__":
	application.run("0.0.0.0",80,debug=True)
