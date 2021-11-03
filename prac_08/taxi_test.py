from prac_08.taxi import Taxi


taxi = Taxi("Prius 1", 100, 1.23)
taxi.start_fare()
taxi.drive(40)
print("fuel: {}\ncurrent fare: {}".format(taxi.fuel, taxi.get_fare()))
taxi.start_fare()
taxi.drive(100)
print("fuel: {}\ncurrent fare: {}".format(taxi.fuel, taxi.get_fare()))
