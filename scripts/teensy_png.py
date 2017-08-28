from PIL import Image

SQUARE_FACTOR = 9

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
			normal_color = LIGHTSEAGREEN
			dark_color = SEAGREEN
		elif color == 5:
			normal_color = ROYALBLUE
			dark_color = MEDIUMBLUE

		x = start % self._num_x
		y = start // self._num_x
		remaining = num
		while remaining != 0:
			for x_offset in range(SQUARE_FACTOR):
				for y_offset in range(SQUARE_FACTOR):
					point = ((x * SQUARE_FACTOR) + x_offset,
                   (y * SQUARE_FACTOR) + y_offset)
					if x_offset % 9 == 0 or x_offset % 9 == 8 or \
					   y_offset % 9 == 0 or y_offset % 9 == 8:
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

s = Squares(120, 120)
s.color(0x0000, 444, 1)
s.color(0x01BC, 312, 2)
s.color(0x0310,  16, 3)
s.color(0x0810,  60, 4)
s.color(0x084C,  44, 5)
s.save()
