# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 19:13:56
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-29 20:01:56

from .base import *

import os


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}