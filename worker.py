from celery import Celery
import datetime


app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    print (x+y)
    with open('test.txt', 'w') as f:
        f.write(f'x+y = {x+y} {datetime.datetime.now()} ')
    return x + y

