package com.masonlian.panelbackend.Dao;


import com.masonlian.panelbackend.Dto.Counts;
import com.masonlian.panelbackend.Dto.FinalLocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationDao {
    Integer  enrollLocation(LocationData locationData);
    FinalLocationJournal getJournalById(Integer journalId);


    Counts getCountsByAddress(String address);
    Integer createCountsEntity (LocationData locationData);
    Integer addCounts(Counts existedCounts);
    Counts getCountsByPublicName(String publicName);

}

