from flask import Flask

from apis.v1.blueprint import api_v1
from apis.v2.blueprint import api_v2


app = Flask(__name__)

# Register blueprints
app.register_blueprint(api_v1, url_prefix='/v1')
app.register_blueprint(api_v2, url_prefix='/v2')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
