#!/bin/sh

# wait-for-db.sh

set -e

# Parse the DATABASE_URL to extract the host and port
host="$(echo $DATABASE_URL | awk -F[@:/]+ '{print $4}')"
port="$(echo $DATABASE_URL | awk -F[@:/]+ '{print $5}')"

# Wait until PostgreSQL is ready
until nc -z "$host" "$port"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"

