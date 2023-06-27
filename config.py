from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH" "670deb1f30b648fbb4f744e406161942")
      API_ID = int(getenv("API_ID", "13984519"))      
      BOT_TOKEN = getenv("BOT_TOKEN", "6210597044:AAHMJw2jiROeZ9F0ZI26LX1QjgTD7IvONfM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001612590180").replace("\n"," -1001807370305").split(' '))
