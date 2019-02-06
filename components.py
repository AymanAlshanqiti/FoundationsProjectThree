# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.member_list = []
        self.president = ""


    def assign_president(self, person):
        # your code goes here!
        self.president = person
        

    def recruit_member(self, person):
        # your code goes here!
        self.member_list.append(person)



    def print_member_list(self):
        # your code goes here!
        ages = 0
        print("- %s (%s years old, president) - %s" % (self.president.name, self.president.age, self.president.bio))
        for member in self.member_list:

            print("- %s (%s years old) - %s" % (member.name, member.age, member.bio))
            ages += member.age

        average_age = ages / len(self.member_list)
        print("Average age in this club: %s " % average_age)


