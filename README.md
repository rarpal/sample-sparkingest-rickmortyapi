# Sample PySpark ETL pipeline for REST API data source with pagination

## Credits
The ingesting data from a REST API is based on the method demostrated in the repo https://github.com/jamesshocking/Spark-REST-API-UDF.git where the API call is integrated into the dataframe via a UDF which has the potiential benefit of making full use of workers on the distributed architecture of Spark as it was inteded to be used rather than running entirely on a driver.

In this sample project I have slightly extended this technique by adding pagination to the calling API. This is a neccesarry addition as most producition API's has a upper limit on the data payload being sent over the internet and provides a facility to itteratively call additional pages until all data is extracted. This sample makes use of the Rick & Morty REST API to demonstrate this feature.

## Project Structure
The project is structured to allow running ad-hoc scripts like notebooks as well as enabling for DevOps CI/CD integration with modularised python folders and files. 
