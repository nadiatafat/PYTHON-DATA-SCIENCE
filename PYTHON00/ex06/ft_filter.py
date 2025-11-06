def ft_filter(function, iterable) -> list:
    """
    filter(function or None, iterable) --> filter object

    Return a list of items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return [x for x in iterable if x]  # garde uniquement les truthy
    return [x for x in iterable if function(x)]
