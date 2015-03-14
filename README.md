# PawtrolServer

### Setup Notes
This uses [GeoDjango](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/). So setup [POSTGIS](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/#platform-specific-instructions). 
Also required to run locally is a .env file with the following values defined

    export DB_USER=
    export DB_PASS=
    export DB_NAME=

    export DEBUG=1

    export EMAIL_HOST=
    export EMAIL_PORT=
    export EMAIL_HOST_USER=
    export EMAIL_HOST_PASSWORD=

    export BASEURL="http://localhost:8000"

DB creation for maximum awesome...

    CREATE USER [DB_USER] WITH ENCRYPTED PASSWORD '[DB_PASS]' CREATEDB;
    CREATE DATABASE [DB_NAME] WITH ENCODING 'UTF-8' OWNER "[DB_USER]";
    GRANT ALL PRIVILEGES ON DATABASE [DB_NAME] TO [DB_USER];
    \c [DB_NAME];
    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;

OR run `sqlcreate_postgis.py` to get the script.

### Navigating logic
The modules are broken up 

* feedback - All things that pertain to badges and feedback
    * models
        * Badge
    * services
    * tasks
    * serializers
* common
    * models
        * Pet
        * Pack
    * services
    * tasks
* billing
    * models
        * Invoice
* profiles
    * models
        * ProfileBase
        * ServiceProviderProfileBase
        * Owner
        * Walker
    * ..
* petservices
    * models
        * PetWalk
        * Walk
        * Route
        * OnWalkNotification
    * ..
