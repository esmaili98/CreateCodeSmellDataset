import csv
import os

import understand as und
def WOC(clas):
    try:
        if(is_interface(clas) or is_abstract(clas)):
            return None
        else:
            count_functionl=0
            metlist=clas.ents("Define","Public Method")
            for m in metlist:
                if not ( is_abstract(m)) and not(is_accesor_or_mutator(m)):
                    count_functionl+=1
            # baraye bazi az class hayy ke be an dastersi nadarad meghdar None bar migardand va mohasebat error mishavad
            if(clas.metric(["CountDeclMethodPublic"])["CountDeclMethodPublic"]==None):
                return None
            else:
                # count public methods for total
                total = clas.metric(["CountDeclMethodPublic"])["CountDeclMethodPublic"]
                # count public variables for total
                total += len(clas.ents("Define", "Java Variable Public Member"))
                if total == 0:
                    return 0
                else:
                    return (count_functionl/total)
    except:
        return None

def NOAM(clas):
    try:
        if(is_interface(clas)):
            return None
        else:
            count = 0

            for mth in clas.ents('Define', 'Method'):
                if str(mth.simplename()).startswith(("get", "set", "Set", "Get")):
                    count += 1
            return count
    except:
        return None

def NOMNAMM(clas):
    try:
        mth_=clas.ents("Define","Method")
        return  ((len(mth_ ))- NOAM(clas))
    except:
        return None

def LOCNAMM(clas):
    try:
        LOC = clas.metric(["CountLine"])["CountLine"]
        if(LOC==None):
            return None
        else:
            LOCAMM = 0
            for mth in clas.ents('Define','Method'):
                if (str(mth.simplename()).startswith(("get","set","Set","Get"))):
                    if (mth.metric(["CountLine"])["CountLine"] != None):
                         LOCAMM += mth.metric(["CountLine"])["CountLine"]
            return (LOC-LOCAMM)
    except:
        return None
def WMCNAMM(clas):
    try:
        if(is_interface(clas)):
            return None
        else:
            sum=0
            for mth in clas.ents('Define','Method'):
                if  not(is_accesor_or_mutator(mth)):
                    if(mth.metric(["Cyclomatic"])["Cyclomatic"]!=None):
                        sum += mth.metric(["Cyclomatic"])["Cyclomatic"]
            return sum
    except:
        return None

def TCC(clas):
    try:
        if(is_abstract(clas)or is_interface(clas)):
            return None
        else:
            # cal NP
            NDC=0
            methodlist = clas.ents('Define', 'Public Method')
            method_list_visible=list()
            for mvvisible in methodlist:
                if is_visible(mvvisible):
                    method_list_visible.append(mvvisible)
            for row in range(0,len(method_list_visible)):
                for col in range(0,len(method_list_visible)):
                    if (row > col):
                        if( connectivity(method_list_visible[row],method_list_visible[col])):
                            NDC+=1
            N=len(method_list_visible)
            NP=N*(N-1)/2
            if(NP!=0):
                return NDC/NP
            else:
                return 0
    except:
        return None

def ATFD_CLASS(clas):
    try:
        count = 0
        family_list = get_family_list(clas)


        varibleset = set()
        methodlist = clas.ents('Define', 'Public Method')
        for methodname in methodlist:
            if (not (is_abstract(methodname)) and methodname.name() != clas.name()):
                method_accessvariable = give_access_use(methodname)
                for var_ in method_accessvariable:
                    if ("Public Variable" in str(var_.kind())):
                        if (var_.parent() not in family_list and str(var_.library()) != "Standard"):
                            varibleset.add(var_)
                            count += 1
                # indirectly
                method_called_list = give_Methods_that_the_measured_method_calls(methodname)
                for m in method_called_list:
                    # if m.parent() not in family_list:

                    if (m.parent() not in family_list and str(m.simplename()).startswith(("get", "Get"))):
                        varibleset.add(m)
                        count += 1
        return len(varibleset)
    except:
        return None
        

#___________________________________________________________________________________

# defs needed to compute above metrics

def give_Methods_that_the_measured_method_calls(funcname):
    call_methods_list = set()
    try:
        for fi in funcname.refs("call"):
            if( fi.ent().library()!="Standard"):
                call_methods_list.add(fi.ent())
        return call_methods_list
    except:
        return call_methods_list


def give_access_use(funcname):
    # create a list and return it:Includes all the variables(fields) that a method uses
    access_field_list = set()
    try:
        for fi in funcname.refs("use"):
            access_field_list.add(fi.ent())
        return access_field_list
    except:
        return access_field_list

