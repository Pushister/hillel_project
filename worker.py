import os
from celery import Celery
import datetime
import models_db
import al_db
from sqlalchemy import select
from sqlalchemy.orm import Session

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('worker', broker='pyamqp://guest@rabbitmq_container//')


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, add.s(x = 2,  y = 4), name='10 seconds')


@app.task
def add(x, y):
    print(x+y)
    record1 = models_db.User(bank='www', currency='GPB', date_exchange='2020-02-01', buy_rate=1.05, sale_rate=0.95)
    with Session(al_db.engine) as session:
        session.add(record1)
        session.commit()
    return x + y