from flask import Blueprint, render_template, redirect, request, url_for, flash
from app import db
from datetime import datetime
from app.transactions.models import Transactions
from app.categories.models import Categories
from sqlalchemy.sql import func, extract


analysis_bp = Blueprint(
    'analysis',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/analysis',
)


@analysis_bp.route('/analysis', methods=['GET'])
def analysis():
    expenses_by_category = db.session.query(
        Categories.name.label('category'),
        func.sum(Transactions.amount).label("total"),
    ).join(
        Categories, Categories.id == Transactions.category_id
    ).filter(
        extract('month', Transactions.date) >= datetime.today().month,
        extract('year', Transactions.date) >= datetime.today().year,
    ).group_by(
        Transactions.category_id,
    ).order_by(
        func.sum(Transactions.amount).desc(),
    ).all()
    return render_template(
        'analysis.html',
        expenses_by_category=expenses_by_category,
    )
