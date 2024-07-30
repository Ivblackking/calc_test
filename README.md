# Pension calculator
This sample application is a calculator for calculating your future pension in Ukraine.

## Run the application with Docker

### Requirements
- Docker (you can install it using the link: https://docs.docker.com/engine/install/).
- Git, to clone this repository (https://git-scm.com/downloads).

### Setup
1. Clone this repository: `git clone https://github.com/Ivblackking/calc_test.git` .
   
2. In the repo directory create a `.env` file. Use the next template:
   ```
   #PostgreSQL settings
    CALC_DB_NAME="dbname"
    CALC_DB_USER="dbuser"
    CALC_DB_PASSWORD="dbpassword"
    CALC_DB_HOST="db"
    CALC_DB_PORT="5432"
    
    #PgAdmin settings
    PGADMIN_DEFAULT_EMAIL="example@mail.com"
    PGADMIN_DEFAULT_PASSWORD="password"
    PGADMIN_PORT="8080"
    
    #Django settings
    INTERFACE_SECRET_KEY='interface-secret'
    CALC_SECRET_KEY='calc-secret'
   ``` 
3. Run a terminal in the repo directory. In the terminal run the next command:<br />
   `docker-compose up -d`.<br />
   Ensure that all containers have started successfully.
   
4. Once all containers are running, run the next command:<br />
   `docker exec -it calc bash`.<br />

5. In the oppened bash of the container 'calc', run the command:<br />
   `python engine/scripts.py`<br />
   to fill the postgres db by required coefficients. These coefficients will be used to calculate the pension.<br />
   After that type `exit` to exit the bash.
   
6. Now you can use the app by following the link: http://localhost:8000 .

## Usage
To calculate future pension just enter/change some parameters in the form in the left column of the page. The result will appear in the right box.
Also try to change width of the browser window and see how it works for small screens like smartphone or tablet.

<img alt="Computer screen" src="https://www.dropbox.com/scl/fi/zgiqbs72nihtcs67gs5vj/screen1.png?rlkey=puqih6hlqcu0boz9hi2citev9&st=clcjha7s&raw=1" width="75%">

<img alt="Small screen" src="https://www.dropbox.com/scl/fi/lxsheyo8hgnahzujg0rp6/screen2.png?rlkey=u1yuetjoxh5ngs759k7hp8efb&st=1njwmjrg&raw=1" width="35%">
