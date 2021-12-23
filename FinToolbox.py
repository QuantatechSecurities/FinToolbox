from math import sqrt, log

#Function 1, argument: decimal number, return: number with two decimals (percentage)
def display_percentage(val):
  return '{:.1f}%'.format(val * 100)

#Function 2, calculates the simple ROI of an investment. Divided is by default zero.
def simple_return(start_price, end_price, dividend=0):
  Simple_ROI = ((end_price - start_price) + dividend)/start_price
  return Simple_ROI

#Function 3, The logartithmic return, where earnings from invested are reinvested over time. Uses log() from math lib.
def log_return(start_price, end_price):
  log_ROI = log(end_price) - log(start_price)
  return log_ROI

#Function 4, aggregates across of timeframes. Argument 1; series of returns. Argument 2; timeframe, Daily = 252, Weekly = 52, Monthly = 12
def annualize_return(log_return, t):
    converted_ROI = log_return*t
    return converted_ROI

#Function 5, aggregates across of timeframes using avarages. Argument 1; series of returns. Argument 2; timeframe, Daily = 252, Weekly = 52, Monthly = 12. You can use this fomrula to aggregate across assets as well within your portfolio 
def convert_returns(log_returns, t):
  return sum(log_returns) / len(log_returns) * t

#Function 6, Calculates the variance of an asset. The greater the variance the greater the risk. 
def variance(dataset): #takes a list of asset prices
  mean = sum(dataset)/len(dataset)
  numerator = 0
  for value in dataset:
    holder = value - mean
    holder_squared = holder**2
    numerator += holder_squared
  variance = numerator/len(dataset)
  return variance

#Function 7, Calculates the standard deviation of an asset. Displayed in percentage
def stddev(dataset):
  variance = variance(dataset)
  stddev = sqrt(variance)
  return display_percentage(stddev)

#Function 8, Calculates the correlation between two assets. The Correlation coefficient is within the interval of -1 (negative correlation) and 1 (positive correlation)
def correlation(set_x, set_y):
  sum_x = sum(set_x)
  sum_y = sum(set_y)
  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])
  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])
  n = len(set_x)
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
  return numerator / denominator

 





