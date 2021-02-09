from flask import Blueprint, redirect, url_for


index_bp = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@index_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('dashboard.dashboard'))
