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

        distance = round(math.sqrt(
            (int(self.location[0]) - int(shop_location[0])) ** 2
            + (int(self.location[1]) - int(shop_location[1])) ** 2
        ), 2)
        return round(distance * car.fuel_consumption * 2 * 2.4 / 100, 2)
