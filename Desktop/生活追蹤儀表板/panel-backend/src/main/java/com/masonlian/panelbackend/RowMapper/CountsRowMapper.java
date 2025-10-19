package com.masonlian.panelbackend.RowMapper;

import com.masonlian.panelbackend.Dto.Counts;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;

public class CountsRowMapper  implements RowMapper<Counts> {

    public Counts mapRow(ResultSet rs, int rowNum) throws SQLException {

        Counts counts = new Counts();

        counts.setCountsId(rs.getInt("counts_id"));
        counts.setAddress(rs.getString("address"));
        counts.setPoi(rs.getString("poi"));
        counts.setLatitude(rs.getBigDecimal("latitude"));
        counts.setLongitude(rs.getBigDecimal("longitude"));
        counts.setMonth(rs.getInt("month"));
        counts.setCounts(rs.getInt("counts"));
        counts.setPublicName(rs.getString("public_name"));


        return counts;





    }
}
