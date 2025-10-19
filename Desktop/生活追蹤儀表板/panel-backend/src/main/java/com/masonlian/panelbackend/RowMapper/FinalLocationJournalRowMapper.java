package com.masonlian.panelbackend.RowMapper;

import com.masonlian.panelbackend.Dto.FinalLocationJournal;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;

public class FinalLocationJournalRowMapper implements RowMapper<FinalLocationJournal> {

    public FinalLocationJournal mapRow(ResultSet rs, int rowNum) throws SQLException {

        FinalLocationJournal finalLocationJournal = new FinalLocationJournal();
        finalLocationJournal.setJournalId(rs.getInt("journal_id"));
        finalLocationJournal.setPlaceId(rs.getString("place_id"));
        finalLocationJournal.setLatitude(rs.getBigDecimal("latitude"));
        finalLocationJournal.setLongitude(rs.getBigDecimal("longitude"));
        finalLocationJournal.setPoi(rs.getString("poi"));
        finalLocationJournal.setPublicName(rs.getString("public_name"));
        finalLocationJournal.setAcquiringTime(rs.getTimestamp("acquiring_time"));

        return finalLocationJournal;


    }
}
