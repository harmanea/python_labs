import functools

# Feedback:
#
#     + Code formatting looks like PEP8, good job!
#     - Please use a hashbang
#     - Assignment says: "The decorator converts a function to a descriptor."
#       You're not using a descriptor.
#
# Possible solution (from one of your colleagues):
#
#     def size(all_instances):
#       def inner(function):
#         #returns instance of descriptor providing value over required instance(s)
#         return CustomDescriptor(function, all_instances)
#       return inner
#     
#     class CustomDescriptor:
#       def __init__(self, function, all_instances):
#         self.function = function
#         self.all_instances = all_instances
#         
#       def __get__(self, instance, owner):
#         if instance != None:
#           return self.function(instance)
#         else: # Feedback: else is unnecessary here.
#           values = [self.function(inst) for inst in self.all_instances()]
#           return sum(values)
#
# Look up "descriptors" in Python (or look at the slides).
#
# Despite of this, thanks for submitting solution.

def size(all_instances):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                return func(*args, **kwargs)
            else:
                return sum([func(x) for x in all_instances()])

        return wrapper
    return decorator


class Cache:
    def __init__(self):
        Cache._all_caches.append(self)
        self._storage = dict()

    _all_caches = []

    def set(self, key, value):
        self._storage[key] = value

    def get(self, key):
        return self._storage[key]

    def _all_instances():
        return Cache._all_caches

    @size(all_instances = _all_instances)
    def entries_count(self):
        return len(self._storage)


if __name__ == '__main__':  # test the implementation
    a = Cache()
    b = Cache()

    a.set("a", 1)
    a.set("b", 2)
    b.set("x", 3)

    print(a.entries_count())  # prints 2
    print(b.entries_count())  # prints 1
    print(Cache.entries_count())  # prints 3
