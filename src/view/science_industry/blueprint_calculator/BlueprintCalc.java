package view.science_industry.blueprint_calculator;

import java.util.Vector;

import model.SubStringContentProposalProvider;
import model.science_industry.Blueprint;
import model.science_industry.BlueprintCalcSupport;

import org.eclipse.jface.fieldassist.ComboContentAdapter;
import org.eclipse.jface.fieldassist.ContentProposalAdapter;
import org.eclipse.jface.fieldassist.IContentProposal;
import org.eclipse.jface.fieldassist.IContentProposalListener;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.layout.RowDataFactory;
import org.eclipse.jface.layout.RowLayoutFactory;
import org.eclipse.jface.viewers.ComboViewer;
import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.jface.viewers.TableViewerColumn;
import org.eclipse.jface.window.ApplicationWindow;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.ModifyEvent;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.layout.RowLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Spinner;

public class BlueprintCalc extends ApplicationWindow {
	Vector<ComboViewer> skills;
	Vector<Spinner> blueprintSettings;
	private ComboViewer blueprintCombo;
	private TableViewer materialTable;
	private BlueprintCalcSupport blueprintSupport;


	public BlueprintCalc() {
		super(null);
		
		skills = new Vector<ComboViewer>();
		blueprintSettings = new Vector<Spinner>();
	}

