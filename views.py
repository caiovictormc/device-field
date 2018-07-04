# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 22:18:31
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-07-02 15:57:01

from flask import Response, jsonify, request
from flask.views import MethodView

from bson import json_util

from auth.decorators import auth_required
from db.models import Device



class MQTTAdminView(MethodView):
    """
    Check if the username is a superuser
    """

    def post(self):
        data = request.form
        status_code = 401

        print(data)

        # if data:
        #     username = data.get('username')
        #     status_code = 200

        return Response(status=status_code, content_type='text/plain')



class MQTTAuthView(MethodView):
    """
    Dynamically authenticates MQTT requests
    """

    def post(self):
        data = request.form
        status_code = 401

        print(data)

        if data:
            username = data.get('username')
            password = data.get('password')

            device = Device.filter(mqtt_username=username,mqtt_password=password)

            if device:
                status_code = 200

        return Response(status=status_code, content_type='text/plain')


class MQTTAclView(MethodView):

    def post(self):
        data = request.form
        status_code = 401

        print(data)

        if data:
            username = data.get('username')
            topic = data.get('topic')
            client_id = data.get('clientid')

            status_code = 200

        return Response(status=status_code, content_type='text/plain')


class DeviceView(MethodView):

    decorators = [auth_required]

    def post(self):
        data = request.json
        status_code = 200

        try:
            device = Device(**data)
            device.save()
            status_code = 201

            data_response = {
                "created": device.to_dict()
            }

        except Exception as e:
            data_response = {"errors": f"{e}"}

        response = Response()
        response.status_code = status_code

        return response

    def get(self):
        args = request.args.to_dict()
        device_list = Device.filter(**args)
        response = {'data': device_list, 'count': len(device_list)}
        return jsonify(response)
