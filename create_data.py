from file_base import ReadFile
import glob

class CreateTrainingData:
    def __init__(self, path):
        self.token_file = "terrier-stop.txt"
        self.output_file = "train.t"
        self.token_counts = {}
        self.path = path
        self.file_names = glob.glob(self.path + "*/*")

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


    def print_progress(self, old_progress, progress):
        if int(old_progress) != int(progress):
            print int(progress),'%'
        return progress


    def get_training_data(self):
        ofs = open(self.output_file, 'w')
        tokens = self.get_all_tokens(self.token_file, '\r\n')
        num_files = len(self.file_names)
        progress = 0.0
        for file_name in self.file_names:
            progress = self.print_progress(progress, progress + 100.0/num_files)
            
            read_file = ReadFile(file_name)
            tmp_count = read_file.get_token_counts(tokens)
            if self.is_spam(file_name):
                ofs.write('+1 ')
            else:
                ofs.write('-1 ')
            ofs.write(" ".join(['%s:%s' % (key + 1, tmp_count[key]) for key in range(len(tmp_count)) if tmp_count[key] != 0]))
            ofs.write('\n')
            

create = CreateTrainingData("/home/sol315/stealML/lingspam_public/bare/")
create.get_training_data()
