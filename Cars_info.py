#Rahaf Saeed Alhalai
#442807504

#Q1: Create Cars_info module

# Dictionary containing cars information
cars_info_dict = {
    "car1": {"carBrand": "Nissan", "CarName": "Camry", "CarColor": "Blue"},
    "car2": {"carBrand": "Honda", "CarName": "Civic", "CarColor": "Red"},
    "car3": {"carBrand": "Mazda", "CarName": "Mustang", "CarColor": "Black"}}

def print_car_info():
    print("Car Information:")
    for brand, info in cars_info_dict.items(): 
        print(f"Brand: {info['carBrand']}, Name: {info['CarName']}, Color: {info['CarColor']}") 

def calculate_car_speed(distance, time):
    speed = distance / time
    if 90 <= speed <= 110:
        return f"Legal Speed: {speed} km/h"
    else:
        return f"Illegal Speed: {speed} km/h"

