from PSI_methods import *




ness = Entity('Ness', 100, 20)

battlefield = [
		[Entity('Pogo Punk', 35, 0, 0.75, 0.75), Entity('Pogo Punk,', 35, 0, 0.75, 0.75)],
		[Entity("Ramblin Evil Mushroom", 60, 0)]
]


def battle_loop(player, field):
	flat_field       = [enemy for row in field for enemy in row]
	enemies_alive    = [enemy.alive for enemy in flat_field]
	enemy_ids        = dict(enumerate(flat_field))

	ROW_1            = field[0]
	ROW_2            = field[1]

	if len(flat_field) == 1:
		print('{} approaches!'.format(flat_field[0].name))
	else:
		print('{} and its cohorts approach!'.format(ROW_1[0].name))

	end_bool = any(enemies_alive)

	while end_bool:
		print('Actions: PSI[1] Check[2] Run[3]')
		player_choice = input()

		if player_choice == '1':
			print('Not implemented yet.')

		if player_choice == '2':
			print(enemy_ids)

		if player_choice == '3':
			print('{} ran away.'.format(player.name))
			break

battle_loop(ness, battlefield)
