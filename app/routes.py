from flask import Blueprint, request, jsonify
from app import db
from app.models import Item

api_bp = Blueprint("api", __name__)

# Create an item
@api_bp.route("/items", methods=["POST"])
def create_item():
    data = request.json
    new_item = Item(name=data["name"], description=data.get("description"))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

# Read all items
@api_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

# Read a single item
@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())

# Update an item
@api_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.json
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    db.session.commit()
    return jsonify(item.to_dict())

# Delete an item
@api_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
