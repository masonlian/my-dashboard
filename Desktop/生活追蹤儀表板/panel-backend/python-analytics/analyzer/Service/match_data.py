import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from analyzer.Dao.get_location_journal import get_location_data , location_journal
from analyzer.Dao.get_location_journal import get_counts_data , counts

from dataclasses import dataclass
from decimal import Decimal , getcontext
import math
import numpy as np
import pandas as pd
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
   #distance = compute_mobility_distance(data1) #回傳一個距離值
   compute_transition_matrix(data1) #回傳一個機率矩陣
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
 
def compute_transition_matrix(data1):
    
    
    #首先先把poi與public_name拉出來形成一種物件據此為單位，按照時間順序建立一個陣列。
    #再把這個順序當中有重複的部分給淘汰掉。
    
    @dataclass(eq=True, frozen=False)
    class poi_sequence :
        public_name:str
        poi: str
        order_number:int
        
        def __hash__(self):
          return hash((self.public_name, self.poi, self.order_number))

        def __eq__(self, other):
          return (
            self.public_name == other.public_name and
            self.poi == other.poi and
            self.order_number == other.order_number
        )
    @dataclass
    class steady_probility:
        public_name:str
        poi: str
        probility:float
        
        
        
    poi_sequence_array=[]
        
    for i in range(len(data1)-1):
        if  data1[i+1].public_name !=  data1[i].public_name:
            poi_sequence_array.append(data1[i])      
            
    
    poi_and_name: list[poi_sequence]=[]
    
    for location_journal in poi_sequence_array:
         poi_object = poi_sequence( public_name = location_journal.public_name,
                                   poi=location_journal.poi,
                                   order_number=None )
         poi_and_name.append(poi_object)
    
    
    # for object in poi_and_name:
      # print("public_name:",object.public_name,"poi:", object.poi,end="\n")
      
    #還需要一個沒有重複元素的矩陣。 
      
    poi_set =[]    
    seen=set()
    for p in poi_and_name:
        if p.public_name not in seen:
            seen.add(p.public_name)
            poi_set.append(p)
    
    for idx , p in enumerate(poi_set):
        p.order_number = idx
    
    N= len(poi_set)
    
    # count的位置隨著row_index變動
    # 可能要先將這個count_matrix的from跟to 都先賦值，然而我想要找到一個方法直接把字串與計數直接設進去。
    count_matrix = np.full((N,N),0.0,dtype=float)
    
    #adjacent_list = []
     
    #關鍵點在於建立以public_name為key的查表搜集相對應所需的index
     
    total_count_list =[] 
    index_map = { p.public_name : p.order_number for p in poi_set}
    for i in index_map:
        print(i,end="")
    
    #從matrix map到index_number，要設定進入新矩陣的變化數列最好是連續的以防數值跑掉
    for i in range(len(poi_and_name)-1):
        
        row = index_map[poi_and_name[i].public_name]
        column= index_map[poi_and_name[i+1].public_name]
        count_matrix[row][column]+=1
    total_count_list = np.sum(count_matrix,axis=1)    
    
    for i in range(N):
      for j in range(N):
          print(count_matrix[i][j],end=",")
      print("\n")
    
        
    print("總次數陣列:",total_count_list)
            
    

    
    #接下來定義機率矩陣
    probility_matrix = np.full((N,N),0.0,dtype=float)
    
    for i in range(N):
        total_count = total_count_list[i]
        if total_count != 0 :
          for j in range(N):
              print("i :",i,"j:",j,"total_count:",total_count)
              if i == j:
                 continue
              else:
                c= count_matrix[i][j] 
                p = c/total_count
                probility_matrix[i][j]= p
                print(f"現在運算到第{i}行第{j}列，機率為{probility_matrix[i][j]}。",end="\n")
           
        
            
            
    for i in range(N):
      for j in range(N):
          print(probility_matrix[i][j],end=",")
      print("\n")
    print("對於每個poi到其他地區的機率總和為:",np.sum(probility_matrix,axis=1))
    
    eigval, eigvecs = np.linalg.eig(probility_matrix.T)
    index = np.argmin(np.abs(eigval-1))
    steady = np.real(eigvecs[:,index])
    steady = np.abs(steady)
    steady = steady/ np.sum(steady)
    
    print("穩定向量為:",steady)
    
    steady_probility_list = []
    
    for i in range(len(steady)):
        p = steady_probility(public_name = poi_set[i].public_name,
                         poi= poi_set[i].poi,
                         probility=steady[i] )
        steady_probility_list.append(p)
        
    total_probility =0.0
    for i in range(len(steady_probility_list)):
        print(
              "偏好poi:",steady_probility_list[i].poi,
              "機率:",steady_probility_list[i].probility,
              end="\n")
        total_probility+= steady_probility_list[i].probility
    print("確認穩定機率向量總和為：",total_probility)
        
        
        
        
    

    
    

            
        
            
    
        
    
                
            
            
            
            
            
            
    
        
        

                
            
      
           

            
                
                      
                      
                      
       
                
              
           
           
           
           
           
    

        
               
               
               
                                  
               
               
              
            
               
               
               
               
        
               
              
               
              
                   
                    
                   
                
                   
               
               
           
    
    
    

  
          
         
        
          
   
    
            
            
            
          
                 
        
           
           
           
           
           
    
        
    
    
    
   
   
    
