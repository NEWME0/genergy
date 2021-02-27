
# Installation

`python manage.py migrate` - create database tables \
`python manage.py loaddata dumpdata.json` - load default fixture \
`python manage.py runserver --settings=config.settings.development` - run application


# API

| Path                         | Methods          | Description                                         |
| -----------------------------|------------------|-----------------------------------------------------|
| /admin/                      | GET              | Login admin site                                    |
| /accounts/users/             | GET, POST        | User list or create                                 |
| /accounts/users/<int:pk>/    | GET, PUT, DELETE | User retrieve, update or delete                     |
| /accounts/users/me/          | GET              | User retrieve current                               |
| /entities/items/             | GET, POST        | Material list or create                             |
| /entities/items/<int:pk>/    | GET, POST        | Material retrieve, update or delete                 |
| /entities/utils/             | GET, POST        | Instrument list or create                           |
| /entities/utils/<int:pk>/    | GET, POST        | Instrument retrieve, update or delete               |
| /entities/works/             | GET, POST        | Work list or create                                 |
| /entities/works/<int:pk>/    | GET, POST        | Work retrieve, update or delete                     |


