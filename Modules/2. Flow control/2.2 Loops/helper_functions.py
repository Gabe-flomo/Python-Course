from random import randint, choice

def generate_names():
    names_string = """Michael
        Christopher
        Jessica
        Matthew
        Ashley
        Jennifer
        Joshua
        Amanda
        Daniel
        David
        James
        Robert
        John
        Joseph
        Andrew
        Ryan
        Brandon
        Jason
        Justin
        Sarah
        William
        Jonathan
        Stephanie
        Brian
        Nicole
        Nicholas
        Anthony
        Heather
        Eric
        Elizabeth
        Adam
        Megan
        Melissa
        Kevin
        Steven
        Thomas
        Timothy
        Christina
        Kyle
        Rachel
        Laura
        Lauren
        Amber
        Brittany
        Danielle
        Richard
        Kimberly
        Jeffrey
        Amy
        Crystal
        Michelle
        Tiffany
        Jeremy
        Benjamin
        Mark
        Emily
        Aaron
        Charles
        Rebecca
        Jacob
        Stephen
        Patrick
        Sean
        Erin
        Zachary
        Jamie
        Kelly
        Samantha
        Nathan
        Sara
        Dustin
        Paul
        Angela
        Tyler
        Scott
        Katherine
        Andrea
        Gregory
        Erica
        Mary
        Travis
        Lisa
        Kenneth
        Bryan
        Lindsey
        Kristen
        Jose
        Alexander
        Jesse
        Katie
        Lindsay
        Shannon
        Vanessa
        Courtney
        Christine
        Alicia
        Cody
        Allison
        Bradley
        Samuel"""
    
    possible_names = names_string.split()
    million_people = [choice(possible_names) for _ in range(1_000_000)]
    return million_people




