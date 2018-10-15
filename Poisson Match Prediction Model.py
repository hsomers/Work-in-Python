# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:16:12 2018

@author: HDSom
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson,skellam

# Gather and manipulate the data
epl_1718 = pd.read_csv('EPL DATA 2017-2018.csv')
epl_1718 = epl_1718[['HomeTeam','AwayTeam','FTHG','FTAG']]
epl_1718 = epl_1718.rename(columns={'FTHG': 'HomeGoals', 'FTAG':'AwayGoals'})
epl_1718.head()

# Since we're predicting the last round of matches, we need to remove the last 10 rows
epl_1718 = epl_1718[:-10]
epl_1718.mean()

# Probability of a draw between home and away team
skellam.pmf(0.0, epl_1718.mean()[0], epl_1718.mean()[1])

# Probability of Home team winning by one goal
skellam.pmf(1, epl_1718.mean()[0], epl_1718.mean()[1])

# Import some more tools for Poisson Regression
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Making the model
goal_model_data = pd.concat([epl_1718[['HomeTeam', 'AwayTeam', 'HomeGoals']].assign(home=1).rename(
        columns = {'HomeTeam':'team', 'AwayTeam':'opponent', 'HomeGoals':'goals'}),
    epl_1718[['AwayTeam', 'HomeTeam', 'AwayGoals']].assign(home=0).rename(
            columns = {'AwayTeam':'team', 'HomeTeam':'opponent', 'AwayGoals':'goals'})])

poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data,
                        family=sm.families.Poisson()).fit()

poisson_model.summary()

# Let's make some predictions
poisson_model.predict(pd.DataFrame(data={'team':'Crystal Palace', 'opponent':'Man City',
                                   'home':1},index=[1]))

poisson_model.predict(pd.DataFrame(data={'team':'Man City', 'opponent':'Crystal Palace',
                                   'home':0},index=[1]))

def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team':homeTeam,
                                                           'opponent':awayTeam,'home':1},
                                                        index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team':awayTeam,
                                                           'opponent':homeTeam,'home':0},
                                                        index=[1])).values[0]
    
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))
    
simulate_match(poisson_model, 'Crystal Palace', 'Man City')

cry_mnc = simulate_match(poisson_model, 'Crystal Palace', 'Man City', max_goals=10)

#Odds that Crystal Palace Win
np.sum(np.tril(cry_mnc, -1))

#Odds of a draw
np.sum(np.diag(cry_mnc))

#Odds of Man City Win
np.sum(np.triu(cry_mnc, 1))