from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET','Post'])
def index():
    return 'CI/CD Pipeline has been Constructedgi'


if __name__ == "__main__":
    app.run(debug=True)
