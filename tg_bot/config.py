from tg_bot.sample_config import Config


class Development(Config):
    LOGGER = True

    # REQUIRED
    API_KEY = "2136337423:AAHVTeCTKr0dnZrI93LFFB0FC8aVk9W2xW0"
    OWNER_ID = "998104621"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "luisx_garcia"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://bnbwczffbraxvq:59952a8f46a223204c4733e3fda4533a630714ead91166ea17dd4ee8b30c040e@ec2-54-211-159-145.compute-1.amazonaws.com:5432/dchs2a888akfmv'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False
