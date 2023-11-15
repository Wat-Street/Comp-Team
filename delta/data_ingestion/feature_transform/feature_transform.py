import pandas as pd

class FeatureTransform:

    def rolling_beta(
        return_series: pd.Series, benchmark_return_series: pd.Series, window: int
    ) -> pd.Series:
        pass

    def rolling_z_score(
        data: pd.DataFrame, axis: int
    ) -> pd.DataFrame:
        pass
