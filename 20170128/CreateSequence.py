# -*- coding: utf-8 -*-

class CreateSequence:
    seq_dic = {}

    def __init__(self, in_file_name, out_file_name):
        self.out_file = open(out_file_name, "w", encoding='utf-8')
        self.in_file = open(in_file_name, "r", encoding='utf-8')

    def execute(self):
        line = self.in_file.readline() #ignore Header
        line = self.in_file.readline()
        while line:
            row = line.split(",")
            if row[1] in self.seq_dic: self.seq_dic[row[1]] += row[4] + "x"
            else: self.seq_dic[row[1]] = row[4] + "x"
            line = self.in_file.readline()

    def outputSeq(self):
        for key in self.seq_dic:
            line = "%s,%s\n" %(key, self.seq_dic[key][0:len(self.seq_dic[key])-1])
            self.out_file.write(line)

    def closeFiles(self):
        self.in_file.close()
        self.out_file.close()

if __name__=="__main__":
    in_file_name = "VisitWebpage.csv"
    out_file_name = "sequence.csv"
    cs = CreateSequence(in_file_name, out_file_name)
    cs.execute()
    cs.outputSeq()
    cs.closeFiles()
