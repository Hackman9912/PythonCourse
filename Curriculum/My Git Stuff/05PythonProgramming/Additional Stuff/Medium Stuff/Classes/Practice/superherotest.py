import superhero

def main():
    superhero = makelist()
    display_list(superhero)
def makelist():
    superhero_list = []

    print("Enter the number of Super Heros to enter data for: ")
    for count in range(int(input())):
        print('Hero number', count + 1)
        hero = input("Enter the Hero alias: ")
        real_name = input("Enter the Hero Name: ")
        powers = input("Enter the Hero powers: ")
        colors = input("Enter the Hero colors: ")
        print()

        super_hero = superhero.SuperHero(hero, real_name, powers, colors)

        superhero_list.append(super_hero)
    return superhero_list

def display_list(superhero_list):
    if len(superhero_list) > 0:
        print("\n" * 100)
        print("Here is the data you entered: ")
        for super in superhero_list:
            print()
            print(super.get_hero_alias())
            print(super.get_hero_name())
            print(super.get_hero_powers())
            print(super.get_hero_colors())
            print('....................')
    else:
        print("Looks like there are no Super Heros here...")
        print("The Joker finally wins....")

main()
