package model.science_industry;

public class Invention {
	public static double researchPointsPerDay(double multiplier, double agentEffectiveQuality, double yourSkill, double agentSkill) {
		return multiplier*(1+agentEffectiveQuality/100)*Math.pow(yourSkill+agentSkill, 2);
	}
	
	public static double succesFormula(double baseChance, double encryptionSkillLevel, double datacore1Skill, double datacore2Skill, double baseItemMetaLevel, double decryptorModifier) {
		return baseChance * (1 + 0.01 * encryptionSkillLevel) *	(1 + (datacore1Skill + datacore2Skill) * (0.1 / (5 - baseItemMetaLevel))) * decryptorModifier;
	}
}
