export FLASK_APP="./app.py"
export FLASK_ENV=development
export DB_URL="postgres://postgres:password@localhost:5432"
pip install -r requirements.txt;
flask run --reload