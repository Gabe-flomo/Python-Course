from random import randint, choice

def generate_number(range_ = (1,100)):
    return randint(range_[0], range_[1])

def random_fruit():
    fruits = ["pomegranate", "apple", "plum", "orange", "kiwi", "pitanga", "pear", "pineapple", "raspberry", "peach", "watermelon" ]
    return choice(fruits)

