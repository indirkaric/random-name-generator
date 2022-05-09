from datetime import datetime
import random


class Generator:
    __ANIMAL_FILE_NAME = "animal-names.txt"
    __COLOR_FILE_NAME = "colors.txt"
    __animals = []
    __colors = []
    __username = None

    def load_data(file_name):
        with open(file_name,'r') as file:
            for line in file:
                if file_name == "animal-names.txt":
                    Generator.__animals.append(line.strip('\n').replace(" ", "_"))
                else:
                    Generator.__colors.append(line.strip('\n').replace(" ", "_"))

    def generate_name():
        Generator.load_data(Generator.__ANIMAL_FILE_NAME)
        Generator.load_data(Generator.__COLOR_FILE_NAME)

        print("Animals size {0}".format(len(Generator.__animals)))
        print("Colors siye {0}".format(len(Generator.__colors)))

        animal = Generator.__animals[random.randint(0, len(Generator.__animals))]
        color = Generator.__colors[random.randint(0, len(Generator.__colors))]
        Generator.__username = color + "-" + animal

    @staticmethod
    def print_output():
        Generator.generate_name()
        print(datetime.now())
        print("Generated name is {0}".format(Generator.__username))