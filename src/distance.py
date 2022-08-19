from geopy.distance import geodesic

# TODO: define Redis consumer that instantiates CalculateDistance,
# calls distance_from_velocity() and publishes updated `data`
# 
       
class CalculateDistance:
    def __init__(self, data):
        self.input_lat = data['input_lat']
        self.input_long = data['input_long']
        self.velocity_lat = None
        self.velocity_long = None
        self.distance = None
       
    def distance_from_velocity(self):
        self.distance = geodesic(
            (self.input_lat, self.input_long), 
            (self.velocity_lat, self.velocity_long)).miles


# cd = CalculateDistance(data)
# distance = cd.distance_from_velocity()
# TODO: publish updated JSON to Redis