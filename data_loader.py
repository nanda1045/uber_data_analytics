import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://storage.googleapis.com/uber-data-engineering-project-nanda/uber_data.csv'
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text), sep=',')
    print("Data loaded from API.")
    print("Data shape:", df.shape)
    print("Data columns:", df.columns)
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
