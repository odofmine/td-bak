#### 思路
当满仓之后，超过20个后，把20作为是否要使用持仓占比作为系数的标准，同时设置满仓条件为10，检验当有20作为满仓之后的控制后，是否能够进一步降低满仓条件

#### 参数

* 候选 60
* 持有 10
* 上限检查 20

#### 描述

```json
{
  "alpha": 37.1246,
  "beta": -0.0575,
  "sharpe_ratio": 4.773,
  "sortino_ratio": 9.6649,
  "annual_volatility": 0.7412,
  "annual_return_ratio": 25.9509,
  "skew": 1.183,
  "kurtosis": 7.264,
  "daily_winning_ratio": 0.6546,
  "max_drawdown": -0.2023
}
```

#### 总结

各项指标都增长了，回撤变大
