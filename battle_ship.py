class Player():
	ships = {
		'c':4,
		'd':3,
		'g':1,
	}
	def __init__(self):
		self.grid = [['']*10 for i in range(10)]
		
	def handle(self,row,col):
		if 0<=row<10 and 0<=col<10:
			if self.grid[row][col] != '':
				return 'x'
		return 'o'

	def check_available(self,coordinates):
		for r,c in coordinates:
			if not 0<=r<10 or not 0<=c<10 or self.grid[r][c] != '':
				return False
		return True

	def place(self,row,col,ship,direction):
		ship_lenght = self.ships[ship]
		coordinates = list()
		for i in range(0,ship_lenght):
			if direction == 'h':
				coordinates.append((row,i+col))
			else:
				coordinates.append((i+row,col))
		available = self.check_available(coordinates)
		
		if available:
			for r,c in coordinates:
				self.grid[r][c] = ship
		else:
			return False
		return True


class Game():
	def __init__(self):
		self.players = []
	
	def add_player(self,player):
		self.players.append(player)

	def ended(self):
		return False
