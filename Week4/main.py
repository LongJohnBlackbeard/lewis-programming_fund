# Daniel Tujo
# Programming Fundamentals
# Week 4 Battery Life


def grab_battery():
    current_battery = float(input("What is the current KWD on the Battery? "))
    while current_battery < 0:
        current_battery = float(input("Please enter a valid value: "))
    return current_battery


def grab_temp():
    return float(input("What is the current temperature outside in Fahrenheit? "))


def grab_traffic():
    traffic = input("How is traffic: (G)ood, (M)oderate, or (S)top-and-go? ".lower())
    while traffic not in ["g", "m", "s"]:
        traffic = input("Please enter Corresponding letter: G for good, M for Moderate, S for Stop-and-go: ")
    if traffic in ["g", "m", "s"]:
        global traffic_m
        traffic_m = traffic
    return traffic


def grab_speed():
    return float(input("What will be your average speed? "))


def grab_climate():
    climate = input("Will the climate control be (O)ff, (L)ow, (M)edium, or (H)igh? ".lower())
    while climate not in ["o", "l", "m", "h"]:
        climate = input("Please enter O for off, L for Low, M for Medium, of H for High: ".lower())
    return climate


def temp_mileage_reduction(temp):
    if temp < 0:
        reduc_m = 40
    elif temp < 20:
        reduc_m = 30
    elif temp < 40:
        reduc_m = 20
    elif temp > 85:
        reduc_m = 10
    elif temp > 100:
        reduc_m = 30
    else:
        reduc_m = 0
    return reduc_m


def traffic_mileage(traffic):

    if traffic == "s":
        reduc_traffic = 25
    elif traffic == "m":
        reduc_traffic = 10
    elif traffic == "g":
        reduc_traffic = 0
    return reduc_traffic


def speed_mileage(speed):
    if speed > 80:
        reduc_speed = 20
    elif speed > 60:
        reduc_speed = 10
    else:
        reduc_speed = 0
    return reduc_speed


def climate_mileage(climate):
    if climate == "o":
        mile_reduc = 0
    elif climate == "l":
        mile_reduc = 5
    elif climate == "m":
        mile_reduc = 10
    elif climate == "h":
        mile_reduc = 20
    return mile_reduc


def battery_range(battery):
    battery_range_conversion = battery * 2.2
    return battery_range_conversion


def converted_battery_mileage(bat_range, reduction):
    new_range = bat_range - (bat_range * (reduction / 100))
    return new_range


def intro():
    print("*" * 70)
    print("*%68s*" % "BATTERY LIFE ESTIMATOR".center(68))
    print("*%68s*" % "(version 374.11)".center(68))
    print("*" * 70)
    print("\n")


def output():
    starting_range = battery_range(grab_battery())
    temp_reduc = temp_mileage_reduction(grab_temp())
    traffic_reduc = traffic_mileage(grab_traffic())
    if traffic_m == "g":
        speed_reduc = speed_mileage(grab_speed())
    else:
        speed_reduc = 0
    climate_reduc = climate_mileage(grab_climate())
    total = climate_reduc + speed_reduc + traffic_reduc + temp_reduc
    overall_range = converted_battery_mileage(starting_range, total)

    print("\n")
    print("Here is your battery range report:")
    print("%-30s %6.2f" % ("Starting Range (miles)", starting_range))
    print("%-30s %6.2f" % ("% Temperature reduction", temp_reduc))
    print("%-30s %6.2f" % ("% Traffic reduction", traffic_reduc))
    print("%-30s %6.2f" % ("% Speed reduction", speed_reduc))
    print("%-30s %6.2f" % ("% Climate control reduction", climate_reduc))
    print("%-30s %6.2f" % ("Total % reduction", total))
    print("%-30s %6.2f" % ("Overall range (miles)", overall_range))
    print("\n")
    print("*" * 75)


intro()
output()
