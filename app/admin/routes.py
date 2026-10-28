from flask import render_template
from . import admin_bp

@admin_bp.route('/panel')
def panel():
    return render_template('admin/panel.html',
                           mensaje="Bienvenido al panel de administración")