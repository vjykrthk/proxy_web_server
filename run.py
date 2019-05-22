from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/v1/api')

    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "ProxyServer"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
