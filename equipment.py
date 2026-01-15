from hero import adventurer #TEMP

class Equipment:
    def __init__(self, name, stat_type, stat_boost):
        self.name = name
        self.stat_type = stat_type
        self.stat_boost = stat_boost

hermes = Equipment("Blessing of Hermes", adventurer.speed, 1)
aphrodite = Equipment("Blessing of Aphrodite", adventurer.regen, round(adventurer.health/10))
plutus = Equipment("Blessing of Plutus", adventurer.wealth, 1)
athena = Equipment("Blessing of Athena", adventurer.weapon, round(adventurer.weapon/5))
ares = Equipment("Blessing of Ares", adventurer.damage, round(adventurer.damage/2))
relic_list = [hermes, aphrodite, plutus, athena, ares]