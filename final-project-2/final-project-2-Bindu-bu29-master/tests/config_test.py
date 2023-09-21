"""Test configurations"""
# project/tests/test_config.py


def test_development_config(application):
    """ Tests development Config"""
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG'], "application config DEBUG is false"
    assert not application.config['TESTING'], "application config TESTING is not false"


def test_testing_config(application):
    """Tests testing Config"""
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG'], "app config DEBUG is false"
    assert application.config['TESTING'], "app config TESTING is false"
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION'], "PRESERVE CONTEXT EXCEPTION"
    # assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'


def test_production_config(application):
    """Tests production Config"""
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG'], "application config DEBUG is not false"
    assert not application.config['TESTING'], "application config TESTING is not false"
