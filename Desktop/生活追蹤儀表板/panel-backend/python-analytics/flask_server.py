#這個檔案我需要的是Flask的基本架構模式如何啟動我這整份Python ANALYTICS專案

from flask import Flask,Request, jsonify
from analyzer.Api.analysis_controller import analyzer_bp
import os 
import json


def create_app():
  app = Flask(__name__)
  app.register_blueprint(analyzer_bp,threaded=False)
  return app





if __name__ =='__main__' : 

 app = create_app()
 for r in app.url_map.iter_rules():
     print(r)
 app.run(port=5001,debug=False,threaded=False )

 
