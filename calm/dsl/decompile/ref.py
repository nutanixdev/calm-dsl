from calm.dsl.decompile.render import render_template
from calm.dsl.builtins import RefType


def render_ref_template(cls):

    if not isinstance(cls, RefType):
        raise TypeError("{} is not of type {}".format(cls, RefType))

    user_attrs = cls.get_user_attrs()
    user_attrs["name"] = cls.__name__
    schema_file = "ref.py.jinja2"

    text = render_template(schema_file=schema_file, obj=user_attrs)
    return text.strip()
