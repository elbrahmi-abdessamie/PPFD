
def ft_filter(function: None, list_of_inputs):
    '''
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    '''
    try:
        filterd = []
        if function:
            filterd = [x for x in list_of_inputs if function(x)]
        else:
            filterd = [x for x in list_of_inputs if bool(x)]
        return filterd
    except:
        return []
