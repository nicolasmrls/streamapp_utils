# streamapp

Base modules to use in a Streamlit project

- Snowflake connection with templates
- Cards generator for landing page
- Country selector if needed
- Auth module to login users and grant roles
- Report generator for .xlsx files and templates

## Requirements

```
streamlit>=1.30.0
streamlit-authenticator==0.2.2
snowflake-connector-python>=3.0.4
openpyxl==3.1.2
pydantic>=2.6.2
```

# secrests file
```
# enviroment variables
key = key for hased passwords with Fernet
queries_path = 'static/queries' # your folder queries path
utils_files = 'static/consume' # your static files path

# snowflake credentials
# see snowflake documentation
[SNOW_SERVER]
account = '************'
database = '*********'
warehouse = '******'
role = '*********'
user = '**********'
password = '***********'

# see streamlit authenticator documentation
[credentials.usernames]
Pepe.name = '**********'
Pepe.roles = ['admin', 'dev', 'other]
Pepe.password = 'password hash' 

[REQUESTS]
get_pockemon.url = 'https://pokeapi.co/api/v2/berry/'
get_pockemon.method = 'get'
```