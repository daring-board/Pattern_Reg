# -*- coding: utf-8 -*-

class PrefixSpan:
    tran_dic = {}
    proj_dbs = []
    sol_dic = {}
    th = 50

    def __init__(self, in_file_name, out_file_name):
        self.out_file = open(out_file_name, "w", encoding='utf-8')
        self.in_file = open(in_file_name, "r", encoding='utf-8')

    def createTranDB(self):
        line = self.in_file.readline()
        while line:
            line = line.replace('\n', '')
            row = line.split(',')
            self.tran_dic[row[0]] = row[1]
            line = self.in_file.readline()

    def countFreq(self, seq):
        counter = 0
        for tran in self.tran_dic.values():
            if seq in tran: counter += 1
        return counter

    def execute(self):
        self.prefixSpan( '', 1, self.tran_dic)

    def prefixSpan(self, seq, ln, db):
        freq_set = {}
        for s in db.values():
            for item in s.split('x'):
                if not seq: seq_t = item
                else: seq_t = seq + 'x' + item
                n_tmp = self.countFreq(seq_t)
                if n_tmp >= self.th: freq_set[item] = n_tmp
        print(freq_set)
        for item in freq_set:
            if not seq: seq_t = str(item)
            else: seq_t = seq + 'x' + item
            n_tmp = self.countFreq(seq + 'x' + item)
            self.sol_dic[seq_t] = n_tmp
            tmp_db = {}
            for sid in self.tran_dic:
                if seq_t in self.tran_dic[sid]: tmp_db[sid] = self.tran_dic[sid]
            self.prefixSpan(seq_t, ln+1, tmp_db)

    def showItems(self):
        count = 0
        for item in self.item_list:
            t_str = '%s: %s'%(count, item)
            print(t_str)
            count += 1

    def showSolutions(self):
        for seq in self.sol_dic:
            print(seq + ':: ' + str(self.sol_dic[seq]))

if __name__== "__main__":
    in_file_name = "sequence.csv"
    out_file_name = "prefixspan.csv"
    ps = PrefixSpan(in_file_name, out_file_name)
    ps.createTranDB()
    ps.execute()
    ps.showSolutions()
