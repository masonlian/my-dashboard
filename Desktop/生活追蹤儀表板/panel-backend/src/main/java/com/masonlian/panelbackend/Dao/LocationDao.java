package com.masonlian.panelbackend.Dao;


import Dto.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationDao {
    Integer enrollLocation(LocationData locationData);
}
