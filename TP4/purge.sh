#!/bin/bash
docker rm -f $(docker ps -aq)
docker system prune -af