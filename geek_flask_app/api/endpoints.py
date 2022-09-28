# -*- coding: utf-8 -*-
 
from flask import jsonify
from api import application
 
@application.route('/', methods=['GET'])
def get_app_properties():
  name = 'geek-flask-api'
  version = '0.0.1'
 
  app_properties = \
  {
    'name': name
    , 'version' : version
  }
 
  return jsonify(app_properties)
