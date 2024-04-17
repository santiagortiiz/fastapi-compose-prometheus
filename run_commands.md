# Reachable endpoint
http://localhost/docs

# Build the image
docker build -t api .
docker build -t api --no-cache .
docker build -t api:test --no-cache .

# Check installation
winpty docker run --rm -it api
winpty docker run --rm --name api -it -p 80:80 api

# Push to the community
docker login community.opengroup.org:5555
docker build -t community.opengroup.org:5555/osdu/platform/system/project-and-workflow .
docker push community.opengroup.org:5555/osdu/platform/system/project-and-workflow

# compose
docker compose up -d
winpty docker exec -it api bash

# compose development
docker compose watch

# Uvicorn
uvicorn app.main:app --reload
uvicorn app.main:app --port 80 --reload


# Deploy with Ngrok
docker run --rm -it -e NGROK_AUTHTOKEN=23h0EkmxfU6nTw1PcfRJopWczdu_2iT6DmA3JoFCgXt1eVsos ngrok/ngrok http 80
