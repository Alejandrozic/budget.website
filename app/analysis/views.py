from flask import Blueprint, render_template, redirect, request, url_for, flash


analysis_bp = Blueprint(
    'analysis',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/analysis',
)


@analysis_bp.route('/analysis', methods=['GET'])
def analysis():
    return render_template(
        'analysis.html',
    )
