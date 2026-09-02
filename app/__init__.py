from flask import Flask, send_from_directory


def create_app():

    app = Flask(
        __name__,
        static_folder="../frontend",
        static_url_path="/static"
    )

    from app.routes.health import health_bp
    from app.routes.chat import chat_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(chat_bp)

    @app.route("/")
    def home():
        return send_from_directory(
            app.static_folder,
            "index.html"
        )

    return app