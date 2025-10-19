package com.masonlian.panelbackend.Dto;


import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class PlaceResponse {
    private String status;
    private List<StayedPlace> results;

    public List<StayedPlace> getResults() {
        return results;
    }

    public void setResults(List<StayedPlace> results) {
        this.results = results;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
