"""
"""

from common.platform import start_spark
import extract.character
import extract.episode
import extract.location

def main():
    """Main ETL script definition.

    :return: None
    """
    # start Spark application and get Spark session, logger and config
    spark, log, config = start_spark(
        app_name='rickandmorty_etl_job',
        files=['configs/etl_config.json'])

    # log that main ETL job is starting
    log.warn('etl_job is up-and-running')

    extract.character.extract_data(spark)
    extract.episode.extract_data(spark)
    extract.location.extract_data(spark)
