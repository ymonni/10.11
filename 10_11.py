#Ymonni Simms 2106646
class FoodItem:
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, servings):
        total_calories = (self.fat * 9 + self.carbs * 4 + self.protein * 4) * servings
        return total_calories


# Main function to test the FoodItem class
def main():
    default_item = FoodItem()
    input_name = input()
    input_fat = float(input())
    input_carbs = float(input())
    input_protein = float(input())
    input_servings = float(input())

    input_item = FoodItem(input_name, input_fat, input_carbs, input_protein)

    print(f'Nutritional information per serving of {default_item.name}:')
    print(f'Fat: {default_item.fat:.2f} g')
    print(f'Carbohydrates: {default_item.carbs:.2f} g')
    print(f'Protein: {default_item.protein:.2f} g')
    print(f'Number of calories for {input_servings:.2f} serving(s): {default_item.get_calories(input_servings):.2f}')

    print(f'Nutritional information per serving of {input_item.name}:')
    print(f'Fat: {input_item.fat:.2f} g')
    print(f'Carbohydrates: {input_item.carbs:.2f} g')
    print(f'Protein: {input_item.protein:.2f} g')
    print(f'Number of calories for {input_servings:.2f} serving(s): {input_item.get_calories(input_servings):.2f}')


if __name__ == "__main__":
    main()