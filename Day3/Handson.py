class Car:
    def start_engine(self):
        print("Start Engine")

    def stop_engine(self):
        print("Stop Engine")

    def accelerate(self):
        print("Accelerate Engine")

    def apply_brakes(self):
        print("Apply Brakes")

    def sound_horn(self):
        print("Sounding")
    

# New Attributes: 
class Truck(Car): 
    def __init__(self,color,max_speed,tyre_friction,max_cargo_weight):
        self.color = input()
        self.max_speed = max_speed
        self.tyre_friction = tyre_friction
        self.is_engine_started = max_cargo_weight
        self.current_speed = 0

        self.max_cargo_weight = 24
        self.current_load = 0

    CarMethods = Car()

    def sound_horn(is_engine_started):
    
        if is_engine_started == True:
            print("Honk Honk")
        else:
            print("Car has not started yet")

    def load_cargo(self, cargo_weight):
       
        if cargo_weight < self.max_cargo_weight:
            print(f"Cannot load cargo more than max limit: {self.max_cargo_weight}")
        elif self.is_engine_started:
            print("Cannot load cargo during motion")
        else:
            self.current_load+=cargo_weight
            print(f"Cargo loaded: {cargo_weight}kg. Current load: {self.current_load}kg")

    
    def unload_cargo(self, cargo_weight):

        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        elif cargo_weight > self.max_cargo_weight:
            print ("Cannot unload more cargo than is currently loaded")
        else:
            self.current_load -= cargo_weight
            print(f"Cargo unloaded: {cargo_weight}kg. Current load: {self.current_load}kg")
                  


'''
# Test code
truck = Truck("Blue", 120, 10, 5, 1000)  # Create a truck object
truck.is_engine_started(False)  # Try to start the engine
truck.sound_horn()  # Should print "Honk Honk"
truck.load_cargo(500)  # Should print "Cannot load cargo during motion" since engine is on
truck.stop_engine()  # Turn the engine off
truck.load_cargo(500)  # Should print "Cargo loaded: 500kg"
truck.unload_cargo(200)  # Should print "Cargo unloaded: 200kg"
truck.sound_horn()  # Should print "Car has not started yet"
'''

# Test code
truck = Truck("Blue", 120, 10, 1000)  # Correctly pass all required arguments
truck.start_engine()  # Start the engine
truck.sound_horn()  # Should print "Honk Honk"

truck.load_cargo(500)  # Should print "Cargo loaded: 500kg. Current load: 500kg"
truck.load_cargo(1200)  # Should print "Cannot load cargo more than max limit: 1000"

truck.stop_engine()  # Stop the engine
truck.load_cargo(500)  # Should print "Cargo loaded: 500kg. Current load: 1000kg"

truck.unload_cargo(200)  # Should print "Cargo unloaded: 200kg. Current load: 800kg"
truck.sound_horn()  # Should print "Car has not started yet"
