class Ship():
	def __init__(self,size):
		self.size = size
		self.ship_state = 'clear'
		self.touched = 0

	def update_state(self):
		self.touched += 1
		if self.touched == self.size:
			self.ship_state = 'drowned'
		else:
			self.ship_state = 'touched'

	def return_state(self):
		return self.ship_state

class Cell():
	def __init__(self,ship,name):
		self.ship = ship
		self.state = 'clear'
		self.name = name
	
	def update_cell(self):
		if self.state == 'clear':
			self.state = 'touched'
			self.ship.update_state()
		return self.ship.return_state()

class Player():
	ships = {
		'c':4,
		'd':3,
		'g':1,
	}
	def __init__(self):
		self.grid = [['']*10 for i in range(10)]
		self.ship_list = []
		
	def handle(self,row,col):
		if 0<=row<10 and 0<=col<10:
			if self.grid[row][col] != '':
				ship_state = self.grid[row][col].update_cell()
				if ship_state == 'touched':
					return 'x'
				else:
					return 'X'
		return 'o'

	def check_available(self,coordinates):
		for r,c in coordinates:
			if not 0<=r<10 or not 0<=c<10 or self.grid[r][c] != '':
				return False
		return True

	def init_ship(self,ship_lenght):
		new_ship = Ship(ship_lenght)
		self.ship_list.append(new_ship)
		return new_ship

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
			new_ship = self.init_ship(ship_lenght)
			for r,c in coordinates:
				cell = Cell(new_ship,ship)
				self.grid[r][c] = cell
		return available

class Game():
	def __init__(self):
		self.players = []
	
	def add_player(self,player):
		self.players.append(player)

	def ended(self):
		return False
