# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# sqlarhry seting
#  class User(Base):
#     __tabelname__ = "user"
#     id = Column(Integer,primary_key=True,autoincrement=True) # 默认主键列就是autoincrement=True
#     name  = Column(String(50),nullable=False)# 默认nullable=Trus
#     password = Column(String(50))
#
#     def __repr__(self):
#         return '<User(id="%s",username="%s",password="%s)>' % (self.id, self.username, self.password)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()