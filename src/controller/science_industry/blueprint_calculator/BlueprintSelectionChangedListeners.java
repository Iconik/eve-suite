package controller.science_industry.blueprint_calculator;

import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.SelectionChangedEvent;

public class BlueprintSelectionChangedListeners implements ISelectionChangedListener {

	@Override
	public void selectionChanged(SelectionChangedEvent event) {
		IStructuredSelection selection = (IStructuredSelection)event.getSelection();
		String selectedBlueprint = (String)selection.getFirstElement();
		
	}
}
