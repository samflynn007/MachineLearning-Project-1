import sys

from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)


@app.route("/", methods=['GET', 'Post'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return 'CI/CD Pipeline has been Constructed'


if __name__ == "__main__":
    app.run(debug=True)
