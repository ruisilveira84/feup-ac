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
    if "players_teams" in tables:
        players_stats = tables["players_teams"]
    else:
        raise KeyError("Table 'players_teams' not found in loaded data!")

    # Map the required columns for PER calculation
    players_stats['MIN'] = players_stats['minutes']
    players_stats['PTS'] = players_stats['points']
    players_stats['ORB'] = players_stats['oRebounds']
    players_stats['DRB'] = players_stats['dRebounds']
    players_stats['AST'] = players_stats.get('assists', 0)
    players_stats['STL'] = players_stats.get('steals', 0)
    players_stats['BLK'] = players_stats.get('blocks', 0)
    players_stats['TO'] = players_stats.get('turnovers', 0)
    players_stats['PF'] = players_stats.get('fouls', 0)

    # Ensure required columns are ready
    print(players_stats[['playerID', 'MIN', 'PTS', 'ORB', 'DRB']].head())

    # Calculate PER
    players_stats = per.calculate_per(players_stats)

    # Save the results
    output_file = "players_with_per.csv"
    players_stats.to_csv(output_file, index=False)
    print(f"Player Efficiency Rating (PER) calculado e salvo com sucesso em '{output_file}'!")

    # Verificar o conteúdo do DataFrame antes de salvar
    print("Linhas no DataFrame antes de salvar:", len(players_stats))
    print(players_stats.head())

    # Salvar os dados no diretório atual
    output_file = "./players_with_per.csv"
    players_stats.to_csv(output_file, index=False)

    print(f"Player Efficiency Rating (PER) calculado e salvo com sucesso em '{output_file}'!")
