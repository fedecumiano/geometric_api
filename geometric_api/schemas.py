from geometric_api.figures import Circle, Rectangle, Square, Triangle
from marshmallow import EXCLUDE, Schema, fields, post_load


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
    sides = fields.List(fields.Float)
    """
    side1 = fields.Float()
    side2 = fields.Float()
    side3 = fields.Float()
    """

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


schema_type = {
    "CIRCLE": CircleSchema(),
    "TRIANGLE": TriangleSchema(),
    "RECTANGLE": RectangleSchema(),
    "SQUARE": SquareSchema(),
}


def deserialize(figure):
    figure_type = figure.get("type")

    if figure_type in schema_type:
        schema = schema_type[figure_type]
        return schema.load(figure)
    # Todo: return 400
    raise ValueError(f"Non supported type: {figure_type}")
