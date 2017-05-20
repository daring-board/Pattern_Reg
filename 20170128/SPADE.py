# -*- coding: utf-8 -*-

class SPADE:
    tran_dic = {}
    item_list = []
    max_len = 0
    th = 30
    set_d = []

    def __init__(self, in_file_name, out_file_name):
        self.out_file = open(out_file_name, "w", encoding='utf-8')
        self.in_file = open(in_file_name, "r", encoding='utf-8')

    def constract(self):
        line = self.in_file.readline()
        while line:
            line = line.replace('\n', '')
            row = line.split(',')
            self.tran_dic[row[0]] = row[1].split('x')
            if self.max_len < len(self.tran_dic[row[0]]):
                self.max_len = len(self.tran_dic[row[0]])
            for item in self.tran_dic[row[0]]:
                if item not in self.item_list: self.item_list.append(item)
            line = self.in_file.readline()

    def apriori(self):
        self.countApper()
        k = 0
        while len(self.set_d) == k+1:
            tmp_d = []
            if k == 0:
                for item1 in self.set_d[0]:
                    for item2 in self.set_d[0]:
                        if item1 != item2:
                            tmp_d.append([item1, item2])
            else:
                for item1 in self.set_d[k]:
                    for item2 in self.set_d[k]:
                        if set(item1) != set(item2):
                            item = set([])
                            for i in item1: item.add(i)
                            for i in item2: item.add(i)
                            if len(item)-1 != k+1: continue
                            if len(tmp_d) == 0: tmp_d.append(list(item))
                            else:
                                if list(item) not in tmp_d: tmp_d.append(list(item))
            tmp_d = self.countAndRemove(tmp_d)
            if len(tmp_d) != 0:
                self.set_d.append(tmp_d)
            k += 1

    def countAndRemove(self, data):
        count_list = {}
        for patt in data:
            str_patt = 'x'.join(patt)
            count_list[str_patt] = 0
        for tran in self.tran_dic.values():
            for patt in data:
                str_patt = 'x'.join(patt)
                set_tran = set(tran)
                set_patt = set(patt)
                if set_patt.issubset(set_tran): count_list[str_patt] += 1
        for str_patt in count_list:
            patt = str_patt.split('x')
            if count_list[str_patt] < self.th:
                data.remove(patt)
        return data

    def countApper(self):
        tmp_d = []
        for item in self.item_list:
            counter = 0
            for tran in self.tran_dic.values():
                if item in tran: counter += 1
            if counter >= self.th: tmp_d.append(item)
        self.set_d.append(tmp_d)

    def showItems(self):
        count = 0
        for item in self.item_list:
            t_str = '%s: %s'%(count, item)
            print(t_str)
            count += 1

    def showDic(self):
        for idx in self.tran_dic:
            t_str = '%s: %s'%(idx, self.tran_dic[idx])
            print(t_str)

    def outputPatterns(self):
        self.out_file.write(str(self.th)+'\n')
        for dat in self.set_d:
            self.out_file.write(str(dat)+'\n')

    def closeFiles(self):
        self.in_file.close()
        self.out_file.close()

if __name__=="__main__":
    in_file_name = "sequence.csv"
    out_file_name = "spade.csv"
    sp = SPADE(in_file_name, out_file_name)
    sp.constract()
    sp.apriori()
    sp.outputPatterns()
    sp.closeFiles()
