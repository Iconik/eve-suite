import re

if __name__ == '__main__':
    input = """CREATE TABLE "invTypes" (
  "typeID" int(11) NOT NULL,
  "groupID" smallint(6) default NULL,
  "typeName" varchar(100) default NULL,
  "description" varchar(3000) default NULL,
  "graphicID" smallint(6) default NULL,
  "radius" double default NULL,
  "mass" double default NULL,
  "volume" double default NULL,
  "capacity" double default NULL,
  "portionSize" int(11) default NULL,
  "raceID" tinyint(3) default NULL,
  "basePrice" double default NULL,
  "published" tinyint(1) default NULL,
  "marketGroupID" smallint(6) default NULL,
  "chanceOfDuplicating" double default NULL,
  "iconID" smallint(6) default NULL,
  PRIMARY KEY  ("typeID")
)"""

    table_name_extractor = re.compile(r'\s*CREATE TABLE "(\w*)" \(') #extracts the table name
    key_extractor = re.compile(r"\s*PRIMARY KEY  \((.*)\)") #extracts the primary keys in a raw string
    variable_extract = re.compile(r'"(\w+)"') #returns variables enclosed in quotation marks
    title_extract = re.compile(r'[a-z]+(\w+)') #removes the category prefix from the table name
    varre = re.compile(r'\s*"(\w+)" (\S+)') #extracts variable name and type
    under = re.compile(r'([A-Z])') #puts underscore in front of uppercase letters
    type_split = re.compile(r'(\w+)(?:\((\d+)\))?') #Splits a type up into its "type" and length 

    lines = input.splitlines()
    table_name = table_name_extractor.match(lines[0]).group(1)
    key = key_extractor.match(lines[-2])
    keys = variable_extract.findall(key.group(1))

    vars = list()
    types = list()
    py = list()

    for line in lines[1:-3]:
        var, type = varre.match(line).group(1,2)
        gr = under.sub(r"_\1", var.replace("ID", "_id"))
        pyvar = gr.lower()
        vars.append(var)
        types.append(type)
        py.append(pyvar)

    output = """from model.flyweight import Flyweight
from model.static.database import database

class %s(Flyweight):
    def __init__(self,%s):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.%s = %s

        cursor = database.get_cursor("select * from %s where \\\n
        %s=\%s;" \% (self.market_group_id))""" % ()

    if len(keys) == 1:
        output+="\n        row = cursor.fetchone()\n"

        for item in zip(vars, py, types):
            if item[2] == "tinyint(1)":
                output += '\n        self.%s = True if row["%s"] == 1 else False' % (item[1], item[0])
            else:
                output += '\n        self.%s = row["%s"]' % (item[1], item[0])

    output += "\n\n        cursor.close()"

    print output
