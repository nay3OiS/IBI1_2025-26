# Define food_item class
class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
# Define a function to calculate total nutrition
def calculate_daily_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0
    for food in food_list:
        total_cal = total_cal + food.calories
        total_pro = total_pro + food.protein
        total_car = total_car + food.carbohydrates
        total_fat = total_fat + food.fat
    # Print results WITHOUT f-string
    print("Total daily nutrition:")
    print("Calories: ",total_cal," kcal")
    print("Protein: ",total_pro," g")
    print("Carbohydrates: ",total_car," g")
    print("Fat: ",total_fat," g")
    # Warnings
    if total_cal > 2500:
        print("Warning: Calories exceed 2500!")
    if total_fat > 90:
        print("Warning: Fat exceeds 90 g!")
# Examples
apple = food_item("Apple", 60, 0.3, 15, 0.5)
banana = food_item("Banana", 100, 1.3, 23, 0.4)
rice = food_item("Rice", 130, 2.7, 28, 0.3)
daily_food = [apple, banana, rice]
calculate_daily_nutrition(daily_food)