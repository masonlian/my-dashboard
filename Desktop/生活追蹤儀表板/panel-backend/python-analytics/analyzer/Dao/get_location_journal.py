import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import mysql.connector
from dataclasses import dataclass
from decimal import Decimal , getcontext
import datetime


conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="springboot",
        database="panel"       
    ) #建立資料庫連線
    

@dataclass
class location_journal:
    
    journal_id:int
    latitude: Decimal
    longitude: Decimal
    acquiring_time:datetime.datetime
    public_name: str
    address: str
    poi: str
    place_id: str
    

@dataclass
class counts:
    counts_id:int
    address: str
    poi: str
    counts:int
    latitude: Decimal
    longitude: Decimal
    month:int
    public_name: str

def get_counts_data():
    cursor = conn.cursor( dictionary=True) #建立游標物件，設定dictionary=True以取得字典格式的結果
    sql = "SELECT * FROM counts"
    cursor.execute(sql) #執行SQL查詢
    results = cursor.fetchall()
    cursor.close() #關閉游標
    
    return [counts(**row) for row in results]
    

    
def get_location_data():
    

    cursor = conn.cursor( dictionary=True) #建立游標物件，設定dictionary=True以取得字典格式的結果
    sql = "SELECT * FROM location_journal ORDER BY acquiring_time ASC"
    cursor.execute(sql) #執行SQL查詢
    results = cursor.fetchall()
    cursor.close() #關閉游標
    
    return [location_journal(**row) for row in results]


    
    
    
    
    
    
    
    




