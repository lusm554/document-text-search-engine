#!/bin/bash
docker pull swaggerapi/swagger-editor
docker run -p 8080:8080 -d swaggerapi/swagger-editor 
