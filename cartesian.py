def cartesian (lists):
    if lists == []: 
    	return [()]

    # return [x + (y,) for x in cartesian(lists[:-1]) for y in lists[-1]]
    cart = []
    for x in cartesian(lists[:-1]):
    	for y in lists[-1]:
    		cart.append(x+(y,))
    return cart


print cartesian([[1, 2, 3], [2, 4, 6]])

def product(lists):
    if not lists:
        yield ()

    else:
        for a in lists[0]:
            for b in product(lists[1:]):
                yield (a,)+ b

print list(product([[1, 2, 3], [2, 4, 6]]))