# flask_vue_boilerplate

This is an example layout for a web application using Flask and Vue.

`api/` Flask

`src/` Vue


## Prerequisites
```
git
npm
python3.7 
pipenv
sqllite3
```

## Project setup
```
git clone https://github.com/rexbrandy/flask-vue-boilerplate.git

cd flask-vue-boilerplate/

pipenv install
npm install

export FLASK_APP='app.py'
```

## Database setup
```
flask db init
flask db migrate
```
To upgrade database with new models
```
flask db upgrade
```

### Run development mode
```
npm run serve # starts Vue server
flask run # starts Flask api
```
