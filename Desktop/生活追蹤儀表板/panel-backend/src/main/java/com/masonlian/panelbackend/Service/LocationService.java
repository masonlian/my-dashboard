package com.masonlian.panelbackend.Service;


import Dto.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationService {
    Integer enrollLocation(LocationData locationData);

}
