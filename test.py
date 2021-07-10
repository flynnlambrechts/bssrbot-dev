
class Meal:
	def __init__(self):
		print("meal")

class Dinner:
	def __init__(self):
		print("dinner")

meal = Meal()
dinner = Dinner()

print(type(meal))
print(type(dinner).__name__)