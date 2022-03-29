import random

delivery_list = ['Pizza', 'Sushi', 'Greek', 'Subs']
american_list = ['Buffalo Chicken Wrap', 'Chicken Noodle Soup', 'Burgers', 'Roast Chicken']
italian_list = ['Chicken Parmigiana', 'Spaghetti and Meatballs', 'Branzino', 'Homemade Ravioli']
mexican_list = ['Tacos', 'Burritos', 'Quesadillas', 'Carnitas']
asian_list = ['Ramen', 'Stir-Fry', 'Pho', 'Fried Rice']
healthy_list = ['Quinoa Bowl', 'Grilled Salmon', 'Grilled Chicken Salad']
fine_dining_list = ['Filet Mignon', 'Lobster']

def calculate_score(day_of_week, cuisine_yesterday, in_a_rush, healthy_eating, special_occasion):

  day_of_week = day_of_week.lower()
  cuisine_yesterday = cuisine_yesterday.lower()
  in_a_rush = in_a_rush.lower()
  healthy_eating = healthy_eating.lower()
  special_occassion = special_occasion.lower()

  if day_of_week == 'weekday':
    Delivery = -50
    American = 0
    Italian = 0
    Healthy = 0
    Mexican = 0
    Asian = 0
  
  elif day_of_week == 'weekend':
    Delivery = 50
    American = 0
    Italian = 0
    Healthy = 0
    Mexican = 0
    Asian = 0
  
  if cuisine_yesterday == 'delivery':
    Delivery -= 50
    American += 10
    Italian += 10
    Healthy += 10
    Mexican += 10
    Asian += 10
  
  elif cuisine_yesterday == 'american':
    Delivery += 10
    American -= 50
    Italian += 10
    Healthy += 10
    Mexican += 10
    Asian += 10
  
  elif cuisine_yesterday == 'italian':
    Delivery += 10
    American += 10
    Italian -= 50
    Healthy += 10
    Mexican += 10
    Asian += 10

  elif cuisine_yesterday == 'healthy':
    Delivery += 10
    American += 10
    Italian += 10
    Healthy -= 25
    Mexican += 10
    Asian += 10
  
  elif cuisine_yesterday == 'mexican':
    Delivery += 10
    American += 10
    Italian += 10
    Healthy += 10
    Mexican -= 50
    Asian += 10

  elif cuisine_yesterday == 'asian':
    Delivery += 10
    American += 10
    Italian += 10
    Healthy += 10
    Mexican += 10
    Asian -= 50

  if in_a_rush == 'yes':
    Delivery += 10
    American += 20
    Italian -= 10
    Healthy += 20
    Mexican -= 15
    Asian -= 10
  
  elif in_a_rush == 'no':
    Delivery -= 30
    American -= 10
    Italian += 15
    Healthy += 0
    Mexican += 15
    Asian += 15
  
  if healthy_eating == 'yes':
    Delivery += 0
    American += 0
    Italian += 0
    Healthy -= 5
    Mexican += 0
    Asian += 0
  
  elif healthy_eating == 'no':
    Delivery += 0
    American += 0
    Italian += 0
    Healthy += 30
    Mexican += 0
    Asian += 15

  if special_occasion == 'yes':
    Fine_Dining = 1000
  
  elif special_occasion == 'no':
    Fine_Dining = 0

  var = {Delivery:"Delivery", American:"American", Italian:"Italian", Healthy:"Healthy", Mexican:"Mexican", Fine_Dining:"Fine Dining"}
  return var.get(max(var))

day_of_week = input("Is it a weekday or the weekend? (choose: Weekday or Weekend) ")
cuisine_yesterday = input("What cuisine did you have yesterday? (choose: Delivery, American, Italian, Healthy, Mexican, Asian, Fine Dining) ")
in_a_rush = input("Are you in a rush? (choose: Yes or No) ")
healthy_eating = input("Have you been eating well lately? (choose: Yes or No) ")
special_occasion = input("Is it a special occasion? (choose: Yes or No) ")


score = calculate_score(day_of_week, cuisine_yesterday, in_a_rush, healthy_eating, special_occasion)

def menu_item(score):
    if score == 'Delivery':
      menu_item_choice = random.choice(delivery_list)
      return menu_item_choice
    elif score == 'American':
      menu_item_choice = random.choice(american_list)
      return menu_item_choice
    elif score == 'Italian':
      menu_item_choice = random.choice(italian_list)
      return menu_item_choice
    elif score == 'Healthy':
      menu_item_choice = random.choice(healthy_list)
      return menu_item_choice
    elif score == 'Mexican':
      menu_item_choice = random.choice(mexican_list)
      return menu_item_choice
    elif score == 'Asian':
      menu_item_choice = random.choice(asian_list)
      return menu_item_choice
    elif score == 'Fine Dining':
      menu_item_choice = random.choice(fine_dining_list)
      return menu_item_choice

score2 = menu_item(score)

print("For dinner tonight you should have", score, "food and you should eat", score2)
