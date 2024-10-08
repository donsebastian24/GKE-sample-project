from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='frontend',
                static_url_path='/')  # Serving static files from the frontend directory

    # Register routes from routes.py
    from .routes import main
    app.register_blueprint(main)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
