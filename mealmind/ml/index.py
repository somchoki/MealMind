import ast
from mealmind.ml.utils.prediction_model import df, recommend_recipes_single_user
from django.utils.text import slugify

def get_recommndated_recipes(user_ingredients):
    # --- Example Usage (assuming df, ingredient_matrix, vectorizer are ready) ---
    top_recommendations = recommend_recipes_single_user(user_ingredients, top_k=3)
    
    return top_recommendations

# returns all the ingredients
def get_all_ingredients():
    ingredients = set()
    for ingredient_list in df['ingredients']:
        # ingredient_list = ast.literal_eval(ingredient_list)
        for ingredient in ingredient_list:
            ingredients.add(ingredient)

    return ingredients

def get_recipe_details(decoded_name):
    recipe_serice = df[df['recipe_slug'] == decoded_name]

    if not recipe_serice.empty:
        recipe_details = {
            'recipe_name': recipe_serice['name'].values[0],
            'tags': recipe_serice['tags'].values[0],
            'description': recipe_serice['description'].values[0],
            'ingredients': recipe_serice['ingredients'].values[0],
            'ingredients_raw_str': recipe_serice['ingredients_raw_str'].values[0],
            'steps': recipe_serice['steps'].values[0],
        }
    else:
        recipe_details = None  # or handle error

    return recipe_details
