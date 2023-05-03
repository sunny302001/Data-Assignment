#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np

# read the trade log file into a pandas DataFrame
trades = pd.read_csv(r'C:\Users\sathw\Downloads\tradelog.csv')

# calculate the number of trades
total_trades = trades.shape[0]

# calculate the number of profitable and loss-making trades
profitable_trades = (trades['Exit Price'] - trades['Entry Price'] > 0).sum()
loss_making_trades = (trades['Exit Price'] - trades['Entry Price'] < 0).sum()

# calculate the win rate
win_rate = profitable_trades / total_trades

# calculate the average profit and average loss per trade
trades['P/L'] = trades['Exit Price'] - trades['Entry Price']
average_profit_per_trade = trades[trades['P/L'] > 0]['P/L'].mean()
average_loss_per_trade = trades[trades['P/L'] < 0]['P/L'].mean()
# calculate the risk reward ratio
risk_reward_ratio = abs(average_profit_per_trade / average_loss_per_trade)

# calculate the expectancy
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit_per_trade) - (loss_rate * average_loss_per_trade)

# calculate the average ROR per trade
portfolio_value = 200000
trades['ROR'] = (trades['P/L'] / trades['Entry Price']) * portfolio_value
average_ROR_per_trade = trades['ROR'].mean()

# calculate the Sharpe ratio
risk_free_rate = 0.05
rate_of_return = average_ROR_per_trade / portfolio_value
volatility = trades['ROR'].std()
sharpe_ratio = (rate_of_return - risk_free_rate) / volatility

# calculate the maximum drawdown and maximum drawdown percentage
trades['Cumulative ROR'] = trades['ROR'].cumsum()
trades['Peak ROR'] = trades['Cumulative ROR'].cummax()
trades['Drawdown'] = trades['Cumulative ROR'] - trades['Peak ROR']
max_drawdown = trades['Drawdown'].min()
max_drawdown_percentage = (max_drawdown / trades['Peak ROR'].iloc[-1]) * 100

# calculate the CAGR
ending_value = portfolio_value + trades['ROR'].sum()
beginning_value = portfolio_value
no_of_periods = total_trades
CAGR = (float(abs(ending_value / beginning_value)) ** float(1 / no_of_periods)) - 1

# calculate the Calmar ratio
calmar_ratio = abs(CAGR / max_drawdown_percentage)

# print the results
print(f'Total Trades: {total_trades}')
print(f'Profitable Trades: {profitable_trades}')
print(f'Loss-Making Trades: {loss_making_trades}')
print(f'Win Rate: {win_rate:.2%}')
print(f'Average Profit per Trade: Rs {average_profit_per_trade:.2f}')
print(f'Average Loss per Trade: Rs {average_loss_per_trade:.2f}')
print(f'Risk Reward Ratio: {risk_reward_ratio:.2f}')
print(f'Expectancy: Rs {expectancy:.2f}')
print(f'Average ROR per Trade: {average_ROR_per_trade:.2%}')
print(f'Sharpe Ratio: {sharpe_ratio:.2f}')
print(f'Maximum Drawdown: Rs {max_drawdown:.2f}')
print(f'Maximum Drawdown Percentage: {max_drawdown_percentage:.2f}%')
print(f'CAGR: {CAGR}')
print(f'calmar_ratio: {calmar_ratio}')

# saving the dataframe


# In[87]:


trades.to_csv('tradelog_final.csv')


# In[69]:


CAGR = (float(abs(ending_value / beginning_value)) ** float(1 / no_of_periods)) - 1
CAGR

