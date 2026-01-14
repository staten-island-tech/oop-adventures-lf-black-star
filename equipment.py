from hero import adventurer #TEMP

class Equipment:
    def __init__(self, name, stat_type, stat_boost):
        self.name = name
        self.stat_type = stat_type
        self.stat_boost = stat_boost

hermes = Equipment("Blessing of Hermes", adventurer.speed, 1)
aphrodite = Equipment("Blessing of Aphrodite", adventurer.regen, (adventurer.health/10))
midas = Equipment("Blessing of Midas", adventurer.wealth, 1)
athena = Equipment("Blessing of Athena", adventurer.weapon, round(adventurer.weapon/5))
ares = Equipment("Blessing of Ares", adventurer.damage, round(adventurer.damage/2))
