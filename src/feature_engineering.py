import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
import os

def engineer_features(data):
    """Create features using the correct column names with enhanced rebounding metrics"""
    print("\nStarting feature engineering...")
    teams_df = data['teams'].copy()
    players_df = data['players_teams'].copy()
    
    print(f"Initial teams_df shape: {teams_df.shape}")
    print(f"Initial players_df shape: {players_df.shape}")
    
    # Basic Performance Metrics
    teams_df['win_pct'] = teams_df['won'] / teams_df['GP']
    print("Added win percentages")
    
    # Offensive Metrics
    teams_df['points_per_game'] = teams_df['o_pts'] / teams_df['GP']
    teams_df['points_allowed_per_game'] = teams_df['d_pts'] / teams_df['GP']
    print("Added points metrics")
    
    # Shooting Efficiency
    teams_df['fg_pct'] = np.where(teams_df['o_fga'] > 0, teams_df['o_fgm'] / teams_df['o_fga'], 0)
    teams_df['three_pt_pct'] = np.where(teams_df['o_3pa'] > 0, teams_df['o_3pm'] / teams_df['o_3pa'], 0)
    teams_df['ft_pct'] = np.where(teams_df['o_fta'] > 0, teams_df['o_ftm'] / teams_df['o_fta'], 0)
    print("Added shooting percentages")
    
    # Enhanced Rebounding Metrics
    # Per Game Metrics
    teams_df['total_rebounds_per_game'] = teams_df['o_reb'] / teams_df['GP']
    teams_df['offensive_rebounds_per_game'] = teams_df['o_oreb'] / teams_df['GP']
    teams_df['defensive_rebounds_per_game'] = teams_df['o_dreb'] / teams_df['GP']
    
    # Opponent Rebounding
    teams_df['opp_total_rebounds_per_game'] = teams_df['d_reb'] / teams_df['GP']
    teams_df['opp_offensive_rebounds_per_game'] = teams_df['d_oreb'] / teams_df['GP']
    teams_df['opp_defensive_rebounds_per_game'] = teams_df['d_dreb'] / teams_df['GP']
    
    # Rebounding Efficiency
    total_rebounds = teams_df['o_reb'] + teams_df['d_reb']
    teams_df['rebounding_pct'] = np.where(total_rebounds > 0, teams_df['o_reb'] / total_rebounds, 0)
    
    offensive_rebound_opportunities = teams_df['o_oreb'] + teams_df['d_dreb']
    defensive_rebound_opportunities = teams_df['o_dreb'] + teams_df['d_oreb']
    
    teams_df['offensive_rebounding_pct'] = np.where(offensive_rebound_opportunities > 0,
                                                   teams_df['o_oreb'] / offensive_rebound_opportunities, 0)
    teams_df['defensive_rebounding_pct'] = np.where(defensive_rebound_opportunities > 0,
                                                   teams_df['o_dreb'] / defensive_rebound_opportunities, 0)
    print("Added enhanced rebounding metrics")
    
    # Home/Away Performance
    total_home = teams_df['homeW'] + teams_df['homeL']
    total_away = teams_df['awayW'] + teams_df['awayL']
    teams_df['home_win_pct'] = np.where(total_home > 0, teams_df['homeW'] / total_home, 0)
    teams_df['away_win_pct'] = np.where(total_away > 0, teams_df['awayW'] / total_away, 0)
    print("Added home/away metrics")
    
    # Conference Performance
    total_conf = teams_df['confW'] + teams_df['confL']
    teams_df['conf_win_pct'] = np.where(total_conf > 0, teams_df['confW'] / total_conf, 0)
    print("Added conference metrics")
    
    # Additional Efficiency Metrics
    teams_df['assists_per_game'] = teams_df['o_asts'] / teams_df['GP']
    teams_df['turnovers_per_game'] = teams_df['o_to'] / teams_df['GP']
    teams_df['assist_to_turnover'] = np.where(teams_df['o_to'] > 0, teams_df['o_asts'] / teams_df['o_to'], 0)
    teams_df['blocks_per_game'] = teams_df['o_blk'] / teams_df['GP']
    teams_df['steals_per_game'] = teams_df['o_stl'] / teams_df['GP']
    print("Added efficiency metrics")
    
    print("\nAggregating player statistics...")
    try:
        player_stats = players_df.groupby(['tmID', 'year']).agg({
            'points': ['mean', 'max', 'std'],
            'assists': ['mean', 'sum'],
            'rebounds': ['mean', 'sum'],
            'steals': ['mean', 'sum'],
            'blocks': ['mean', 'sum'],
            'minutes': ['sum', 'mean']
        }).reset_index()
        
        player_stats.columns = ['tmID', 'year'] + [
            f'team_{col[0]}_{col[1]}' for col in player_stats.columns[2:]
        ]
        print(f"Player stats shape after aggregation: {player_stats.shape}")
        
        final_df = teams_df.merge(player_stats, on=['tmID', 'year'], how='left')
        print(f"Shape after merge: {final_df.shape}")
        
    except Exception as e:
        print(f"Error in player statistics aggregation: {str(e)}")
        final_df = teams_df.copy()
    
    # Create target variable
    print("\nCreating target variable...")
    final_df['made_playoffs_next_season'] = final_df.groupby('tmID')['playoff'].shift(-1)
    final_df['made_playoffs_next_season'] = (final_df['made_playoffs_next_season'] == 'Y').astype(int)
    
    # Drop the original zero-filled columns
    columns_to_drop = ['tmORB', 'tmDRB', 'tmTRB', 'opptmORB', 'opptmDRB', 'opptmTRB']
    final_df.drop(columns=columns_to_drop, inplace=True)

    final_df = final_df.round(2)
    
    print(f"Final dataframe shape: {final_df.shape}")
    
    return final_df

def main():
    # Set up base path
    base_path = r"C:\Users\PRECISION\Desktop\feup-ac\data\02-data_selection"
    output_path = os.path.join(base_path, 'processed_data')
    os.makedirs(output_path, exist_ok=True)
    
    # Load data
    print("Loading data...")
    data = {}
    for file in ['teams.csv', 'players_teams.csv']:
        file_path = os.path.join(base_path, file)
        data[file.replace('.csv', '')] = pd.read_csv(file_path)
        print(f"Loaded {file}")
    
    # Engineer features
    print("\nEngineering features...")
    enhanced_teams = engineer_features(data)
    
    # Save the enhanced dataset
    print("\nSaving processed data...")
    enhanced_teams.to_csv(os.path.join(output_path, 'enhanced_teams.csv'), index=False)
    
    # Generate feature summary
    feature_summary = pd.DataFrame({
        'feature': enhanced_teams.columns,
        'non_null_count': enhanced_teams.count(),
        'mean': enhanced_teams.mean(numeric_only=True),
        'std': enhanced_teams.std(numeric_only=True)
    })
    feature_summary.to_csv(os.path.join(output_path, 'feature_summary.csv'), index=False)
    
    print(f"\nData processing complete!")
    print(f"Total features created: {len(enhanced_teams.columns)}")
    print(f"Total samples: {len(enhanced_teams)}")
    print(f"\nOutput saved to: {output_path}")
    
    return enhanced_teams

if __name__ == "__main__":
    enhanced_teams = main()