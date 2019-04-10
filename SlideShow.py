"""Creates a slideshow"""
""" A slide show is an ordered list of slides"""

def scoring(slideList):
    "The slideshow is scored based on how interesting the transitions between each pair of subsequent SLIDES are."
    score =  0
    for i in range(len(slideList)):
        if (i+i) < len(slideList):
           interest_factor = min (tag_comparision(slideList[i].tags, slideList[i+1].tags))
           # print(f"interest factor between slide {i} and slide {i+1} = {interest_factor}")
           score = score + interest_factor

    return score

def tag_comparision(tags1, tags2):
    tagList = tags1.split(" ") + tags2.split(" ")
    # print (tagList)

    tagfreq  = {i:tagList.count(i) for i in tagList}
    common = 0
    for k,v in tagfreq.items():
        if (v == 2):
            common = common + 1

    size_tags1 = len(tags1.split(" ")) - common
    size_tags2 = len(tags2.split(" ")) - common

    return common, size_tags1, size_tags2



