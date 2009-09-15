xjc = /System/Library/Frameworks/JavaVm.framework/Versions/1.6/Commands/xjc
trang = java -jar ~/Programming/Libraries/trang.jar -I xml -O xsd

xml = .xml.aspx
xsd = .xsd

char = api/account/Characters

ch = api/character/
co = api/corporation/
ev = api/eve/
ma = api/map/

ab = accountbalances/AccountBalance
al = assetlist/AssetList
cs = charactersheet/CharacterSheet
fw = factionalwarfarestats/FacWarStats
ij = industryjobs/IndustryJobs
km = killmails/KillLog
mo = marketorders/MarketOrders
me = medals/Medals
st = skillintraining/SkillInTraining
sq = skillqueue/SkillQueue
st = standings/Standings
wj = walletjournal/WalletJournal
wt = wallettransactions/WalletTransactions
cl = containerlog/ContainerLog
cos = corporationsheet/CorporationSheet
mm = membermedals/MemberMedals
ms = membersecurity/MemberSecurity
msl = membersecuritylog/MemberSecurityLog
mt = membertracking/MemberTracking
pd = posdetails/StarbaseDetail
pl = poslist/StarbaseList
sh = shareholder/Shareholders
ti = titles/Titles
all = alliancelist/AllianceList
ct = certificatetree/CertificateTree
csl = conquerablestationlist/ConquerableStationList
el = errorlist/ErrorList
fws = factionalwarfaretopstats/FacWarTopStats
itn = idtoname/CharacterID
nti = nametoid/CharacterName
rt = reftypeslist/RefTypes
skt = skilltree/SkillTree
fwsy = factionalwarfaresystems/FacWarSystems
ju = jumps/Jumps
ki = kills/Kills
so = sovereignty/Sovereignty

se = api/server/serverstatus/ServerStatus

all: schema objects

schema:
	$(trang) $(char)$(xml) $(char)$(xsd)
	$(trang) $(ch)$(ab)$(xml) $(ch)$(ab)$(xsd)
	$(trang) $(ch)$(al)$(xml) $(ch)$(al)$(xsd)
	$(trang) $(ch)$(cs)$(xml) $(ch)$(cs)$(xsd)
	$(trang) $(ch)$(fw)$(xml) $(ch)$(fw)$(xsd)
	$(trang) $(ch)$(ij)$(xml) $(ch)$(ij)$(xsd)
	$(trang) $(ch)$(km)$(xml) $(ch)$(km)$(xsd)
	$(trang) $(ch)$(mo)$(xml) $(ch)$(mo)$(xsd)
	$(trang) $(ch)$(me)$(xml) $(ch)$(me)$(xsd)
	$(trang) $(ch)$(st)$(xml) $(ch)$(st)$(xsd)
	$(trang) $(ch)$(sq)$(xml) $(ch)$(sq)$(xsd)
	$(trang) $(ch)$(st)$(xml) $(ch)$(st)$(xsd)
	$(trang) $(ch)$(wj)$(xml) $(ch)$(wj)$(xsd)
	$(trang) $(ch)$(wt)$(xml) $(ch)$(wt)$(xsd)
	
	$(trang) $(co)$(ab)$(xml) $(co)$(ab)$(xsd)
	$(trang) $(co)$(al)$(xml) $(co)$(al)$(xsd)
	$(trang) $(co)$(cl)$(xml) $(co)$(cl)$(xsd)
	$(trang) $(co)$(cos)$(xml) $(co)$(cos)$(xsd)
	$(trang) $(co)$(fw)$(xml) $(co)$(fw)$(xsd)
	$(trang) $(co)$(ij)$(xml) $(co)$(ij)$(xsd)
	$(trang) $(co)$(km)$(xml) $(co)$(km)$(xsd)
	$(trang) $(co)$(mo)$(xml) $(co)$(mo)$(xsd)
	$(trang) $(co)$(me)$(xml) $(co)$(me)$(xsd)
	$(trang) $(co)$(mm)$(xml) $(co)$(mm)$(xsd)
	$(trang) $(co)$(ms)$(xml) $(co)$(ms)$(xsd)
	$(trang) $(co)$(msl)$(xml) $(co)$(msl)$(xsd)
	$(trang) $(co)$(mt)$(xml) $(co)$(mt)$(xsd)
	$(trang) $(co)$(pd)$(xml) $(co)$(pd)$(xsd)
	$(trang) $(co)$(pl)$(xml) $(co)$(pl)$(xsd)
	$(trang) $(co)$(sh)$(xml) $(co)$(sh)$(xsd)
	$(trang) $(co)$(st)$(xml) $(co)$(st)$(xsd)
	$(trang) $(co)$(ti)$(xml) $(co)$(ti)$(xsd)
	$(trang) $(co)$(wj)$(xml) $(co)$(wj)$(xsd)
	$(trang) $(co)$(wt)$(xml) $(co)$(wt)$(xsd)
	
	$(trang) $(ev)$(all)$(xml) $(ev)$(all)$(xsd)
	$(trang) $(ev)$(ct)$(xml) $(ev)$(ct)$(xsd)
	$(trang) $(ev)$(csl)$(xml) $(ev)$(csl)$(xsd)
	$(trang) $(ev)$(el)$(xml) $(ev)$(el)$(xsd)
	$(trang) $(ev)$(fws)$(xml) $(ev)$(fws)$(xsd)
	$(trang) $(ev)$(itn)$(xml) $(ev)$(itn)$(xsd)
