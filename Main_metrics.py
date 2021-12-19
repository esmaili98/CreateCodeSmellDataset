import progressbar


class cls_get_metrics:
    def is_interface(self,classname):
        try:
            if("Interface"in str(classname.kind())  ) :
                return True
            else:
                return False
        except:
            return True


    def get_family_list(self,classname):
        family = list()
        try:
            if(len(classname.refs("Base"))==0):
                family.append(classname)
                return family
        except:
            return family
        family_list=list()
        family_list.append(classname)
        for cla in family_list:
            for f in cla.refs("Base,Derive"):
                if not (f.ent() in family_list)   and  not(len(f.ent().refs("Base"))==0 )     :
                    family_list.append(f.ent())
        return family_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def get_childs(self,classname):
        child_list = list()
        try:
            for f in classname.refs("Derive"):
                 child_list.append(f.ent())
            return child_list
        except:
            return child_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def get_fathers_and_grandfathers(self,classname):
        fathers_list=list()
        try:
            fathers_list.append(classname)
            while(True):
                for f in classname.refs("Base"):
                    parent=f.ent()
                    print("f:",f)
                print("parent        :",parent.name())
                if(parent.name()=="Object" or parent.name()=="page" ):
                    break
                classname=parent
                fathers_list.append(classname)
            return fathers_list
        except:
            return fathers_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NOPA(self, classname):
        try:
            if (classname.language() == "Java"):
                return len(classname.ents("define", "Java Variable Public Member"))
            else:
                return classname.metric(["CountDeclInstanceVariablePublic"])["CountDeclInstanceVariablePublic"]
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MAXNESTING(self,funcname):
        try:
            if(self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxNesting"])["MaxNesting"]
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountOutPut(self, funcname):
        try:
            if(self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountOutPut"])["CountOutPut"] )
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # def Allclass(self, classname):
    #     try:
    #         if(self.is_abstract(classname) or self.is_interface(classname.parent())):
    #             return None
    #         else:
    #             ProperMetricsApiName=classname.metrics()
    #             PrpperMetricsValue=list()
    #             # for metricName in ProperMetricsApiName:
    #             #     PrpperMetricsValue.append(classname.metric([metricName])[metricName])
    #             print('000@',ProperMetricsApiName)
    #             # print('111@',PrpperMetricsValue)
    #             # return [ProperMetricsApiName,PrpperMetricsValue]
    #     except:
    #         return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountInput(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountInput"])["CountInput"])
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CYCLO(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["Cyclomatic"])["Cyclomatic"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountLineBlank(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountLineBlank"])["CountLineBlank"])
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountLineCode(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountLineCode"])["CountLineCode"])
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountLineCodeDecl(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountLineCodeDecl"])["CountLineCodeDecl"])
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountLineCodeExe(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountLineCodeExe"])["CountLineCodeExe"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountLineComment(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountLineComment"])["CountLineComment"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountPath(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountPath"])["CountPath"])
        except:
            return None
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountPathLog(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountPathLog"])["CountPathLog"])
        except:
            return None
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountSemicolon(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountSemicolon"])["CountSemicolon"])
        except:
            return None
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountStmt(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountStmt"])["CountStmt"])
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountStmtDecl(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountStmtDecl"])["CountStmtDecl"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountStmtExe(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CountStmtExe"])["CountStmtExe"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CyclomaticModified(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CyclomaticModified"])["CyclomaticModified"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CyclomaticStrict(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["CyclomaticStrict"])["CyclomaticStrict"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Essential(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["Essential"])["Essential"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Knots(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["Knots"])["Knots"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxEssentialKnots(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["MaxEssentialKnots"])["MaxEssentialKnots"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MinEssentialKnots(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["MinEssentialKnots"])["MinEssentialKnots"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def RatioCommentToCode(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["RatioCommentToCode"])["RatioCommentToCode"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def SumCyclomatic(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["SumCyclomatic"])["SumCyclomatic"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def SumCyclomaticModified(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["SumCyclomaticModified"])["SumCyclomaticModified"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def SumCyclomaticStrict(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["SumCyclomaticStrict"])["SumCyclomaticStrict"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def SumEssential(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return (funcname.metric(["SumEssential"])["SumEssential"])
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # def is_abstract(self,funcname):
    #     if (str(funcname).startswith(("get", "set", "Set", "Get"))   or    funcname.metric(["CountLine"])["CountLine"]<=6):
    #         return True
    #     else:
    #         return False
    def is_abstract(self,ent):
        try:
            if("Abstract" in str(ent.kind())):
                return True
            else:
                return False
        except:
            return True
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NOLV(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                # bug
                varlist = funcname.ents("", "Variable , Parameter")
                return len(varlist)
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NOPL(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                # bug
                parlist = funcname.ents("", "Parameter")
                return len(parlist)
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NOAM(self,class_name):
        try:
            if(self.is_interface(class_name)):
                return None
            else:
                count = 0

                for mth in class_name.ents('Define', 'Method'):
                    if (str(mth.name()).startswith(("get", "set", "Set", "Get"))):
                        # print(mth.longname())
                        count += 1
                        # print(mth.longname())
                return count
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NOMNAMM(self,class_name):
        try:
            mth_=class_name.ents("Define","Method")
            return  ((len(mth_ ))- self.NOAM(class_name))
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def LOCNAMM(self,class_name):
        try:
            LOC = class_name.metric(["CountLine"])["CountLine"]
            if(LOC==None):
                return None
            else:
                LOCAMM = 0
                for mth in class_name.ents('Define','Method'):
                    mthfullname = str(mth.name())
                    ind = mthfullname.index('.')
                    mthname = mthfullname[ind + 1:]
                    if (str(mthname).startswith(("get","set","Set","Get"))):
                        if (mth.metric(["CountLine"])["CountLine"] != None):
                             LOCAMM += mth.metric(["CountLine"])["CountLine"]
                return (LOC-LOCAMM)
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def LOC(self,entname):
        try:
            return entname.metric(["CountLine"])["CountLine"]
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def WOC(self,class_name):
        try:
            if(self.is_interface(class_name) or self.is_abstract(class_name)):
                return None
            else:
                count_functionl=0
                metlist=class_name.ents("Define","Public Method")
                for m in metlist:
                    if not ( self.is_abstract(m)):
                        count_functionl+=1
                # baraye bazi az class hayy ke be an dastersi nadarad meghdar None bar migardand va mohasebat error mishavad
                if(class_name.metric(["CountDeclInstanceVariablePublic"])["CountDeclInstanceVariablePublic"]==None  or class_name.metric(["CountDeclMethodPublic"])["CountDeclMethodPublic"]==None):
                    return None
                else:
                    total = class_name.metric(["CountDeclInstanceVariablePublic"])["CountDeclInstanceVariablePublic"] + class_name.metric(["CountDeclMethodPublic"])["CountDeclMethodPublic"]
                    if total == 0:
                        return 0
                    else:
                        return (count_functionl/total)
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def WMCNAMM(self,class_name):
        try:
            if(self.is_interface(class_name)):
                return None
            else:
                sum=0
                for mth in class_name.ents('Define','Method'):
                    if  not(self.is_accesor_or_mutator(mth)):
                        if(mth.metric(["Cyclomatic"])["Cyclomatic"]!=None):
                            sum += mth.metric(["Cyclomatic"])["Cyclomatic"]
                return sum
        except:
            return None
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def is_accesor_or_mutator(self,funcname):
        try:
            if (str(funcname).startswith(("get", "set", "Get", "Set"))):
                return True
            else:
                return False
        except:
            return False
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def TCC(self, class_name):
        try:
            if(self.is_abstract(class_name)or self.is_interface(class_name)):
                return None
            else:
                # cal NP
                NDC=0
                methodlist = class_name.ents('Define', 'Public Method')
                method_list_visible=list()
                for mvvisible in methodlist:
                    if self.is_visible(mvvisible):
                        method_list_visible.append(mvvisible)
                for row in range(0,len(method_list_visible)):
                    for col in range(0,len(method_list_visible)):
                        if (row > col):
                            if( self.connectivity(method_list_visible[row],method_list_visible[col])):
                                NDC+=1
                N=len(method_list_visible)
                NP=N*(N-1)/2
                if(NP!=0):
                    return NDC/NP
                else:
                    return 0
        except:
            return None
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def connectivity(self,row,col):
        try:
            if(self.connectivity_directly(row,col)   or self.connectivity_indirectly(row,col) ):
                return True
            else:
                return False
        except:
            return False
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def connectivity_indirectly(self,row,col):
        listrow = set()
        listcol = set()
        try:
            for callrow in row.refs("call"):
                if (str(callrow.ent().name()).startswith(("get",  "Get"))):
                    listrow.add(callrow.ent().longname())
            for callcol in col.refs("call"):
                if (str(callcol.ent().name()).startswith(("get", "Get"))):
                  listcol.add(callcol.ent().longname())
            intersect = [value for value in listrow if value in listcol]
            if (len(intersect) > 0):
                return True
            else:
                return False
        except:
            return False
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def connectivity_directly(self,row,col):
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
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def is_visible(self, funcname):
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
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CDISP(self,method_name):
        try:
            if (self.is_abstract(method_name) or self.is_interface(method_name.parent())):
                return None
            else:
                cint = self.CINT(method_name)

                if cint==0:
                    return 0
                elif(cint==None):
                    return None
                else:
                    return self.FANOUT_OUR(method_name)/cint
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def FANOUT_OUR(self,methodname):
        try:
            if (self.is_abstract(methodname) or self.is_interface(methodname.parent())):
                return None
            else:
                called_classes_set=set()
                for call in methodname.refs("call"):
                    if (call.ent().library() != "Standard"):
                        called_classes_set.add(  call.ent().parent() )
                return len(called_classes_set)
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def ATLD(self,db,method_name):
        try:
            if (  not(self.is_abstract(method_name)) or  not(self.is_interface(method_name.parent()))   ):
                # cal directly access
                count=0
                system_att_=db.ents('field')
                access_att_=self.give_access_use(method_name)
                for att_ in access_att_:
                    if att_ in system_att_:
                        if (str(att_.kind()) in ["Unknown Variable", "Unknown Class"]):
                            continue
                        if(att_.library()!="Standard"):
                            count+=1
                # cal indirectly access
                calls=self.give_ALL_sys_and_lib_method_that_th_measyred_method_calls( method_name)
                for call in calls:
                    if (str(call).startswith(("get", "Get"))):
                        usevariable=call.refs("use")
                        if( len(usevariable)>0):
                            flag=True
                            for us in usevariable:
                                if(us.ent().library()=="Standard"):
                                    flag=False
                            if(flag):
                                count += 1
                return count
            else:
                return None
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_ALL_sys_and_lib_method_that_th_measyred_method_calls(self,funcname):

        methodlist=set()
        try:
            for refmethod in funcname.refs("call"):
                methodlist.add(refmethod.ent())
            return methodlist
        except:
            return methodlist
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def get_Namespace(self,entity):
        while (str(entity.parent().kind()) != "Unresolved Namespace" or str(entity.parent().kind()) != "Namespace"):
            entity = entity.parent()
            if (str(entity.parent().kind()) == "Unresolved Namespace" or str(   entity.parent().kind()) == "Namespace"):
                break
        return entity.parent()
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def ATFD_method(self, db, method_name):
        try:
            if not (str(method_name).startswith("get", "set", "Get", "Set")):
                # cal directly access
                count = 0
                system_att_ = db.ents('Variable')
                access_att_ = self.give_access_use(method_name)
                for att_ in access_att_:
                    if not (att_ in system_att_):
                        count += 1
                # cal indirectly access
                calls = self.give_Methods_that_the_measured_method_calls(self, method_name)
                for call in calls:
                    if (str(call).startswith(("get", "set", "Set", "Get"))):
                        get_att_ = self.give_access_use(call)
                        if not (get_att_ in system_att_):
                            count += 1
                return count
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # checked ok successfully ( ckeck field of librabry ex:math.PI isincluded or not ? at :if(var_.parent() not in family_list and var_.library()!="Standard"   ):
    def ATFD_CLASS(self, class_namee):
        try:
            count = 0
            family_list = self.get_family_list(class_namee)
            varibleset = set()
            methodlist = class_namee.ents('Define', 'Public Method')
            for methodname in methodlist:
                # directly
                if (not (self.is_abstract(methodname)) and methodname.name() != class_namee.name()):
                    method_accessvariable = self.give_access_use(methodname)
                    for var_ in method_accessvariable:
                        if ("Field" in str(var_.kind())):
                            if (var_.parent() not in family_list and var_.library() != "Standard"):
                                varibleset.add(var_)
                                count += 1
                    # indirectly
                    method_called_list = self.give_Methods_that_the_measured_method_calls(methodname)
                    # print(method_called_list)
                    for m in method_called_list:
                        # print(m.parent())
                        if (m.parent() not in family_list and str(m).startswith(("get", "Get"))):
                            varibleset.add(m)
                            count += 1
            return len(varibleset)
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def max_depth(self,method_name):
        # at least two
        if self.len(self.give_Methods_that_the_measured_method_calls(method_name)) ==0:
            return 0
        #if self.give_Methods_that_the_measured_method_calls(method_name).count() ==1:
        #    return 1
        return 1+ max([self.Mamcl(node) for node in self.give_Methods_that_the_measured_method_calls(method_name)])
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def total_nods(self,method_name):
        if self.give_Methods_that_the_measured_method_calls(method_name).count() ==0:
            return 0
        if self.give_Methods_that_the_measured_method_calls(method_name).count() ==1:
            return 1
        return 1+ sum([self.Mamcl(node) for node in self.give_Methods_that_the_measured_method_calls(method_name)])
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def NMCS(self, method_name):
        try:
            count=0
            for mth in  self.give_Methods_that_the_measured_method_calls(method_name):
                if str(mth).startswith("get","set","Get","Set"):
                    count+=1
            return count
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaMCL(self,method_name):
        try:
            max_dep=self.max_depth(method_name)
            if max_dep>=2:
                return max_dep
            else:
                return 0
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Memcl(self,method_name):
        try:
            total=self.total_nods(method_name)
            nmcs=self.NMCS(method_name)
            if nmcs==0:
                return 0
            else:
                return round(total/nmcs)
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # def CC(self,funcname):
    #     refset = set()
    #     reflist = list()
    #     for callint in funcname.refs("callby"):
    #         refset.add(callint.ent().parent())
    #         #reflist.append(callint.ent().parent())
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CM(self,funcname):
        try:
            if(self.is_private(funcname)):
                return None
            else:
                refset = set()
                for callint in funcname.refs("callby"):
                    refset.add(callint.ent())
                return len(refset)
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def is_private (slef,funcname):
        try:
            if(str(funcname.kind())=="Private Method"):
                return True
            else:
                return False
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CINT(self,method_name):
        try:
            if(self.is_abstract(method_name)  or self.is_interface(method_name.parent())):
                return None
            else:
                count=0
                family_list=self.get_family_list(method_name.parent())
                for mth in method_name.refs("call"):
                       if(  mth.ent().parent() in family_list):
                           count+=1
                return count
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_access_use(self,funcname):
        # create a list and return it:Includes all the variables(fields) that a method uses
        access_field_list = set()
        try:
            for fi in funcname.refs("use"):
                access_field_list.add(fi.ent())
            return access_field_list
        except:
            return access_field_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_access_use_for_class(self,classname):
        # create a list and return it:Includes all the variables(fields) that a method uses
        access_field_list = list()
        try:
            for fi in classname.refs("use"):
                access_field_list.append(fi.ent())
            return access_field_list
        except:
            return access_field_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_Methods_that_the_measured_method_calls(self,funcname):
        call_methods_list = set()
        try:
            for fi in funcname.refs("call"):
                if( fi.ent().library()!="Standard"):
                    call_methods_list.add(fi.ent())
            return call_methods_list
        except:
            return call_methods_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_cc(self,db,funcname):
        try:
            if(self.is_private(funcname)):
                return None
            else:
                refset = set()
                for callint in funcname.refs("callby"):
                    refset.add(callint.ent().parent())
                return len((refset))
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def give_Methods_that_the_measured_class_calls(self,classname):
        # create a list and return it:Includes all Methods entity(also cunstructor method ) that the measured method calls
        call_methods_list = list()
        try:
            for fi in classname.refs("call"):
                # if namespace == method namespace
                if (fi.ent().parent().parent() == classname.parent()  ):
                    call_methods_list.append(fi.ent())
            return call_methods_list
        except:
            return call_methods_list
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgCyclomatic(self,funcname):
        try:
            if(self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgCyclomatic"])["AvgCyclomatic"]
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgCyclomaticModified(self,funcname):
        try:
            if(self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgCyclomaticModified"])["AvgCyclomaticModified"]
        except:
            return None
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgCyclomaticStrict(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgCyclomaticStrict"])["AvgCyclomaticStrict"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgEssential(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgEssential"])["AvgEssential"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgLine(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgLine"])["AvgLine"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgLineBlank(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgLineBlank"])["AvgLineBlank"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgLineCode(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgLineCode"])["AvgLineCode"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def AvgLineComment(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["AvgLineComment"])["AvgLineComment"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountClassBase(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountClassBase"])["CountClassBase"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountClassCoupled(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountClassCoupled"])["CountClassCoupled"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountClassCoupledModified(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountClassCoupledModified"])["CountClassCoupledModified"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountClassDerived(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountClassDerived"])["CountClassDerived"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclClassMethod(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclClassMethod"])["CountDeclClassMethod"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclClassVariable(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclClassVariable"])["CountDeclClassVariable"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclInstanceMethod(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclInstanceMethod"])["CountDeclInstanceMethod"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclInstanceVariable(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclInstanceVariable"])["CountDeclInstanceVariable"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethod(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethod"])["CountDeclMethod"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethodAll(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethodAll"])["CountDeclMethodAll"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethodDefault(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethodDefault"])["CountDeclMethodDefault"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethodPrivate(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethodPrivate"])["CountDeclMethodPrivate"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethodProtected(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethodProtected"])["CountDeclMethodProtected"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def CountDeclMethodPublic(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["CountDeclMethodPublic"])["CountDeclMethodPublic"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxCyclomatic(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxCyclomatic"])["MaxCyclomatic"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxCyclomaticModified(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxCyclomaticModified"])["MaxCyclomaticModified"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxCyclomaticStrict(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxCyclomaticStrict"])["MaxCyclomaticStrict"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxEssential(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxEssential"])["MaxEssential"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def MaxInheritanceTree(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["MaxInheritanceTree"])["MaxInheritanceTree"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def PercentLackOfCohesion(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["PercentLackOfCohesion"])["PercentLackOfCohesion"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def PercentLackOfCohesionModified(self, funcname):
        try:
            if (self.is_abstract(funcname) or self.is_interface(funcname.parent())):
                return None
            else:
                return funcname.metric(["PercentLackOfCohesionModified"])["PercentLackOfCohesionModified"]
        except:
            return None

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def returt_result(self,db):
        self.get_metrics(db)
        return [self.class_metrics, self.method_metrics]
        # return a list consist of classes and methods and thier metrics value
#
# obj=cls_main()
# obj.main()
class cls_arangement:
    def class_metrics_arange(self,db):
        class_name=list();class_metric_values=list()
        class_metric_name = ['LOC',"LOCNAMM","WMCNAMM","NOMNAMM","TCC","ATFD","WOC","NOAM","NOPA", 'AvgCyclomatic', 'AvgCyclomaticModified', 'AvgCyclomaticStrict', 'AvgEssential',
                             'AvgLine', 'AvgLineBlank', 'AvgLineCode', 'AvgLineComment', 'CountClassBase', 'CountClassCoupled', 'CountClassCoupledModified',
                             'CountClassDerived', 'CountDeclClassMethod', 'CountDeclClassVariable', 'CountDeclInstanceMethod','CountDeclInstanceVariable', 'CountDeclMethod',
                             'CountDeclMethodAll', 'CountDeclMethodDefault','CountDeclMethodPrivate', 'CountDeclMethodProtected', 'CountDeclMethodPublic',
                             'CountLineBlank','CountLineCode', 'CountLineCodeDecl', 'CountLineCodeExe', 'CountLineComment', 'CountSemicolon', 'CountStmt','CountStmtDecl',
                             'CountStmtExe', 'MaxCyclomatic', 'MaxCyclomaticModified', 'MaxCyclomaticStrict','MaxEssential', 'MaxInheritanceTree', 'MaxNesting',
                             'PercentLackOfCohesion', 'PercentLackOfCohesionModified','RatioCommentToCode', 'SumCyclomatic', 'SumCyclomaticModified', 'SumCyclomaticStrict',
                             'SumEssential']

        # root = tk.Tk()

        print("getting classes metrics...")
        totalclasses= db.ents("class")
        bar = progressbar.ProgressBar(maxval=len(totalclasses),widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for cls in range(0,len(totalclasses)):
            if str(totalclasses[cls].library()) != "Standard":
                try:
                    if (self.is_abstract(totalclasses[cls]) or self.is_interface(totalclasses[cls].parent())):
                        continue
                    else:
                # if True:
                        class_name.append(str(totalclasses[cls].longname()))
                        class_metric_values.append(self.call_class_metrics(db,totalclasses[cls]))
                        bar.update(cls)
                except:
                    class_name.append(str(totalclasses[cls].longname()))
                    class_metric_values.append(self.call_class_metrics(db, totalclasses[cls]))
                    bar.update(cls)
        bar.finish()
        return [class_name,class_metric_name,class_metric_values]
        # return a list consist of classes and methods and thier metrics value

    def call_class_metrics(self,db,class_name):
        class_metrics_value=list()
        obj_get_metrics = cls_get_metrics()
        # the order of the following invokes code is based on class_metric_name list

        class_metrics_value.append(obj_get_metrics.LOC(class_name))
        class_metrics_value.append(obj_get_metrics.LOCNAMM(class_name))
        class_metrics_value.append(obj_get_metrics.WMCNAMM(class_name))
        class_metrics_value.append(obj_get_metrics.NOMNAMM(class_name))
        class_metrics_value.append(obj_get_metrics.TCC(class_name))
        class_metrics_value.append(obj_get_metrics.ATFD_CLASS(class_name))
        class_metrics_value.append(obj_get_metrics.WOC(class_name))
        class_metrics_value.append(obj_get_metrics.NOAM(class_name))
        class_metrics_value.append(obj_get_metrics.NOPA(class_name))
        class_metrics_value.append(obj_get_metrics.AvgCyclomatic(class_name))
        class_metrics_value.append(obj_get_metrics.AvgCyclomaticModified(class_name))
        class_metrics_value.append(obj_get_metrics.AvgCyclomaticStrict(class_name))
        class_metrics_value.append(obj_get_metrics.AvgEssential(class_name))
        class_metrics_value.append(obj_get_metrics.AvgLine(class_name))
        class_metrics_value.append(obj_get_metrics.AvgLineBlank(class_name))
        class_metrics_value.append(obj_get_metrics.AvgLineCode(class_name))
        class_metrics_value.append(obj_get_metrics.AvgLineComment(class_name))
        class_metrics_value.append(obj_get_metrics.CountClassBase(class_name))
        class_metrics_value.append(obj_get_metrics.CountClassCoupled(class_name))
        class_metrics_value.append(obj_get_metrics.CountClassCoupledModified(class_name))
        class_metrics_value.append(obj_get_metrics.CountClassDerived(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclClassMethod(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclClassVariable(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclInstanceMethod(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclInstanceVariable(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethod(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethodAll(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethodDefault(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethodPrivate(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethodProtected(class_name))
        class_metrics_value.append(obj_get_metrics.CountDeclMethodPublic(class_name))
        class_metrics_value.append(obj_get_metrics.CountLineBlank(class_name))
        class_metrics_value.append(obj_get_metrics.CountLineCode(class_name))
        class_metrics_value.append(obj_get_metrics.CountLineCodeDecl(class_name))
        class_metrics_value.append(obj_get_metrics.CountLineCodeExe(class_name))
        class_metrics_value.append(obj_get_metrics.CountLineComment(class_name))
        class_metrics_value.append(obj_get_metrics.CountSemicolon(class_name))
        class_metrics_value.append(obj_get_metrics.CountStmt(class_name))
        class_metrics_value.append(obj_get_metrics.CountStmtDecl(class_name))
        class_metrics_value.append(obj_get_metrics.CountStmtExe(class_name))
        class_metrics_value.append(obj_get_metrics.MaxCyclomatic(class_name))
        class_metrics_value.append(obj_get_metrics.MaxCyclomaticModified(class_name))
        class_metrics_value.append(obj_get_metrics.MaxCyclomaticStrict(class_name))
        class_metrics_value.append(obj_get_metrics.MaxEssential(class_name))
        class_metrics_value.append(obj_get_metrics.MaxInheritanceTree(class_name))
        class_metrics_value.append(obj_get_metrics.MAXNESTING(class_name))
        class_metrics_value.append(obj_get_metrics.PercentLackOfCohesion(class_name))
        class_metrics_value.append(obj_get_metrics.PercentLackOfCohesionModified(class_name))
        class_metrics_value.append(obj_get_metrics.RatioCommentToCode(class_name))
        class_metrics_value.append(obj_get_metrics.SumCyclomatic(class_name))
        class_metrics_value.append(obj_get_metrics.SumCyclomaticModified(class_name))
        class_metrics_value.append(obj_get_metrics.SumCyclomaticStrict(class_name))
        class_metrics_value.append(obj_get_metrics.SumEssential(class_name))


        return class_metrics_value

    def method_metrics_arange(self,db):
        method_name=list();method_metric_values=list()
        method_metric_name = ["LOC","CYCLO","MAXNESTING","NOLV","ATLD","CC","CM","FANOUT","CINT","CDISP",
                              'CountInput', 'CountLineBlank', 'CountLineCode', 'CountLineCodeDecl', 'CountLineCodeExe',
                                'CountLineComment', 'CountOutput', 'CountPath', 'CountPathLog', 'CountSemicolon', 'CountStmt',
                              'CountStmtDecl','CountStmtExe', 'CyclomaticModified', 'CyclomaticStrict',
                              'Essential', 'Knots','MaxEssentialKnots', 'MinEssentialKnots', 'RatioCommentToCode',
                              'SumCyclomatic', 'SumCyclomaticModified', 'SumCyclomaticStrict', 'SumEssential','NOPL']


        print("\n getting methods metrics...")
        totalmethods = db.ents("method")
        bar2 = progressbar.ProgressBar(maxval=len(totalmethods), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar2.start()
        for mth in range(0,len(totalmethods)):
            if str(totalmethods[mth].library()) != "Standard":
                try:
                    if (self.is_abstract(totalmethods[mth]) or self.is_interface(totalmethods[mth].parent())):
                        continue
                    else:
            # if True:
                        method_name.append(str(totalmethods[mth].longname()))
                        method_metric_values.append(self.call_method_metrics(db,totalmethods[mth]))
                        bar2.update(mth)
                except:
                    method_name.append(str(totalmethods[mth].longname()))
                    method_metric_values.append(self.call_method_metrics(db, totalmethods[mth]))
                    bar2.update(mth)
        bar2.finish()
        return [method_name,method_metric_name,method_metric_values]
        # self.get_metrics(db)
        # return [self.method_metrics, self.method_metrics]
        # return a list consist of methodes and methods and thier metrics value
    def call_method_metrics(self,db,method_name):
        method_metrics_value=list()
        obj_get_metrics = cls_get_metrics()
        #the order of the following invokes code is based on method_metric_name list
        method_metrics_value.append(obj_get_metrics.LOC(method_name))
        method_metrics_value.append(obj_get_metrics.CYCLO(method_name))
        method_metrics_value.append(obj_get_metrics.MAXNESTING(method_name))
        method_metrics_value.append(obj_get_metrics.NOLV(method_name))
        method_metrics_value.append(obj_get_metrics.ATLD(db,method_name))
        method_metrics_value.append(obj_get_metrics.give_cc(db,method_name))
        method_metrics_value.append(obj_get_metrics.CM(method_name))
        method_metrics_value.append(obj_get_metrics.FANOUT_OUR(method_name))
        method_metrics_value.append(obj_get_metrics.CINT(method_name))
        method_metrics_value.append(obj_get_metrics.CDISP(method_name))
        method_metrics_value.append(obj_get_metrics.CountInput(method_name))
        method_metrics_value.append(obj_get_metrics.CountLineBlank(method_name))
        method_metrics_value.append(obj_get_metrics.CountLineCode(method_name))
        method_metrics_value.append(obj_get_metrics.CountLineCodeDecl(method_name))
        method_metrics_value.append(obj_get_metrics.CountLineCodeExe(method_name))
        method_metrics_value.append(obj_get_metrics.CountLineComment(method_name))
        method_metrics_value.append(obj_get_metrics.CountOutPut(method_name))
        method_metrics_value.append(obj_get_metrics.CountPath(method_name))
        method_metrics_value.append(obj_get_metrics.CountPathLog(method_name))
        method_metrics_value.append(obj_get_metrics.CountSemicolon(method_name))
        method_metrics_value.append(obj_get_metrics.CountStmt(method_name))
        method_metrics_value.append(obj_get_metrics.CountStmtDecl(method_name))
        method_metrics_value.append(obj_get_metrics.CountStmtExe(method_name))
        method_metrics_value.append(obj_get_metrics.CyclomaticModified(method_name))
        method_metrics_value.append(obj_get_metrics.CyclomaticStrict(method_name))
        method_metrics_value.append(obj_get_metrics.Essential(method_name))
        method_metrics_value.append(obj_get_metrics.Knots(method_name))
        method_metrics_value.append(obj_get_metrics.MaxEssentialKnots(method_name))
        method_metrics_value.append(obj_get_metrics.MinEssentialKnots(method_name))
        method_metrics_value.append(obj_get_metrics.RatioCommentToCode(method_name))
        method_metrics_value.append(obj_get_metrics.SumCyclomatic(method_name))
        method_metrics_value.append(obj_get_metrics.SumCyclomaticModified(method_name))
        method_metrics_value.append(obj_get_metrics.SumCyclomaticStrict(method_name))
        method_metrics_value.append(obj_get_metrics.SumEssential(method_name))
        method_metrics_value.append(obj_get_metrics.NOPL(method_name))

        return method_metrics_value

    def return_results(self,db):
        return([self.class_metrics_arange(db),self.method_metrics_arange(db)])

    def returnClassMetrics(self,db):
        return self.class_metrics_arange(db)

    def returnMethodMetrics(self,db):
        return self.method_metrics_arange(db)