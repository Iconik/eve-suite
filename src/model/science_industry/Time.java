package model.science_industry;

public class Time {
	public static int ResearchTime(int blueprintBaseResearchTime, int metallurgySkillLevel, double researchSlotModifier, double implantModifier) {
		return (int) (((double)blueprintBaseResearchTime)*
				(1-(0.05*((double)metallurgySkillLevel)))*
				researchSlotModifier*
				implantModifier);
	}

	public static int productionTime(int baseProductionTime, double productivityModifier, int productionEfficiency, int industrySkill, double implantModifier, double productionSlotModifier) {
		return (int) (((double)baseProductionTime)*(1-(productivityModifier/((double)baseProductionTime))*(productionEfficiency<0?(productionEfficiency-1):(((double)productionEfficiency)/(1+((double)productionEfficiency)))))*((1-(0.04*((double)industrySkill)))*implantModifier*productionSlotModifier));
	}

	public static int inventionTime(int blueprintBaseInventionTime, double inventionSlotModifier, double implantModifier) {
		return (int) (((double)blueprintBaseInventionTime)*inventionSlotModifier*implantModifier);
	}
}
