# List homework
import random

# baseball_teams = []
#
# condition = True
# while condition:
#     team = input("What team do you want to add to the list? Press Enter to quit: ")
#     if team == "":
#         condition = False
#     else:
#         baseball_teams.append(team.lower())
#
# print(baseball_teams)
#
#
# def print_items(team_list):
#     for team_name in team_list:
#         print(team)
#
#
# print_items(baseball_teams)
#
# condition_two = True
# while condition_two:
#     team_remove = input("What team do you want to remove? Press enter to finish: ")
#     if team_remove == "":
#         condition_two = False
#     elif team_remove.lower() in baseball_teams:
#         baseball_teams.remove(team_remove.lower())
#         print(baseball_teams)
#     else:
#         print("Team not in list, try again")
#
# condition_three = True
# while condition_three:
#     team_index = input("What team do you want to find the position for? Press Enter to finish: ")
#     if team_index.lower() in baseball_teams:
#         print(baseball_teams.index(team_index.lower()))
#     elif team_index == "":
#         condition_three = False
#     else:
#         print("Team not in list, try again: ")
#
#
# def slice_list(user_list, start_index, end_index):
#     new_list = []
#     for i in range(start_index, end_index):
#         new_list.append(user_list[i])
#     return new_list
#
#
# start_ind = int(input("What index do you want to start? "))
# end_ind = int(input("What index do you want to end? "))
#
# print(slice_list(baseball_teams, start_ind, end_ind))

baseball_teams = ["white_sox", "red_sox", "cubs", "marlins", "dodgers", "angels", "dodgers", "cubs", "cubs"]
baseball_teams_two = ["brewers", "white sox", "cubs", "tigers", "cardinals"]


# def count_items(user_list, user_value):
#     counter = 0
#     for i in user_list:
#         if i == user_value.lower():
#             counter += 1
#     return counter
#
#
# team = input("What team do you want to counter for in list? ")
# print(count_items(baseball_teams, team))

def merge(list_one, list_two):
    new_list = list_one + list_two
    return new_list


# print(merge(baseball_teams, baseball_teams_two))

my_list = merge(baseball_teams, baseball_teams_two)
list_length = len(my_list)
condition = True
while condition:
    print(my_list[random.randint(0, list_length)])
    keep_going = input("Keep going? type (y) to keep going or press enter to stop: ")
    if keep_going.lower() != "y":
        condition = False


