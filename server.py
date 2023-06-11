# -*- coding: utf-8 -*-
"""
@author:David Euler
@description:
python3 -m pip install flask
"""
import sys
from flask import Flask, request
from loguru import logger
import sys
import time
import os
sys.path.append("..")
from pycorrector import Corrector
from pycorrector.macbert.macbert_corrector import MacBertCorrector
pwd_path = os.path.abspath(os.path.dirname(__file__))
startTime = time.time()
app = Flask(__name__)
rule_model = Corrector()
rule_model.check_corrector_initialized()
# macbert_model = MacBertCorrector()
macbert_model = MacBertCorrector(pwd_path+"pycorrector/datasets/shibing624/macbert4csc-base-chinese")
help = """
You can request the service by HTTP get: <br> 
   http://0.0.0.0:5001/macbert_correct?text=我从北京南做高铁到南京南<br>

or HTTP post with json: <br>  
   {"text":"xxxx"} <p>
Post example: <br>
  curl -H "Content-Type: application/json" -X POST -d '{"text":"我从北京南做高铁到南京南"}' http://0.0.0.0:5001/macbert_correct
"""


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    return help

@app.route('/macbert_correct', methods=['POST', 'GET'])
def correct_api():
    if request.method == 'POST':
        data = request.json
        logger.info("Received data: {}".format(data))
        text = data["text"]
        results = macbert_model.macbert_correct(text)
        # return results[0] + " " + str(results[1])
        return results[0]
    else:
        if "text" in request.args:
            text = request.args.get("text")
            logger.info("Received data: {}".format(text))
            results = macbert_model.macbert_correct(text)
            # return results[0] + " " + str(results[1])
            return results[0]
    return help


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)