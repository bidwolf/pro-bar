"""
This module contains the routes for the tags
"""

from flask import Blueprint, jsonify, request

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    """
    This method is used to create a tag from a product code
    """
    print(request.json)
    return jsonify({"response": "tag created successfully"}), 200
