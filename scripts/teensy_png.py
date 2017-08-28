from PIL import Image

SQUARE_FACTOR = 9

BLACK = (0, 0, 0)

HOTPINK = (255, 105, 180)
DEEPPINK = (255, 20, 147)

GREEN = (0, 128, 0)
DARKGREEN = (0, 100, 0)

LIME = (50, 205, 50)
LIMEGREEN = (0, 255, 0)

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
			normal_color = LIME
			dark_color = LIMEGREEN

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

	def go(self):
		for x in range(0, 1080):
			for y in range(0, 27):
				if x % 9 == 0 or x % 9 == 8:
					img.putpixel((x, y), DEEPPINK)
				elif y % 9 == 0 or y % 9 == 8:
					img.putpixel((x, y), DEEPPINK)
				else:
					img.putpixel((x, y), HOTPINK)


s = Squares(120, 120)
s.color(0x0000, 444, 1)
s.color(0x01BC, 312, 2)
s.color(0x0310,  16, 3)
s.save()
