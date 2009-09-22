package model.science_industry;

import java.sql.SQLException;
import java.util.Vector;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class RequiredMaterials {
	private Blueprint blueprint;
	private int activityID;
	private Vector<Material> minerals;
	private Vector<Material> components;
	private Vector<Material> skills;
	private Vector<Material> miscellaneous;

	public RequiredMaterials(Blueprint blueprint, int activityID) {
		this.blueprint = blueprint;
		this.activityID = activityID;
		loadMaterials();
	}

	public void loadMaterials() {
		minerals = new Vector<Material>();
		components = new Vector<Material>();
		skills = new Vector<Material>();
		miscellaneous = new Vector<Material>();
		CachedRowSet dbOut = DatabaseReader.reader("SELECT typeName, quantity, damagePerJob, invTypes.groupID, categoryID  FROM typeActivityMaterials LEFT JOIN invTypes LEFT JOIN invGroups ON typeActivityMaterials.requiredTypeID=invTypes.typeID AND invTypes.groupID=invGroups.groupID WHERE typeActivityMaterials.typeID='"+blueprint.getId()+"' AND activityID='"+activityID+"';");
		try {
			while(dbOut.next()) {
				Material material = new Material(dbOut.getString(1), dbOut.getInt(2), dbOut.getDouble(3));
				switch(dbOut.getInt(4)) {
				case 18:
					minerals.add(material);
					break;
				case 334:
					components.add(material);
					break;
				default:
					switch(dbOut.getInt(5)) {
					case 16:
						skills.add(material);
						break;
					default:
						miscellaneous.add(material);
						break;
					}
					break;
				}
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/*public Vector<String> getNames() {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<String> names = new Vector<String>();
		for(Material material:minerals) {
			names.add(material.getName());
		}
		for(Material material:components) {
			names.add(material.getName());
		}
		for(Material material:miscellaneous) {
			names.add(material.getName());
		}
		return names;
	}
	
	public Vector<Integer> getBaseAmounts() {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<Integer> materials = new Vector<Integer>();
		for(Material material:minerals) {
			materials.add(material.getPerfectAmount());
		}
		for(Material material:components) {
			materials.add(material.getPerfectAmount());
		}
		for(Material material:miscellaneous) {
			materials.add(material.getPerfectAmount());
		}
		return materials;
	}
	
	public Vector<Double> getDamages() {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<Double> materials = new Vector<Double>();
		for(Material material:minerals) {
			materials.add(material.getDamagePerJob());
		}
		for(Material material:components) {
			materials.add(material.getDamagePerJob());
		}
		for(Material material:miscellaneous) {
			materials.add(material.getDamagePerJob());
		}
		return materials;
	}

	public Vector<Integer> getNextImprovements(double baseWasteFactor, int currentMaterialEfficiency) {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<Integer> levels = new Vector<Integer>();
		for(Material material:minerals) {
			levels.add(material.nextImprovement(baseWasteFactor, currentMaterialEfficiency));
		}
		for(Material material:components) {
			levels.add(material.nextImprovement(baseWasteFactor, currentMaterialEfficiency));
		}
		for(Material material:miscellaneous) {
			levels.add(material.nextImprovement(baseWasteFactor, currentMaterialEfficiency));
		}
		return levels;
	}
	
	public Vector<Integer> eliminateWaste(double baseWasteFactor, int currentMaterialEfficiency) {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<Integer> levels = new Vector<Integer>();
		for(Material material:minerals) {
			levels.add(material.eliminateWaste(baseWasteFactor));
		}
		for(Material material:components) {
			levels.add(material.eliminateWaste(baseWasteFactor));
		}
		for(Material material:miscellaneous) {
			levels.add(material.eliminateWaste(baseWasteFactor));
		}
		return levels;
	}
	
	public Vector<Integer> waste(double baseWasteFactor, int currentMaterialEfficiency) {
		if(minerals==null || components==null || miscellaneous==null)
			loadMaterials();
		Vector<Integer> materials = new Vector<Integer>();
		for(Material material:minerals) {
			materials.add(material.wasteFormula(baseWasteFactor, currentMaterialEfficiency));
		}
		for(Material material:components) {
			materials.add(material.wasteFormula(baseWasteFactor, currentMaterialEfficiency));
		}
		for(Material material:miscellaneous) {
			materials.add(material.wasteFormula(baseWasteFactor, currentMaterialEfficiency));
		}
		return materials;
	}*/
}
