from flask import Blueprint, render_template
import requests, json

from src.http.utils import mustBeLoggedIn
from src.utils import logger


defaultBp = Blueprint("default", __name__)

@defaultBp.route("/")
# Following decorator(and more) can be found in src/http/utils/
# @mustBeLoggedIn
def index():
    logger.debug("Into default's index method..")
    return render_template("default/index.html")
