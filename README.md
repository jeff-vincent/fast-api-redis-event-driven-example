# fast-api-redis-event-driven-example

## Run in Docker-Compose
```shell
docker-compose -f docker_compose.yml up --build
```

## Run in Minikube
```shell
minikube start
minikube addons enable kong
minikube tunnel
```
In a second terminal, from the `k8s` directory:
```shell
helm template . --values values.yaml | kubectl apply -f -
```

## Run in Velocity
From the `k8s` directory, run:
```shell
helm template . --values velocity-values.yml | veloctl env creat -f -
```
