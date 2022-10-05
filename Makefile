docker-backend:
	- docker stop duplicati_dashboard_backend
	- docker rm duplicati_dashboard_backend
	docker build -f docker/Backend -t ghcr.io/marcorfilacarreras/duplicati-dashboard:backend .

docker-frontend:
	- docker stop duplicati_dashboard_frontend
	- docker rm duplicati_dashboard_frontend
	docker build -f docker/Frontend -t ghcr.io/marcorfilacarreras/duplicati-dashboard:frontend .

docker-test: docker-backend docker-frontend
	- docker stop duplicati_dashboard_database
	- docker rm duplicati_dashboard_database
	docker-compose -f docker/docker-compose.yml up -d