# This program demonstrates polymorphism

import animals

def main():
    # Create a Mammel object, a Dog object and a Cat object
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()
    # pass animals to the function
    print('Here are some animals and the sounds they make.')
    print('----------------------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
# This function shows the animal and its sound
def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal.')

main()