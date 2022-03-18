import random
import json

property_types = ["Apartment", "Maisonette", "Penthouse", "Townhouse", "Duplex", "Villa", "Bungalow"]
property_locations = ["Mellieha", "Zabbar", "Valletta", "Birgu"]


def write_to_json(json_object):
    with open('json_data.json', 'w') as outfile:
        json.dump(json_object, outfile)


def generate_random_properties():
    property_listings = []
    for i in range(100):
        property_listings.append({
            "Type": random.choice(property_types),
            "Cost": random.randint(100000, 900000),
            "Location": random.choice(property_locations)
        })

    write_to_json(property_listings)

if __name__ == '__main__':
    generate_random_properties()
