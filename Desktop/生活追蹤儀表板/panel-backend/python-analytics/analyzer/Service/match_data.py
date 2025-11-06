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
import json 


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITY_TEMPLATE_PATH= os.path.join(BASE_DIR, "Data", "city_template.json")

@dataclass
class city_score:
    city_name:str
    description:str
    match_score:float
    
@dataclass
class match_result:
    return_entropy:float
    return_avg_distance:float
    return_steady_metrix:list
    return_most_matched_city:city_score
    


   #match_region(entroypy,distance,matrix) 由於城市資料尚未建立資料，匹配的動作先暫此打住。
   #場所轉移矩陣是唯一用來刻畫行為結構的資料，在我的專案裡，最主要可以評斷一個人的1.生活穩定度 2.最常在哪兩個地點間來回 3.預測一個人下一個可能出現的地點。
   
   
   #print("Entropy:", entroypy, end="\n")
   #print("Mobility Distance:", distance, end="\n")
   #print("Transition Matrix:", matrix, end="\n")
def match_location_data():
    

   @dataclass
   class SteadyProb:
       poi:str
       probility:float
       
       
   @dataclass
   class CityTemplate:
    city_name: str
    description: str
    entropy: float
    avg_distance: float
    max_distance: float
    steady_vector: list[SteadyProb]
    transition_type: str
       
    
    
   get_location_data()
#    這邊進來是一個dict而非object
   with open(CITY_TEMPLATE_PATH, 'r', encoding='utf-8') as file:
    city_templates = json.load(file)

   
   data1: list[location_journal] = get_location_data()
   data2: list[counts] = get_counts_data()
   entropy = compute_entropy(data2)
   print("最後計算出來的熵值為:", entropy, end="\n")
   
   entropy = compute_entropy(data2)#回傳一個熵值
   avg_distance = compute_mobility_distance(data1) #回傳一個距離值
   steady_metrix = compute_transition_matrix(data1) #回傳一個機率矩陣
   
   user_major_activity = major_activity(steady_metrix)
   
   
   entroypy_similarity=0.0
   distance_similarity=0.0
   steady_matrix_similarity=0.0
   
   city_to_match=[]
   
   
   for city_type in city_templates:
     print("正在對比的城市為:",city_type,end="\n")
     
     city_object = CityTemplate(city_name =city_type['city_name'],
                                description = city_type['description'],
                                entropy = city_type['entropy'],
                                avg_distance = city_type['avg_distance'],
                                max_distance = city_type['max_distance'],
                                steady_vector = city_type['steady_vector'],
                                transition_type = city_type['transition_type']
                                )
     city_to_match.append(city_object)
    
     
   match_scores_list = []   

   for city in city_to_match:
       
     city_entropy = city.entropy
     city_avg_distance = city.avg_distance 
     
     entroypy_similarity =  compute_entroypy_similarity(entropy,city_entropy,city_to_match)
     distance_similarity =  compute_distance_similarity(avg_distance,city_avg_distance,city_to_match)
     steady_matrix_similarity = compute_steady_matrix_similarity(user_major_activity,city.steady_vector) #回傳一個穩定狀態餘弦相似度
     
     match_score_result= (0.5*steady_matrix_similarity) + (0.3*distance_similarity) + (0.2*entroypy_similarity)
     candidate_city=city_score(city_name=city.city_name,description=city.description, match_score=match_score_result)
     match_scores_list.append(candidate_city)
   
   most_matched_city =max(match_scores_list, key = lambda x: x.match_score )
   
   print("最符合的城市為:", most_matched_city.city_name, "說明為:", most_matched_city.description, "匹配分數為:", most_matched_city.match_score , end="\n")
   match_return = match_result(return_entropy=entropy, return_avg_distance=avg_distance, return_steady_metrix=steady_metrix, return_most_matched_city=most_matched_city)
   
   return match_return


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
         
    
#    for k in compute_list:
    #   print(k,end="\n")
    #   print("--------",end="\n")
   
   
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
        #  print("計算出來的距離為:",distance,end="\n")
         
         j+=1
         
         
      daily_distances.append(distance)
         
    
    # for i in daily_distances:
        # print("每日平均移動距離為:",i,end="\n")
        # print("________",end="\n")
    
    average_distance = np.mean(daily_distances) 
    return average_distance
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
    # for i in index_map:
    #     print(i,end="")
    
    #從matrix map到index_number，要設定進入新矩陣的變化數列最好是連續的以防數值跑掉
    for i in range(len(poi_and_name)-1):
        
        row = index_map[poi_and_name[i].public_name]
        column= index_map[poi_and_name[i+1].public_name]
        count_matrix[row][column]+=1
    total_count_list = np.sum(count_matrix,axis=1)    
    
    # for i in range(N):
    #   for j in range(N):
    #       print(count_matrix[i][j],end=",")
    #   print("\n")
    
        
    # print("總次數陣列:",total_count_list)
            
    

    
    #接下來定義機率矩陣
    probility_matrix = np.full((N,N),0.0,dtype=float)
    
    for i in range(N):
        total_count = total_count_list[i]
        if total_count != 0 :
          for j in range(N):
            #   print("i :",i,"j:",j,"total_count:",total_count)
              if i == j:
                 continue
              else:
                c= count_matrix[i][j] 
                p = c/total_count
                probility_matrix[i][j]= p
                # print(f"現在運算到第{i}行第{j}列，機率為{probility_matrix[i][j]}。",end="\n")
           
        
    
    eigval, eigvecs = np.linalg.eig(probility_matrix.T)
    index = np.argmin(np.abs(eigval-1))
    steady = np.real(eigvecs[:,index])
    steady = np.abs(steady)
    steady = steady/ np.sum(steady)
    
    # print("穩定向量為:",steady)
    
    steady_probility_list = []
    
    for i in range(len(steady)):
        p = steady_probility(public_name = poi_set[i].public_name,
                         poi= poi_set[i].poi,
                         probility=steady[i] )
        steady_probility_list.append(p)
        
    total_probility =0.0
    for i in range(len(steady_probility_list)):
        # print(
            #   "偏好poi:",steady_probility_list[i].poi,
            #   "機率:",steady_probility_list[i].probility,
            #   end="\n")
        total_probility+= steady_probility_list[i].probility
    print("確認穩定機率向量總和為：",total_probility)
    
    return steady_probility_list