	protected Control createContents(Composite parent)
	{
		getShell().setText("Blueprint Calculator");
		RowLayoutFactory.fillDefaults().spacing(0).type(SWT.VERTICAL).fill(true).applyTo(parent);

		{
			//Control Section
			Composite controls = new Composite(parent, SWT.NONE);
			GridLayoutFactory.fillDefaults().numColumns(4).spacing(0,0).generateLayout(controls);

			{
				//Blueprint Selector
				Composite blueprintComposite = new Composite(controls, 0);
				GridDataFactory.fillDefaults().span(3, 1).applyTo(blueprintComposite);
				blueprintComposite.setLayout(new RowLayout(SWT.HORIZONTAL));
				Label blueprintLabel = new Label(blueprintComposite, 0);
				blueprintLabel.setText("Blueprint:");
				blueprintCombo = new ComboViewer(blueprintComposite, SWT.DROP_DOWN | SWT.BORDER);
				String[] blueprintList = Blueprint.listOfBlueprints();
				blueprintCombo.add(blueprintList);
				blueprintCombo.addSelectionChangedListener(new ISelectionChangedListener() {
					@Override
					public void selectionChanged(SelectionChangedEvent event) {
						blueprintChanged();
					}
				});

				{
					//Blueprint Selector Proposals
					char[] autoActivationCharacters = new char[] {
							'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
							'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
							'0','1','2','3','4','5','6','7','8','9','\'',' '};
					SubStringContentProposalProvider scpp = new SubStringContentProposalProvider(blueprintList);
					scpp.setFiltering(true);
					ContentProposalAdapter adapter = new ContentProposalAdapter(blueprintCombo.getCombo(), new ComboContentAdapter(), scpp, null, autoActivationCharacters);
					adapter.setProposalAcceptanceStyle(ContentProposalAdapter.PROPOSAL_REPLACE);
					adapter.addContentProposalListener(new IContentProposalListener() {
						@Override
						public void proposalAccepted(IContentProposal arg0) {
							blueprintChanged();
						}
					});
				}
			}

			{
				//Skill Section
				Composite skillContainer = new Composite(controls, SWT.BORDER);
				GridDataFactory.fillDefaults().span(1, 2).applyTo(skillContainer);
				GridLayoutFactory.fillDefaults().numColumns(2).spacing(0, 0).generateLayout(skillContainer);


				for(int i=0;i<4;i++) {
					Composite container = new Composite(skillContainer, SWT.NONE);
					container.setLayout(new RowLayout(SWT.HORIZONTAL));
					ComboViewer combo = new ComboViewer(container, SWT.DROP_DOWN | SWT.BORDER | SWT.READ_ONLY);
					for(int j = 1;j<=5;j++) {
						combo.add(j);
					}
					Label label = new Label(container, SWT.NONE);
					String[] labels = {"Industry","Metallurgy","Production Efficiency","Research"};
					label.setText(labels[i]);
					skills.add(combo);
				}
			}

			{
				//ME, PE, Runs Section
				for(int i=0;i<3;i++) {
					Composite container = new Composite(controls, SWT.NONE);
					RowLayoutFactory.fillDefaults().type(SWT.HORIZONTAL).applyTo(container);
					Label label = new Label(container, SWT.NONE);
					String[] labels = {"ME:","PE:","Runs:"};
					label.setText(labels[i]);
					Spinner spinner = new Spinner(container, SWT.BORDER);
					RowDataFactory.swtDefaults().hint(50, SWT.DEFAULT).applyTo(spinner);
					blueprintSettings.add(spinner);
					spinner.setMinimum(Integer.MIN_VALUE);
					spinner.setMaximum(Integer.MAX_VALUE);
				}
				
				blueprintSettings.get(0).addModifyListener(new ModifyListener() {
					@Override
					public void modifyText(ModifyEvent e) {
						meChanged();
					}
				});
				blueprintSettings.get(2).setSelection(1);
				blueprintSettings.get(2).addModifyListener(new ModifyListener() {
					@Override
					public void modifyText(ModifyEvent e) {
						runsChanged();
					}
				});
			}

			{
				Composite materials = new Composite(parent, SWT.NONE);
				RowDataFactory.swtDefaults().applyTo(materials);
				RowLayoutFactory.fillDefaults().type(SWT.HORIZONTAL).fill(true).applyTo(materials);
				materialTable = new TableViewer(materials, SWT.SINGLE | SWT.NO_SCROLL | SWT.FULL_SELECTION | SWT.BORDER);

				String[] headers = {"Material","Perfect Amounts","Waste","Total","Damage Per Job","Perfect ME","Improves At Level"};
				int[] bounds = {250,100,100,100,100,100,100};
				int[] alignment = {SWT.LEFT, SWT.RIGHT, SWT.RIGHT, SWT.RIGHT, SWT.RIGHT, SWT.RIGHT, SWT.RIGHT,};

				for(int i = 0; i<headers.length;i++) {
					TableViewerColumn column = new TableViewerColumn(materialTable, alignment[i]);
					column.getColumn().setText(headers[i]);
					column.getColumn().setWidth(bounds[i]);
					column.getColumn().setResizable(false);
					column.getColumn().setMoveable(true);
				}
				materialTable.getTable().setHeaderVisible(true);
				materialTable.getTable().setLinesVisible(true);

				materialTable.setContentProvider(new BlueprintCalcContentProvider());
				materialTable.setLabelProvider(new BlueprintCalcLabelProvider());
			}
		}
		getShell().pack();
		return parent;
	}

	protected void blueprintChanged() {
		blueprintSupport = new BlueprintCalcSupport(blueprintCombo.getCombo().getText(),
				Integer.parseInt(blueprintSettings.get(0).getText()),
				Integer.parseInt(blueprintSettings.get(1).getText()),
				Integer.parseInt(blueprintSettings.get(2).getText()));
		materialTable.setInput(blueprintSupport.getManufacturingMaterials());
		getShell().pack();
	}
	
	protected void meChanged() {
		blueprintSupport.setMe(blueprintSettings.get(0).getSelection());
		blueprintSupport.updateME();
		materialTable.refresh();
	}
	
	protected void runsChanged() {
		blueprintSupport.setRuns(Integer.parseInt(blueprintSettings.get(2).getText()));
		blueprintSupport.updateRuns();
		materialTable.refresh();
	}

	public static void main(String[] args) {
		BlueprintCalc awin = new BlueprintCalc();
		awin.setBlockOnOpen(true);
		awin.open();
		Display.getCurrent().dispose();
	}
}
