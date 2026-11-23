from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import time
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/tododb')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    # Lógica de reintento de conexión
    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.create_all()
                print("¡Conexión a la base de datos exitosa y tablas creadas!")
                break
            except OperationalError:
                retries -= 1
                print(f"Base de datos no lista. Reintentando en 3 segundos... (Intentos restantes: {retries})")
                time.sleep(3)

    return app
