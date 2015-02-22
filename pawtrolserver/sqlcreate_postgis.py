import os

# It isn't possible to do this as a management command because one of the settings
# is causing Django to check the database before execution

print "CREATE USER {} WITH ENCRYPTED PASSWORD '{}' CREATEDB;".format(os.getenv('DB_USER'), os.getenv('DB_PASS'))
print "CREATE DATABASE {} WITH ENCODING 'UTF-8' OWNER '{}';".format(os.getenv('DB_NAME'), os.getenv('DB_USER'))
print "GRANT ALL PRIVILEGES ON DATABASE {} TO {};".format(os.getenv('DB_NAME'), os.getenv('DB_USER'))
print "CREATE EXTENSION postgis;"
print "CREATE EXTENSION postgis_topology;"
