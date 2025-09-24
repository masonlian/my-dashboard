package com.masonlian.panelbackend.RowMapper;

import Dto.LocationJournal;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;

public class LocationJournalRowMapper implements RowMapper<LocationJournal> {

    public LocationJournal mapRow(ResultSet rs, int rowNum) throws SQLException {

        LocationJournal locationJournal = new LocationJournal();
        locationJournal.setJournalId(rs.getInt("journal_id"));
        locationJournal.setLongitude(rs.getBigDecimal("longitude"));
        locationJournal.setLatitude(rs.getBigDecimal("latitude"));
        locationJournal.setAcquiringTime(rs.getTimestamp("acquiring_time"));
        locationJournal.setPublicName(rs.getString("public_name"));
        locationJournal.setAddress(rs.getString("address"));
        locationJournal.setPoi(rs.getString("poi"));

        return locationJournal;


    }
}
