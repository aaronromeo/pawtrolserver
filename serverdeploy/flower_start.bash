#!/bin/bash

source /data/venv_pawtrolserver/pawtrolserver/serverdeploy/vars.secure

/data/venv_pawtrolserver/bin/celery -A pawtrolserver flower -l info basic_auth=$PAWTROLSERVER_FLOWER_USER:$PAWTROLSERVER_FLOWER_PASSWORD
