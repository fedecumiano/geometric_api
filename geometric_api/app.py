from flask import Flask, request

app = Flask("geometric_api")


@app.route("/", methods=["POST"])
def hello():
    # Use request.json to get the body
    print(request.json)
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
