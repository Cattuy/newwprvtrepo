from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5097632527:AAEyKN7goIl0lupYgQVqJJH1ghg4fT6wdk0")
API_ID = int(getenv("API_ID", "8192152"))
API_HASH = getenv("API_HASH", "2931e14598cd0f0763236bc84ee4bd6d")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://guri:guri@cluster0.8ega1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5034422341").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5034422341").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001686049931"))
MUSIC_BOT_NAME = getenv("Romeo")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Shailendra34/Hero-OP"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
