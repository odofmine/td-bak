#### 思路
当满仓之后，超过20个后，把20作为是否要使用持仓占比作为系数的标准

#### 参数

* 候选 60
* 持有 15
* 上限检查 20

#### 描述

```json
{
  "alpha": 28.4142,
  "beta": -0.0733,
  "sharpe_ratio": 4.7558,
  "sortino_ratio": 8.9859,
  "annual_volatility": 0.685,
  "annual_return_ratio": 20.151,
  "skew": 0.6059,
  "kurtosis": 4.9365,
  "daily_winning_ratio": 0.6569,
  "max_drawdown": -0.1619
}
```

#### 总结

回撤不变，收益和夏普都比之前高
