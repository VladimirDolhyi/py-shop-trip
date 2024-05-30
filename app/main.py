from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json
import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    customers = [Customer(**customer)
                 for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]
    customer_cars = {
        customer["name"]:
            Car(**customer["car"]) for customer in data["customers"]
    }

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_cost = float("inf")
        best_shop = None
        home_location = customer.location
        for shop in shops:
            car = customer_cars[customer.name]
            tr_cost = customer.calculate_trip_cost(shop.location, car)
            shop_cost = shop.calculate_product(customer)
            total_cost = tr_cost + shop_cost
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {total_cost}")
            if total_cost < best_cost:
                best_cost = total_cost
                best_shop = shop
        if customer.money >= best_cost:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            _time = datetime.datetime.now()
            print(f"Date: {_time.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, value in customer.product_cart.items():
                cost_product = (best_shop.products[product]
                                * customer.product_cart[product])
                if int(cost_product) == cost_product:
                    print(f"{value} {product}s "
                          f"for {int(cost_product)} dollars")
                else:
                    print(f"{value} {product}s for {cost_product} dollars")
            print(f"Total cost is "
                  f"{best_shop.calculate_product(customer)} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has "
                  f"{customer.money - best_cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
