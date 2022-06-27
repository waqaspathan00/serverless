from flask import jsonify

def Response(body, status):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (jsonify(body), status, headers)