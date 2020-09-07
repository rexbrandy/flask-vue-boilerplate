from flask import Blueprint, jsonify

example_bp = Blueprint('example', __name__)

@example_bp.route('/example', methods=['GET'])
def example():
    msg = 'Hello World'
    return jsonify({'msg': msg})