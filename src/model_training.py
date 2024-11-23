import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def get_data_of_year(tables: dict[str, pd.DataFrame], year: int):
    pass

def train_model(tables: dict[str, pd.DataFrame]):
    pass

def train_random_forest(X, y):
    """
    Trains a Random Forest classifier and computes feature importance.

    Args:
        X (pd.DataFrame): Feature matrix.
        y (pd.Series): Target variable.

    Returns:
        pd.DataFrame: Feature importance sorted by relevance.
    """
    model = RandomForestClassifier()
    model.fit(X, y)
    feature_importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)
    return feature_importance
