"""
Utility collection

"""

__all__ = ('clamp', 'property_setter', 'get_normal_tex_size',)


def clamp(val, min_val, max_val):
    """Limits a value within a given minimum and maximum range.

    """
    return min(max(val, min_val), max_val)


def property_setter(this, value, other, other_prop, this_prop=None):
    """Sets property value for value bindings.

    Use this with functools.partial function.

    ```
    this.bind(some_prop=partial(
        property_setter,
        other=other, other_prop='some_prop'
    ))
    ```

    :params this: Binding source object.
    :params this_prop: Binding object's property to get value from.
        Defaults to `value` if not given.
    :params other: Observing object.
    :params other_prop: Observing object's property that we want to update
        when Binding object's property value changes.

    """
    this_val = getattr(this, this_prop) if this_prop else value
    setattr(other, other_prop, this_val)


def get_normal_tex_size(texture):
    """Returns a texture's normal size based on its width / height ratio.

    Based on kivy.uix.image.Image but without the heaviness of an actual
    widget.

    """
    tw, th = texture.size
    ratio = tw / float(th)
    th = tw / ratio
    return tw, th
