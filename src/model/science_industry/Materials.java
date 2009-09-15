package model.science_industry;

import java.sql.SQLException;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class Materials {
	private String material;
	private int perfectAmount;
	private int waste;
	private int total;
	private int improvesAtLevel;
	private int perfectME;
	
	public Materials(String material, int perfectAmount, int waste, int total,
			int improvesAtLevel, int perfectME) {
		super();
		this.material = material;
		this.perfectAmount = perfectAmount;
		this.waste = waste;
		this.total = total;
		this.improvesAtLevel = improvesAtLevel;
		this.perfectME = perfectME;
	}

	public String getMaterial() {
		return material;
	}

	public void setMaterial(String material) {
		this.material = material;
	}

	public int getPerfectAmount() {
		return perfectAmount;
	}

	public void setPerfectAmount(int perfectAmount) {
		this.perfectAmount = perfectAmount;
	}

	public int getWaste() {
		return waste;
	}

	public void setWaste(int waste) {
		this.waste = waste;
	}

	public int getTotal() {
		return total;
	}

	public void setTotal(int total) {
		this.total = total;
	}

	public int getImprovesAtLevel() {
		return improvesAtLevel;
	}

	public void setImprovesAtLevel(int improvesAtLevel) {
		this.improvesAtLevel = improvesAtLevel;
	}

	public int getPerfectME() {
		return perfectME;
	}

	public void setPerfectME(int perfectME) {
		this.perfectME = perfectME;
	}

	public static double[][] billOfMaterials(int blueprintID, int activityID) {
		double[][] materials = null;
		String query = "SELECT requiredTypeID, quantity, damagePerJob FROM typeActivityMaterials WHERE typeID='"+blueprintID+"' AND activityID='"+activityID+"';";
	
		CachedRowSet dbOut = DatabaseReader.reader(query);
	
		try {
			materials = new double[3][dbOut.size()];
			while(dbOut.next()) {
				materials[0][dbOut.getRow()-1] = dbOut.getDouble(1);
				materials[1][dbOut.getRow()-1] = dbOut.getDouble(2);
				materials[2][dbOut.getRow()-1] = dbOut.getDouble(3);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
		return materials;
	}

	public static int wasteFormula(int materialAmount, int baseWasteFactor, int materialEfficiency) {
		return (int) Math.round(((double)materialAmount)*
				(((double)baseWasteFactor)/100)*
				((materialEfficiency<0?1-materialEfficiency:1/(((double)materialEfficiency)+1))));
	}

	public static int[] blueprintWaste(int[] materialAmounts, int baseWasteFactor, int materialEfficiency) {
		int[] waste = new int[materialAmounts.length];
		for(int i=0; i<materialAmounts.length; i++) {
			waste[i]=wasteFormula(materialAmounts[i], baseWasteFactor, materialEfficiency);
		}
		return waste;
	}

	public static int eliminateWaste(int materialAmount, int baseWasteFactor) {
		return (int) Math.ceil(0.02*((double)baseWasteFactor)*((double)materialAmount));
	}

	public static int[] blueprintEliminateWaste(int[] materialAmounts, int baseWasteFactor) {
		int[] perfect = new int[materialAmounts.length];
		for(int i=0; i<materialAmounts.length; i++) {
			perfect[i]=eliminateWaste(materialAmounts[i], baseWasteFactor);
		}
		return perfect;
	}

	public static int nextImprovement(int materialAmount, int perfectME, int baseWasteFactor, int currentMaterialEfficiency) {
		if(currentMaterialEfficiency>perfectME) {
			return perfectME;
		} else {
			int currentWaste = wasteFormula(materialAmount, baseWasteFactor, currentMaterialEfficiency);
			for(int i=currentMaterialEfficiency;i<=perfectME;++i) {
				int projectedWaste = wasteFormula(materialAmount, baseWasteFactor, i);
				if(projectedWaste<currentWaste) {
					return i;
				}
			}
		}
		return 0;
	}

	public static int[] blueprintNextImprovements(int[] materialAmounts, int[] perfectME, int baseWasteFactor, int currentMaterialEfficiency) {
		int[] waste = new int[materialAmounts.length];
		for(int i = 0;i<materialAmounts.length;i++) {
			waste[i] = nextImprovement(materialAmounts[i], perfectME[i], baseWasteFactor, currentMaterialEfficiency);
		}
		return waste;
	}

	public static String resolveMaterial(int id) {
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
