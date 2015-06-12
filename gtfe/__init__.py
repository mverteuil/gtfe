from email import utils as emailutils
import time

from dateutil import tz


RFC2822_FORMAT = '%a, %d %b %Y %T %z'


def get_epoch_for_datetime(datetime):
    """ Given a timezone-naive datetime-like object, calculates the number of seconds that have elapsed since the Unix epoch.

    Assumes that the datetime is in local time.

    """
    timezone_aware_datetime = datetime.replace(tzinfo=tz.tzlocal())
    return get_epoch_for_datetime_tz(timezone_aware_datetime)


def get_epoch_for_datetime_tz(datetime):
    """ Given a timezone aware datetime-like object, calculates the number of seconds that have elapsed since the Unix epoch. """
    if not all((datetime, datetime.tzinfo)):
        raise ValueError("Expected a timezone-aware datetime, received {}.".format(datetime))
    rfc2822_formatted_datetime = datetime.strftime(RFC2822_FORMAT)
    time_tuple = emailutils.parsedate_tz(rfc2822_formatted_datetime)
    return emailutils.mktime_tz(time_tuple)
