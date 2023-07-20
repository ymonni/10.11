#Ymonni Simms 2106646
class FoodItem:


    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


fitem = FoodItem()
fitem.print_info()
print('Number of calories for 1.00 serving(s): ',fitem.get_calories(1))
name = input('Enter name:')
fat = float(input('Enter fat: '))
carbs = float(input('Enter carbs: '))
protein = float(input('Enter protein: '))

fitem = FoodItem(name,fat,carbs,protein)
fitem.print_info()
print('Number of calories for 1.00 serving(s): ',fitem.get_calories(1))