class Crop:
	"""this is a class"""
	def __init__(self, growth_rate, light_need, water_need):
		self._growth = 0
		self._days_growing = 0
		self._growth_rate = growth_rate
		self._light_need = light_need
		self._water_need = water_need
		self._status = "seed"
		self._type = "generic"
	
	def plant(self):
		return {'growth':self._growth, 'light':self._light_need}

def main():
	new_crop = Crop(3,4,5)
	print(new_crop._growth_rate)
	print(new_crop._status)
	print(new_crop.plant())

if __name__ =="__main__":
	main()