def is_accesor_or_mutator(method):
    
    try:

        if str(method.simplename()).startswith(("get", "set", "Set", "Get")):
            return True
        else:
            return False
    except:
        return False


def is_abstract(entity):
    try:
        if ("Abstract" in str(entity.kind())):
            return True
        else:
            return False
    except:
        return True

def is_interface(classname):
    try:
        if("Interface"in str(classname.kind())) :
            return True
        else:
            return False
    except:
        return True

def is_visible(funcname):
    try:
        flag = False
        # """all parameter not  only use or declare """
        par = funcname.ents("", "Parameter")
        for p in par:
            if (str(p.type()) == "EventArgs"):
                flag = True
                break
        if not (str(funcname.kind()) == "Public Constructor") or not (flag) or not (
                str(funcname.kind()) == "Private Method"):
            return True
        else:
            return False
    except:
        return False

def connectivity(row,col):
    try:
        if(connectivity_directly(row,col)   or connectivity_indirectly(row,col) ):
            return True
        else:
            return False
    except:
        return False

def connectivity_directly(row,col):
    listrow = set()
    listcol = set()
    try:
        for callrow in row.refs("use"):
             listrow.add(callrow.ent().longname())
        for callcol in col.refs("use"):
             listcol.add(callcol.ent().longname())
        intersect = [value for value in listrow if value in listcol]
        if(len(intersect)>0):
            return True
        else:
            return False
    except:
        return False
def connectivity_indirectly(row,col):
    listrow = set()
    listcol = set()
    try:
        for callrow in row.refs("call"):
            
            if (str(callrow.ent().simplename()).startswith(("get",  "Get"))):
                listrow.add(callrow.ent().longname())


        for callcol in col.refs("call"):
            
            if (str(callcol.ent().simplename()).startswith(("get", "Get"))):
              listcol.add(callcol.ent().longname())
        intersect = [value for value in listrow if value in listcol]
        if (len(intersect) > 0):
            return True
        else:
            return False
    except:
        return False

def get_family_list(classname):
    family = list()
    if ((classname.language()) == "Java"):  # fo java
        try:
            if (len(classname.refs("Extend")) == 0):  # for library class that not extenf by "Object" class
                family.append(classname)
                return family
        except:
            return family

        family_list = list()
        family_list.append(classname)
        for cla in family_list:
            for f in cla.refs("Extend,Extendby"):
                if not (f.ent() in family_list) and not (len(f.ent().refs("Extend")) == 0):
                    family_list.append(f.ent())
                    # print(f.ent().longname())
        return family_list



    else:  # for csharp(c#)

        try:
            print(classname.refs())
            if (len(classname.refs("Base")) == 0):
                family.append(classname)
                return family
        except:
            return family
        # print("ddd")
        family_list = list()
        family_list.append(classname)
        for cla in family_list:
            for f in cla.refs("Base,Derive"):
                if not (f.ent() in family_list) and not (len(f.ent().refs("Base")) == 0):
                    family_list.append(f.ent())
        return family_list

def class_metrics_arange(classent):
    class_metric_values=list()
    if str(classent.library()) != "Standard":
        try:
            if (is_abstract(classent) or is_interface(classent.parent())):
                pass
            else:
        # if True:
                class_metric_values=call_class_metrics(classent)
        except:
            class_metric_values=call_class_metrics(classent)
    return class_metric_values
    # return a list consist of classes and methods and thier metrics value

def call_class_metrics(clas):
    class_metrics=list()

    class_metrics.append(WOC(clas))
    class_metrics.append(WMCNAMM(clas))
    class_metrics.append(LOCNAMM(clas))
    class_metrics.append(NOMNAMM(clas))
    class_metrics.append(NOAM(clas))
    class_metrics.append(ATFD_CLASS(clas))
    class_metrics.append(TCC(clas))
    return class_metrics

if __name__ == '__main__':

    # db = und.open(udb_path='.udb file address...')
    db=und.open('C:\\Users\Sadaf\Desktop\\apache-ant-1.5.2.udb')
    metricsDataset=[['ClassLongname','WOC','WMCNAMM','LOCNAMM','NOMNAMM','NOAM','ATFD','TCC']]
    for cls in db.ents('class'):
        result=class_metrics_arange(cls)
        result.insert(0,cls.longname())
        metricsDataset.append(result)

    desktopadd = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    with open(desktopadd +'/MetricDataset.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(metricsDataset)


