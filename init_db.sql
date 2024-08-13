-- init_db.sql
CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    session_id VARCHAR(255) NOT NULL,
    metric_type VARCHAR(50) NOT NULL,
    metric_value VARCHAR(255),
    device_id VARCHAR(255),
    app_version VARCHAR(50),
    location VARCHAR(255),
    sentiment_score NUMERIC
);

CREATE INDEX idx_user_id ON metrics(user_id);
CREATE INDEX idx_session_id ON metrics(session_id);
CREATE INDEX idx_timestamp ON metrics(timestamp);
CREATE INDEX idx_metric_type ON metrics(metric_type);

CREATE OR REPLACE PROCEDURE insert_metric(
    _timestamp TIMESTAMP,
    _user_id VARCHAR,
    _session_id VARCHAR,
    _metric_type VARCHAR,
    _metric_value VARCHAR,
    _device_id VARCHAR,
    _app_version VARCHAR,
    _location VARCHAR,
    _sentiment_score FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO metrics (timestamp, user_id, session_id, metric_type, metric_value, device_id, app_version, location, sentiment_score)
    VALUES (_timestamp, _user_id, _session_id, _metric_type, _metric_value, _device_id, _app_version, _location, _sentiment_score);
END;
$$;
