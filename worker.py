import os
from celery import Celery
import datetime


rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('worker', broker='pyamqp://guest@rabbitmq_container//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, add.s(x = 2,  y = 4), name='10 seconds')


@app.task
def add(x, y):
    print(x+y)
    with open('test.txt', 'w') as f:
        f.write(f'x+y = {x+y} {datetime.datetime.now()} ')
    return x + y
