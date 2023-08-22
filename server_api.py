"""
-------------------------------------------
Developer Notice:
-------------------------------------------
This script sets up a Flask application that provides endpoints for the "Vertretungsplan" management.

Features:
1. Connection to a PostgreSQL database using SQLAlchemy.
2. Endpoints to retrieve and upload "Vertretungsplan" data.
3. Authorization checks using provided authentication tokens.

Restrictions:
Commercial use and distribution of this code is not permitted without explicit permission from the author.

Created on: 31.07.2023
Last Modified: 01.08.2023
Developed by: Miguel C. Zapp

For issues or further enhancements, contact contact@miguelcz.com.
-------------------------------------------
"""


# Import necessary Flask modules and tools
from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
from urllib.parse import quote
from datetime import datetime
import json

# Import authentication information
import db_auth
import auth

# Initialize Flask app
app = Flask(__name__)

# Define API endpoint path
API_ENDPOINT = "/api/"

# Configure SQLAlchemy to connect to PostgreSQL database using provided authentication details
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_auth.username}:{db_auth.password}@{db_auth.host}/{db_auth.database}'

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define Vertretungsplan database model
class Vertretungsplan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.now)
    data = db.Column(db.Text, nullable=False)

# Function to check Authorization headers against provided authentication tokens
def checkAuth(req, authToken=auth.lehrerToken):
    reqHeads = req.headers
    res = False
    if "Authorization" in reqHeads:
        res = reqHeads["Authorization"] == authToken
    return res

# Function to create a standardized JSON response
def createResponse(jsonData={"err": "Unauthorized", "status": "failed"}, code=403):
    response = make_response(json.dumps(jsonData), code)
    response.headers["Content-Type"] = "application/json"
    return response

# Route to fetch latest Vertretungsplan entry
@Flask.route(app, rule=f"{API_ENDPOINT}/vertretungsplan", methods=["GET"])
def homePage():
    response = createResponse()
    if checkAuth(request):
        d = Vertretungsplan.query.order_by(
            Vertretungsplan.datetime.desc()).first()
        if d:
            response = createResponse(
                {"datetime": str(d.datetime), "data": d.data}, code=200)
        else:
            return createResponse({"err": "No Vertretungsplan found", "status": "failed"})
    return response

# Route to upload new Vertretungsplan entry
@Flask.route(app, rule=f"{API_ENDPOINT}/hochladen", methods=["POST"])
def uploadRoute():
    d = request.get_json()
    response = createResponse()
    if checkAuth(request, authToken=auth.verwaltungToken):
        if d:
            new_data = Vertretungsplan(data=json.dumps(d))
            db.session.add(new_data)
            db.session.commit()
            db.session.close()
            response = createResponse({"status": "OK"}, code=200)
        else:
            response = createResponse(
                {"err": "Invalid request body", "status": "failed"}, code=400)
    return response

# Run the Flask app when script is run as the main module
if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
