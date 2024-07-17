# Trending YouTube Videos Data Processing Pipeline

  

This project implements a Trending YouTube videos data processing pipeline using FastAPI, SQLAlchemy, and asyncio. It ingests YouTube videos data from a CSV file, profiles the data, stores it in a SQLite database, and provides an API to query video statistics, also handling event management and data movement to object store and key-value store.

  

## Features

  

- Data ingestion and profiling

- Data storage using SQLAlchemy

- API development with FastAPI

- Asynchronous event management

- Data movement to object store and key-value store

  

## File Structure

  

-  `app/`: Contains the main application code.

-  `routers/`: Contains api endpoints functions.

-  `scripts/`: Contains scripts for data ingestion.

-  `config/`: Configuration files.

-  `data/`: Directory for storing the dataset.

-  `requirements.txt`: List of Python dependencies.

-  `README.md`: Project documentation.

  

## Setup and Usage

  

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```
  

2. Data ingestion: parsing, profiling, formatting and storing in Database:

```bash
python scripts/data_ingestion.py
```
the above creates _youtube_videos.db_ at root level and stores the videos profiles data
```bash
python scripts/verify_data.py
```
this is to verify the above data ingestion, prints first 10 video profiles


3. FastAPI endpoints: to fetch videos based on video_id
da
```bash
python -m app.main
```
Swagger UI: Open http://localhost:8000/docs to see the organized endpoints.

4. Asynchronous Events:
_fetch_trending_video_ async function is created on startup and this will prints the most trending video every 30 sec

5. Data mover: to Object Store and Redis (key-value storage):
```bash
python  -m  app.data_mover
``` 	
this creates local Object store which stores description of the video and add data to redis with key as video_id & value as video profile stats
Steps to check this: 
```bash
for redis: to check execute below commands
redis-cli
GET video_metadata:example_video_id

for local object store: 
ls object_store/
cat object_store/example_video_id.txt
```


