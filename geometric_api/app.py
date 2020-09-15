from flask import Flask, request
from geometric_api.schemas import deserialize
from geometric_api.services.sum import operations

app = Flask("geometric_api")


@app.route("/sum", methods=["POST"])
def adding():
    # --- Deserialize Input

    # Use request.args to get query params
    query = request.args.get("op", default="area", type=str)

    # Use request.get_json() to get the body
    request_data = request.get_json()

    figures = [deserialize(f) for f in request_data["figures"]]

    # --- Perform Logic
    operation = operations[query]
    result = operation(figures)

    # --- Serialize Output
    return str(result)


if __name__ == '__main__':
    app.run()
