import re
class File:
    def __init__(self, fileName):
        self.path = fileName
        self.rfs = open(self.path, 'r')

class readFile(File):
    def __init__(self, fileName):
        File.__init__(self, fileName)
    
    def getRaw(self):
        return self.rfs.read();
    
    def getLines(self):
        #return self.rfs.readlines()
        return self.rfs.read().split('\n')
    
    # take in the tokenFile, the separator and count the number of
    # words in the aim file
    def getTokenCounts(self, tokenFile, separator):
        try:
            t = open(tokenFile, 'r')
        except:
            print ("Token file open failed\n")
        
        tokens = t.read().strip().split(separator)
        lines = self.getLines()
        tokenCounts = {}
        for t in tokens:
            tokenCounts[t] = 0
            
        for line in lines:
            if line == None:
                continue
            wordsInFile = line.strip().split()
            for i in range(0, len(wordsInFile)):
                alphas = re.sub("[^a-zA-Z]","", wordsInFile[i])
                if alphas in tokenCounts:
                    tokenCounts[alphas] += 1
        return tokenCounts


      
