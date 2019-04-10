from sys import argv
from Photo import *
from PhotoList import *
from hashData import *
from slide import *
import SlideShow as ss
import random

def mergeList( v, h):
    return v + h

filename, data  =  argv
pList = PhotoList.photo_list

def deserialize(pList):
    for (k,v) in hashData(data).items():
       # print(v)
       pList.append( Photo(k,v) )

    return  pList

pList = deserialize(pList)

# print([ (i.id,i.type, i.tags) for i in pList])


vertical_images =  []
horizontal_images =  []

def splitImages():
    for i in  pList:
        if (i.type == "H"):
            horizontal_images.append([i])
        else:
            vertical_images.append(i)

splitImages()
# def removeNoRepeat(  ):
#     random.shuffle(data)
#     for elem in data: process(elem)

random.shuffle(vertical_images)
if (len(vertical_images) % 2) != 0:
     vertical_images = vertical_images[1:]

vertical_pairs = [[vertical_images[i], vertical_images[i+1]] for i in range(0, len(vertical_images), 2)]
# for s in


# print(vertical_pairs)
pList = mergeList(horizontal_images,vertical_pairs)
random.shuffle(pList)
# print(pList)

slideList = []

for p in pList:
    s = Slide(p)
    slideList.append(s)

# print (ss.scoring(slideList))
# for i in range(len(slideList)):
    # print(slideList[i].tags)
    # pass

def writeToFile():
    print("Created file: " + "output_" + data)
    f = open("output_" + data, "w+" )

    f.write("Submission file\t\t\t\t\t\t-----\t\t\t\t\t\t Description\n".format(len(slideList)))
    f.write("{0}\t\t\t\t\t\t-----\t\t\t\t\t\tThis submission has {0} slides\n".format(len(slideList)))
    for i  in range(len(slideList)):
        if (len(slideList[i].photo) > 1):
            image_id = [slideList[i].photo[j].id for j in range(len(slideList[i].photo)) ]
            f.write("{0}\t\t\t\t\t\t-----\t\t\t\t\t\tSlide number {1}  contains photo {0} \n".format(image_id,i))
        else:
            f.write("{0}\t\t\t\t\t\t-----\t\t\t\t\t\tSlide number {1}  contains photo {0} \n".format(slideList[i].photo[0].id,i))

    f.write("Score:\t\t\t\t\t\t{0}".format(ss.scoring(slideList)))
    f.close()

writeToFile()
