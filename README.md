# QUANTATECH SECURITIES **FinToolBox**
## Open source python library for risk/return asset management

**FinToolBox** features eight simple functions for quicker risk/return calculations.

```
from FinToolbox import *
```

| Function     | Description |
| ----------- | ----------- |
| display_percentage    | Returns a percentage number. **Argument:** decimal number. |
| simple_return  | Returns the simple rate of return of the asset. **Arguments:** [1] purchase price, [2] ending/selling price, [3] potential dividends        |
|log_return | Returns the logarithmic rate of return of the asset. **Arguments:** [1] purchase price, [2] ending/selling price.|
|annualize_return| Aggregates across timeframes. **Arguments:** [1] The logarithmic rate of return of the asset, [2] The number of the current timeframes in a year. E.g. **Current timeframe:** days, [2] = 252 because there are 252 trading days in a year.|
|convert_returns| Aggregates across timeframes. **Arguments:** [1] The logarithmic rate of return of the asset, [2] The number of current timeframes of the current timeframe. E.g. **Current timeframe:** days, [2] = you have data from the last 5 days, therefore your second argument is 5.|
|variance| Returns the variance of the asset. **Arguments:** [1] The assets dataset's of prices|
|stddev| Returns the standard deviation of the asset. **Arguments:** [1] The asset's dataset of prices|
|correlation| Returns the correlation between two assets. **Arguments:** [1] Asset 1's dataset of prices, [2] Assets 2's dataset of prices.

 #### Aditional Information
 If you have any questions related to this or other projects feel free to contact us over [Mail](quantatech.securities@gmail.com)








