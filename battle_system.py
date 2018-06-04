from PSI_methods import *



ness = Entity('Ness', 100, 20)


def battle_loop(player, field):
	flat_field = [enemy for row in field for enemy in row]

	ROW_1 = field[0]
	ROW_2 = field[1]

	if len(flat_field) == 1:
		print('{} approaches!'.format(flat_field[0].name))
	else:
		print('{} and its cohorts approach!'.format(ROW_1[0]))