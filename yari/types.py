from kivy.vector import Vector as KivyVector


class Vector(KivyVector):
    """Vector type

    Subclasses Kivy's Vector type to implement __radd__ and __rsub__

    """

    def __radd__(self, v):
        return Vector(v[0] + self.x, v[1] + self.y)

    def __rsub__(self, v):
        return Vector(v[0] - self.x, v[1] - self.y)

    def __mul__(self, *args):
        val = super().__mul__(*args)
        return Vector(*val)

    def __rmul__(self, *args):
        val = super().__rmul__(*args)
        return Vector(*val)

    def __div__(self, *args):
        val = super().__div__(*args)
        return Vector(*val)

    def __rdiv__(self, *args):
        val = super().__rdiv__(*args)
        return Vector(*val)

    def __truediv__(self, *args):
        val = super().__truediv__(*args)
        return Vector(*val)

    def __rtruediv__(self, *args):
        val = super().__rtruediv__(*args)
        return Vector(*val)
