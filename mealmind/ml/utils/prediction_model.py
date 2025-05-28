import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
from pathlib import Path
from django.utils.text import slugify
import ast


# Load everything
BASE_DIR = Path(__file__).resolve().parent.parent
dataset_path = f"{BASE_DIR}/dataset/dish_recommendation_dataset.csv"

df = pd.read_csv(dataset_path)
recipe_embeddings = np.load(f"{BASE_DIR}/models/recipe_embeddings.npy")
model = SentenceTransformer(f"{BASE_DIR}/models/recipe_model")

def str_to_object(data):
    data_list = ast.literal_eval(data)  # convert string to list

    return data_list

df['ingredients'] = df['ingredients'].apply(str_to_object)
df['steps'] = df['steps'].apply(str_to_object)
df['recipe_slug'] = df['name'].apply(slugify)
df['ingredients_raw_str'] = df['ingredients_raw_str'].apply(str_to_object)
df['tags'] = df['tags'].apply(str_to_object)

def recommend_recipes_single_user(user_ingredients, top_k = 5):
    recommended_recipes = []
    # Now you can run recommendations as usual
    user_embedding = model.encode(user_ingredients)
    similarities = util.cos_sim(user_embedding, recipe_embeddings)[0]

    top_results = np.argpartition(-similarities, range(top_k))[:top_k]
    for idx in top_results:
        idx_int = idx.item()
        
        recommended_recipes.append({
            'recipe_name': df.iloc[idx_int]["name"],
            'recipe_slug': df.iloc[idx_int]["recipe_slug"],
            'ingredients': df.iloc[idx_int]["ingredients"],
            'steps':df.iloc[idx_int]["steps"],
        })
    
    return recommended_recipes
