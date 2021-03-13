from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from app.categories.models import Categories
from app import db


categories_bp = Blueprint(
    'categories',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/categories/static',
)


@categories_bp.route('/categories', methods=['GET'])
def categories():
    return render_template(
        'categories.html',
        categories=Categories.query.order_by(Categories.name.asc()),
    )


@categories_bp.route('/categories/new', methods=['POST'])
def new_category():
    name = request.form['newCategoryName']
    name = ' '.join([
        n.capitalize()
        for n in name.split(' ')
    ])
    exists = Categories.query.filter_by(name=name).first()
    if exists is None:
        category = Categories(name=name)
        db.session.add(category)
        db.session.commit()
        flash(message='Success.', category='success')
    else:
        flash(message=f'Category "{name}" already exists.', category='error')
    return redirect(url_for('categories.categories'))


@categories_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Categories.query.filter_by(id=category_id).first()
    return jsonify(category.to_json())


@categories_bp.route('/categories/<int:category_id>/update', methods=['POST'])
def update_category(category_id):
    new_name = request.form['updatedCategoryName']
    new_name = ' '.join([
        n.capitalize()
        for n in new_name.split(' ')
    ])
    category = Categories.query.filter_by(id=category_id).first()
    category.name = new_name
    db.session.commit()
    return redirect(url_for('categories.categories'))


@categories_bp.route('/categories/<int:category_id>/delete', methods=['POST'])
def delete_category(category_id):
    Categories.query.filter_by(id=category_id).delete()
    db.session.commit()
    return redirect(url_for('categories.categories'))
