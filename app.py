from flask import (
    Flask,
    render_template,
    jsonify,
    redirect,
    request,
    session,
    send_from_directory,
)

import datetime

app = Flask(__name__)


@app.route("/api/<id>")
def index(id):
    metadata = {
        "description": "Friendly Johnny Lemiau.",
        "image": "https://storage.googleapis.com/opensea-prod.appspot.com/puffs/3.png",
        "name": "NFT #" + id,
        "attributes": [
            {
                "trait_type": "Johnny",
                "value": "Extra",
            },
        ],
    }

    return jsonify(metadata)


@app.route("/contracts/boda")
def api():
    metadata = {
        "name": "Boda Gatitos",
        "description": "BODA GATITOS Miau Miau!",
        "image": "https://storage.googleapis.com/opensea-prod.appspot.com/puffs/2.png",
        "external_link": "https://bodorrio-gatitos.netlify.app/",
    }
    return jsonify(metadata)


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
