import json
from flask_restplus import Resource

from apis.v1.blueprint import api


@api.route('/export-docs')
class ExportDocs(Resource):
    def get(self):
        urlvars = False  # Build query strings in URLs
        swagger = True  # Export Swagger specifications
        data = api.as_postman(urlvars=urlvars, swagger=swagger)
        return json.dumps(data)
