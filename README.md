Logging
=======

This logger is designed to send JSON to Loggly in a format that matches our
OWS1 standard. This package is published to our internal Pypi server.
Installation is minimal:

```bash
pip install -i https://pypi.theorchard.io/pypi/ owslogger
```

Alternatively, put the following in your requirements file:

```
-i https://pypi.theorchard.io/pypi/

owslogger
```

Setting your flask python application:

```python
from flask import Flask
from owslogger import flask_logger
import logging


app = Flask(__name__)
flask_logger.setup(
    app, 'loggly http/s url', 'environment', 'logger_name', logging.INFO,
    'service_name', '1.0.0')
```

If your application does not use flask, you can use:

```python
from owslogger import logger

# Global logger
app_logger = logger.setup(
    'loggly http/s url', 'environment', 'logger_name', logging.INFO,
    'service_name', '1.0.0')

# Make it specific to a request by creating an adapter and adding the
# correlation id.
current_app_logger = logger.OwsLoggingAdapter(app_logger, {
    'correlation_id': 'correlation_id'
})

# If you just want to set the logger in one time:
current_app_logger = logger.setup(
    'loggly http/s url', 'environment', 'logger_name', logging.INFO,
    'service_name', '1.0.0', correlation_id='correlation_id')
```

# Contributing
Be sure to publish the latest version of this package to Pypi when contributing.
This [Jenkins
job](http://jenkins.theorchard.com:8080/view/pypi/job/publish-pypi-package/)
will bump the version, tag and publish the package to Pypi.
