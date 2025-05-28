from urllib.parse import unquote
import json
from django.shortcuts import render
# from .ml.main import get_all_ingredients, get_recommndated_recipes, get_recipe_details
from .ml.index import get_all_ingredients, get_recommndated_recipes, get_recipe_details
from django.utils.safestring import mark_safe
from django.views.decorators.cache import cache_page

# Cache for 10 minutes (or use low-level caching per your setup)
@cache_page(60 * 10)
def index(request):
    ingredients = list(get_all_ingredients())

    # ingredients_json = mark_safe(json.dumps(ingredients))
    dish_data = {
            "ingredients": ingredients,
            "recommended_recipes": []
        }

    if request.method == 'POST':
        data = request.POST.get('selected_ingredients')
        user_ingredients = json.loads(data) if data else []
        
        top_3_recommendation = get_recommndated_recipes(user_ingredients)
        dish_data["recommended_recipes"] = top_3_recommendation
    
    serialized_data = json.dumps(dish_data)
    return render(request, 'index.html',{'data': serialized_data})


def about(request):
    return render(request, 'about.html')

def details(request, slug):
    decoded_name = unquote(slug)
    recipe_detail = get_recipe_details(decoded_name)

    return render(request, 'details.html', recipe_detail)

def food(request):
    if request.method == 'POST':
        data = request.POST.get('selected_ingredients')
        user_ingredients = json.loads(data) if data else []
        top_3_recommendation = get_recommndated_recipes(user_ingredients)
        
    return render(request, 'food.html', {'recommended_recipes': top_3_recommendation})