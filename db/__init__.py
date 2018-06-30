# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-06-30 15:00:24
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-06-30 15:13:46

 
from pymongo import MongoClient 


client = MongoClient() 
db = client['field'] 
collection = db['device']
