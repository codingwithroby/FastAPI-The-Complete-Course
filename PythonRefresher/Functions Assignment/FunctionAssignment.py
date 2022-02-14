"""
Function Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""


def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary


solution_dictionary = user_dictionary(firstname="Eric", lastname="Roby", age=32)
print(solution_dictionary)









