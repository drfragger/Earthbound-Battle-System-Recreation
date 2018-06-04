from PSI_defs import PSI
from random import randint
from random import choice


class Entity:
	def __init__(self, name, hp, pp, fire_res=1, freeze_res=1, thunder_res=1):
		
		self.alive     = True
		self.name      = name
		self._hp       = hp
		self.pp        = pp

		self.resist = {
			'fire': fire_res,
			'freeze': freeze_res,
			'thunder': thunder_res
		}

	def __repr__(self):
		return '{0}: HP={1}, PP={2}'.format(self.name, self.hp, self.pp)

	@property
	def hp(self):
		return self._hp

	@hp.setter
	def hp(self, value):
		if value > self._hp:
			print('{0} recovered {1} HP!'.format(self.name, value - self.hp))

		else:
			print('{0} HP of damage to {1}!'.format(self.hp - value, self.name))
		
		self._hp = value

		if self._hp <= 0:
			self._hp = 0
			self.alive = False






def psi_check(psi_type):
	def decorator(func):
		def wrapper(user, level, target):
			valid_levels = ['a', 'b', 'y', 'o']
			assert level in valid_levels, f'{level} is not a valid level.'

			cost = psi_type[level]['cost']
			if user.pp < cost:
				print('Not enough PP!')
			else:
				user.pp -= cost
				return func(user, level, target)
		return wrapper
	return decorator




		



@psi_check(PSI['lifeup'])
def heal(user, level, target):
		health_gained     = randint(*PSI['lifeup'][level]['restore'])
		target.hp         += health_gained
		print('{0} recovered {1} HP.'.format(target.name, health_gained))


@psi_check(PSI['fire'])
def fire(user, level, row):
	
	for enemy in row:
		if enemy.alive:
			dmg                   = randint(*PSI['fire'][level]['damage'])
			resisted_dmg          = dmg * enemy.resist['fire']
			enemy.hp             -= resisted_dmg

@psi_check(PSI['freeze'])
def freeze(user, level, target):
	dmg            = randint(*PSI['freeze'][level]['damage'])
	resisted_dmg   = dmg * target.resist['freeze']
	target.hp     -= resisted_dmg



@psi_check(PSI['thunder'])
def thunder(user, level, field):
	repeated_attacks    = {'a': 1, 'b': 2, 'y': 3, 'o': 4}
	flat_field          = [enemy for row in field for enemy in row]
	
	for count in range(repeated_attacks[level]):
		target       = choice(flat_field)
		dmg          = randint(*PSI['thunder'][level]['damage'])
		resisted_dmg = dmg * target.resist['thunder']
		target.hp   -= resisted_dmg



@psi_check(PSI['wonder'])
def wonder(user, level, field):
	flat_field = [enemy for row in field for enemy in row]

	for enemy in flat_field:
		dmg         = randint(*PSI['wonder'][level]['damage'])
		enemy.hp   -= dmg


@psi_check(PSI['starstorm'])
def starstorm(user, level, field):
	flat_field = [enemy for row in field for enemy in row]

	for enemy in flat_field:
		dmg         = randint(*PSI['starstorm'][level]['damage'])
		enemy.hp   -= dmg






