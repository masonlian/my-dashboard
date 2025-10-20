import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from analyzer.Dao.get_location_journal import get_location_data , location_journal
from analyzer.Dao.get_location_journal import get_counts_data , counts

from dataclasses import dataclass
from decimal import Decimal , getcontext
import math
import numpy as np
from datetime import datetime , date , timedelta




def match_location_data():
   get_location_data()
   
   data1: list[location_journal] = get_location_data()
   data2: list[counts] = get_counts_data()
   #entropy = compute_entropy(data2)
   #print("最後計算出來的熵值為:", entropy, end="\n")
   
    #for data in data2:
    # print(data,end="\n")
    # print("--------",end="\n")
    

   
   #entroypy = compute_entropy(data2)#回傳一個熵值
   distance = compute_mobility_distance(data1) #回傳一個距離值
   #matrix = compute_transition_matrix(data) #回傳一個機率矩陣
   #match_region(entroypy,distance,matrix) 由於城市資料尚未建立資料，匹配的動作先暫此打住。
   #場所轉移矩陣是唯一用來刻畫行為結構的資料，在我的專案裡，最主要可以評斷一個人的1.生活穩定度 2.最常在哪兩個地點間來回 3.預測一個人下一個可能出現的地點。
   
   
   #print("Entropy:", entroypy, end="\n")
   #print("Mobility Distance:", distance, end="\n")
   #print("Transition Matrix:", matrix, end="\n")



#需要的變數有 1.單一場所抵達次數，2.場所總次數 3.出現過的地點數量 
def compute_entropy(data2) :
    
   #以單一場所為單位計算熵值

   
   @dataclass
   class unit_place:
        address: str
        total_count: int

   compute_list: list[unit_place] =[]
   @dataclass
   class unit_place_probility:
        address: str
        probability: float
  
   i=0
   while i< len(data2):
       j=i+1
       while j < len(data2):
           if  data2[i].address==data2[j].address and data2[i].month !=data2[j].month :
               data2[j].counts += data2[i].counts
               data2[i].counts =0
           j+=1
       i+=1 #迴圈的計數器要手動增數    
               
               
   for k in data2:
       if k.counts !=0:
           place = unit_place(address=k.address,total_count=k.counts)
           compute_list.append(place)
         
    
   for k in compute_list:
      print(k,end="\n")
      print("--------",end="\n")
   
   
   total_counts_amount =0
   
   for k in compute_list:
       total_counts_amount += k.total_count
       
   probability_list: list[unit_place_probility] =[]
   
   for k in compute_list:
       probility = k.total_count / total_counts_amount
       unit_problility = unit_place_probility(address=k.address,probability=probility) 
       probability_list.append(unit_problility)
   
   minus_entropy =0.0
   for k in probability_list:
       k.probability *= math.log(k.probability)
       minus_entropy += k.probability
   entropy = -1 * minus_entropy    
   
   return entropy
   
   
   


    
def compute_mobility_distance(data1):
    
    #先將data1的資料以日為單位切割，再計算每日的移動距離，最後取平均值。
    
    split_journal: list[list[location_journal]] =[]
    

    i=0

    while i < len(data1):
        
        d_i = data1[i].acquiring_time.date()
        j=i+1
  
        same_day_distances: list[location_journal] =[]
        
        while j < len(data1):   
                     
          
              d_j = data1[j].acquiring_time.date()
              
            #   print("d_i的值為:",d_i,end="\n")
            #   print("d_j的值為:",d_j,end="\n")
              
            #   print("被登記的資料為:",data1[j].journal_id,"日期為:",data1[j].acquiring_time,end="\n")
            
              if d_i == d_j:
                  
                   same_day_distances.append(data1[j])
                   # print("________",end="\n")
                   #print("待登錄的陣列長度為:",len(same_day_distances),end="\n")
                   j+=1
                   
              else: 
                     same_day_distances.append(data1[i])  
                     break
    
             
        #print("________",end="\n")   
        #print("j的值變更為:",j,end="\n")            

        split_journal.append(same_day_distances)  
        #print("日期記錄陣列以登記資料筆數:",len(split_journal), end="\n")    
        #print("新的一天。")  
        #print("________",end="\n") 
             
        i=j
        #print("i的值變更為:",i,end="\n")
    
    #print("=========",end="\n")
    # print("以日為單位切割後的資料筆數:",len(split_journal), end="\n")
   
    daily_distances: list[float] =[] 
    
    print("分割後的陣列長度為：",len(split_journal),end="\n")
    R = 6371.0 # 地球半徑，單位為公里
   
    for one_day in split_journal:
        
      distance =0.0
      j=0
    
      while j < len(one_day)-1:
         
         latitude_front=math.radians(float(one_day[j].latitude))
         longitude_front=math.radians(float(one_day[j].longitude))
         
         latitude_back= math.radians(float(one_day[j+1].latitude))
         longitude_back= math.radians(float(one_day[j+1].longitude))


         
         factor_1=math.sin((latitude_back-latitude_front)/2)**2
         factor_2=math.cos(latitude_front)*math.cos(latitude_back)*((math.sin(longitude_back-longitude_front)/2)**2)
         distance += 2*R*math.asin(math.sqrt(factor_1+factor_2))
         print("計算出來的距離為:",distance,end="\n")
         
         j+=1
         
         
      daily_distances.append(distance)
         
         
    
   
    
    
    for i in daily_distances:
        print("每日平均移動距離為:",i,end="\n")
        print("________",end="\n")
    
    average_distance = np.mean(daily_distances)
    print("最終計算出來的平均移動距離為:", average_distance, end="\n")

  
          
         
        
          
   
    
            
            
            
          
                 
        
           
           
           
           
           
    
        
    
    
    
   
   
    
