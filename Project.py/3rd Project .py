"""
import random

subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmla Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Riksa Driver from dehli"
]

actions=[
    "Lunches",
    "Cancel",
    "Dances With",
    "Eats",
    "Decelear war on",
    "Orders",
    "Celebrates"
]

places_or_things=[
    "At red fort",
    "In mumbai local train",
    "A plate of samosa",
    "Inside parliyament",
    "At ganga ghat",
    "During IPL Match",
    "At India Gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(action)
    places_or_thing=random.choice(places_or_things)

    headlines= f"BREAKING NEWS:{subject}{action}{places_or_thing}"
    print("\n"+headlines)

"""
