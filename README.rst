gtfe
----

Get the fucking epoch for a given datetime in python. Holy shit. Why is this so hard?

installation
------------

`pip install gtfe`

usage
-----

```
>>> import time, datetime, gtfe
>>> time.time(), gtfe.get_epoch_for_datetime(datetime.datetime.now())
(1434054301.937659, 1434054301.0)
```

testing
-------

- Clone the repository
- `python setup.py test`
