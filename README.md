<h1 align="center">Duplicati dashboard</h1>

<div align="center">

[![License](https://img.shields.io/github/license/MarcOrfilaCarreras/duplicati-dashboard?style=flat)](https://github.com/MarcOrfilaCarreras/duplicati-dashboard) &nbsp; ![Docker](https://img.shields.io/github/workflow/status/MarcOrfilaCarreras/duplicati-dashboard/docker?label=docker&style=flat) &nbsp; ![Last commit](https://img.shields.io/github/last-commit/MarcOrfilaCarreras/duplicati-dashboard?style=flat) &nbsp; [![Crowdin](https://badges.crowdin.net/duplicati-dashboard/localized.svg)](https://crowdin.com/project/duplicati-dashboard)

</div>

## Getting Started

### Installation

The best way to install this software is using Docker.

First, download the backend image from the Github repository.

```
docker pull ghcr.io/marcorfilacarreras/duplicati-dashboard:backend
```

Also, download the frontend image.

```
docker pull ghcr.io/marcorfilacarreras/duplicati-dashboard:frontend
```

Then, you will have to download the [*docker-compose.yml*](https://raw.githubusercontent.com/MarcOrfilaCarreras/duplicati-dashboard/master/docker/docker-compose.yml) file with the following command.

``` bash
wget https://raw.githubusercontent.com/MarcOrfilaCarreras/duplicati-dashboard/master/docker/docker-compose.yml
```

Finally, you will be able to start the containers.

```
docker-compose up -d
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
