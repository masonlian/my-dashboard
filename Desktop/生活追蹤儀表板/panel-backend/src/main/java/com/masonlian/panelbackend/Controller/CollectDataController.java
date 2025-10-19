package com.masonlian.panelbackend.Controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.masonlian.panelbackend.request.LocationData;
import com.masonlian.panelbackend.request.PlaceRequest;
import com.masonlian.panelbackend.Service.LocationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

import java.math.BigDecimal;
import java.sql.Timestamp;
import java.util.List;
import java.util.Map;

@RestController
public class CollectDataController {

    @Autowired
    LocationService locationService;

    @PostMapping("/collectData")
    public ResponseEntity<LocationData> addLocation(@RequestBody List<PlaceRequest> placeRequestList) throws JsonProcessingException {

        String key = "";
        String url = "https://places.googleapis.com/v1";

        for (PlaceRequest placeRequest : placeRequestList) {
            System.out.println(new ObjectMapper().writeValueAsString(placeRequest));

            WebClient client = WebClient.builder()
                    .baseUrl(url)
                    .defaultHeader("Content-Type", "application/json; charset=UTF-8")
                    .defaultHeader("X-Goog-Api-Key", key)
                    .defaultHeader("X-Goog-FieldMask", "places.formattedAddress", "places.displayName", "places.types", "places.id", "places.location")
                    .build();

            String response = client.
                    post().
                    uri("/places:searchText").
                    bodyValue(placeRequest.getPlaceApiRequest()).
                    retrieve().bodyToMono(String.class).
                    block();

            System.out.println(response);

            ObjectMapper mapper = new ObjectMapper();
            JsonNode root = mapper.readTree(response);

            String address = root.path("places").get(0).path("formattedAddress").asText();
            String publicName = root.path("places").get(0).path("displayName").path("text").asText();
            String placeId = root.path("places").get(0).path("id").asText();
            List<String> poiList = mapper.convertValue(root.path("places").get(0).path("types"), new TypeReference<List<String>>() {
            });
            String poi = poiList.toString();

            Double lat = root.path("places").get(0).path("location").path("latitude").asDouble();
            Double lon = root.path("places").get(0).path("location").path("longitude").asDouble();


            BigDecimal latitude = new BigDecimal(lat);
            BigDecimal longitude = new BigDecimal(lon);
            Timestamp acquiringTime = placeRequest.getAcquiringTime();


            LocationData locationData = new LocationData();

            locationData.setAddress(address);
            locationData.setLatitude(latitude);
            locationData.setLongitude(longitude);
            locationData.setPublicName(publicName);
            locationData.setAcquiringTime(acquiringTime);
            locationData.setPoi(poi);
            locationData.setPlaceId(placeId);


            if (locationData != null) {

                locationService.enrollLocation(locationData);
            }

            else System.out.println("此資料未被登記：" + placeRequest.getPlaceApiRequest().getTextQuery());

        }

        return ResponseEntity.status(HttpStatus.CREATED).build();
    }
}
