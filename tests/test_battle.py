from battle_ship import Player, Game
import pytest

def test_player_response():
	player = Player()
	res = player.handle(4,4)
	assert(res == 'o')

def test_place_ship():
	player = Player()
	player.place(1,4,'g','h')
	assert(player.grid[1][4] == 'g')

def test_player_receive_on_ship():
	player = Player()
	player.place(1,4,'g','h')
	res = player.handle(1,4)
	assert(res == 'x')

def test_game_end():
	game = Game()
	assert(game.ended() == False)

def test_player_added():
	game = Game()
	player = Player()
	game.add_player(player)
	assert(player in game.players)

def test_player_place_cargot():
	player = Player()
	player.place(0,0,'c','h')
	assert(player.grid[0][0] == 'c')
	assert(player.grid[0][1] == 'c')
	assert(player.grid[0][2] == 'c')
	assert(player.grid[0][3] == 'c')

def test_player_place_destroyer():
	player = Player()
	player.place(0,0,'d','h')
	for __ in range(3):
		assert(player.grid[0][__] == 'd')
	
def test_player_place_destroyer_vertical():
	player = Player()
	player.place(0,0,'d','v')
	for __ in range(3):
		assert(player.grid[__][0] == 'd')

def test_player_place_destroyer_middle():
	player = Player()
	player.place(3,3,'d','h')
	for i in range(3):
		assert(player.grid[3][3+i] == 'd')

def test_partial():
	player = Player()
	res = player.place(8,8,'c','v')
	assert(res == False)
	assert(player.handle(8,8) == 'o')

def test_collide():
	player = Player()
	res = player.place(5,3,'c','h')
	assert(res == True)
	res = player.place(4,6,'c','v')
	assert(res == False)
	assert(player.handle(5,6) == 'x')
	assert(player.handle(5,6) == 'x')

def test_collide_smool():
	player = Player()
	res = player.place(5,3,'g','h')
	assert(res == True)
	res = player.place(5,3,'g','v')
	assert(res == False)
	assert(player.handle(5,3) == 'x')


@pytest.mark.parametrize('ship', 'dc')
@pytest.mark.parametrize('direction', 'hv')
@pytest.mark.parametrize('line,col', [(i,j) for i in range(5) for j in range(5,10)])
def test_hit(line, col, direction, ship):
	player = Player()

	length = {
		'd': 3,
		'c': 4,
	}[ship]

	dl, dc = {
		'v': (1, 0),
		'h': (0, 1),
	}[direction]

	#line, col = 1, 3
	res = player.place(line,col,ship,direction)

	if line + dl*length > 10 or col + dc*length > 10:
		assert(res == False)
		return
	assert(res == True)

	pos_in = {(line+dl*i, col+dc*i) for i in range(length)}
	for l,c in pos_in:
		assert(player.handle(l,c) == 'x')
	for i in range(-20, 20):
		for j in range(-20, 20):
			if (i,j) not in pos_in:
				assert(player.handle(i,j) == 'o')

def test_destroy_hit_h():
	player = Player()
	res = player.place(3,3,'d','h')
	assert(res == True)
	assert(player.handle(3,4) == 'x')

def test_player_place_cargo_middle():
	player = Player()
	res = player.place(3,3,'c','h')
	assert(res == True)
	for i in range(4):
		assert(player.grid[3][3+i] == 'c')
