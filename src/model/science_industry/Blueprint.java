package model.science_industry;

import java.sql.SQLException;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class Blueprint {
	private int id;
	private String name;
	private int productID;
	private int tech;
	private double baseWasteFactor;
	private int productionLimit;
	private int race;
	private RequiredMaterials[] materials;

	public Blueprint(int id) {
		this.id=id;
		System.out.println("BlueprintID: "+id);
		this.materials = new RequiredMaterials[8];
		CachedRowSet dbOut = DatabaseReader.reader("SELECT typeName, productTypeID, techLevel, wasteFactor, maxProductionLimit, raceID FROM invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE BlueprintID='"+id+"';");
		try {
			dbOut.first();
			name = dbOut.getString(1);
			productID = dbOut.getInt(2);
			tech = dbOut.getInt(3);
			baseWasteFactor = dbOut.getInt(4);
			productionLimit = dbOut.getInt(5);
			race = dbOut.getInt(6);
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public Blueprint(String name) {
		this.name = name;
		this.materials = new RequiredMaterials[8];
		CachedRowSet dbOut = DatabaseReader.reader("SELECT typeID, productTypeID, techLevel, wasteFactor, maxProductionLimit, raceID FROM invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE typeName='"+name+"';");
		try {
			dbOut.first();
			id = dbOut.getInt(1);
			System.out.println("BlueprintID: "+id);
			productID = dbOut.getInt(2);
			tech = dbOut.getInt(3);
			baseWasteFactor = dbOut.getInt(4);
			productionLimit = dbOut.getInt(5);
			race = dbOut.getInt(6);
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public void loadMaterials(int activityID) {
		materials[activityID-1] = new RequiredMaterials(this, activityID);
	}

	public int getId() {
		return id;
	}

	public String getName() {
		return name;
	}

	public int getProductID() {
		return productID;
	}

	public int getTech() {
		return tech;
	}

	public double getBaseWasteFactor() {
		return baseWasteFactor;
	}

	public int getProductionLimit() {
		return productionLimit;
	}

	public int getRace() {
		return race;
	}
	
	/*public Vector<String> getMaterialNames(int activityID) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].getNames();
	}
	
	public Vector<Integer> getMaterialBaseAmounts(int activityID) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].getBaseAmounts();
	}
	
	public Vector<Double> getMaterialDamages(int activityID) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].getDamages();
	}
	
	public Vector<Integer> getMaterialWaste(int activityID, int materialEfficiency) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].waste(baseWasteFactor, materialEfficiency);
	}
	
	public Vector<Integer> getMaterialEliminateWaste(int activityID, int materialEfficiency) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].eliminateWaste(baseWasteFactor, materialEfficiency);
	}
	
	public Vector<Integer> getMaterialNextImprovement(int activityID, int materialEfficiency) {
		if(materials[activityID-1]==null)
			loadMaterials(activityID);
		return materials[activityID-1].getNextImprovements(baseWasteFactor, materialEfficiency);
	}

	public RequiredMaterials getMaterials(int activityID) {
		if(materials[activityID-1] == null) {
			loadMaterials(activityID);
		}
		return materials[activityID-1];
	}*/

	public static String[] listOfBlueprints() {
		String[] blueprints=null;

		String query = "SELECT typeName FROM invBlueprintTypes LEFT JOIN invTypes ON invBlueprintTypes.blueprintTypeID=invTypes.typeID WHERE published=1 ORDER BY typeName";

		CachedRowSet dbOut = DatabaseReader.reader(query);

		try {
			blueprints = new String[dbOut.size()];
			dbOut.beforeFirst();
			while(dbOut.next()) {
				blueprints[dbOut.getRow()-1]=dbOut.getString(1);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return blueprints;
	}
}
