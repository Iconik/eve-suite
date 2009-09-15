package model.science_industry;

public class Invention {
	public static int researchPointsPerDay(double multiplier, int agentEffectiveQuality, int yourSkill, int agentSkill) {
		return (int) (multiplier*(1+((double)agentEffectiveQuality)/100)*Math.pow((double)yourSkill+(double)agentSkill, 2));
	}
	
	public static double succesFormula(int baseChance, int encryptionSkillLevel, int datacore1Skill, int datacore2Skill, int baseItemMetaLevel, double decryptorModifier) {
		return ((double)baseChance) *
		(1 + (0.01 * ((double)encryptionSkillLevel))) *
		(1 + ((((double)datacore1Skill) + ((double)datacore2Skill)) * (0.1 / (5 - ((double)baseItemMetaLevel))))) *
		((double)decryptorModifier);
	}
}
