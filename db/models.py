# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-29 22:28:44
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-07-04 09:49:26

from . import collection
import uuid


class Document:

    REQUIRED_FIELDS = []
    FIELDS = []


    @classmethod
    def filter(cls, **kwargs):
        unallowed_fields = list(
            filter(lambda key: key not in cls.FIELDS, kwargs.keys())
        )

        if unallowed_fields:
            e_msg = '{} fields not allowed were found: {}'.format( 
                len(unallowed_fields), ', '.join(unallowed_fields)
            )
            raise TypeError(e_msg)
        else:
            return list(collection.find(kwargs, {'_id': False}))


    def __filled_required_fields(self):
        empty_fields = []

        for field in self.REQUIRED_FIELDS:
            if not getattr(self, field):
                empty_fields.append(field)

        if empty_fields:
            e_msg = 'missing {} empty fields: {}'.format( 
                len(empty_fields), ', '.join(empty_fields)
            )
            raise TypeError(e_msg)

        return not empty_fields


    def __save(self):
        if self.__filled_required_fields():
            data = self.to_dict()
            return collection.insert_one(data).inserted_id


    # def is_unique(self):
    #     if self.__filled_required_fields():
    #         list_of_dicts = [
    #             {unique_field: getattr(self, unique_field)} for unique_field in self.UNIQUE_FIELDS 
    #         ]
    #         return list(collection.find({"$or": list_of_dicts}))


    def to_dict(self):
        return {
            field: getattr(self, field) for field in self.FIELDS
        }



class Device(Document):

    REQUIRED_FIELDS = ['app', 'user_id', 'device_name']

    FIELDS = [
        'app', 'user_id', 'device_name', 
        'mqtt_username', 'mqtt_client_id', 'mqtt_password'
    ]


    def __init__(self, **kwargs):
        self.mqtt_client_id = None
        self.mqtt_username = None
        self.mqtt_password = None
        
        self.app = None
        self.user_id = None
        self.device_name = None

        unallowed_fields = list(
            filter(lambda key: key not in self.REQUIRED_FIELDS, kwargs.keys())
        )

        if unallowed_fields:
            e_msg = '{} fields not allowed were found: {}'.format( 
                len(unallowed_fields), ', '.join(unallowed_fields)
            )
            raise TypeError(e_msg)

        else:
            for field, value in kwargs.items():
                setattr(self, field, str(value))


    def save(self):
        if self.__exists():
            e_msg = 'This is already a registered device'
            raise ValueError(e_msg)

        else:
            self.__update_mqtt_auth()
        return self.__save()


    def __update_mqtt_auth(self):
        get_doc = collection.find_one({'user_id': self.user_id})
        if get_doc:
            self.mqtt_username = get_doc.get('mqtt_username')
            self.mqtt_password = get_doc.get('mqtt_password')
        else:
            self.mqtt_username = self.__create_uuid('mqtt_username')
            self.mqtt_password = self.__create_uuid('mqtt_password')


    def __create_uuid(self, field_name):
        while True:
            value = str(uuid.uuid4())
            if not collection.find_one({field_name: value}):
                setattr(self, field_name, str(value))
                return value


    def __exists(self):
        object_credentials = {
            'app': self.app,
            'user_id': self.user_id,
            'device_name': self.device_name
        }

        return collection.find_one(object_credentials)
