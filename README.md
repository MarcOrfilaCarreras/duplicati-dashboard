<div align="center">

[![License](https://img.shields.io/github/license/MarcOrfilaCarreras/duplicati-dashboard?style=flat)](https://github.com/MarcOrfilaCarreras/duplicati-dashboard) &nbsp; ![Docker](https://img.shields.io/github/workflow/status/MarcOrfilaCarreras/duplicati-dashboard/docker?label=docker&style=flat) &nbsp; ![Last commit](https://img.shields.io/github/last-commit/MarcOrfilaCarreras/duplicati-dashboard?style=flat) &nbsp; [![Crowdin](https://badges.crowdin.net/duplicati-dashboard/localized.svg)](https://crowdin.com/project/duplicati-dashboard)

</div>

<div align="center">
    <h1>Duplicati dashboard</h1>
    <h4> A simple DASHBOARD for monitoring you Duplicati instances</h4>
    <a href="https://github.com/MarcOrfilaCarreras/duplicati-dashboard/wiki">Explore the docs</a>
</div>

<br>

## :arrow_right: Getting Started

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

<br>

## :hammer: Roadmap

- [ ] Add historical data
- [ ] Add some charts

See the [open issues](https://github.com/MarcOrfilaCarreras/duplicati-dashboard/issues) for a full list of proposed features (and known issues).

<br>

## :key: License

Distributed under the MIT License. See `LICENSE` for more information.
