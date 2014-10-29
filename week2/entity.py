class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points >= self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points >= self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
            return True
        else:
            self.health += healing_points
            return True

    def has_weapon(self):
        if self.weapon is None:
            return False
        else:
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return 0
        if self.weapon.critical_hit() is True:
            return self.weapon.damage * 2
        else:
            return self.weapon.damage

    
