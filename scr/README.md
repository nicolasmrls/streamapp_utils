# streamapp

Base modules to use in a Streamlit project.

- Snowflake connection with templates
- Cards generator for landing page
- Environment selector if needed
- Auth module to login users and grant roles
- Report generator for .xlsx files and templates
- Request handler to integrate with .secrets
- Subpages selector

## Requirements

```
streamlit>=1.30.0
streamlit-authenticator==0.2.2
snowflake-connector-python>=3.0.4
openpyxl==3.1.2
pydantic>=2.5.3
```

# Secrets file
```
# environment variables
key = streamlit cookies key for auth module
snow_key = key for hased snowflake password with Fernet
queries_path = 'static/queries'  # your folder queries path
utils_files = 'static/consume'  # your static files path
admin_contact = 'admin@admin.com'  # show contact if something went wrong
dev = false  # sert true to see a detailed error in development
allowed_roles = ['analysts', 'support', 'guess', 'admin']  # roles for UI interface

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

# if you prefer user credentials in an Mongo DDBB
[mongo_auth]
host = 'localhost'
port = 27017
username = 'root'
password = 'example'

[auth_cookie]
cookie_name = 'cookie'
cookie_key = 'INTJB0EvLz1PzeEVp...'
cookie_expiry_days = 1

[ENVIRONMENTS]
name.image = ''  # Some image to show for the environment
name.url = 'https://pokeapi.co'  # host url for request with different environments  

[REQUESTS]
get_pockemon.url = '/api/v2/berry/'
get_pockemon.method = 'get'
```

### Generate Passwords
To generate passwords use `Hasher` from `streamlit_authenticator`
```Hasher([password]).generate()[0]```
