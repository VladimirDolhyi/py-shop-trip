from app.car import Car

from dataclasses import dataclass
import math


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: "Car(**car)"

    def calculate_trip_cost(self,
                            shop_location: list[int],
                            car: "Car"
                            ) -> float:

        distance = math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )
        return round((distance / 100) * car.fuel_consumption * 2 * 2.4, 2)
