package com.masonlian.panelbackend.Controller;


import Dto.LocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import com.masonlian.panelbackend.Service.LocationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LocationController {

    @Autowired
    private LocationService locationService;

    // 先移除 consumes/produces 做測試
    //一個locationData 進來至少要有

    @PostMapping("/location") public ResponseEntity<LocationJournal> enrollLocation(@RequestBody LocationData locationData ){


        if(locationData != null){


           Integer journalId  =  locationService.enrollLocation(locationData);
           LocationJournal enrolledLocationData = locationService.getJournalById(journalId);
           return ResponseEntity.status(HttpStatus.OK).body(enrolledLocationData);



        }
        else {
            System.out.println("資料傳輸失敗。");
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();


        }
}


}
