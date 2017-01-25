from flask import Blueprint
from flask_restplus import Api


api_v2 = Blueprint('api_v2', __name__)
api = Api(api_v2)

# Add api files
import apis.v2.node
