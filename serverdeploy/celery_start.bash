#!/bin/bash

source /data/venv_pawtrolserver/pawtrolserver/serverdeploy/vars.secure

/data/venv_pawtrolserver/bin/celery -A pawtrolserver worker -l info --concurrency=1
