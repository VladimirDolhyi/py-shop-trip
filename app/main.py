from app.customer import Customer
from app.shop import Shop

import json
import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    customers = [Customer(*customer)
                 for customer in data["customers"]]
    shops = [Shop(*shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_cost = float("inf")
        best_shop = None
        total_cost = 0
        home_location = customer.location
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop.location, customer.car)
            shop_cost = shop.calculate_product(customer)
            total_cost = trip_cost + shop_cost
            print(f"{customer.name}'s to the {shop.name} costs {total_cost}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_shop = shop
        if customer.money >= best_cost:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.location = best_shop.location
            _time = datetime.datetime.now()
            print(f"Date {_time.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name} for your purchase!")
            print("You have bought:")
            for product, value in customer.product_cart.items():
                cost_product = (best_shop.products[product]
                                * customer.product_cart[product])
                print(f"{value} {product} for {cost_product} dollars")
            print(f"Total cost is"
                  f"{best_shop.calculate_product(customer)} dollars")
            print("See you again!")

            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has"
                  f"{customer.money - total_cost} dollars")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f"to make a purchase in any shop")
