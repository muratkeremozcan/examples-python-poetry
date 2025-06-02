import pandas as pd
import pytest

# Fixture to read the dataframe
@pytest.fixture
def get_df():
    return pd.read_csv('https://assets.datacamp.com/production/repositories/6253/datasets/757c6cb769f7effc5f5496050ea4d73e4586c2dd/laptops_train.csv')

# verify the type of the object returned from get_df equals pd.DataFrame.
def test_get_df(get_df):
	assert isinstance(get_df, pd.DataFrame)

  # check the number of rows
	assert len(get_df) > 0
