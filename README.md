Data Ingestion Pipeline

This project sets up a data ingestion pipeline that processes user metrics data and stores it in a PostgreSQL database. The pipeline is implemented using Docker, with containers for the application and the database. The setup is designed for high performance and scalability.


2.Prerequisites

  Docker: Version 20.10.x or later
  
  Docker Compose: Version 1.28.x or later
  
  Git: Version control to clone the repository

3.Setup and Installation  

  1. Clone the repository.
     
       ```git clone https://github.com/Hrant3/data-ingestion-pipeline.git```

       ```cd data-ingestion-pipeline```

  3. Build and Start Containers:
     
       ```/usr/lib/docker/cli-plugins/docker-compose up --build```   (first should be the path where your docker-compose is )

5. Database Schema Explanation
   
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

7. Running the application
   
     Start the application by running ```/usr/lib/docker/cli-plugins/docker-compose up```

6.1 ## Testing the setup


You can test the data ingestion by sending a `POST` request to the `/ingest` endpoint:

```bash
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


### 6.2 Testing the Stored Procedure

You can test the stored procedure by following these steps:

1. **Activate the Stored Procedure**:
    - Run the following command to create the procedure:
    
    ```bash
    docker exec -it data-ingestion-pipeline-db-1 psql -U user -d metrics_db -f /app/init_db.sql
    ```

2. **Access the Database Shell**:
    - Use this command to access the database shell:
    
    ```bash
    /usr/lib/docker/cli-plugins/docker-compose exec db psql -U user -d metrics_db
    ```

3. **Run the Stored Procedure**:
    - Once inside the database shell, execute the following command to call the `insert_metric` procedure:
    
    ```sql
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
    ```

This will insert a new metric into the `metrics` table.


7. Maintaining and Extending the Pipeline
      Adding new metrics. Update the `metrics` table schema if new types of metrics are introduced.
        

      Scaling. Adjust Docker Compose settings to increase number of containers
            Docker allows us to to scale services by specifying number of container instances we want to run. For
            example, if our application is under heavy load , we can run multiple instances of the same service.
            ``` docker-compose up --scale app=3 ``` -  Using this command we can start three instances
            of the  ```app``` service , allowing to handle more requests simultaneously.

      Load Balancer.
            When we scale by adding more containers, we might need to add a load balancer to distribute traffic

            evenly among the containers.

8. Assumptions

      The application ensures that input data is correctly formatted.
      The database credentials are stored securely in environment variables.

9. Limitations

      Error handling and validation are minimal

10. Future improvements

      Implement authentication and authorization.

      Add data validation and error handling.

      Scale the application using Kubernetes.









    



