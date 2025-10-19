package com.masonlian.panelbackend.Dto;

import java.math.BigDecimal;
import java.sql.Timestamp;

public class LocationJournal {


    private BigDecimal latitude;
    private BigDecimal longitude;
    private Timestamp acquiringTime;
    private PlaceResponse placeResponse;

    public BigDecimal getLatitude() {
        return latitude;
    }

    public void setLatitude(BigDecimal latitude) {
        this.latitude = latitude;
    }

    public BigDecimal getLongitude() {
        return longitude;
    }

    public void setLongitude(BigDecimal longitude) {
        this.longitude = longitude;
    }

    public Timestamp getAcquiringTime() {
        return acquiringTime;
    }

    public void setAcquiringTime(Timestamp acquiringTime) {
        this.acquiringTime = acquiringTime;
    }

    public PlaceResponse getPlaceResponse() {
        return placeResponse;
    }

    public void setPlaceResponse(PlaceResponse placeResponse) {
        this.placeResponse = placeResponse;
    }
}
