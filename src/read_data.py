import pandas as pd

# Importar as relações
awards_players = pd.read_csv('../data/development_data/awards_players.csv')
coaches = pd.read_csv('../data/development_data/coaches.csv')
players = pd.read_csv('../data/development_data/players.csv')
players_teams = pd.read_csv('../data/development_data/players_teams.csv')
series_post = pd.read_csv('../data/development_data/series_post.csv')
teams = pd.read_csv('../data/development_data/teams.csv')
teams_post = pd.read_csv('../data/development_data/teams_post.csv')

# Verificar os primeiros registos de cada tabela
print(awards_players.head())
print(coaches.head())
print(players.head())
