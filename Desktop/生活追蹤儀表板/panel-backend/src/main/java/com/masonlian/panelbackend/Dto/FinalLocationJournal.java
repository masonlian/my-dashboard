package com.masonlian.panelbackend.Dto;

import java.math.BigDecimal;
import java.sql.Timestamp;

public class FinalLocationJournal {

    private Integer journalId;
    private BigDecimal latitude;
    private BigDecimal longitude;
    private Timestamp acquiringTime;
    private String publicName;
    private String address;
    private String poi;
    private String placeId;


    public Integer getJournalId() {
        return journalId;
    }

    public void setJournalId(Integer journalId) {
        this.journalId = journalId;
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

    public Timestamp getAcquiringTime() {
        return acquiringTime;
    }

    public void setAcquiringTime(Timestamp acquiringTime) {
        this.acquiringTime = acquiringTime;
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

    public String getPlaceId() {
        return placeId;
    }

    public void setPlaceId(String placeId) {
        this.placeId = placeId;
    }

    public String getPoi() {
        return poi;
    }

    public void setPoi(String poi) {
        this.poi = poi;
    }
}
