pwd:
	@echo "Building the PWA image and creating the container"
	docker build -f PWD . -t ghcr.io/marcorfilacarreras/duplicati-dashboard:pwd
	docker push ghcr.io/marcorfilacarreras/duplicati-dashboard:pwd
	@echo "Finish"

push:
	@echo "Pushing the code and the image"
	git add .
	git commit -m "$(version)"
	git push
	@echo "Finish"