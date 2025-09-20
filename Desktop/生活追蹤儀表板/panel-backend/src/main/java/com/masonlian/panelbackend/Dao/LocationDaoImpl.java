package com.masonlian.panelbackend.Dao;

import Dto.LocationData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class LocationDaoImpl implements LocationDao {

    @Autowired
    private NamedParameterJdbcTemplate namedParameterJdbcTemplate;


    @Override
   public Integer enrollLocation(LocationData locationData){

        System.out.println(locationData.getLocationName());
        System.out.println(locationData.getLatitude());
        System.out.println(locationData.getLongitude());


        String sql = "INSERT  location ( name, longitude, latitude) VALUES ( :name, :longitude, :latitude ) ";
       Map<String,Object > map = new HashMap<>();

       map.put("name", locationData.getLocationName());
       map.put("longitude", locationData.getLongitude());
       map.put("latitude", locationData.getLatitude());
      // map.put("acquiring_time", locationData.getAcquiringTime());

       KeyHolder keyHolder = new GeneratedKeyHolder();
       namedParameterJdbcTemplate.update(sql ,new MapSqlParameterSource(map), keyHolder);
       Integer locationId= keyHolder.getKey().intValue();

       return locationId;




   }


}
