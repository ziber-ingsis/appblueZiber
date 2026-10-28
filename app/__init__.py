from flask import Flask

def create_app():
    app = Flask(__name__)
    # Registro de los blueprints (Modulos)
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.auth.routes import auth_bp
      # Registrar Blueprints
    from .admin import admin_bp
    from .blog import blog_bp
    
    
    
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(auth_bp)
    
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    
    return app
