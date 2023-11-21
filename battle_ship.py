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

	def reset(self,row,col,index,direction):
		for i in range(0,index):
			if direction == 'h':
				self.grid[row][col+i] = ''
			else:
				self.grid[row+i][col] = ''

	def place(self,row,col,ship,direction):
		ship_lenght = self.ships[ship]

		for c in range(0,ship_lenght):
			if direction == 'h':
				if 0<=col+c<10:
					if self.grid[row][col+c] != '':
						self.reset(row,col,c,direction)
						return False
					
					self.grid[row][col+c] = ship
				else:
					self.reset(row,col,c,direction)
					return False
			else:
				if 0<=row+c<10:
					if self.grid[row+c][col] != '':
						self.reset(row,col,c,direction)
						return False
					self.grid[row+c][col] = ship
				else:
					self.reset(row,col,c,direction)
					return False
		return True


class Game():
	def __init__(self):
		self.players = []
	
	def add_player(self,player):
		self.players.append(player)

	def ended(self):
		return False
