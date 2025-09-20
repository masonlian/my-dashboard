package Dto;

import java.math.BigDecimal;
import java.sql.Timestamp;

public class LocationData {

    public BigDecimal latitude;
    public BigDecimal longitude;
    public String locationName;
   // public Timestamp acquiringTime;

    public String getLocationName() {
        return locationName;
    }

    public void setLocationName(String locationName) {
        this.locationName = locationName;
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

//    public Timestamp getAcquiringTime() {
//        return acquiringTime;
//    }

//    public void setAcquiringTime(Timestamp acquiringTime) {
//        this.acquiringTime = acquiringTime;
//    }
}
