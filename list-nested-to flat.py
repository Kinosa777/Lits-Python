lst = [[[1, 2.9], 8], 'r', [3, 5], 4]

def flatten(arr):
'''
    Transforms a nested list into a flat one
    
    Returns: flat
'''
    for elem in arr:
        if isinstance(elem, list):
            flatten(elem)
        else:
            flat.append(elem)
    return (flat)

flat = []
flatten(lst)
print(flat)
