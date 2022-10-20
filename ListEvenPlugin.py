class ListEvenPlugin:
    def input(self, infile):
        self.myfile = open(infile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')

        for num in self.myfile:
            if int( num) % 2 == 0:
                outfile.write(num)
