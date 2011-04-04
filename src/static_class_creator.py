import re

if __name__ == '__main__':
    input = """CREATE TABLE "ramInstallationTypeContents" (
  "installationTypeID" int(11) NOT NULL,
  "assemblyLineTypeID" tinyint(3) NOT NULL,
  "quantity" tinyint(4) default NULL,
  PRIMARY KEY  ("installationTypeID","assemblyLineTypeID")
)"""

    table_name_extractor = re.compile(r'\s*CREATE TABLE "(\w*)" \(') #extracts the table name
    key_extractor = re.compile(r"\s*PRIMARY KEY  \((.*)\)") #extracts the primary keys in a raw string
    variable_extract = re.compile(r'"(\w+)"') #returns variables enclosed in quotation marks
    title_extract = re.compile(r'[a-z]+(\w+)') #removes the category prefix from the table name
    varre = re.compile(r'\s*"(\w+)" (\S+)') #extracts variable name and type
    under = re.compile(r'([A-Z])') #puts underscore in front of uppercase letters
    type_split = re.compile(r'(\w+)(?:\((\d+)\))?') #Splits a type up into its "type" and length 

    lines = input.strip().splitlines()
    table_name = table_name_extractor.match(lines[0]).group(1)
    class_name = title_extract.match(table_name).group(1)
    if class_name[-3:] == 'ies':
        class_name = class_name[:-3]+'y'
    elif class_name[-1] == 's':
        class_name = class_name[:-1]
    key = key_extractor.match(lines[-2])
    keys = variable_extract.findall(key.group(1))

    vars = list()
    types = list()
    py = list()

    for line in lines[1:-2]:
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

        cursor = database.get_cursor("select * from %s where \\
        %s=%%s;" %% (self.%s))\n""" % (class_name, py[0], py[0], py[0], table_name, vars[0], py[0])

    if len(keys) == 1:
        output+="        row = cursor.fetchone()\n\n"
    
        for item in zip(vars[1:], py[1:], types[1:]):
            if item[2] == "tinyint(1)":
                output += '        self.%s = True if row["%s"] == 1 else False\n' % (item[1], item[0])
            else:
                output += '        self.%s = row["%s"]\n' % (item[1], item[0])
    elif len(keys) == 2:
        output += "\n        self.YYY = list()\n\n"
        if len(vars) == 2:
            pass
        else:
            output = "from collections import namedtuple\n"+output
            tuple_vars = ""
            for item in py[1:]:
                tuple_vars += item+" "
            output += '        XXX = namedtuple("XXX", "%s")\n\n' % (tuple_vars)
        output += "        for row in cursor:\n"
        if len(vars) == 2:
            output += '            self.YYY.append(row["%s"])\n' % vars[1]
        else:
            output += "            self.YYY.append(XXX(\n"
            for item in zip(vars[1:], py[1:], types[1:]):
                if item[2] == "tinyint(1)":
                    output += '                %s=True if row["%s"] == 1 else False,\n' % (item[1], item[0])
                else:
                    output += '                %s=row["%s"],\n' % (item[1], item[0])
                
            output += "            ))\n"

    output += "\n        cursor.close()"

    print output
