package com.masonlian.panelbackend.Dao;

import Dto.Counts;
import Dto.LocationJournal;
import com.masonlian.panelbackend.RowMapper.LocationJournalRowMapper;
import com.masonlian.panelbackend.request.LocationData;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Component
public class LocationDaoImpl implements LocationDao {

    private static final Logger log = LoggerFactory.getLogger(LocationDaoImpl.class);

    @Autowired
    private NamedParameterJdbcTemplate namedParameterJdbcTemplate;


    @Override
   public Integer enrollLocation(LocationData locationData){


        System.out.println(locationData.getLatitude());
        System.out.println(locationData.getLongitude());


       String sql = "INSERT location_journal (  longitude, latitude, acquiring_time, public_name, address, poi ) VALUES ( :public_name, :longitude, :latitude, :acquiring_time, :address, :poi ) ";
       Map<String,Object > map = new HashMap<>();

       map.put("public_name", locationData.getPublicName());
       map.put("longitude", locationData.getLongitude());
       map.put("latitude", locationData.getLatitude());
       map.put("acquiring_time", locationData.getAcquiringTime());
       map.put("address", locationData.getAddress());
       map.put("poi", locationData.getPoi());

       KeyHolder keyHolder = new GeneratedKeyHolder();

       namedParameterJdbcTemplate.update(sql ,new MapSqlParameterSource(map), keyHolder);
       Integer  journalId= keyHolder.getKey().intValue();
       return journalId;

   }
    @Override
    public  LocationJournal getJournalById(Integer journalId){

        String sql = " SELECT * FROM location_journal WHERE journal_id = :journalId ";
        Map<String,Object> map = new HashMap<>();
        map.put("journalId", journalId);
        List< LocationJournal> locationJournalList =  namedParameterJdbcTemplate.query(sql,map, new LocationJournalRowMapper());
       if(locationJournalList.size()>0){
           return locationJournalList.get(0);
       } else  log.warn("找不到該ID代表資料:{}",journalId);
       return null;

    }

    @Override
    public  Integer createCountsEntity (LocationData locationData){

        String sql = " INSERT counts (address, poi, counts, latitude, longitude, month )   VALUES (:address, :poi, :counts, :latitude, :longitude, :month)";

        Map<String,Object> map = new HashMap<>();
        map.put("address", locationData.getAddress());
        map.put("poi", locationData.getPoi());
        map.put("counts",1);
        map.put("latitude", locationData.getLatitude());
        map.put("longitude", locationData.getLongitude());

        LocalDateTime acquireTime =  locationData.getAcquiringTime().toLocalDateTime();
        Integer month = acquireTime.getMonthValue();

        map.put("month", month);

        KeyHolder keyHolder = new GeneratedKeyHolder();
        namedParameterJdbcTemplate.update(sql,new MapSqlParameterSource(map),keyHolder);
        Integer countsId = keyHolder.getKey().intValue();
        return countsId;

    }

    @Override
    public Counts  getCountsByAddress(String address){
        String sql = " SELECT * FROM location_journal WHERE  address = :address ";
        Map<String,Object> map = new HashMap<>();
        map.put("address", address);
        List<Counts> countsList =  namedParameterJdbcTemplate.query(sql,map,new LocationJournalRowMapper());
        if(countsList.size()>0){
            return countsList.get(0);
        }else  log.warn("並無此地址。");
        return null;

    }

    @Override
    public Integer addCounts(Counts existedCounts){

        String sql = " UPDATE counts  SET counts = :counts  WHERE counts_id = :countsId  ";
        Map<String,Object> map = new HashMap<>();
        map.put("counts",existedCounts.getCounts());
        map.put("counts_id",existedCounts.getCountsId());
        namedParameterJdbcTemplate.update(sql,map);


        Counts countsAfter =  getCountsByAddress(existedCounts.getAddress());
        return countsAfter.getCounts();


    }

}
