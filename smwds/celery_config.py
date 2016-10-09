#!/usr/bin/python
#coding:utf-8
from datetime import timedelta
# Celery configuration

BROKER_URL = 'redis://localhost:6379/5'
CELERY_BACKEND = 'redis://localhost:6379/5'
CELERY_TASK_SERIALIZER='json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_RESULT_SERIALIZER='json'

# Celery task to sync between CMDB and monitor DB
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_task.sync_from_influxdb',
        'schedule': timedelta(seconds=30)
    },
}

CELERY_TIMEZONE = 'UTC'