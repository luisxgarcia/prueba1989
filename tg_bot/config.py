from tg_bot import ALLOW_EXCL, BAN_STICKER, CERT_PATH, DEL_CMDS, DONATION_LINK, PORT, STRICT_GBAN, SUPPORT_USERS, WEBHOOK, WHITELIST_USERS, WORKERS
from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 998104621  # my telegram ID
    OWNER_USERNAME = "luisx_garcia"  # my telegram username
    API_KEY = "2136337423:AAHVTeCTKr0dnZrI93LFFB0FC8aVk9W2xW0"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://buprojwbmxkmcm:fba203f997f6c8103bb1163cc21f92567bf8e61229b3655102229a700cdfcd25@ec2-54-211-159-145.compute-1.amazonaws.com:5432/d14o2otfak99ke'  # sample db credentials
    MESSAGE_DUMP = '-1007777777777' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
