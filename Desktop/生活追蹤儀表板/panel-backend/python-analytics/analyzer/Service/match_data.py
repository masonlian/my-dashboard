import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from analyzer.Dao.get_location_journal import get_location_data , location_journal
from analyzer.Dao.get_location_journal import get_counts_data , counts

from decimal import Decimal , getcontext
import math


def match_location_data():
   get_location_data()
   
   data1: list[location_journal] = get_location_data()
   data2: list[counts] = get_counts_data()
   print("Location Data:", data1, end="\n")
   print("Counts Data:", data2, end="\n")
   
   
   #entroypy = compute_entropy(data2)#回傳一個熵值
   #distance = compute_mobility_distance(data) #回傳一個距離值
   #matrix = compute_transition_matrix(data) #回傳一個機率矩陣
   #match_region(entroypy,distance,matrix) 由於城市資料尚未建立資料，匹配的動作先暫此打住。
   #場所轉移矩陣是唯一用來刻畫行為結構的資料，在我的專案裡，最主要可以評斷一個人的1.生活穩定度 2.最常在哪兩個地點間來回 3.預測一個人下一個可能出現的地點。
   
   
   #print("Entropy:", entroypy, end="\n")
   #print("Mobility Distance:", distance, end="\n")
   #print("Transition Matrix:", matrix, end="\n")
   
#def compute_entropy(data2) :
    
    
    
   
   
   
    
