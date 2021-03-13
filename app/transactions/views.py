from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from app.transactions.models import Transactions, TransactionTypes
from app.categories.models import Categories
from app import db


transactions_bp = Blueprint(
    'transactions',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/transactions/static',
)


@transactions_bp.route('/transactions', methods=['GET'])
def transactions():
    ts = Transactions.query.order_by(Transactions.date.desc()).all()
    by_date = {}
    for t in ts:
        try:
            by_date[t.get_date()].append(t)
        except KeyError:
            by_date[t.get_date()] = [t]
    return render_template(
        'transactions.html',
        transactions_by_date=by_date,
        categories=Categories.query.order_by(Categories.name.asc()),
        transaction_types=TransactionTypes.query.order_by(TransactionTypes.name.asc()),
        transactions=Transactions.query.order_by(Transactions.date.desc()).limit(10),
    )


@transactions_bp.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = Transactions.query.filter_by(id=transaction_id).first()
    return jsonify(transaction.to_json())


@transactions_bp.route('/transactions/new', methods=['POST'])
def new_transaction():
    transaction_type = TransactionTypes.query.filter_by(id=int(request.form['typeSelectorName'])).first()
    if transaction_type.name == 'Expense':
        category = Categories.query.filter_by(id=int(request.form['categorySelectorName'])).first()
    else:
        category = None
    transaction = Transactions(
        transaction_type=transaction_type,
        name=request.form['transactionName'],
        category=category,
        amount=round(float(request.form['amountSelectorName']), 2),
        date=request.form['dateSelectorName'],
    )
    db.session.add(transaction)
    db.session.commit()
    return redirect(url_for('dashboard.dashboard'))


@transactions_bp.route('/transactions/<int:transaction_id>/update', methods=['POST'])
def update_category(transaction_id):
    transaction = Transactions.query.filter_by(id=transaction_id).first()
    #   Date
    transaction.set_date(date=request.form['date'])
    #   Transaction Type
    transaction.transaction_type = TransactionTypes.query.filter_by(id=int(request.form['transactionTypeName'])).first()
    #   Category
    if transaction.transaction_type.name == 'Expense':
        transaction.category = Categories.query.filter_by(id=int(request.form['categoryName'])).first()
    else:
        transaction.category = None
    #   Name
    transaction.name = request.form['transactionName']
    #   Amount
    transaction.amount = round(float(request.form['amount']), 2)
    db.session.commit()
    return redirect(url_for('transactions.transactions'))
