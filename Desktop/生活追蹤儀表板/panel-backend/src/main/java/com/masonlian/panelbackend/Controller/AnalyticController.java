package com.masonlian.panelbackend.Controller;


import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class AnalyticController {

    private final RestTemplate restTemplate = new RestTemplate();
    @GetMapping("/matchResult")
    public ResponseEntity<?> getAnalytics(@RequestParam (required = false) String until) {

        try {
            String flaskUrl = "http://localhost:5001/analytics/api/compute";
            if (until != null) {
                flaskUrl = flaskUrl + "?until=" + until;
            }

            ResponseEntity<?> response = restTemplate.getForEntity(flaskUrl, String.class);
            return ResponseEntity.status(HttpStatus.OK).body(response);
        }catch (Exception e){
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(e.getMessage());
        }

    }


}
