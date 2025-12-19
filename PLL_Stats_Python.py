#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 11:04:47 2025

@author: thomasschindler
"""

import pandas as pd

stats_2019 = pd.read_csv('pll-player-stats-2019.csv')
stats_2020 = pd.read_csv('pll-player-stats-2020.csv')
stats_2021 = pd.read_csv('pll-player-stats-2021.csv')
stats_2022 = pd.read_csv('pll-player-stats-2022.csv')
stats_2023 = pd.read_csv('pll-player-stats-2023.csv')
stats_2024 = pd.read_csv('pll-player-stats-2024.csv')
stats_2025 = pd.read_csv('pll-player-stats-2025.csv')

""" In python, all I want to do is a simple dataframe that has
    per game stats, rather than number stats, since per game statistics
    are much more telling. Second, I want to try to focus on gathering
    insights from defensive stats, since those are often neglected
    or overlooked
"""

all_time_stats = pd.concat([stats_2019, stats_2020, stats_2021,
                           stats_2022, stats_2023, stats_2024,
                           stats_2025])

# For now, I will just make per game stats for each year
per_game_cols = ['points', 'scoringPoints', 'goals', 'onePointGoals',
                 'twoPointGoals', 'assists', 'shots', 'shotsOnGoal',
                 'twoPointShots', 'twoPointShotsOnGoal', 'turnovers',
                 'causedTurnovers', 'groundBalls', 'totalPasses', 'faceoffsWon',
                 'faceoffsLost', 'faceoffs', 'saves', 'scoresAgainst',
                 'twoPointGoalsAgainst', 'numPenalties', 'pim', 'powerPlayGoals',
                 'powerPlayShots', 'powerPlayGoalsAgainst', 'shortHandedGoals',
                 'shortHandedShots', 'unassistedGoals', 'assistedGoals']

# Create a dictionary of stats for years 2019-2025
years = range(2019, 2026)
per_game_stats = {}  # dictionary to hold per-game DataFrames

for year in years:
    # get the original stats DataFrame dynamically
    stats_df = globals()[f'stats_{year}'].copy()
    
    # convert selected columns to per-game
    stats_df[per_game_cols] = stats_df[per_game_cols].div(stats_df['gamesPlayed'], axis=0)
    
    # select columns to keep
    cols_keep = ['First Name', 'Last Name', 'Position', 'Team'] + per_game_cols
    stats_df = stats_df[cols_keep]
    
    # store in dictionary
    per_game_stats[year] = stats_df
    