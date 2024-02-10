"""
This module contains the routes for the tags
"""

from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    """
    This method is used to create a tag from a product code
    """
    tag_creator_view = TagCreatorView()
    http_request = HttpRequest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)
    return jsonify(response.body), response.status_code
