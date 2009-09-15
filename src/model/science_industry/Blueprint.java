package model.science_industry;

import java.sql.SQLException;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class Blueprint {
	private int id;
	private int ml;
	private int baseWaste;

	public Blueprint(int id, int ml, int baseWaste) {
		this.id=id;
		this.ml=ml;
		this.baseWaste=baseWaste;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getMl() {
		return ml;
	}

	public void setMl(int ml) {
		this.ml = ml;
	}

	public int getBaseWaste() {
		return baseWaste;
	}

	public void setBaseWaste(int baseWaste) {
		this.baseWaste = baseWaste;
	}

	public static String[] listOfBlueprints() {
		String[] blueprints=null;

		String query = "SELECT typeName FROM invBlueprintTypes LEFT JOIN invTypes ON invBlueprintTypes.blueprintTypeID=invTypes.typeID WHERE published=1 ORDER BY typeName";

		CachedRowSet dbOut = DatabaseReader.reader(query);

		try {
			blueprints = new String[dbOut.size()];
			while(dbOut.next()) {
				blueprints[dbOut.getRow()-1]=dbOut.getString(1);
			}
			System.out.println();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return blueprints;
	}
}
