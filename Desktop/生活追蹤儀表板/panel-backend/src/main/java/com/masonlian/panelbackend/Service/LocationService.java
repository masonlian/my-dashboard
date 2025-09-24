package com.masonlian.panelbackend.Service;


import Dto.LocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationService {
    Integer  enrollLocation(LocationData locationData);
    LocationJournal getJournalById(Integer journalId);

}
