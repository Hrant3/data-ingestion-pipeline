Data Ingestion Pipeline

This project sets up a data ingestion pipeline that processes user metrics data and stores it in a PostgreSQL database. The pipeline is implemented using Docker, with containers for the application and the database. The setup is designed for high performance and scalability.


2.Prerequisites
  Docker: Version 20.10.x or later
  
  Docker Compose: Version 1.28.x or later
  
  Git: Version control to clone the repository

3.Setup and Installation  

  1. Clone the repository.
       git clone https://github.com/yourusername/data-ingestion-pipeline.git
       cd data-ingestion-pipeline

  2. Build and Start Containers:
       /usr/lib/docker/cli-plugins/docker-compose up --build (first should be the path where your docker-compose is )

4. Database Schema Explanation
      The database consists of a single table, metrics, with the following columns
        id: Serial primary key.
        timestamp: The time when the metric was recorded.
        user_id: The identifier for the user.
        session_id: The session identifier.
        metric_type: The type of metric (e.g., talked_time,microphone_used,speaker_used).
        metric_value: The value of the metric.
        device_id: The identifier for the user's device.
        app_version: The version of the application.
        location: The location where the metric was recorded.
        sentiment_score: The sentiment score associated with the user’s interaction
    Indices
        Indexes are created on timestamp, user_id, session_id, and metric_type to optimize query performance.
   
    Stored Procedures:
        insert_metric: Procedure to insert a new metric into the metrics table.

5. Running the application
     Start the application by running /usr/lib/docker/cli-plugins/docker-compose up

6.1 Testing the setup
     curl -X POST http://localhost:5000/ingest \
-H "Content-Type: application/json" \
-d '[{
    "timestamp": "2024-08-12T12:00:00+00:00",
    "user_id": "user456",
    "session_id": "session789",
    "metric_type": "microphone_used",
    "metric_value": "1",
    "device_id": "device012",
    "app_version": "1.0.1",
    "location": "Los Angeles",
    "sentiment_score": 0.8
}]'

6.2 We can also test stored procedure where you simply call insert_metric with arguments

    First we need to activate the stored procedure. For that we need to run this command.
    docker exec -it data-ingestion-pipeline-db-1 psql -U user -d metrics_db -f /app/init_db.sql
    This creates the procedure. 
    Then we go to the db shell with this command.
    /usr/lib/docker/cli-plugins/docker-compose exec db psql -U user -d metrics_db
    and run the procedure code

    CALL insert_metric(
    '2024-08-12 12:00:00'::TIMESTAMP,
    'user123'::VARCHAR,
    'session456'::VARCHAR,
    'talked_time'::VARCHAR,
    '300'::VARCHAR,
    'device789'::VARCHAR,
    '1.0.0'::VARCHAR,
    'New York'::VARCHAR,
    0.9::FLOAT
);



    



