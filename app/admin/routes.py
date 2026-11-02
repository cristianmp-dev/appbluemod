from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

# /admin/panel
@admin_bp.route('/panel')
def panel():
    return render_template('panel.html')