package model.database;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.sql.rowset.CachedRowSet;

import com.sun.rowset.CachedRowSetImpl;

/***************************************************
 * Remember that everything read from the database *
 * should be disposed as soon as it is not needed  *
 * anymore, to conserve memory                     *
 ***************************************************/

public class DatabaseReader {
	public static CachedRowSet reader(String query) {
		Connection connection = null;
		ResultSet rs = null;
		CachedRowSet rowSet = null;

		try {
			Class.forName("org.sqlite.JDBC");

			// Create a database connection
			connection = DriverManager.getConnection("jdbc:sqlite:Resources/Database/apo15-sqlite3-v1.db");
			Statement stat = connection.createStatement();
			rs = stat.executeQuery(query);
			
			rowSet = new CachedRowSetImpl();
			rowSet.populate(rs);
			rowSet.first();
		}
		catch(SQLException e) {
			// If the error message is "out of memory", it probably means no database file is found
			System.err.println(e.getMessage());
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if(connection != null)
					// Closing connection to database, everything regarding the database should be done before closing.
					connection.close();
			} catch(SQLException e) {
				// Connection close failed.
				System.err.println(e);
			}
		}
		return rowSet;
	}
	
	public static int resolveTypeID(String typeName) {
		typeName.replace("'", "\'");
		CachedRowSet crs = reader("SELECT typeID FROM invTypes WHERE typeName='"+typeName+"';");
		try {
			return crs.getInt(1);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return 0;
	}
}
