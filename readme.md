
# Local installation

`python manage.py migrate` - create database tables \
`python manage.py loaddata dumpdata.json` - load default fixture \
`python manage.py runserver --settings=config.settings.development` - run application


# Heroku deployment

Application is deployed on [Heroku](https://genergy-backend.herokuapp.com/). Visit link to access API.


# API

| Path                                  | Methods          | Description                                         |
| --------------------------------------|------------------|-----------------------------------------------------|
| /admin/                               | GET              | Login admin site                                    |
| /accounts/users/                      | GET, POST        | User list or create                                 |
| /accounts/users/<int:pk>/             | GET, PUT, DELETE | User retrieve, update or delete                     |
| /accounts/users/me/                   | GET              | User retrieve current                               |
| /entities/works/                      | GET, POST        | Work list or create                                 |
| /entities/works/<int:pk>/             | GET, PUT, DELETE | Work retrieve, update or delete                     |
| /entities/items/                      | GET, POST        | Material list or create                             |
| /entities/items/<int:pk>/             | GET, PUT, DELETE | Material retrieve, update or delete                 |
| /entities/items/<int:pk>/supply/      | POST             | Supply materials                                    |
| /entities/items/<int:pk>/afford/      | POST             | Afford materials to User                            |
| /entities/utils/                      | GET, POST        | Instrument list or create                           |
| /entities/utils/<int:pk>/             | GET, PUT, DELETE | Instrument retrieve, update or delete               |
| /entities/items/<int:pk>/supply/      | POST             | Supply instruments                                  |
| /entities/items/<int:pk>/afford/      | POST             | Afford instruments to User                          |


