Install dependencies:

pip install flask
pip install flask-cors
pip install psycopg2-binary
pip install python-dotenv
pip install bcrypt
pip install pyjwt
pip install pytesseract pillow

to start the database use this command:

docker compose up -d

to stop the db:

docker compose down

database migration:

docker exec -i finance_tracker_db psql -U postgres -d finance_tracker < app/db/migrations/001_create_users.sql

docker exec -i finance_tracker_db psql -U postgres -d finance_tracker < app/db/migrations/002_create_expenses.sql