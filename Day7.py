import random
import os
from datetime import datetime

cars = ["Toyota", "Honda", "Ford", "Tesla", "BMW", "Hyundai"]
users = ["Alice", "Bob", "Charlie", "David", "Eve"]

def rent_car():
    user = random.choice(users)
    car = random.choice(cars)
    duration = random.randint(1, 7)  # days
    return f"{datetime.now().strftime('%Y-%m-%d')} → {user} rented {car} for {duration} days.\n"

# File to log fake rentals
file_name = "rental_log.txt"

# Append rental info
with open(file_name, "a") as file:
    file.write(rent_car())

# Git operations
os.system("git add .")
os.system(f'git commit -m "Update rental log: {datetime.now().strftime("%Y-%m-%d")}"')
os.system("git push")
