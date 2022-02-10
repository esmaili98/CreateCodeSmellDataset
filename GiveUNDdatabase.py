import understand as und
import tkinter
import os
from tkinter import filedialog

class GvieUNDdatabase:
    def browsefile_path(self):
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Select source code directory')
        if len(tempdir) > 0:
            print("You chose: %s" % tempdir)

        print("\nfile_path_variable = ", tempdir)
        return tempdir

    def give_db(self):
        sourcedir=self.browsefile_path()
        print("select the system : ")
        udb_name_path = self.search_for_file_path(sourcedir)
        print("the '.udb' file created.")
        udb_path = udb_name_path[1] + "/" + udb_name_path[0] + ".udb"
        print("'.udb' file path is : ", udb_path)
        db = und.open(udb_path)
        return db

    def search_for_file_path(self,sourcedir):
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window
        currdir = os.getcwd()
        # tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        tempdir = sourcedir
        if len(tempdir) > 0:
            print("You choose: %s" % tempdir)

        print("\nfile_path_variable = ", tempdir)
        # {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
        rootpath = tempdir + "/"
        # path
        project_name = self.create_understand_database_from_project(rootpath)
        # print('111',project_name,'2222',tempdir)
        return [project_name, tempdir]


    def create_understand_database_from_project(self,root_path):
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
