#   ___          _    _      ______                                  _
#  / _ \        | |  | |     |  _  \                                | |
# / /_\ \ _   _ | |_ | |__   | | | |  ___   ___   ___   _ __   __ _ | |_   ___   _ __  ___
# |  _  || | | || __|| '_ \  | | | | / _ \ / __| / _ \ | '__| / _` || __| / _ \ | '__|/ __|
# | | | || |_| || |_ | | | | | |/ / |  __/| (__ | (_) || |   | (_| || |_ | (_) || |   \__ \
# \_| |_/ \__,_| \__||_| |_| |___/   \___| \___| \___/ |_|    \__,_| \__| \___/ |_|   |___/


from flask import session, redirect, url_for
from functools import wraps


def mustBeLoggedIn(func):
    '''
    Redirects to "login" if not logged in already
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not "userId" in session:
            return redirect(url_for("default.login"))
        return func(*args, **kwargs)
    return wrapper


def mustBeLoggedOut(func):
    '''
    Redirects to "index" if logged in already
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "userId" in session:
            return redirect(url_for("default.index"))
        return func(*args, **kwargs)
    return wrapper
