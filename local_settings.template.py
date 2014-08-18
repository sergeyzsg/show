DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "282c20c4-521b-4e16-82b5-cc8f3d24242f7550472f-606c-45b2-a2d2-c54f041cb600398ea041-7386-46c4-805f-955e94291aff"
NEVERCACHE_KEY = "b90915ba-489c-4829-8571-d2ebc5c6889761770c3e-5338-4458-8571-df1bb9b148561c8758d7-f151-4a13-b5b3-17793bf292c2"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
