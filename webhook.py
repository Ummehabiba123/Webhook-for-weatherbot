import json
import os
import requestr

from flask import Flask
from flask import request
from flast import make_response

app=Flask(__name__)
 @app.route('/webhook', methods=['POST'])

 def webhook():
    req=request.get_json(silent=True, force=True)
    print(json.dumps(req, indent4))
    res=makeResponse(req)
    res=json.dumps(req, indent=4)
    r=make_response(res)
    r.headers['Content-Type']='application/json'
    return r

def makeResponse(req):
    result=req.get("result")
    params=result.get("parameters")
    city=params.get("geo-city")
    date=params.get("date")
    speech=" The forecast for"+city+ "for "+date+ " is "
    return{
        "speech":speech,
        "displayText": speech,
        "source": "apiai-weather-webhook"
    }
if __name__=="'__main__":
    port=int(os.getenv('PORT', 5000))
    print("starting app on port %d"  %port)
    app.run(debug=false, port=port, host='0.0.0.0')