
<div align="center"><font size="35">Docker Cheat Sheet</font></div>

- [1: Process Management](#1-process-management)
- [2: Images/Repository](#2-imagesrepository)
- [3: Volumes & Ports](#3-volumes--ports)
- [4: Troubleshooting(故障排除)](#4-troubleshooting故障排除)
- [5: Docker Compose](#5-docker-compose)

# 1: Process Management

```bash
# Show all running docker containers
docker ps
# Show all docker containers
docker ps -a
# Run a container
docker run <image>:<tag>
# Run a container and connect to it
docker run -it <image>:<tag>
# Run a container in the background
docker run -d <image>:<tag>
# Stop a container
docker stop <container>
# Kill a container
docker kill <container>
```

# 2: Images/Repository

```bash
# List available local images
docker images
# Search for docker images
docker search <image>
# Pull a docker image
docker pull <image>
# Build an image with a dockerfile
docker build -t <image>:<tag> <run_directory> -f <dockerfile>
# Login to a remote repository
docker login <repository>
# Push an image to your remotee repository
docker push <image>:<tag>
# Remove a local docker image
docker rmi <image>:<tag>
# Show metadata for an image
docker inspect <image>
# Remove all unused docker images
docker image prune
```

# 3: Volumes & Ports

```bash
# List volumes
docker volume ls
# Create a volume
docker volume create <volume>
# Delete a volume
docker volume rm <volume>
# Show volume metadata
docker volume inspect <volume>
# Delete all volumes not attached to a container
docker volume prune
# Mount a local directory to your container
docker run -v <local_dir>:<container_dir> <image>
# Copy file or folder from a docker container to host machine
docker cp <container>:<container_dir> <local_dir>
# Copy file or folder from local machine onto a container
docker cp <local_dir> <container>:<container_dir>
# Map a local port to a docker instance
docker run -d -p 127.0.0.1:<local_port>:<docker_port> <image>
# List the ports a docker container is running on
docker port <container>
```

# 4: Troubleshooting(故障排除)

```bash
# Show the logs of a container
docker logs <container>
# Follow/tail the logs of a container
docker logs -f <container>
# Show timestamps on docker logs
docker logs -t <container>
# Show details/metadata of a container
docker inspect <container>
# Show a 'top' view of processes running on a container
docker top <container>
# Show a 'top' view of all docker containers
docker stats
# Show any files that have changed since startup
docker diff <container>
# Connect to an already running container
docker attach <container>
# Execute a command on a container
docker exec -it <container_id> /bin/bash
# Show docker system wide information
docker system info
# Show docker disk space used
docker system df
```

# 5: Docker Compose

```bash
# Start your docker-compose defined resources in detached mode
docker-compose up -d -f <docker_compose_yaml>
# Stop all docker-compose resources
docker-compose stop
# Destroy all docker-compose resources
docker-compose down
# Show docker-compose processes
docker-compose ps
# Show docker-compose logs
docker-compose logs
# Show docker-compose resource consumption
docker-compose top
```
