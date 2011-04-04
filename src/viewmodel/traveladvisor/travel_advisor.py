from model.static.database import database
from collections import deque

class TravelAdvisor(object):
    def __init__(self):
        cursor = database.get_cursor("select * from mapSolarSystemJumps;")
        self.connections = dict()

        for row in cursor:
            if row["fromSolarSystemID"] not in self.connections:
                self.connections[row["fromSolarSystemID"]] = set()
            self.connections[row["fromSolarSystemID"]].add(row["toSolarSystemID"])

    def breadth_first(self, fromid, toid):
        closed_set = dict()
        open_set = deque([fromid])

        while len(open_set) > 0:
            current = open_set.popleft()
            #print current
            if current == toid:
                route = list()
                route.append(toid)
                while route[0] in closed_set: 
                    route.insert(0,closed_set[route[0]])
                    if route[0] == fromid:
                        return route
            for adjacent in self.connections[current]:
                if adjacent not in closed_set:
                    closed_set[adjacent] = current
                    open_set.append(adjacent)
        return 1;
