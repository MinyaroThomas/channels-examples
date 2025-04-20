INSTALLED_APPS = [
    # ...
    'channels',
    'chat',
    'allauth',
    'allauth.account',
]

ASGI_APPLICATION = 'chat_app.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
