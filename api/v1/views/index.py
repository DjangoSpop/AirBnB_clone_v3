from flask import jsonify
from api.v1.views import app_views
from models import storage
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
# @app_views.route("/")
# def index():  
count()
