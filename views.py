from flask import Blueprint, jsonify

# Створюємо Blueprint для організації ендпоінтів
main = Blueprint('main', __name__)

@main.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "OK"}), 200
