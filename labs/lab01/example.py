
class Object(object):

    def __init__(self, param=None):
        self.__private_field = param

    def __str__(self):
        return 'Object: %s' % self.__private_field

    def __repr__(self):
        return '<Object: __private_field=%s>' % self.__private_field

    def __hash__(self):
        return hash(self.__private_field)

    def __bool__(self):
        return bool(self.__private_field)


class ComparableObject(Object):

    def __eq__(self, other):
        return self.__private_field == other.__private_field

    def __lt__(self, other):
        return self.__private_field < other.__private_field

    def __ge__(self, other):
        return not self.__private_field < other.__private_field


class DynamicObject(Object):

    __fields = dict()

    def __str__(self):
        return 'Object: fields: %s' % self.__fields

    def __repr__(self):
        return '<Object: fields=%s>' % self.__fields

    def __getattr__(self, name):
        return self.__fields.get(name)

    def __setattr__(self, name, value):
        self.__fields[name] = value

    def __delattr__(self, name):
        del self.__fields[name]


class CalledObject(Object):

    @property
    def name(self):
        return self.__private_field

    def __call__(self, *args, **kwargs):
        return 'Called %s with (%s, %s)' % (self.name, str(args), str(kwargs))


class Container(object):

    def __init__(self, container=list()):
        self.__container = container

    def __getitem__(self, key):
        return self.__container[key]

    def __setitem__(self, key, value):
        self.__container[key] = value

    def __delitem__(self, key):
        del self.__container[key]

    def __contains__(self, key):
        return key in self.__container

    def __iter__(self):
        for obj in self.__container:
            yield obj


if __name__ == '__main__':
    a = Object('first')
    b = Object('second')
    print(a)
    print(b)
