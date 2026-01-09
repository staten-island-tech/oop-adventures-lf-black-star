from hero import adventurer #TEMP
class Relic:
    def __init__(self, name, stat_type, stat_boost):
        self.name = name
        self.stat_type = stat_type
        self.stat_boost = stat_boost
    
    def boost(self):
        (adventurer[7]) += self.stat_boost
        print(adventurer)

hermes = Relic("Blessing of Hermes", "speed", 1)

relic_list = [hermes]
