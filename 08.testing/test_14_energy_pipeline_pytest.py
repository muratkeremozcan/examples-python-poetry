import pytest
import pandas as pd

DF_PATH = 'https://assets.datacamp.com/production/repositories/6253/datasets/f015ac99df614ada3ef5e011c168054ca369d23b/energy_truncated.csv'

def get_data():
    return pd.read_csv(DF_PATH)

# finds the minimum value in that column
# returns the index label of the first row where that minimum value appears
def min_country(df):
    return df['VALUE'].idxmin()

@pytest.fixture
def setup_data():
    df = get_data()
    df.drop('previousYearToDate', axis=1, inplace=True)
    df = df.groupby('COUNTRY').agg({'VALUE': 'sum'})
    yield df
    # Teardown
    df.drop(df.index, inplace=True)

def test_NAs(setup_data):
    # Check the number of nulls in the entire DataFrame
    assert setup_data.isna().sum().sum() == 0

def test_argmax(setup_data):
    # Check that min_country returns a string
    assert isinstance(min_country(setup_data), str)
