# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 21:46:16
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-30 11:52:03

from flask import Flask, jsonify, render_template
from prettyconf import config

from views import Device


app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')


# URLs
BASE_ENDPOINT = '/api/v1/'

app.add_url_rule(BASE_ENDPOINT + 'device', view_func=Device.as_view('device'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=config('PORT'), use_reloader=True, debug=True)