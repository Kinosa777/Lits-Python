lst = [[[1, 2.9], 8], 'r', [3, 5], 4]

def flatten(arr):
    for elem in arr:
        if isinstance(elem, list):
            flatten(elem)
        else:
            flat.append(elem)
    return (flat)

flat = []
flatten(lst)
print(flat)
