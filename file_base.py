import re
class File:
    def __init__(self, fileName):
        self.path = fileName
        self.rfs = open(self.path, 'r')

class ReadFile(File):
    def __init__(self, fileName):
        File.__init__(self, fileName)

    def set_path(self, path):
        self.path = path
    
    def get_raw(self):
        return self.rfs.read();
    
    def get_lines(self):
        #return self.rfs.readlines()
        return self.rfs.readlines()

    # take in the tokenFile, the separator and count the number of
    # words in the aim file
    def get_token_counts(self, tokens):
        lines = self.get_lines()
        token_counts = {}
        for t in tokens:
            token_counts[t] = 0
            
        for line in lines:
            wordsInFile = line.strip().split()
            for i in range(0, len(wordsInFile)):
                alphas = re.sub("[^a-zA-Z]","", wordsInFile[i])
                if alphas in token_counts:
                    token_counts[alphas] += 1
        return token_counts


      
