from mealmind.ml.utils.recommendate_recipes import df, recipe_names, recommend_recipes_single_user
from django.utils.text import slugify

def get_recommndated_recipes(user_ingredients):
    # --- Example Usage (assuming df, ingredient_matrix, vectorizer are ready) ---
    top_recommendations = recommend_recipes_single_user(user_ingredients, top_n=3)
    recommended_recipes = []
    for _, row in top_recommendations.iterrows():
        steps_list =  [s.strip() for s in row['steps'].split(',') if s.strip()]
        recipe_name = row['recipe_name']
        
        recommended_recipes.append({
            'recipe_name': recipe_name,
            'recipe_slug': slugify(recipe_name),
            'ingredients': row['ingredients'],
            'steps':steps_list,
        })
    
    return recommended_recipes

# returns all the ingredients
def get_all_ingredients():
    ingredients = set()
    for count, ingredient in enumerate(recipe_names):
        ingredients.add(ingredient)
    
    return ingredients

def get_recipe_details(decoded_name):
    df['slug'] = df['name'].apply(slugify)
    recipe_serice = df[df['slug'] == decoded_name]
    recipe_details = {
            'recipe_name': recipe_serice['name'],
            'ingredients': recipe_serice['ingredients'],
            'ingredients_raw_str': recipe_serice['ingredients_raw_str'],
            'steps':recipe_serice['steps'],
        }
    
    return recipe_details
