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

def tune_model(X_train, y_train):
    from sklearn.model_selection import GridSearchCV
    from sklearn.ensemble import RandomForestClassifier

    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }

    grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_
