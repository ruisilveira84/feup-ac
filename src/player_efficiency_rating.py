
import pandas as pd

def calculate_per(players_stats):
    """
    Calculates the Player Efficiency Rating (PER) for each player in the dataset.

    Args:
        players_stats (pd.DataFrame): A DataFrame containing player statistics. Must include:
            - Points (PTS)
            - Field Goals Made (FGM)
            - Field Goals Attempted (FGA)
            - Free Throws Made (FTM)
            - Free Throws Attempted (FTA)
            - Offensive Rebounds (ORB)
            - Defensive Rebounds (DRB)
            - Assists (AST)
            - Steals (STL)
            - Blocks (BLK)
            - Turnovers (TO)
            - Personal Fouls (PF)
            - Minutes Played (MIN)

    Returns:
        pd.DataFrame: The original DataFrame with an additional 'PER' column.
    """
    # Constants based on the NBA's original PER calculation
    league_avg_per = 15
    league_factor = 1.0  # Adjust this based on league stats normalization if needed
    
    # Check if required columns exist
    required_columns = ['PTS', 'FGM', 'FGA', 'FTM', 'FTA', 'ORB', 'DRB', 
                        'AST', 'STL', 'BLK', 'TO', 'PF', 'MIN']
    
    for col in required_columns:
        if col not in players_stats.columns:
            players_stats[col] = 0  # Fill missing columns with 0
    
    # Calculate components of PER
    players_stats['uPER'] = (
        (players_stats['PTS'] + 
         0.7 * players_stats['ORB'] + 
         0.3 * players_stats['DRB'] + 
         players_stats['AST'] + 
         players_stats['STL'] + 
         players_stats['BLK'] - 
         players_stats['TO'] - 
         0.5 * players_stats['PF']) /
        (players_stats['MIN'] + 1e-5)  # Avoid division by zero
    )
    
    # Normalize to league factor
    players_stats['PER'] = players_stats['uPER'] * league_factor
    
    return players_stats