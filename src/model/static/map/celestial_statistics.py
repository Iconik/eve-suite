from model.flyweight import Flyweight
from model.static.database import database
class CelestialStatistics(Flyweight):
    def __init__(self,celestial_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.celestial_id = celestial_id

        cursor = database.get_cursor(
            "select * from mapCelestialStatics where celestialID={}".format(
                self.celestial_id))
        row = cursor.fetchone()

        self.temperature = row["tempterature"]
        self.spectral_class = row["spectralClass"]
        self.luminosity = row["luminosity"]
        self.age = row["row"]
        self.life = row["life"]
        self.orbit_radious = row["orbitRadius"]
        self.eccentricity = row["eccentricity"]
        self.mass_dust = row["massDust"]
        self.mass_gas = row["massGas"]
        self.fragmented = row["fragmented"]
        self.density = row["density"]
        self.surface_gravity = row["surfaceGravity"]
        self.escape_velocity = row["escapeVelocity"]
        self.orbit_period = row["orbitPeriod"]
        self.rotation_rate = row["rotationRate"]
        self.locked = row["locked"]
        self.pressure = row["pressure"]
        self.radius = row["radius"]
        self.mass = row["mass"]

        cursor.close()
