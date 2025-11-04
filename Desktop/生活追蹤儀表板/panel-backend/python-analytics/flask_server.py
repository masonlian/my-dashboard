#這個檔案我需要的是Flask的基本架構模式如何啟動我這整份Python ANALYTICS專案

from flask import Flask,Request, jsonify
from analyzer.Api.analysis_controller import analyzer_bp
import os 
import json


app = Flask(__name__)
app.register_blueprint(analyzer_bp,url_prefix="/analysis_controller",threaded=False)





if __name__ =='__main__' : 
 app.run(port=5001,debug=False,threaded=False )

 
