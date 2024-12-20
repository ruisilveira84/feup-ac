import os
import pandas as pd

# Function to read multiple data files and return them as DataFrames
def read_data():
    """
    Reads data files from the specified directory and loads them into pandas DataFrames.

    Returns:
        dict: A dictionary containing the loaded data tables with keys as table names 
              and values as pandas DataFrames.
    """
    # Define the base path to the data directory
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/01-starting_data/development_data'))
    
    # Load each CSV file into a pandas DataFrame
    awards_players = pd.read_csv(os.path.join(base_path, 'awards_players.csv'))
    coaches = pd.read_csv(os.path.join(base_path, 'coaches.csv'))
    players = pd.read_csv(os.path.join(base_path, 'players.csv'))
    players_teams = pd.read_csv(os.path.join(base_path, 'players_teams.csv'))
    series_post = pd.read_csv(os.path.join(base_path, 'series_post.csv'))
    teams = pd.read_csv(os.path.join(base_path, 'teams.csv'))
    teams_post = pd.read_csv(os.path.join(base_path, 'teams_post.csv'))

    # Return a dictionary with all the loaded tables
    return {
        "awards_players": awards_players,
        "coaches": coaches,
        "players": players,
        "players_teams": players_teams,
        "series_post": series_post,
        "teams": teams,
        "teams_post": teams_post
    }

# Function to save a list of DataFrames to CSV files in a specified folder
def save_files(folder: str, names: list[str], tables: list[pd.DataFrame]):
    """
    Writes tables to CSV files in the specified folder.

    Args:
        folder (str): The target folder path, relative to the data directory.
        names (list[str]): List of strings with the names for the output files (without extensions).
        tables (list[pd.DataFrame]): List of pandas DataFrames to save as CSV files.
    """
    # Ensure the number of names matches the number of tables
    assert(len(names) == len(tables))
    
    # Iterate through each name and corresponding table
    for name, table in zip(names, tables):
        # Save each DataFrame to a CSV file in the specified folder
        table.to_csv(os.path.join("..", "data", folder, name) + ".csv", index=False)
        
        # Print a confirmation message for each saved file
        print(f"Data {name} saved to {os.path.join('..', 'data', folder)}")
