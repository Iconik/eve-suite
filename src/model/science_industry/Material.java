package model.science_industry;

import java.sql.SQLException;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class Material {
	private String name;
	private int typeID;
	private double perfectAmount;
	private double damagePerJob;
	
	public Material(String name, int typeID, double perfectAmount, double damagePerJob) {
		this.name = name;
		this.typeID = typeID;
		this.perfectAmount = perfectAmount;
		this.damagePerJob = damagePerJob;
	}
	
	public Material(String name, int perfectAmount, double damagePerJob) {
		this.name = name;
		this.perfectAmount = perfectAmount;
		this.damagePerJob = damagePerJob;
	}
	
	public Material(int typeID, int perfectAmount, double damagePerJob) {
		this.typeID = typeID;
		this.perfectAmount = perfectAmount;
		this.damagePerJob = damagePerJob;
	}

	public String getName() {
		return name;
	}

	public int getTypeID() {
		return typeID;
	}

	public double getPerfectAmount() {
		return perfectAmount;
	}

	public double getDamagePerJob() {
		return damagePerJob;
	}

	public double wasteFormula(double baseWasteFactor, double materialEfficiency) {
		return Math.round(perfectAmount*
				(baseWasteFactor/100*
				(materialEfficiency<0?1-materialEfficiency:1/(materialEfficiency+1))));
	}

	public double eliminateWaste(double baseWasteFactor) {
		return Math.ceil(0.02*baseWasteFactor*perfectAmount);
	}
	
	public double nextImprovement(double baseWasteFactor, double currentMaterialEfficiency) {
		double perfectME = eliminateWaste(baseWasteFactor); 
		if(currentMaterialEfficiency>perfectME) {
			return perfectME;
		} else {
			double currentWaste = wasteFormula(baseWasteFactor, currentMaterialEfficiency);
			for(double i=currentMaterialEfficiency;i<=perfectME;++i) {
				double projectedWaste = wasteFormula(baseWasteFactor, i);
				if(projectedWaste<currentWaste) {
					return i;
				}
			}
		}
		return 0;
	}
	
	public static double eliminateWaste(double perfectAmount, double baseWasteFactor) {
		return Math.ceil(0.02*baseWasteFactor*perfectAmount);
	}
	
	public static double wasteFormula(double perfectAmount, double baseWasteFactor, double materialEfficiency) {
		return Math.round(perfectAmount*
				(baseWasteFactor/100*
				(materialEfficiency<0?1-materialEfficiency:1/(materialEfficiency+1))));
	}
	
	public static double nextImprovement(double perfectAmount, double baseWasteFactor, double perfectME, double currentMaterialEfficiency) {
		if(currentMaterialEfficiency>perfectME) {
			return perfectME;
		} else {
			double currentWaste = wasteFormula(perfectAmount, baseWasteFactor, currentMaterialEfficiency);
			for(double i=currentMaterialEfficiency;i<=perfectME;++i) {
				double projectedWaste = wasteFormula(perfectAmount, baseWasteFactor, i);
				if(projectedWaste<currentWaste) {
					return i;
				}
			}
		}
		return 0;
	}

	public static String idToName(int id) {
		try {
			CachedRowSet crs = DatabaseReader.reader("SELECT typeName FROM invTypes WHERE typeID='"+id+"';");
			crs.first();
			return crs.getString(1);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
}
