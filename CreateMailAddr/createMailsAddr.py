# -*- coding: utf-8 -*-

class CreateMailAddr:
    name_dic = {}
    comp_dic = {}

    def __init__(self, file1, file2, output):
        self.out_file = open(output, "w", encoding='utf-8')
        self.in_file1 = open(file1, "r", encoding='utf-8')
        self.in_file2 = open(file2, "r", encoding='utf-8')

    def selectNameOrComp(self, name_or_comp):
        if name_or_comp == "name":
            target_file = self.in_file2
            target_dict = self.name_dic
        elif name_or_comp == "comp":
            target_file = self.in_file1
            target_dict = self.comp_dic
        return target_dict, target_file

    def createDic(self, name_or_comp):
        target_dict, target_file = self.selectNameOrComp(name_or_comp)
        line = target_file.readline()
        while line:
            row = line.split(",")
            row[1] = row[1].replace('"', '')
            target_dict[row[0]] = row[1].replace("kabushikigaisha\n", "")
            line = target_file.readline()

    def showDic(self, name_or_comp):
        target_dict, target_file = self.selectNameOrComp(name_or_comp)
        for val in target_dict.values():
            print(val)

    def readOrgFile(self, org_file_name):
        org_file = open(org_file_name, "r", encoding='utf-8')
        line = org_file.readline()
        self.out_file.write(line)
        line = org_file.readline() #Header行を無視
        while line:
            row = line.split(",")
            domain = self.comp_dic[row[3].replace('"', '')]+".co.jp"
            for name in self.name_dic:
                if name in row[1]:
                    addr = self.name_dic[name].replace("\n", "")
                    break
            row[2] = '"%s@%s"' %(addr, domain)
            self.out_file.write(','.join(row))
            #print(addr + '@'+ domain)
            line = org_file.readline()
        org_file.close()

    def closeFiles(self):
        self.in_file2.close()
        self.in_file1.close()
        self.out_file.close()

if __name__=="__main__":
    in_file_name1 = "comp.csv"
    in_file_name2 = "name.csv"
    out_file_name = "score_list.csv"
    cma = CreateMailAddr(in_file_name1, in_file_name2, out_file_name)
    cma.createDic("comp")
    cma.createDic("name")
    cma.readOrgFile("score_list_org.csv")
    cma.closeFiles()
