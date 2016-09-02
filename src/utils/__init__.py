
import config


#  _
# | |
# | |      ___    __ _   __ _   ___  _ __
# | |     / _ \  / _` | / _` | / _ \| '__|
# | |____| (_) || (_| || (_| ||  __/| |
# \_____/ \___/  \__, | \__, | \___||_|
#                 __/ |  __/ |
#                |___/  |___/

import logging
from logging.config import dictConfig

dictConfig(config.log)
logger = logging.getLogger()


#  _____                      _
# /  __ \                    | |
# | /  \/ _ __  _   _  _ __  | |_   ___
# | |    | '__|| | | || '_ \ | __| / _ \
# | \__/\| |   | |_| || |_) || |_ | (_) |
#  \____/|_|    \__, || .__/  \__| \___/
#                __/ || |
#               |___/ |_|

# from cryptography.fernet import Fernet
# f = Fernet(config.SECRET_KEY)

# def encrypt(string):
#     return f.encrypt(string)

# def decrypt(token):
#     return f.decrypt(token)
