from app.car import Car

from dataclasses import dataclass
import math


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: "Car"

    def calculate_trip_cost(self,
                            shop_location: list[int],
                            car: "Car"
                            ) -> float:
        print("Customer location:", self.location)
        print("Shop location:", shop_location)
        distance = round(math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        ), 2)
        print("Distance to the shop:", distance)
        return round(distance * car.fuel_consumption * 2 * 2.4 / 100, 2)
