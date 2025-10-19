package com.masonlian.panelbackend.Controller;


import com.masonlian.panelbackend.Dto.FinalLocationJournal;
import com.masonlian.panelbackend.Dto.LocationJournal;
import com.masonlian.panelbackend.Dto.PlaceResponse;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.masonlian.panelbackend.request.LocationData;
import com.masonlian.panelbackend.Service.LocationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.sql.Timestamp;

@RestController
public class LocationController {

    @Autowired
    private LocationService locationService;

    // 先移除 consumes/produces 做測試
    //一個locationData 進來至少要有

    @PostMapping("/location") public ResponseEntity<FinalLocationJournal> enrollLocation(@RequestBody LocationData locationData ){

        System.out.println("前端傳來的地址為："+locationData.getAddress());


        if(locationData != null){
            Integer journalId  =  locationService.enrollLocation(locationData);
          FinalLocationJournal finalLocationJournal = locationService.getJournalById(journalId);

           return ResponseEntity.status(HttpStatus.OK).body(finalLocationJournal);



        }
        else {
            System.out.println("資料傳輸失敗。");
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"前端資料傳送空值！>");


        }
    }


    @GetMapping("/locationDetail")
    public ResponseEntity<LocationJournal> getLocationDetail(BigDecimal latitude, BigDecimal longitude) throws  Exception{

        String key = "";

        String url1 = String.format("https://maps.googleapis.com/maps/api/geocode/json?latlng=%f,%f&radius=20&key=%s", latitude, longitude, key);
        WebClient client1 = WebClient.create(url1);

        String url2 = String.format("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f&radius=50&key=%s", latitude, longitude, key);
        WebClient client2 = WebClient.create(url2);

        String response1 = client1.get()
                .retrieve()
                .bodyToMono(String.class)
                .block();

        //資料應該是以json格式從客戶端傳回來，
        String response2 = client2.get()
                .retrieve()
                .bodyToMono(String.class)
                .block();


         ObjectMapper mapper = new ObjectMapper();
         PlaceResponse placeResponse = mapper.readValue(response2, PlaceResponse.class);




         LocationJournal locationJournal = new LocationJournal();
         locationJournal.setLatitude(latitude);
         locationJournal.setLongitude(longitude);
         locationJournal.setPlaceResponse(placeResponse);

        Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        locationJournal.setAcquiringTime(timestamp);



        if (locationJournal != null) {


            return ResponseEntity.status(HttpStatus.OK).body(locationJournal);
        }

    else return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();

    }





}
