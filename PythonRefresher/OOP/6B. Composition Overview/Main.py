from Engine import *
from Vehicle import *

engine = Engine("V6")
vehicle = Vehicle("Car", True, engine)
vehicle.engine.startEngine()