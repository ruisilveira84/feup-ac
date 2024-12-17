import read_data as rd
import process_data as pd
import model_training as mt
import player_efficiency_rating as per
import os
#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

if __name__ == "__main__":
    # Step 1: Load the data
    print("Loading data...")
    tables = rd.read_data()
    teams = tables["teams"]

    # Step 2: Prepare the data (feature engineering)
    print("Preparing data...")
    teams = pd.add_features(teams)

    # Step 3: Split data into training and testing sets
    from sklearn.model_selection import train_test_split

    print("Splitting data into train and test sets...")
    X = teams[["win_rate", "point_balance"]]  # Add more features as necessary
    y = teams["playoff"].apply(lambda x: 1 if x == "Y" else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Train the model
    print("Training the model...")
    from sklearn.ensemble import RandomForestClassifier

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Feature importance
    import pandas as pd
    feature_importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)

    print("Feature Importance:")
    print(feature_importance)

    # Step 5: Evaluate the model
    from sklearn.metrics import classification_report

    print("Evaluating the model...")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Step 6: Calculate PER
    print("Calculating Player Efficiency Rating (PER)...")
    players_stats = tables["players_teams"]  # Use the correct table
    players_stats = per.calculate_per(players_stats)

    # Ensure the output directory exists and save the data
    output_dir = "../data/01-starting_data/development_data"
    os.makedirs(output_dir, exist_ok=True)

    players_stats.to_csv(os.path.join(output_dir, "players_with_per.csv"), index=False)
    print("Player Efficiency Rating (PER) calculado e salvo com sucesso!")
    