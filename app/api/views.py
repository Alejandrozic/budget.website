from flask import Blueprint, request, redirect, url_for


api_bp = Blueprint(
    'api',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/categories/static',
)
