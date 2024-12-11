import pandas as pd

# Importar as relações
import os
import pandas as pd

def read_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/development_data'))
    awards_players = pd.read_csv(os.path.join(base_path, 'awards_players.csv'))
    coaches = pd.read_csv(os.path.join(base_path, 'coaches.csv'))
    players = pd.read_csv(os.path.join(base_path, 'players.csv'))
    players_teams = pd.read_csv(os.path.join(base_path, 'players_teams.csv'))
    series_post = pd.read_csv(os.path.join(base_path, 'series_post.csv'))
    teams = pd.read_csv(os.path.join(base_path, 'teams.csv'))
    teams_post = pd.read_csv(os.path.join(base_path, 'teams_post.csv'))

    return {
        "awards_players": awards_players,
        "coaches": coaches,
        "players": players,
        "players_teams": players_teams,
        "series_post": series_post,
        "teams": teams,
        "teams_post": teams_post
    }

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

def save_files(folder: str, names: list[str], tables: list[pd.DataFrame]):
    assert(len(names) == len(tables))
    for name,table in zip(names, tables):
        table.to_csv(os.path.join("..","data",folder, name)+".csv", index=False)
        print(f"Data {name} saved to {os.path.join('..','data',folder)}")
