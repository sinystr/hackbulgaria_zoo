import database_helper
import config
from animal import Animal
from zoo import Zoo


start_message = "Hello, here is the Zoo you can use one the the following commands:\
                \n see_animals\
                \n accommodate <species> <age> <name> <gender> <weight> \
                \n move_to_habitat <species> <name>\
                \n simulate <interval_of_time> <period>"


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_arr, command):
    return command_arr[0] == command


def print_arr(zoopark):
    for animal in zoopark.animals:
        print("{}: {}, {} months, {}kg".format(animal.name, animal.species, animal.age, animal.weight))


def unknown_command():
    message = "Unknown command, you can use one the the following commands:\
                \n see_animals\
                \n accommodate <species> <age> <name> <gender> <weight> \
                \n move_to_habitat <species> <name>\
                \n simulate <interval_of_time> <period>"
    return message

#defining zoo and animals
zoopark = Zoo(5, 5)
puh_panda = Animal("panda", 3, "Puh", "male", 100)
zoopark.add_animal(puh_panda)
gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
zoopark.add_animal(gosho_tiger)
ivan_tiger = Animal("tiger", 4, "Ivan", "male", 30)
zoopark.add_animal(ivan_tiger)


def main():
    print(start_message)

    while True:
        command = split_command_str(input("Enter command>"))
        if the_command(command, "see_animals"):
            print_arr(zoopark)
        elif the_command(command, "accommodate"):
            species = command[1]
            age = int(command[2])
            name = command[3]
            gender = command[4]
            weight = int(command[5])
            zoopark.accommodate(species, age, name, gender, weight)
        elif the_command(command, "move_to_habitat"):
            zoopark.move_to_habitat(command[1], command[2])
        elif the_command(command, "finish"):
            print("GoodBye")
            break
        else:
            print(unknown_command())

if __name__ == '__main__':
    main()
