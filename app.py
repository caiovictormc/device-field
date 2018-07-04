# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 21:46:16
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-07-02 15:27:23

from flask import Flask, jsonify, render_template
from prettyconf import config

from views import DeviceView, MQTTAuthView, MQTTAclView, MQTTAdminView


app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')


# BASE URLs
API_BASE_URL = '/api/v1/'
MQTT_BASE_URL = '/mqtt/v1/'

# API URLs
app.add_url_rule(
	API_BASE_URL + 'device', 
	view_func=DeviceView.as_view('device'))

# MQTT Auth URLs
app.add_url_rule(
	MQTT_BASE_URL + 'auth', 
	view_func=MQTTAuthView.as_view('mqtt-auth'))

app.add_url_rule(
	MQTT_BASE_URL + 'superuser', 
	view_func=MQTTAdminView.as_view('mqtt-admin'))

app.add_url_rule(
	MQTT_BASE_URL + 'acl', 
	view_func=MQTTAclView.as_view('mqtt-acl'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=config('PORT'), use_reloader=True, debug=True)