def major_activity (steady_matrix):
    
    if steady_matrix is None or len(steady_matrix) ==0:
        return []
    else :
        major_activity =[]
        for i in range(3):
          element = max(steady_matrix, key=lambda x: x.probility)
          major_activity.append(element)
          steady_matrix.remove(element)
        return major_activity
        
def compute_entroypy_similarity(entropy,city_entropy,city_to_match):
    
    max_city = max(city_to_match, key = lambda x: x.entropy)
    min_city = min(city_to_match, key = lambda x: x.entropy)

    similarity = 1-abs(entropy - city_entropy)/(max_city.entropy-min_city.entropy)
    print("熵值相似度為:",similarity,end="\n")
    return similarity

def compute_distance_similarity(avg_distance,city_avg_distance,city_to_match):
    
    scale_oare = 0.4*avg_distance
    dis_similarity = math.exp(-1*(abs((avg_distance - city_avg_distance))/scale_oare))
    print("移動距離相似度為:",dis_similarity,end="\n")
    return dis_similarity

def compute_steady_matrix_similarity(user_major_activity, city_steady_vector):
    
    print("city_steady_vector的類別為:",type(city_steady_vector))
    print("user_major_activity的類別為:",type(user_major_activity))
  

 
    for spot in user_major_activity:
        
        print("主要活動地點為:", spot.public_name, "類別為:", spot.poi, "機率為:", spot.probility,end="\n")
        if spot.public_name  is "向陽路182號":
            spot.poi = "Work"
        if spot.public_name is "光啟路247巷19號":
            spot.poi = "Home"
        else : 
            spot.poi = "Leisure"
            
        
    print("興趣點變更後的的穩定向量:",user_major_activity, end="\n")        
    print("比較城市對象的穩定向量為:", city_steady_vector, end="\n")
    
    city_map = { c["poi"] :c for c in  city_steady_vector}
    city_aligned  = [city_map[u.poi] for   u  in user_major_activity if u.poi in  city_map] 
    
    if (len(city_aligned) != len (user_major_activity)):
        print("使用者的主要活動地點與城市模板無法完全對應，無法計算相似度。")
        return 0.0
    else :
      molecular = 0
      a_dominator =0
      b_dominator =0
      for i in range(len(user_major_activity)):
          c=city_aligned[i]
          molecular += user_major_activity[i].probility*c["probility"]
    
      for i in range (len(user_major_activity)):
          c=city_aligned[i]
          a_dominator += user_major_activity[i].probility **2
          b_dominator += c["probility"] **2
    
      cosine_simularity = molecular/(math.sqrt(a_dominator)*math.sqrt(b_dominator))
      print("穩定狀態向量餘弦相似度為:",cosine_simularity,end="\n")
      return cosine_simularity
        
        
        
        
    
    
    
    
    
    
   
    
    
    
    #製作出一個查表讓兩個list可以根據poi來對應機率值。
   
    
        
        
     
    
    
    
    

    
    
        
        
        
        
    

    
    

            
        
            
    
        
    
                
            
            
            
            
            
            
    
        
        

                
            
      
           

            
                
                      
                      
                      
       
                
              
           
           
           
           
           
    

        
               
               
               
                                  
               
               
              
            
               
               
               
               
        
               
              
               
              
                   
                    
                   
                
                   
               
               
           
    
    
    

  
          
         
        
          
   
    
            
            
            
          
                 
        
           
           
           
           
           
    
        
    
    
    
   
   
    
