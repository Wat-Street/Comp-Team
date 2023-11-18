import math
from typing import Optional
import pandas as pd

class FeatureTransform:
    """
    Feature transformation and engineering functions. Assume that all inputs have been cleaned, validated,
    and aligned. For example, if a function requires two Series, they must be date and shape aligned.

    All dataframes must have format as follows ("long format"):
    
    date index | ticker | price | market_cap | earnings_per_share | ...
    ----------------------------------------------------------------------
    2023-01-01 |  AAPL  |  230  |    1.54    |          20
    2023-01-01 |  META  |  150  |    1.54    |
    2022-01-01 |  AAPL  |  230  |    1.54    |          20
    2022-01-01 |  META  |  150  |    1.54    |

    Sample Data:
    ```
    import pandas as pd
    df = pd.read_parquet("")
    ```
    """

    @staticmethod
    def rolling_beta(
        security_series: pd.Series, benchmark_series: pd.Series, window: int, min_window_pct: float=0.8
    ) -> pd.Series:
        """Compute beta with a rolling lookback window"""

        assert window > 0
        assert 0 <= min_window_pct <= 1
        min_periods = FeatureTransform._get_min_periods_length(window, min_window_pct)

        return_series = security_series.pct_change(1).rolling(window, min_periods=min_periods)
        benchmark_return_series = benchmark_series.pct_change(1).rolling(window, min_periods=min_periods)
        
        # Beta = Cov(R_p, R_m) / Var(R_m) where R_p is portfolio return, R_m is market (benchmark) return
        betas = return_series.cov(benchmark_return_series) / benchmark_return_series.var()
        return betas

    @staticmethod
    def rolling_zscore(
        data: pd.DataFrame, window: int, min_window_pct=0.8, group_column='ticker', inplace=True
    ) -> pd.DataFrame:
        """Compute a rolling window Z score grouped by some column.

        Args:
            data (pd.DataFrame): _description_
            window (int): _description_
            min_window_pct (float, optional): _description_. Defaults to 0.8.
            group_column (str, optional): _description_. Defaults to 'ticker'.
            inplace (bool, optional): _description_. Defaults to True.

        Returns:
            pd.DataFrame: _description_
        """
        assert window > 0
        assert 0 <= min_window_pct <= 1
        min_periods = FeatureTransform._get_min_periods_length(window, min_window_pct)
        if not inplace:
            data = data.copy()

        # TODO: group by 'ticker', apply a rolling Z score for each ticker
        pass

    @staticmethod
    def cross_sectional_zscore(
        data: pd.DataFrame, min_window_pct=0.8, inplace=True
    ) -> pd.DataFrame:
        """Compute the cross-sectional Z score grouped by the dataframe index.

        Args:
            data (pd.DataFrame): _description_
            min_window_pct (float, optional): _description_. Defaults to 0.8.
            inplace (bool, optional): _description_. Defaults to True.

        Returns:
            pd.DataFrame: _description_
        """
        assert 0 <= min_window_pct <= 1
        if not inplace:
            data = data.copy()

        # TODO: group by 'ticker', apply a rolling Z score for each ticker
        pass
    
    ############################################
    # Private Methods
    ############################################

    @staticmethod
    def _get_min_periods_length(window: int, min_window_pct: float) -> int:
        """Gets the minimum period required for a rolling window."""
        return int(math.ceil(window * min_window_pct))

