package com.masonlian.panelbackend.Service;

import Dto.LocationData;
import com.masonlian.panelbackend.Dao.LocationDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ResponseStatusException;

@Component
public class LocationServiceImpl implements LocationService {

    @Autowired
    LocationDao locationDao;

    @Override
    public Integer enrollLocation(LocationData locationData){

        if(locationData != null){
            return locationDao.enrollLocation(locationData);

        }
       else throw new ResponseStatusException(HttpStatus.BAD_REQUEST);



    }
}