#	$(trang) $(ev)$(nti)$(xml) $(ev)$(nti)$(xsd)
	$(trang) $(ev)$(rt)$(xml) $(ev)$(rt)$(xsd)
	$(trang) $(ev)$(skt)$(xml) $(ev)$(skt)$(xsd)
	
	$(trang) $(ma)$(fwsy)$(xml) $(ma)$(fwsy)$(xsd)
	$(trang) $(ma)$(ju)$(xml) $(ma)$(ju)$(xsd)
	$(trang) $(ma)$(ki)$(xml) $(ma)$(ki)$(xsd)
	$(trang) $(ma)$(so)$(xml) $(ma)$(so)$(xsd)
	
	$(trang) $(se)$(xml) $(se)$(xsd)

objects:
	$(xjc) -p api.account $(char)$(xsd)
	
	$(xjc) -p api.character.accountbalances $(ch)$(ab)$(xsd)
	$(xjc) -p api.character.assetlist $(ch)$(al)$(xsd)
	$(xjc) -p api.character.charactersheet $(ch)$(cs)$(xsd)
	$(xjc) -p api.character.factionalwarfarestats $(ch)$(fw)$(xsd)
	$(xjc) -p api.character.industryjobs $(ch)$(ij)$(xsd)
	$(xjc) -p api.character.killmails $(ch)$(km)$(xsd)
	$(xjc) -p api.character.marketorders $(ch)$(mo)$(xsd)
	$(xjc) -p api.character.medals $(ch)$(me)$(xsd)
	$(xjc) -p api.character.skillintraining $(ch)$(st)$(xsd)
	$(xjc) -p api.character.skillqueue $(ch)$(sq)$(xsd)
	$(xjc) -p api.character.standings $(ch)$(st)$(xsd)
	$(xjc) -p api.character.walletjournal $(ch)$(wj)$(xsd)
	$(xjc) -p api.character.wallettransactions $(ch)$(wt)$(xsd)
	
	$(xjc) -p api.corporation.accountbalances $(co)$(ab)$(xsd)
	$(xjc) -p api.corporation.assetlist $(co)$(al)$(xsd)
	$(xjc) -p api.corporation.containerlog $(co)$(cl)$(xsd)
	$(xjc) -p api.corporation.corporationsheet $(co)$(cos)$(xsd)
	$(xjc) -p api.corporation.factionalwarfarestats $(co)$(fw)$(xsd)
	$(xjc) -p api.corporation.industryjobs $(co)$(ij)$(xsd)
	$(xjc) -p api.corporation.killmails $(co)$(km)$(xsd)
	$(xjc) -p api.corporation.marketorders $(co)$(mo)$(xsd)
	$(xjc) -p api.corporation.medals $(co)$(me)$(xsd)
	$(xjc) -p api.corporation.membermedals $(co)$(mm)$(xsd)
	$(xjc) -p api.corporation.membersecurity $(co)$(ms)$(xsd)
	$(xjc) -p api.corporation.membersecuritylog $(co)$(msl)$(xsd)
	$(xjc) -p api.corporation.membertracking $(co)$(mt)$(xsd)
	$(xjc) -p api.corporation.posdetails $(co)$(pd)$(xsd)
	$(xjc) -p api.corporation.poslist $(co)$(pl)$(xsd)
	$(xjc) -p api.corporation.shareholder $(co)$(sh)$(xsd)
#	$(xjc) -p api.corporation.standings $(co)$(st)$(xsd)
	$(xjc) -p api.corporation.titles $(co)$(ti)$(xsd)
	$(xjc) -p api.corporation.walletjournal $(co)$(wj)$(xsd)
	$(xjc) -p api.corporation.wallettransactions $(co)$(wt)$(xsd)
	
	$(xjc) -p api.eve.alliancelist $(ev)$(all)$(xsd)
	$(xjc) -p api.eve.certificatetree $(ev)$(ct)$(xsd)
	$(xjc) -p api.eve.conquerablestationlist $(ev)$(csl)$(xsd)
	$(xjc) -p api.eve.errorlist $(ev)$(el)$(xsd)
	$(xjc) -p api.eve.factionalwarfaretopstats $(ev)$(fws)$(xsd)
#	$(xjc) -p api.eve.idtoname $(ev)$(itn)$(xsd)
#	$(xjc) -p api.eve.nametoid $(ev)$(nti)$(xsd)
	$(xjc) -p api.eve.reftypeslist $(ev)$(rt)$(xsd)
	$(xjc) -p api.eve.skilltree $(ev)$(skt)$(xsd)
	
	$(xjc) -p api.map.factionalwarfaresystems $(ma)$(fwsy)$(xsd)
	$(xjc) -p api.map.jumps $(ma)$(ju)$(xsd)
	$(xjc) -p api.map.kills $(ma)$(ki)$(xsd)
	$(xjc) -p api.map.sovereignty $(ma)$(so)$(xsd)
	
	$(xjc) -p api.server.serverstatus $(se)$(xsd)