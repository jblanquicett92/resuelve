export DB_HOST=db
export DB_NAME=app
export DB_USER=postgres
export DB_PASS=supersecretpassword

export POSTGRES_DB=app
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=supersecretpassword

export PGADMIN_DEFAULT_EMAIL=root@root.com
export PGADMIN_DEFAULT_PASSWORD=root

printenv | grep DB_
printenv | grep POSTGRES_
printenv | grep PGADMIN_

docker-compose build
docker-compose up
