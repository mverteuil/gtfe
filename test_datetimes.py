from datetime import datetime
import time

from dateutil import tz
import pytest

import gtfe


def almost_equal(left, right, threshold=10):
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


    def test_tz_aware_now(self):
        """ Should respect timezone awareness, producing the seconds since the epoch. """
        expected_epoch_now = round(time.time())
        actual_epoch_now = gtfe.get_epoch_for_datetime_tz(self.tz_aware_now)
        valid = almost_equal(expected_epoch_now, actual_epoch_now)
        assert valid, (expected_epoch_now, actual_epoch_now)

    def test_tz_naive_now(self):
        """ Should respect timezone naiveness, producing the seconds since the epoch. """
        expected_epoch_now = round(time.time())
        actual_epoch_now = gtfe.get_epoch_for_datetime(self.tz_naive_now)
        valid = almost_equal(expected_epoch_now, actual_epoch_now)
        assert valid, (expected_epoch_now, actual_epoch_now)

    def test_tz_aware_utc_epoch_start(self):
        """ Should respect timezone awareness, producing the seconds since the epoch. """
        expected_epoch_start = 0
        actual_epoch_start = gtfe.get_epoch_for_datetime_tz(self.tz_aware_utc_epoch_start)
        valid = almost_equal(expected_epoch_start, actual_epoch_start)
        assert valid, (expected_epoch_start, actual_epoch_start)

    def test_tz_naive_epoch_start(self):
        """ Should respect timezone naiveness, producing the seconds since the epoch. """
        expected_epoch_start = 0
        actual_epoch_start = gtfe.get_epoch_for_datetime(self.tz_naive_local_epoch_start)
        valid = almost_equal(expected_epoch_start, actual_epoch_start)
        assert valid, (expected_epoch_start, actual_epoch_start)

    def test_tz_naive_with_tz_aware_dispatch(self):
        """ Should raise an assertion error if using naive datetimes with tz aware version. """
        with pytest.raises(ValueError):
            gtfe.get_epoch_for_datetime_tz(self.tz_naive_now)
