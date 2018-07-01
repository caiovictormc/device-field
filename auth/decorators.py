# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-30 18:37:48
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-30 20:17:02

from flask import request, Response, jsonify

from functools import wraps



def check_auth(token):
    return True


def authenticate():
    response = jsonify({
		"errors": {
			"message": "You have to login with proper credentials"
		}
	})	
    response.status_code = 401
    return response


def get_auth_token(request):
	headers = request.headers
	return headers.get('Authorization')


def auth_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
	    token = get_auth_token(request)
	    if not check_auth(token):
	        return authenticate()
	    return f(*args, **kwargs)
	return decorated
