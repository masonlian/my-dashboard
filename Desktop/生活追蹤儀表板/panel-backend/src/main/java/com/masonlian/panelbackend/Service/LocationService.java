package com.masonlian.panelbackend.Service;


import com.masonlian.panelbackend.Dto.FinalLocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import org.springframework.stereotype.Component;

@Component
public interface LocationService {
    Integer  enrollLocation(LocationData locationData);
    FinalLocationJournal getJournalById(Integer journalId);

}
