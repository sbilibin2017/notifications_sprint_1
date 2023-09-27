tests

up-dev
	docker compose -f docker-compose.yml --env_file .env.dev up --build

down-dev
	docker compose -f docker-compose.yml --env_file .env.dev stop
	docker container prune 
	docker volume rm db_volume cache_volume 

up-prod
	docker compose -f docker-compose.yml --env_file .env.prod up --build

down-prod
	docker compose -f docker-compose.yml --env_file .env.prod stop