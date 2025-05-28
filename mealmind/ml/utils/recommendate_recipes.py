import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
dataset_path = f"{BASE_DIR}/dataset/recipe_recommendation_dataset.feather"
ingredient_vectorizer_path = f"{BASE_DIR}/models/ingredient_vectorizer.joblib"
ingredient_matrix_path = f"{BASE_DIR}/models/ingredient_matrix.joblib"

df = pd.read_feather(dataset_path)

vectorizer = joblib.load(ingredient_vectorizer_path)
ingredient_matrix = joblib.load(ingredient_matrix_path)

recipe_names = vectorizer.get_feature_names_out()

def recommend_recipes_single_user(user_ingredients, top_n=5):
    user_vector = vectorizer.transform([' '.join(user_ingredients)])
    similarity_scores = cosine_similarity(user_vector, ingredient_matrix)[0]
    recommendation_df = pd.DataFrame({'recipe_name': df['name'], 'ingredients': df['ingredients'], 'ingredients_raw_str': recipe_df['ingredients_raw_str'], 'steps': recipe_df['steps'] , 'similarity': similarity_scores})
    recommended_recipes = recommendation_df.sort_values(by='similarity', ascending=False)
    return recommended_recipes[recommended_recipes['similarity'] > 0].head(top_n)
