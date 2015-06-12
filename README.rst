installation
------------

`pip install gtfe`

usage
-----

didactic example::

    >>> import time, datetime, gtfe
    >>> time.time(), gtfe.get_epoch_for_datetime(datetime.datetime.now())
    (1434054301.937659, 1434054301.0)

testing
-------

- Clone the repository
- `python setup.py test`
