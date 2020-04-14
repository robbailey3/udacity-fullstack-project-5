export FLASK_APP="./app.py"
export FLASK_ENV=development
export DATABASE_URL="postgres://postgres:password@localhost:5432/capstone"
export AUTH0_DOMAIN="fsnd-capstone.eu.auth0.com"
export API_AUDIENCE="FSND-Capstone-API"
pip install -r requirements.txt;
flask run --reload