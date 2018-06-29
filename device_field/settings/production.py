# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 19:14:26
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-29 20:00:47

from .base import *

from prettyconf import config
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}