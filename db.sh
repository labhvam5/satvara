# Remove the existing MySQL container if it exists
docker rm -f my_postgres_container 2>/dev/null || tr

docker run -d \
  --name my_postgres_container \
  -e POSTGRES_DB=satvara_db \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -p 5432:5432 \
  postgres:latest
