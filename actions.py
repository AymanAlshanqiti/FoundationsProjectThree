# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input("What is your name? \n")
my_age = input("How old are you? \n")
my_bio = input("Tell as something about your briefly.. \n")
myself = Person(my_name, my_bio, my_age)

def introduction():

    print("Hello, %s. Welcome to our portal." % my_name)
    print("--------------------------------------------\n")
    print("Would you like to:")
    print("1) Create a new club. \n or:")
    print("2) Browse and join clubs. \n or:")
    print("3) View existing clubs. \n or:")
    print("4) Display members of a club. \n or:")
    print("-1) Close application. \n or:")

    options()
    


def options():

    user_choise = input()
    if user_choise == "1":
        create_club()
    elif user_choise == "2":
        join_clubs()
    elif user_choise == "3":
        view_clubs()
    elif user_choise == "4":
        view_club_members()
    elif user_choise == "-1":
        print("It nice to chat with you %s, see you soon." % my_name)
        quit()
    

def create_club():

    club_name = input("Pick a name for your awesome new club: ")
    club_description = input("What is your club about?\n")

    user_club = Club(club_name, club_description)

    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):")
    print("--------------------------------------------")

    for index, person in enumerate(population):
        print("[%s] %s" % (index+1, person.name))
 
    user_members_choise = int(input())

    while int(user_members_choise) != -1:

        if user_members_choise in range(1, len(population)):
            user_club.recruit_member(population[user_members_choise-1])
            user_members_choise = int(input())

        else:
            user_members_choise = int(input("Sorry, this user isn't in our planet!, please try one of the list: "))

        user_club.assign_president(myself)

    else:
        print("Here's your club:")
        print(user_club.name)
        print(user_club.description)
        print("Members:")
        user_club.print_member_list()

    options()


def view_clubs():

    print("Existing clubs:")
    for club in clubs:
        print("\n\t NAME: %s \n\t DESCRIPTION: %s \n\t MEMBERS: %s" % (club.name, club.description , len(club.member_list)))
    print("--------------------------------------------")
    

def view_club_members():

    view_clubs()
    user_review_club = input("Enter the name of the club whose member's you'd like to see: ")

    for club in clubs:
        if user_review_club.lower() == club.name.lower():
            club.print_member_list()

    options()

def join_clubs():

    view_clubs()
    user_choosen_club = input("Enter the name of the club you'd like to join: ")

    for club in clubs:
        if user_choosen_club == club.name:
            club.recruit_member(myself)
            print("%s just joind %s " % (myself.name, user_choosen_club))
            print("--------------------------------------------")
            return True

    options()

def application():
    introduction()
    # your code goes here!
    