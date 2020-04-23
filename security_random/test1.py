# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test1.py
# __time__  : 2020/4/23 11:56 AM

import secrets
import random

# from celery.schedules import schedule

import schedule
import time


def myjob():
    print("I'm working...")
    
    return random.randint(1, 10)


# job = schedule.every(2).seconds
# job.job_func = myjob
# schedule.jobs.append(job)
# result = job.run()
res = schedule.every().minute.at(":20").do(myjob)
# print(result)
while True:
    runnable_jobs = (job for job in schedule.jobs if job.should_run)
    for job in sorted(runnable_jobs):
        result = job.run()
        print(result)
    time.sleep(1)
