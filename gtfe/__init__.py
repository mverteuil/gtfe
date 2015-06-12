from email import utils as emailutils
import logging

from dateutil import tz


log = logging.getLogger(__name__)

RFC2822_FORMAT = '%a, %d %b %Y %T %z'


def get_epoch_for_datetime(datetime):
    """ Given a datetime-like object, calculates the number of seconds that have elapsed since the Unix epoch.

    If given a timezone-naive object, it is assumed to be local time.

    """
    if not (datetime.tzinfo):
        log.warning("Received naive datetime-like object. Assuming local time.")
        datetime = datetime.replace(tzinfo=tz.tzlocal())
    rfc2822_formatted_datetime = datetime.strftime(RFC2822_FORMAT)
    time_tuple = emailutils.parsedate_tz(rfc2822_formatted_datetime)
    return emailutils.mktime_tz(time_tuple)
