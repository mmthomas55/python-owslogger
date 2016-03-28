from datetime import datetime
from flask import Flask
from flask import g
from unittest.mock import Mock
from unittest.mock import patch
import logging
import pytest
import uuid

from sample import app
from owslogger import flask_logger



def test_setting_up_flask_app():
    """Test setting up a flask application.
    """

    app = Flask(__name__)
    flask_logger.setup(
        app, '', 'qa', 'logging', logging.INFO, 'service',  '1.0.0')


def test_setting_up_flask_app_with_excluded_paths(monkeypatch):
    """Test setting up a flask application.
    """

    app = Flask(__name__)
    monkeypatch.setattr(flask_logger, 'global_logger', Mock())

    flask_logger.setup(
        app, '', 'qa', 'logging', logging.INFO, 'service',  '1.0.0',
        exclude_paths=['/hello/'])

    with app.test_request_context('/hello/'):
        g.log = Mock()
        app.global_correlation_id()
        assert not g.log.info.called


def test_app_correlation_id_creation(monkeypatch):
    """Test creation of the correlation id.
    """

    monkeypatch.setattr(flask_logger, 'global_logger', Mock())
    with app.test_request_context('/hello/'):
        g.log = Mock()
        app.global_correlation_id()
        assert g.correlation_id
        assert g.log.info.called


def test_app_correlation_id_reuse():
    """Test correlation id reuse.

    When passed from the header, the correlation id should be reused.
    """

    correlation_id = str(uuid.uuid1())
    with app.test_request_context(
            '/hello/', headers={'Correlation-Id': correlation_id}):
        app.global_correlation_id()
        assert g.correlation_id == correlation_id


def test_logger_creation():
    """Test creation of the logger.
    """

    with app.test_request_context('/hello/'):
        app.global_logger()
        assert g.correlation_id
        assert isinstance(g.log, logging.LoggerAdapter)
        assert 'correlation_id' in g.log.extra
        assert g.log.extra.get('correlation_id') == g.correlation_id
