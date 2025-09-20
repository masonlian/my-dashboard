package com.masonlian.panelbackend.Controller;


import Dto.LocationData;
import com.masonlian.panelbackend.Service.LocationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LocationController {

    @Autowired
    private LocationService locationService;
    // 先移除 consumes/produces 做測試


    @PostMapping("/location") public ResponseEntity<Integer> enrollLocation(@RequestBody LocationData locationData ){

        if(locationData != null){
            System.out.println(locationData.getLocationName());
            System.out.println(locationData.getLatitude());
            System.out.println(locationData.getLongitude());
           // System.out.println(locationData.getAcquiringTime());

           Integer locationId =  locationService.enrollLocation(locationData);
           return ResponseEntity.status(HttpStatus.OK).body(locationId);

        }
        else {
            System.out.println("資料傳輸失敗。");
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();


        }
}


}
