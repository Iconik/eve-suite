package view.science_industry.blueprint_calculator;

import java.text.NumberFormat;

import model.science_industry.Materials;

import org.eclipse.jface.viewers.ITableLabelProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.swt.graphics.Image;

public class BlueprintCalcLabelProvider extends LabelProvider implements ITableLabelProvider {

	@Override
	public Image getColumnImage(Object element, int columnIndex) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String getColumnText(Object element, int columnIndex) {
		Materials material = (Materials)element;
		
		switch(columnIndex) {
		case 0:
			return material.getMaterial();
		case 1:
			return NumberFormat.getInstance().format(material.getPerfectAmount());
		case 2:
			return NumberFormat.getInstance().format(material.getWaste());
		case 3:
			return NumberFormat.getInstance().format(material.getTotal());
		case 4:
			return NumberFormat.getInstance().format(material.getPerfectME());
		case 5:
			return NumberFormat.getInstance().format(material.getImprovesAtLevel());
		default:
			throw new RuntimeException("Should not happen");
		}
	}
	
}
