import os
"""
Project configuration
"""


class DefaultConfig(object):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SITE_NAME = 'Lord Simeon\'s World of Cylindrical Sandwiches'

    # Secret stuffs
    ADMINS = frozenset(['steve@stevehurwitz.com'])
    SECRET_KEY = '22215a362ed5a586cebebd1cddfcc2e1'

    SQLALCHEMY_DATABASE_URI = 'mysql://lordsimeon:password123@127.0.0.1/lord_simeon'
    SQLALCHEMY_CONNECT_OPTIONS = {}

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'ThisIsSoSuperSecretSHHHHH'

    ASSETS_DEBUG = DEBUG

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')

    UPLOADS_FOLDER = os.path.join(APP_ROOT, 'uploads/')
    UPLOADS_DEFAULT_DEST = UPLOADS_FOLDER

    MEDIA_FOLDER = UPLOADS_FOLDER
    MEDIA_URL = 'uploads/'
    MEDIA_THUMBNAIL_FOLDER = '/'.join([MEDIA_FOLDER, 'cache'])
    MEDIA_THUMBNAIL_URL = 'cache/'
