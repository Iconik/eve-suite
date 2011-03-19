class Character(object):
    def __init__(self, account, name, character_id, #IGNORE:R0913
                 corporation_name, corporation_id):
        self.account = account
        
        self.name = name
        self.character_id = character_id
        self.corporation_name = corporation_name
        self.corporation_id = corporation_id
        
        self.skill_queue = None
        self.character_sheet = None
        
    
    def get_skill_queue(self):
        """Populates and returns the characters skill queue"""
        if self.skill_queue is None:
            from model.dynamic.skills.skill_queue import SkillQueue
            self.skill_queue = SkillQueue(self.account.get_userID(),
                                         self.account.get_apiKey(),
                                         self.character_id)
        return self.skill_queue.get_skill_queue()
        
    def get_character_sheet(self):
        pass