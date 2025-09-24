package com.masonlian.panelbackend.Dao;


import Dto.Counts;
import Dto.LocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationDao {
    Integer  enrollLocation(LocationData locationData);
    LocationJournal getJournalById(Integer journalId);


    Counts getCountsByAddress(String address);
    Integer createCountsEntity (LocationData locationData);
    Integer addCounts(Counts existedCounts);

}

