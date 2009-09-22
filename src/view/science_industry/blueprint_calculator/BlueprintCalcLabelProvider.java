package view.science_industry.blueprint_calculator;

import java.text.NumberFormat;

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
		Object[] material = (Object[])element;
		
		switch(columnIndex) {
		case 0:
			return (String)material[0];
		case 1:
			return NumberFormat.getInstance().format((Double)material[1]);
		case 2:
			return NumberFormat.getInstance().format((Double)material[2]);
		case 3:
			return NumberFormat.getInstance().format((Double)material[3]);
		case 4:
			return NumberFormat.getInstance().format((Double)material[4]);
		case 5:
			return NumberFormat.getInstance().format((Double)material[5]);
		case 6:
			return NumberFormat.getInstance().format((Double)material[6]);
		default:
			throw new RuntimeException("Should not happen");
		}
	}
}
