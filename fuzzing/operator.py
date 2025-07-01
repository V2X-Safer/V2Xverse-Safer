import random

WEATHER_RANGE = {
    'cloudiness': (0, 100),
    'precipitation': (0, 100),
    'fog_density': (0, 100),
    'wetness': (0, 100),
    'sun_azimuth_angle': (-180, 180),
    'sun_altitude_angle': (-90, 90),
}
TRAFFIC_RANGE = {
    'vehicle_num': (1, 20),
    'pedestrian_num': (0, 30),
}
RSU_RANGE = {
    'comm_quality': (0.7, 1.0),
    'rsu_num': (1, 5),
}
class Operator:
    def random_weather(self):
        return {k: random.uniform(*v) for k, v in WEATHER_RANGE.items()}
    def random_traffic(self):
        return {k: random.randint(*v) for k, v in TRAFFIC_RANGE.items()}
    def random_rsu(self):
        return {k: random.uniform(*v) if isinstance(v[0], float) else random.randint(*v) for k, v in RSU_RANGE.items()}
