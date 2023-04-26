from flask import Flask, request, jsonify, make_response
from  pythonsql import a,b,c,d,e,f

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_clientes():
    return jsonify(a,b,c,d,e,f)

app.run()