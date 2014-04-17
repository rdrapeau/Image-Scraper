import time
import os.path
import datetime


def get_modified_date(file_path):
    return time.ctime(os.path.getmtime(file_path))


def modified_recently(file_path, allowed_margin):
    margin = datetime.timedelta(days=allowed_margin)
    today = datetime.date.today()

    modified = get_modified_date(file_path).split(' ')
    modified = ' '.join(modified[:3]) + ' ' + modified[4]

    modified_date = datetime.datetime.strptime(modified, "%a %b %d %Y").date()

    return today - margin <= modified_date <= today + margin


def modified(date_modified, allowed_margin):
    margin = datetime.timedelta(days=allowed_margin)
    today = datetime.date.today()

    modified_date = datetime.datetime.strptime(date_modified, "%a, %d %b %Y %H:%M:%S %Z").date()
    return today - margin <= modified_date <= today + margin
