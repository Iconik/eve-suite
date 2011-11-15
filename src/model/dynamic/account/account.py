from model.flyweight import Flyweight
from model.dynamic.api import api
from model.dynamic.character.character import Character
import xml.etree.ElementTree as ET

class Account(Flyweight):
    def __init__(self, user_id, api_key):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.user_id = int(user_id)
        self.api_key = api_key.strip()

        api.fetch("account", "Characters", self.user_id, self.api_key)
        
        tree = ET.parse("{}/Characters.xml.aspx".format(api.build_path("account", self.user_id)))
        root = tree.getroot()
        rowset = root.find("result").find("rowset")

        self.characters = list()

        for element in rowset:
            self.characters.append(Character(
                self, element.get("name"), int(element.get("characterID")),
                element.get("corporationName"), int(element.get(
                    "corporationID"))))

    def get_user_id(self):
        """Returns the account's user_id"""
        return self.user_id

    def get_api_key(self):
        """Returns the account's api_key"""
        return self.api_key

    def get_characters(self):
        """Returns the list of characters the account contains"""
        return self.characters
