from PIL import Image

SQUARE_FACTOR = 18

BLACK = (0, 0, 0)

HOTPINK = (255, 105, 180)
DEEPPINK = (255, 20, 147)

GREEN = (0, 128, 0)
DARKGREEN = (0, 100, 0)

LIME = (50, 205, 50)
LIMEGREEN = (0, 255, 0)

LIGHTSEAGREEN = (32, 178, 170)
SEAGREEN = (46, 139, 87)

ROYALBLUE = (65, 105, 225)
MEDIUMBLUE = (0, 0, 205)

ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)

RED = (255, 0, 0)
DARKRED = (139, 0, 0)

class Squares:


	def __init__(self, x, y):
		self._num_x = x
		self._num_y = y
		self._img = Image.new('RGB',
		                      (x * SQUARE_FACTOR, y * SQUARE_FACTOR),
		                      BLACK)

	def color(self, start, num, color):
		if color == 1:
			normal_color = HOTPINK
			dark_color = DEEPPINK
		elif color == 2:
			normal_color = GREEN
			dark_color = DARKGREEN
		elif color == 3:
			normal_color = LIMEGREEN
			dark_color = LIME
		elif color == 4:
			normal_color = ROYALBLUE
			dark_color = MEDIUMBLUE
		elif color == 5:
			normal_color = LIGHTSEAGREEN
			dark_color = SEAGREEN
		elif color == 6:
			normal_color = ORANGE
			dark_color = DARKORANGE
		elif color == 7:
			normal_color = RED
			dark_color = DARKRED

		x = start % self._num_x
		y = start // self._num_x
		remaining = num
		while remaining != 0:
			for x_offset in range(SQUARE_FACTOR):
				for y_offset in range(SQUARE_FACTOR):
					point = ((x * SQUARE_FACTOR) + x_offset,
                   (y * SQUARE_FACTOR) + y_offset)
					if x_offset % SQUARE_FACTOR == 0 \
					   or x_offset % SQUARE_FACTOR == (SQUARE_FACTOR - 1) \
					   or y_offset % SQUARE_FACTOR == 0 \
					   or y_offset % SQUARE_FACTOR == (SQUARE_FACTOR - 1):
						self._img.putpixel(point, dark_color)
					else:
						self._img.putpixel(point, normal_color)
			x += 1
			if x == self._num_x:
				x = 0
				y += 1
			remaining -= 1

	def save(self):
		self._img.save('test.png')

s = Squares(128, 112)

# vector table
s.color(0x0000,  444, 1)

# ResetHandler
s.color(0x01BC,  320, 2)
s.color(0x02FC,  100, 3)

# digitWriteFast
s.color(0x0798,   60, 2)
s.color(0x07D4,    4, 3)

# digitWriteFast
s.color(0x07D8,   52, 4)
s.color(0x080C,    4, 5)

# micros
s.color(0x0810,   48, 2)
s.color(0x0840,   12, 3)

# delay
s.color(0x084C,   42, 4)
s.color(0x0876,    2, 7)

s.color(0x31F0, 1540, 6)
s.save()
