package com.masonlian.panelbackend.Dto;

import java.math.BigDecimal;

public class Counts {

    private  Integer countsId;
    private  String  address  ;
    private String poi ;
    private Integer counts ;
    private BigDecimal latitude;
    private BigDecimal longitude;
    private Integer month;

    public String getPublicName() {
        return publicName;
    }

    public void setPublicName(String publicName) {
        this.publicName = publicName;
    }

    private String publicName;

    public Integer getCountsId() {
        return countsId;
    }

    public void setCountsId(Integer countsId) {
        this.countsId = countsId;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPoi() {
        return poi;
    }

    public void setPoi(String poi) {
        this.poi = poi;
    }

    public Integer getCounts() {
        return counts;
    }

    public void setCounts(Integer counts) {
        this.counts = counts;
    }

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

    public Integer getMonth() {
        return month;
    }

    public void setMonth(Integer month) {
        this.month = month;
    }

}
