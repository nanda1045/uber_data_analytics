from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Debugging statement to verify data
    for key,value in data.items():
        table_id = 'uber-data-analytics-431702.uber_DataEngineering_yt.fact_table'
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
    

    

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
