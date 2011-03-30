import xml.etree.ElementTree as ElementTree
from model.dynamic.api import api
from model.dynamic.skills.skill_queue_item import SkillQueueItem

class SkillQueue(object):
    def __init__(self, user_id, api_key, character_id):
        api.fetch("char", "SkillQueue", user_id, api_key, character_id)

        tree = ElementTree.parse("%s/SkillQueue.xml.aspx" % \
                                 api.build_path("char", user_id, character_id))
        root = tree.getroot()
        rowset = root.find("result").find("rowset")
        self.skill_queue = list()
        if rowset.getchildren():
            for element in rowset:
                self.skill_queue.insert\
                (int(element.get("queuePosition")),
                 SkillQueueItem(int(element.get("typeID")),
                                int(element.get("level")),
                                int(element.get("startSP")),
                                int(element.get("endSP")),
                                element.get("startTime"),
                                element.get("endTime")))
