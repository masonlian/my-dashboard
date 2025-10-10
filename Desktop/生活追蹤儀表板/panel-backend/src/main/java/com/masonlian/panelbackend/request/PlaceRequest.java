package com.masonlian.panelbackend.request;

import java.sql.Timestamp;

public class PlaceRequest {

    private PlaceApiRequest placeApiRequest;
    private Timestamp acquiringTime;


    public PlaceApiRequest getPlaceApiRequest() {
        return placeApiRequest;
    }

    public void setPlaceApiRequest(PlaceApiRequest placeApiRequest) {
        this.placeApiRequest = placeApiRequest;
    }

    public Timestamp getAcquiringTime() {
        return acquiringTime;
    }

    public void setAcquiringTime(Timestamp acquiringTime) {
        this.acquiringTime = acquiringTime;
    }
}
