from collections import OrderedDict
from typing import Any, Dict


class _ChoiceEnumMeta(type):
    """
    Metaclass for implementing django-compatible enums.

        class MyChoiceEnum(metaclass=_ChoiceEnumMeta):
            FOO = 'foo description'
            BAR = 'bar description'

    Technically each row produces 3 values:

    * Key (the variable name)
    * Human readable value (the variable value)
    * The actual value of the constant - it can be anything!

    As provided in the default implementations, you can see that the actual
    value can be just the string value of the variable, or an int based on the
    order of the statement.

    Given these 3 values you use them like so:

    * Actual value, Human value pair - for django model choices
    * Key, actual value - when comparing/setting them in python code.

    See related .serializer_fields.ChoiceEnumField.
    """

    def __new__(cls, name, bases, dct):
        """Do the magic of processing constant expressions into 3 values."""

        data = OrderedDict()

        # back up the initial values for later
        for key, val in dct.items():
            if key.upper() == key:
                data[key] = val

        try:
            # callback used to generate the actual value based on the current statement
            convert_key = dct["_convert_key_"]
        except KeyError:
            # have to look through all parents because MRO is not in place yet
            for base in bases:
                convert_key = getattr(base, "_convert_key_", None)

                if convert_key:
                    break

            else:
                # default is to just use the variable name
                convert_key = lambda key, count: key

        # replace the constants with their generated value
        for count, key in enumerate(data, 1):
            dct[key] = convert_key(key, count)

        # choices for django models
        dct["_choices"] = data
        klass = super().__new__(cls, name, bases, dct)
        objects = {}

        # after the child class is created, instantiate all of the default values
        for key, val in data.items():
            instance = klass(dct[key])
            objects[instance] = key
            setattr(klass, key, instance)

        klass._objects = objects

        return klass

    def __iter__(self):
        return iter(self._objects.keys())


class _ChoiceEnumBase(metaclass=_ChoiceEnumMeta):
    """Provide some useful defaults for subclasses."""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self}"

    @classmethod
    def choices(cls) -> Dict[Any, str]:  # really should be Dict[*current class*, str]
        return {getattr(cls, key): val for key, val in cls._choices.items()}


class ChoiceEnum(_ChoiceEnumBase, str):
    """
    Simple enum class suitable for use in django models' choices.

    Define your subclass with human readable names:

        class MyEnum(ChoiceEnum):
            FOO = "This is a foo"
            BAR = "And this is a bar"

    Use the `choices` attribute on the class for the model:

        choices = models.CharField(choices=MyEnum.choices, ...)

    Iterate over the keys:

        set(MyEnum) == {"FOO", "BAR"}

    The initial attributes always return their own string value:

        MyEnum.FOO == "FOO"
    """


class IntChoiceEnum(_ChoiceEnumBase, int):
    """
    Same as `ChoiceEnum` but objects are ints. Counter starts at 1.

        class MyEnum(IntChoiceEnum):
            FOO = "This is a foo"
            BAR = "And this is a bar"

        MyEnum.FOO == 1
        set(MyEnum) == {1, 2}
    """

    def _convert_key_(name: str, count: int) -> int:
        """Automatic constant value generator - use order position as value."""

        return count

    def __str__(self):
        return self._objects[self]
