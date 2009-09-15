package model.api;

public interface URLs {

    static final String staticURL = "http://api.eve-online.com";
    
    //Prefix
    static final String character = "char";
    static final String account = "account";
    static final String corp = "corp";
    static final String eve = "eve";
    static final String map = "map";
    
    //suffix
    static final String xml = ".xml.aspx";
    
    //Account
    static final String characterList = "Characters";
    
    //Character
    static final String AccountBalances = "AccountBalance";
    static final String AssetList = "AssetList";
    static final String CharacterSheet = "CharacterSheet";
    static final String FacWarStats = "FacWarStats";
    static final String IndustryJobs = "IndustryJobs";
    static final String Killlog = "Killlog";
    static final String MarketOrders = "MarketOrders";
    static final String Medals = "Medals";
    static final String SkillInTraining = "SkillInTraining";
    static final String SkillQueue = "SkillQueue";
    static final String Standings = "Standings";
    static final String WalletJournal = "WalletJournal";
    static final String WalletTransactions = "WalletTransactions";
    
    //corp only
    static final String ContainerLod = "ContainerLog";
    static final String CorporationSheet = "CorporationSheet";
    static final String MemberMedals = "MemberMedals";
    static final String MemberSecurity = "MemberSecurity";
    static final String MemberSecurityLog = "MemberSecurityLog";
    static final String MemberTracking = "MemberTracking";
    static final String POSDetails = "StarbaseDetail";
    static final String POSList = "StarbaseList";
    static final String Shareholders = "Shareholders";
    static final String Titles = "Titles";
    
    //EVE
    static final String AllianceList = "AllianceList";
    static final String CertificateTree = "CertificateTree";
    static final String OutpostList = "ConquerableStationList";
    static final String ErrorList = "ErrorList";
    static final String FacWarTopStats = "FacWarTopStats";
    static final String IDToName = "CharacterName";
    static final String NameToID = "CharacterID";
    static final String RefTypesList = "RefTypes";
    static final String SkillTree = "SkillTree";
    
    //Map
    static final String FacWarOccupancy = "FacWarSystems";
    static final String Jumps = "Jumps";
    static final String Kills = "Kills";
    static final String Sovereignty = "Sovereignty";
    
    //Server
    static final String servServerStatus = "/server/ServerStatus.xml.aspx";
    
    //Misc
    static final String IDToPortrait = "http://img.eve.is/serv.asp";
}
