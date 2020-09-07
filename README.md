# flask_vue_boilerplate

This is an example layout for a web application using Flask and Vue.
`api` Flask
`src` Vue


## Prerequisites
```
python3.7 
npm
pipenv
sqllite3
```

## Project setup
```
pipenv install
npm install
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
`npm run serve` starts Vue server
`flask run` starts Flask api
