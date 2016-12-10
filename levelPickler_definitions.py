import config, cPickle, os

# inventory class for the first level

class Level():
    """This class is a template for any level you want to create. Add and modify
    attributes to create a level layout.
    Remember: if you add any new attributes you will need to ammend the methods
    of the Level_creator class in the classes module accordingly - otherwise the
    attributes will go unrecognized and only take up memory in the namespace.
    This is something of a lowly level editor. Sorry, no GUI for this mofo.
    C programming Master Race gives a thubms up (their asses)."""

    # bug workaround, look in the changelog for details @ commit nr.8
    __module__ = os.path.splitext(os.path.basename(__file__))[0]

    def __init__(self):
        self.objects = {}
        self.music = '02_1.wav'
        self.background = os.getcwd() + '/' + 'Duda_okej.png'
        self.spawners = [config.classes.Spawn("Peon", (config.res_x/2, config.res_y/3), 50, 50)]
        self.misc = {}

Level1 = Level()

def main():
    # create instance to pickle
    ogur = Level1
    print ogur.music # debug print
    print ogur.background # debug print
    print
    # this is the part for the levelPickler module
    directory = os.getcwd()
    cwdDirList = os.listdir(directory)
    if 'Levels' in cwdDirList:
        print "Detected a level dir, moving on..."
        pass
    else:
        outputPath = directory + "/" + "Levels"
        os.makedirs(outputPath)

        with open(outputPath + "/" + "level1ogur.txt",'wb') as output_file:
            cPickle.dump(ogur, output_file, protocol=2)

if __name__ == '__main__':
    main()
