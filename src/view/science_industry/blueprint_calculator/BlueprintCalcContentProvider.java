package view.science_industry.blueprint_calculator;

import model.science_industry.Activities;
import model.science_industry.Blueprint;
import model.science_industry.Materials;

import org.eclipse.jface.viewers.IStructuredContentProvider;
import org.eclipse.jface.viewers.Viewer;

public class BlueprintCalcContentProvider implements IStructuredContentProvider {

	@Override
	public Object[] getElements(Object inputElement) {
		
		Blueprint blueprint = (Blueprint) inputElement;
		
		double[][] raw = Materials.billOfMaterials(blueprint.getId(), Activities.manufacturing);
		if(raw.length<=0 || raw[0].length<=0)
			return new Object[0];
		int[] mats = new int[raw[1].length];
		for(int i=0;i<mats.length;i++){
			mats[i]=(int)(raw[1][i]);
		}
		
		int[] waste = Materials.blueprintWaste(mats, blueprint.getBaseWaste(), blueprint.getMl());
		
		int[] perfectME = Materials.blueprintEliminateWaste(mats, blueprint.getBaseWaste());
		
		int[] nextImprovement = Materials.blueprintNextImprovements(mats, perfectME, blueprint.getBaseWaste(), blueprint.getMl());
		
		Materials[] materials = new Materials[mats.length]; 
		
		for(int i=0;i<materials.length;i++) {
			materials[i] = new Materials(Materials.resolveMaterial((int)raw[0][i]), mats[i], waste[i], mats[i]+waste[i], nextImprovement[i], perfectME[i]);
		}
		
		return materials;
	}
	
	@Override
	public void dispose() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void inputChanged(Viewer viewer, Object oldInput, Object newInput) {
		// TODO Auto-generated method stub
	}
}
