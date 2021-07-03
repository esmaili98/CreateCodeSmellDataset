import understand as und

import main_metrics

import tkinter
from tkinter import filedialog
import os
import csv




def give_db():
        print("select the system : ")
        udb_name_path=search_for_file_path()
        print("the '.udb' file created.")
        udb_path=udb_name_path[1]+"/"+udb_name_path[0]+".udb"
        print("'.udb' file path is : ",udb_path)
        db = und.open(udb_path)
        return db


def search_for_file_path():
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print("You chose: %s" % tempdir)

        print("\nfile_path_variable = ", tempdir)
        # {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
        rootpath=tempdir+"/"


        # path
        project_name=create_understand_database_from_project(rootpath)
        return [project_name,tempdir]

def create_understand_database_from_project(root_path):
        # root_path = 'C:\\Users\\saeed\\Desktop\\csharpprojectfortestudb\\Root_projects_folder\\'
        STRNAME = "project"
        count = 1
        # {0}: understand_db_directory, {1}: understand_db_name, {2}: project_root_directory
        cmd = 'und create -db {0}{1}.udb -languages C# java python add {2} analyze -all'
        # projects = [x[0] for x in os.walk(root_path)]
        projects = [name for name in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, name))]
        # print("list :",projects)
        for project_ in projects:
            command = cmd.format(root_path, project_, root_path + project_)
            count += 1
            print('executing ... ', command)
            os.system('cmd /c "{0}"'.format(command))
            print("finished ", project_)
        return project_




def def_get_metrics():
        db=give_db()
        classes=0
        totalclasses = db.ents("class")
        for cls in range(0, len(totalclasses)):
            if str(totalclasses[cls].library()) != "Standard":
                classes+=1

        methods = 0
        totalmethods = db.ents("method")
        for mth in range(0, len(totalmethods)):
            if str(totalmethods[mth].library()) != "Standard":
                methods += 1

        print("total classes : ",classes)
        print("total methods : ",methods)
        obj_return_result=main_metrics.cls_arangement()

        return obj_return_result.return_results(db)

def createCSVfiles():
    ClassMethodMetrics=def_get_metrics()
    ClassMethodMetrics[0][1].insert(0, 'longname')
    ClassMethodMetrics[1][1].insert(0, 'longname')

    for i in range(len(ClassMethodMetrics[0][0])):
        ClassMethodMetrics[0][2][i].insert(0,ClassMethodMetrics[0][0][i])
    for i in range(len(ClassMethodMetrics[1][0])):
        ClassMethodMetrics[1][2][i].insert(0,ClassMethodMetrics[1][0][i])


    for i in range(len(ClassMethodMetrics[0][2])):
        ClassMethodMetrics[0].append(ClassMethodMetrics[0][2].pop(0))
    for i in range(len(ClassMethodMetrics[1][2])):
        ClassMethodMetrics[1].append(ClassMethodMetrics[1][2].pop(0))

    ClassMethodMetrics[0].pop(0)
    ClassMethodMetrics[1].pop(0)

    with open('ClassMetricsFile.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(ClassMethodMetrics[0])
    print('______________________Class Metrics CSV file has been created______________________')

    with open('MethodMetricsFile.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(ClassMethodMetrics[1])
    print('______________________Method Metrics CSV file has been created______________________')
    return ClassMethodMetrics
# createCSVfiles()