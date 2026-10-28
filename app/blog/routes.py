from flask import render_template
from . import blog_bp

# Datos de ejemplo
entradas = {
    1: {"titulo": "Primera entrada del blog"},
    2: {"titulo": "Consejos de programación con Flask"},
    3: {"titulo": "Modularización con Blueprints"}
}

@blog_bp.route('/entrada/<id>')
def entrada(id):
    id_num = int(id)
    datos = entradas.get(id_num, {"titulo": "Entrada no encontrada"})
    return render_template('blog/entrada.html',
                           titulo=datos["titulo"],
                           id=id_num)