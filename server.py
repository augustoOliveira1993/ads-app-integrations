import json
from flask import Flask, jsonify

from controllers.Login import Login
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/findniche')
def index():
   inpUser = '/html/body/div/div[2]/div[2]/div/div/form/div[1]/div/input'
   inpPwd =  '/html/body/div/div[2]/div[2]/div/div/form/div[2]/input'
   user, pwd = "silva12312312@bugfoo.com", "Spy12345"
   url = "https://findniche.com/user/login"
   conn = Login([inpUser, inpPwd], [user, pwd], url)
   session = conn.login()
   session_id = conn.getSessionId()
   response = jsonify(id = session_id)
   response.headers.add("Access-Control-Allow-Origin", "*")
   return response


app.run(debug=True,port=5005,host="0.0.0.0")
