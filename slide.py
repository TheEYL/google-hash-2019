"""Create a Slide"""
def removeDuplicates(x):
  return list(dict.fromkeys(x))



class Slide():

    def __init__(self, photo):
        """pass a list of photos"""
        self.photo = photo
        if (len(self.photo) > 1 ):
            self.tags = " ".join(removeDuplicates(photo[0].tags.split(" ") + photo[1].tags.split(" ")))
        else :
            self.tags  = photo[0].tags

