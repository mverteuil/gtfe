from datetime import datetime
import time

from dateutil import tz

import gtfe


def almost_equal(left, right, threshold=10):
    """ Determines if the values given are within the threshold distance of each other. """
    return abs(left - right) < threshold


class TestDatetimes(object):
    """ Exercises general cases of using datetimes with GTFE. """
    def setup(self):
        """ Prepares several use cases of datetime for exercising the module. """
        self.tz_aware_now = datetime.now().replace(tzinfo=tz.tzlocal())
        self.tz_naive_now = datetime.now()
        self.tz_aware_utc_epoch_start = datetime(1970, 1, 1, 0, 0, 0, 0, tzinfo=tz.tzutc())
        self.tz_aware_local_epoch_start = self.tz_aware_utc_epoch_start.astimezone(tz.tzlocal())
        self.tz_naive_local_epoch_start = self.tz_aware_local_epoch_start.replace(tzinfo=None)
        self.expected_epoch_now = round(time.time())
        self.expected_epoch_start = 0

    def test_aware_now(self):
        """ Should respect timezone awareness, producing the seconds since the epoch. """
        actual_epoch_now = gtfe.get_epoch_for_datetime(self.tz_aware_now)
        valid = almost_equal(self.expected_epoch_now, actual_epoch_now)
        assert valid, (self.expected_epoch_now, actual_epoch_now)

    def test_naive_now(self):
        """ Should respect timezone naiveness, producing the seconds since the epoch. """
        actual_epoch_now = gtfe.get_epoch_for_datetime(self.tz_naive_now)
        valid = almost_equal(self.expected_epoch_now, actual_epoch_now)
        assert valid, (self.expected_epoch_now, actual_epoch_now)

    def test_aware_utc_epoch_start(self):
        """ Should respect timezone awareness, producing the seconds since the epoch. """
        actual_epoch_start = gtfe.get_epoch_for_datetime(self.tz_aware_utc_epoch_start)
        valid = almost_equal(self.expected_epoch_start, actual_epoch_start)
        assert valid, (self.expected_epoch_start, actual_epoch_start)

    def test_naive_epoch_start(self):
        """ Should respect timezone naiveness, producing the seconds since the epoch. """
        actual_epoch_start = gtfe.get_epoch_for_datetime(self.tz_naive_local_epoch_start)
        valid = almost_equal(self.expected_epoch_start, actual_epoch_start)
        assert valid, (self.expected_epoch_start, actual_epoch_start)
