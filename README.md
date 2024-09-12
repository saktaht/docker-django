docker compose up --build --detachの後に次のコマンドを実行する

docker exec -it django /bin/bash

python manage.py makemigrations

python manage.py migrate
