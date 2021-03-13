from flask import Blueprint,  render_template
from app.transactions.models import TransactionTypes, Transactions
from app.categories.models import Categories


dashboard_bp = Blueprint(
    'dashboard',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/dashboard/static',
)


@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():

    return render_template(
        'dashboard.html',
        categories=Categories.query.order_by(Categories.name.asc()),
        transaction_types=TransactionTypes.query.order_by(TransactionTypes.name.asc()),
        transactions=Transactions.query.order_by(Transactions.date.desc()).limit(10),
    )
