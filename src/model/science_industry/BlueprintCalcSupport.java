package model.science_industry;

import java.sql.SQLException;

import javax.sql.rowset.CachedRowSet;

import model.database.DatabaseReader;

public class BlueprintCalcSupport {
	Blueprint blueprint;
	double me;
	double pe;
	double runs;
	Object[][] baseMaterials;
	Object[][] derivedMaterials;

	public BlueprintCalcSupport(Blueprint blueprint, double me, double pe, double runs) {
		this.blueprint = blueprint;
		this.me = me;
		this.pe = pe;
		this.runs = runs;
	}

	public BlueprintCalcSupport(String name, double me, double pe, double runs) {
		this.blueprint = new Blueprint(name);
		this.me = me;
		this.pe = pe;
		this.runs = runs;
	}

	public BlueprintCalcSupport(int id, double me, double pe, double runs) {
		this.blueprint = new Blueprint(id);
		this.me = me;
		this.pe = pe;
		this.runs = runs;
	}

	public void setBase() {

		CachedRowSet crs = DatabaseReader.reader("SELECT typeName,quantity,damagePerJob FROM typeActivityMaterials LEFT JOIN invTypes ON invTypes.typeID=typeActivityMaterials.requiredTypeID WHERE typeActivityMaterials.typeID='"+blueprint.getId()+"' AND activityID='1'");

		baseMaterials = new Object[crs.size()][7];

		try {
			for(int i = 0;i<baseMaterials.length;i++) {
				baseMaterials[i][0] = crs.getString(1);
				baseMaterials[i][1] = crs.getDouble(2);
				baseMaterials[i][2] = crs.getDouble(3);
				crs.next();
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void setDerived() {
		derivedMaterials = new Object[baseMaterials.length][7];
		for(int i = 0;i<baseMaterials.length;i++) {
			derivedMaterials[i][0] = baseMaterials[i][0]; 
			derivedMaterials[i][1] = (Double)baseMaterials[i][1]*runs;
			derivedMaterials[i][2] = Material.wasteFormula((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor(), me)*runs;
			derivedMaterials[i][3] = ((Double)derivedMaterials[i][1])+((Double)derivedMaterials[i][2]);
			derivedMaterials[i][4] = baseMaterials[i][2];
			derivedMaterials[i][5] = Material.eliminateWaste((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor());
			derivedMaterials[i][6] = Material.nextImprovement((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor(), (Double)derivedMaterials[i][5], me);
		}
	}

	public void updateME() {
		for(int i = 0;i<baseMaterials.length;i++) {
			derivedMaterials[i][2] = Material.wasteFormula((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor(), me)*runs;
			derivedMaterials[i][3] = ((Double)derivedMaterials[i][1])+((Double)derivedMaterials[i][2]);
			derivedMaterials[i][6] = Material.nextImprovement((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor(), (Double)derivedMaterials[i][5], me);
		}
	}

	public void updateRuns() {
		for(int i = 0;i<baseMaterials.length;i++) {
			derivedMaterials[i][1] = (Double)baseMaterials[i][1]*runs;
			derivedMaterials[i][2] = Material.wasteFormula((Double)baseMaterials[i][1], blueprint.getBaseWasteFactor(), me)*runs;
			derivedMaterials[i][3] = ((Double)derivedMaterials[i][1])+((Double)derivedMaterials[i][2]);
		}
	}

	public Object[] getManufacturingMaterials() {
		if(baseMaterials == null) {
			setBase();
		}
		if(derivedMaterials == null) {
			setDerived();
		}
		
		return derivedMaterials;

		/*Vector<String> names = blueprint.getMaterialNames(Activities.manufacturing);
		Vector<Integer> amounts = blueprint.getMaterialBaseAmounts(Activities.manufacturing);
		Vector<Integer> waste = blueprint.getMaterialWaste(Activities.manufacturing, me);
		Vector<Integer> total = new Vector<Integer>();
		for(int i = 0;i<amounts.size();i++) {
			total.add(amounts.get(i)+waste.get(i));
		}
		Vector<Double> damage = blueprint.getMaterialDamages(Activities.manufacturing);
		Vector<Integer> eliminateWaste = blueprint.getMaterialEliminateWaste(Activities.manufacturing, me);
		Vector<Integer> nextImprovement = blueprint.getMaterialNextImprovement(Activities.manufacturing, me);

		Object[] table = new Object[amounts.size()];
		for(int i = 0;i<amounts.size();i++) {
			table[i] = new Vector<Object>();
		}

		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(names.get(i));
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(amounts.get(i)*runs);
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(waste.get(i)*runs);
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(total.get(i)*runs);
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(damage.get(i));
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(eliminateWaste.get(i));
		}
		for(int i = 0;i < table.length; i++) {
			((Vector<Object>)table[i]).add(nextImprovement.get(i));
		}*/
	}

	public double getMe() {
		return me;
	}

	public void setMe(double me) {
		this.me = me;
	}

	public double getPe() {
		return pe;
	}

	public void setPe(double pe) {
		this.pe = pe;
	}

	public double getRuns() {
		return runs;
	}

	public void setRuns(double runs) {
		this.runs = runs;
	}
}