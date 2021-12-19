import understand as und
import tkinter as tk
import os
from tkinter import filedialog
import glob


def browsefile_path(title="Select the file"):
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title=title)
    return files[0]


def is_abstract(ent):
    try:
        if("Abstract" in str(ent.kind())):
            return True
        else:
            return False
    except:
        return True

def is_interface(classname):
    try:
        if("Interface"in str(classname.kind())  ) :
            return True
        else:
            return False
    except:
        return True

def read_udb(udbaddress):
    db = und.open(udbaddress)
    return db

def feRefactoringOpps(entitylongname,smellstxtaddress):
    index = len(smellstxtaddress) - 1
    counter = 0
    while counter != 3:
        if smellstxtaddress[index] != '/':
            index -= 1
        else:
            index -= 1
            counter += 1
    udbdatabaseaddress = smellstxtaddress[:index + 1]
    print(udbdatabaseaddress)
    os.chdir(udbdatabaseaddress)
    udbfile = glob.glob("*.udb")[0]
    udbdatabaseaddress = udbdatabaseaddress + '/' + udbfile

    db=read_udb(udbdatabaseaddress)
    totalmethods = db.ents("method")
    for mth in range(0, len(totalmethods)):
        if str(totalmethods[mth].library()) != "Standard" and totalmethods[mth].longname()==entitylongname:
            varlist = totalmethods[mth].ents("", "Variable , Parameter")
            methodlist = totalmethods[mth].ents("", "method")
            break


    print(totalmethods[mth].longname())
    methodFather= totalmethods[mth].parent()
    print(methodFather.longname())

    if (is_abstract(methodFather) or is_interface(methodFather)):
        print('Father class is abstract or interface!!!!')
        return None
    else:
        foreignvar=list()
        foreignmeth = list()
        for var in varlist:
            if var.parent().longname() == methodFather.longname() or var.parent().parent().longname() == methodFather.longname():
                pass
            else:
                foreignvar.append(var)

        for method in methodlist:
            if method.parent().longname() == methodFather.longname() or method.parent().parent().longname() == methodFather.longname():
                pass
            else:
                foreignmeth.append(method)
        foreignent=foreignvar + foreignmeth
        # print(foreignent)
        numberoflocalfields = len(totalmethods[mth].ents("", "Variable , Parameter")) - len(totalmethods[mth].ents("define", "Variable , Parameter")) - len(foreignvar) # to exclude inside method variables
        numberoflocalmethods = len(totalmethods[mth].ents("", "method")) - len(totalmethods[mth].ents("define", "method")) - len(foreignmeth)  # to exclude inside method methods
        numberofallentities = len(varlist) + len(methodlist)


        index = len(smellstxtaddress) - 1
        counter = 0
        while counter != 2:
            if smellstxtaddress[index] != '/':
                index -= 1
            else:
                index -= 1
                counter += 1
        refactoropppath = smellstxtaddress[:index + 1]

        index = len(smellstxtaddress) - 1
        while smellstxtaddress[index] != '/':
            index -= 1
        smellname = smellstxtaddress[index:-4]
        refoppspath=refactoropppath+'/RefactorOpps/'
        if not os.path.exists(refoppspath):
            os.makedirs(refoppspath)

        logfile = open(refoppspath+smellname+'RedactorOpps.txt', 'w')

        print("Number of total entities: ", numberofallentities)
        print('Nubmer of local fields: ', numberoflocalfields)
        print('Number of local methods: ', numberoflocalmethods)
        print('Number of foreign entities: ',len(foreignent))

        logfile.writelines("\nNumber of total entities: {}".format(numberofallentities))
        logfile.writelines("\nNubmer of local fields: {}".format(numberoflocalfields))
        logfile.writelines("\nNumber of local methods: {}".format(numberoflocalmethods))
        logfile.writelines("\nNumber of foreign entities: {}".format(len(foreignent)))

        foreignentparentlongname = [[i, i.parent().longname()] for i in foreignent]
        # print(foreignentparentlongname)
        all_values = [lis[1] for lis in foreignentparentlongname]
        unique_values = set(all_values)

        group_list = []
        for value in unique_values:
            this_group = []
            for lis in foreignentparentlongname:
                if lis[1] == value:
                    this_group.append(lis[0])
            group_list.append(this_group)
        group_list.sort(key=len,reverse=True)

        for item in group_list:
            print('entities: ',[[entity.simplename(),entity.kind()] for entity in item])
            print('entities parent longname: ',item[0].parent().longname())
            print('iteration: ',len(item))
            print('========================================================================')

            logfile.writelines("\n\nentities: {}".format([[entity.simplename(),entity.kind()] for entity in item]))
            logfile.writelines("\nentities parent longname: {}".format(item[0].parent().longname()))
            logfile.writelines("\niteration: {}".format(len(item)))
            logfile.writelines("\n========================================================================")



def main():
    smellstxtaddress=browsefile_path(title="Select \".txt\" Smell file")
    print(smellstxtaddress)


    with open(smellstxtaddress) as f:
        entitylongname = f.readlines()
    for entname in entitylongname:
        feRefactoringOpps(entname[:-1],smellstxtaddress)


main()