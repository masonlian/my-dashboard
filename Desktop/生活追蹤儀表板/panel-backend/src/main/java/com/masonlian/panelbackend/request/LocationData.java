package com.masonlian.panelbackend.request;

import java.math.BigDecimal;
import java.sql.Timestamp;

public class LocationData {

    private  BigDecimal latitude;
    private BigDecimal longitude;
    private  String publicName;
    private  Timestamp acquiringTime;
    private String address ;
    private String poi;



    public String getPoi() {
        return poi;
    }

    public void setPoi(String poi) {
        this.poi = poi;
    }



    public String getPublicName() {
        return publicName;
    }

    public void setPublicName(String publicName) {
        this.publicName = publicName;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


    public BigDecimal getLongitude() {
        return longitude;
    }

    public void setLongitude(BigDecimal longitude) {
        this.longitude = longitude;
    }

    public BigDecimal getLatitude() {
        return latitude;
    }

    public void setLatitude(BigDecimal latitude) {
        this.latitude = latitude;
    }

    public Timestamp getAcquiringTime() {
        return acquiringTime;
    }

    public void setAcquiringTime(Timestamp acquiringTime) {
        this.acquiringTime = acquiringTime;
    }
}
