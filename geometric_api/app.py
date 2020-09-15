from flask import Flask, jsonify, request
from geometric_api.figures import Circle, Rectangle, Square, Triangle
from marshmallow import EXCLUDE, Schema, fields, post_load

app = Flask("geometric_api")

expected_data = {
    "figures": [{
        "type": "CIRCLE",
        "name": "Circulo1",
        "radius": 2
    }, {
        "type": "CIRCLE",
        "name": "Circulo2",
        "radius": 5
    }, {
        "type": "CIRCLE",
        "name": "Circulo3",
        "radius": 3
    }]
}


class CircleSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    radius = fields.Float()

    @post_load
    def make_circle(self, data, **kwargs):
        return Circle(**data)


class TriangleSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    side1 = fields.Float()
    side2 = fields.Float()
    side3 = fields.Float()

    @post_load
    def make_circle(self, data, **kwargs):
        return Triangle(**data)


class RectangleSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    side1 = fields.Float()
    side2 = fields.Float()

    @post_load
    def make_circle(self, data, **kwargs):
        return Rectangle(**data)


class SquareSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    side = fields.Float()

    @post_load
    def make_circle(self, data, **kwargs):
        return Square(**data)


def get_circle_area(figure):
    schema = CircleSchema()
    circle = schema.load(figure)
    return circle.calculate_area()


def get_square_area(figure):
    schema = SquareSchema()
    square = schema.load(figure)
    return square.calculate_area()


def get_rectangle_area(figure):
    schema = RectangleSchema()
    rectangle = schema.load(figure)
    return rectangle.calculate_area()


def get_triangle_area(figure):
    schema = TriangleSchema()
    triangle = schema.load(figure)
    return triangle.calculate_area()


def get_circle_perimeter(figure):
    schema = CircleSchema()
    circle = schema.load(figure)
    return circle.calculate_perimeter()


def get_square_perimeter(figure):
    schema = SquareSchema()
    square = schema.load(figure)
    return square.calculate_perimeter()


def get_rectangle_perimeter(figure):
    schema = RectangleSchema()
    rectangle = schema.load(figure)
    return rectangle.calculate_perimeter()


def get_triangle_perimeter(figure):
    schema = TriangleSchema()
    triangle = schema.load(figure)
    return triangle.calculate_perimeter()


@app.route("/sum", methods=["POST"])
def adding():
    total = 0
    # Use request.args to get query params
    query = request.args.get("op", default="area", type=str)
    # Use request.get_json() to get the body
    request_data = request.get_json()
    if query == "area":
        for figure in request_data["figures"]:
            if figure["type"] == "CIRCLE":
                total += get_circle_area(figure)
            elif figure["type"] == "TRIANGLE":
                total += get_triangle_area(figure)
            elif figure["type"] == "RECTANGLE":
                total += get_rectangle_area(figure)
            elif figure["type"] == "SQUARE":
                total += get_square_area(figure)
    elif query == "perimeter":
        for figure in request_data["figures"]:
            if figure["type"] == "CIRCLE":
                total += get_circle_perimeter(figure)
            elif figure["type"] == "TRIANGLE":
                total += get_triangle_perimeter(figure)
            elif figure["type"] == "RECTANGLE":
                total += get_rectangle_perimeter(figure)
            elif figure["type"] == "SQUARE":
                total += get_square_perimeter(figure)
    return str(total)


@app.route("/prueba")
def prueba():
    circles = []
    schema = CircleSchema()
    for figure in expected_data["figures"]:
        circles.append(schema.load(figure))


if __name__ == '__main__':
    app.run()
