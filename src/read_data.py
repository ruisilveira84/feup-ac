import pandas as pd

# Importar as relações
def read_data():
    awards_players = pd.read_csv('../data/development_data/awards_players.csv')
    coaches = pd.read_csv('../data/development_data/coaches.csv')
    players = pd.read_csv('../data/development_data/players.csv')
    players_teams = pd.read_csv('../data/development_data/players_teams.csv')
    series_post = pd.read_csv('../data/development_data/series_post.csv')
    teams = pd.read_csv('../data/development_data/teams.csv')
    teams_post = pd.read_csv('../data/development_data/teams_post.csv')

    tables = {"awards_players": awards_players,
            "coaches": coaches, 
            "players": players, 
            "players_teams": players_teams, 
            "series_post": series_post, 
            "teams": teams, 
            "teams_post": teams_post}
    
    return tables

def print_null_fields(tables: dict[str, pd.DataFrame]):
    for name,table in tables.items():
        print(f"Table {name}:")
        print(table.isnull().sum())
        print("\n")

def print_empty_fields(tables: dict[str, pd.DataFrame]):
    for name,table in tables.items():
        print(f"Table {name}:")
        print(table[table.isnull().any(axis=1)])
        print("\n")

def remove_null_entries(tables: dict[str, pd.DataFrame]):
    tables["players"] = tables["players"].dropna(axis=1, thresh=len(tables["players"]) - 100)

    for key in tables:
        tables[key] = tables[key].dropna()

    return tables
