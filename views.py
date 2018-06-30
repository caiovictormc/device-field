# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 22:18:31
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-30 20:05:53

from flask import jsonify, render_template, request
from flask.views import MethodView

from auth.decorators import auth_required
from db.models import Device


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

        response = jsonify(data_response)
        response.status_code = status_code

        return response