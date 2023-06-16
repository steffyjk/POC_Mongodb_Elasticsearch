import json

from flask import jsonify, Blueprint, request

search_module = Blueprint("search", __name__)


@search_module.route('/search', methods=['GET'])
def search():
    if not request.json:
        return jsonify(json.dumps("Empty Request Form")), 400
    form_data = request.json
    filters = form_data.get("filters")





    # document = {
    #     "user_data": {
    #         "name": "stella"
    #     },
    #     "current_experience_insight": {
    #         "properties": {
    #             "is_long_tenure": False,
    #             "total_exp": 5,
    #             "total_jobs": 3
    #         }
    #     },
    #     # Rest of the document properties...
    # }
    #
    # return jsonify(document)
