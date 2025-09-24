package com.masonlian.panelbackend.Service;

import Dto.Counts;
import Dto.LocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import com.masonlian.panelbackend.Dao.LocationDao;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ResponseStatusException;


@Component
public class LocationServiceImpl implements LocationService {

   private static final Logger log = LoggerFactory.getLogger(LocationServiceImpl.class);

    @Autowired
    LocationDao locationDao;

    @Override
    public Integer  enrollLocation(LocationData locationData) {

        if (locationData != null) {


            Integer journalId = locationDao.enrollLocation(locationData);

            Counts existedCounts = locationDao.getCountsByAddress(locationData.getAddress());//查總表

            if (existedCounts != null) {
                log.info("到達次數增加前為：{}",existedCounts.getCounts());
                existedCounts.setCounts(existedCounts.getCounts() + 1);
                Integer number  =  locationDao.addCounts(existedCounts);

                log.info("到達次數增加後為：{}",number);
            }
            else {
                Integer countsId = locationDao.createCountsEntity(locationData);
                log.info("新增的Counts ID為：{}！", countsId);
            }

        return journalId ;
    }

       else throw new ResponseStatusException(HttpStatus.BAD_REQUEST);

    }

    @Override
    public  LocationJournal getJournalById(Integer journalId){

        if (journalId != null) {
            return locationDao.getJournalById(journalId);
        }
        else log.warn("journalId is null");
        return null;
    }

}
