""" This file uses hashing to create IDs for the different photos"""
# import hashlib as hl

def hashData(file):
    id_images = {}
    images = open(file).read().split('\n')
    i = 0
    for img in images[  1 : len(images) - 1 ]:
        # id_images[ hl.md5(img.encode()).hexdigest() ] = img
        id_images[i] = img[0] + img[3:]
        # print (type(img[3:]))
        i = i + 1
        # id_images[ hl.md5(img.encode()).hexdigest() ] = img.split(' ') # split tags into a list

    # print(id_images)
    return (id_images)

# hashData("a_example.txt")
# hashData("b_lovely_landscapes.txt")
