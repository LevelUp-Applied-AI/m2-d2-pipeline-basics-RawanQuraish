"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # TODO: Create a pd.Series with at least one NaN value
    # TODO: Call clean_column() on it
    # TODO: Assert no NaN values remain in the result
    # TODO: Assert the NaN was filled with the correct median value
    s = pd.Series([1, 2, np.nan, 4])
    cleaned = clean_column(s)
    assert cleaned.isna().sum() == 0 
    expected_median = s.median()
    assert cleaned[2] == expected_median


def test_compute_revenue():
    # TODO: Create two small pd.Series (quantity and price)
    # TODO: Call compute_revenue() on them
    # TODO: Assert the result matches the expected element-wise product
    quantity = pd.Series([2, 5, 3])
    price = pd.Series([10, 7, 4])
    revenue = compute_revenue(quantity, price)
    expected = pd.Series([20, 35, 12])
    pd.testing.assert_series_equal(revenue, expected)
