from flask import Blueprint
from flask_restplus import Api


api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)

# Add api files
import apis.v1.node
import apis.v1.documentation
