# run container
docker run -p 9090:9090 prom/prometheus

# Reload prometheus config
docker kill -s SIGHUP <container_name>
docker kill -s SIGHUP prometheus

172.24.0.1:55082
