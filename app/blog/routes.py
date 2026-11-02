from flask import Blueprint, render_template, abort

blog_bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates')

# Datos de ejemplo (no se usa base de datos)
entradas = {
    1: 'Mi primera entrada en el blog',
    2: 'Aprendiendo Blueprints en Flask',
    3: 'Plantillas con Jinja2 y extends',
}

# /blog/entrada/1
@blog_bp.route('/entrada/<int:id>')
def ver_entrada(id):
    titulo = entradas.get(id)
    if titulo is None:
        abort(404)
    return render_template('entrada.html', id=id, titulo=titulo)