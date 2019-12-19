class SuperHero:
    def __init__(self, hero, name, powers, colors):
        self.__hero = hero
        self.__real_name = name
        self.__powers = powers
        self.__colors = colors

    def set_hero_alias(self, hero):
        self.__hero = hero

    def set_hero_name(self, name):
        self.__real_name = name

    def set_hero_powers(self, powers):
        self.__powers = powers

    def set_hero_colors(self, colors):
        self._colors = colors

    def get_hero_alias(self):
        return self.__hero

    def get_hero_name(self):
        return self.__real_name

    def get_hero_powers(self):
        return self.__powers

    def get_hero_colors(self):
        return self.__colors

