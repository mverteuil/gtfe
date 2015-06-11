from email import utils as emailutils
import time


RFC2822_FORMAT = '%a, %d %b %Y %T %z'


def get_epoch_for_datetime(datetime):
    """ Given a datetime-like object, calculates the number of seconds that have elapsed since the Unix epoch. """
    rfc2822_formatted_date = datetime.strftime(RFC2822_FORMAT)
    time_tuple = emailutils.parsedate(rfc2822_formatted_date)
    return time.mktime(time_tuple)


def get_epoch_for_datetime_tz(datetime):
    """ Given a timezone aware datetime-like object, calculates the number of seconds that have elapsed since the Unix epoch. """
    rfc2822_formatted_date = datetime.strftime(RFC2822_FORMAT)
    time_tuple = emailutils.parsedate_tz(rfc2822_formatted_date)
    return emailutils.mktime_tz(time_tuple)
