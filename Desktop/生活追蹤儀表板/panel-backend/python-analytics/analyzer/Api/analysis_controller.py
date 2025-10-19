import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from flask import Blueprint, request, jsonify
from analyzer.Service.match_data import match_location_data


analyzer_bp = Blueprint("analysis", __name__)
match_location_data()


#@analyzer_bp.route("/matchRegion", methods=["GET"])
#def matchRegion():
    
#    match_data()
    
    
    
    