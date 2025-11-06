import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from flask import Blueprint, request, jsonify
from analyzer.Service.match_data import match_location_data


analyzer_bp = Blueprint("analysis", __name__,url_prefix="/api/analysis")

@analyzer_bp.route("/match_data",methods=["GET"])

#之後這邊要記得jsonfy
def match_data():

    data = match_location_data()
    data_json = jsonify(data)
    
   
    if data is None :
       return jsonfy({ "result" : "城市匹配失敗！" })
    else : 
         return data_json 



#@analyzer_bp.route("/matchRegion", methods=["GET"])
#def matchRegion():
    
#    match_data()
    
    
    
    