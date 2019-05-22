from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint

from app import api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    set_default_root(app)

    app.register_blueprint(api_bp, url_prefix='/v1/api')

    set_swagger_end_point(app)

    return app


def set_default_root(app):
    @app.route('/')
    def default():
        return redirect("/swagger", code=302)


def set_swagger_end_point(app):
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


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
