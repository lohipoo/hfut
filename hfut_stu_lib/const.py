# -*- coding:utf-8 -*-
from __future__ import unicode_literals, division

SITE_ENCODING = 'gbk'
HOST_URL = 'http://222.195.8.201/'

GUEST = 'guest'
STUDENT = 'student'
TEACHER = 'teacher'
ADMIN = 'admin'
USER_TYPES = (STUDENT, TEACHER, ADMIN)

GET = 'get'
POST = 'post'
METHODS = (GET, POST)

HTML_PARSER = 'lxml'