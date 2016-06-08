import os
import re
import pickle
from rsstory.rss import *
from crontab import CronTab


def setup_cron(fpath, time_between):
    tab = CronTab(user=True)
    cmd = os.path.join(os.getcwd(), 'venv', 'bin', 'python') + ' ' + os.path.join(os.getcwd(), 'rsstory', 'periodic.py') + ' ' + fpath
    cron_job = tab.new(cmd)
    cron_job.every(time_between.days).dom()
    cron_job.comment = 'Job for {} at interval (days) {}'.format(fpath, time_between.days)
    tab.write()

def update_feed(fpath):
    pass # TODO: get it updating the pages regularly using the database store
    # rss_items, url, title = pickle.load(open(fpath, "rb"))
    # page_num = re.findall(r'\d+', fpath)[-1]
    # write_rss(rss_items, url, archive_id=page_num, title=title)

if __name__ == "__main__":
    update_feed(sys.argv[1])
