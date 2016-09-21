from file_base import ReadFile
import glob

class CreateTrainingData:
    def __init__(self, path):
        self.token_file = "terrier-stop.txt"
        self.token_counts = {}
        self.path = path
        self.file_names = glob.glob(self.path + "*")

    def get_all_tokens(self, tokenFile, separator):
        try:
            t = open(tokenFile, 'r')
        except:
            print ("Token file open failed\n")
        token_list = t.read().strip().split(separator)
        return token_list

    def is_spam(self, file_name):
        if "spm" in file_name:
            return True
        return False

    def get_training_data(self):
        tokens = self.get_all_tokens(self.token_file, '\r\n')
        for file_name in self.file_names:
            read_file = ReadFile(file_name)
            tmp_count = read_file.get_token_counts(tokens)
            if self.is_spam(file_name):
                print '+1',
            else:
                print '-1',
            print " ".join(['%s:%s' % (tokens.index(key), value) for (key, value) in tmp_count.items() if value != 0])
            

create = CreateTrainingData("/home/sol315/stealML/lingspam_public/bare/part1/")
create.get_training_data()
