from flask import Flask
 
application = Flask(__name__)
 
import api.res.endpoints
