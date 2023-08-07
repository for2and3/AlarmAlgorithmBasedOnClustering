import numpy as np
import pandas as pd
import re

np.set_printoptions(threshold=np.inf)

class DataTreating():

    def __init__(self,filename):
        f = open(filename,'r',encoding='UTF-8')
        self.wa_data = f.read()
        self.filename = filename
        self.line_data = []
        self.dictionary = {
            'cpu.idle': '1',
            'cpu.iowait': '2',
            'cpu.guest': '3',
            'cpu.irq': '4',
            'cpu.softirq': '5',
            'cpu.nice': '6',
            'cpu.steal': '7',
            'cpu.switcher': '8',
            'cpu.system': '9',
            'cpu.user': '10',
            'df.bytes.free': '21',
            'df.bytes.free.percent': '22',
            'df.inodes.total': '23',
            'df.inodes.free': '24',
            'df.inodes.free.percent': '25',
            'df.sdf.statistics.total':'26',
            'df.statistics.used':'27',
            'df.statistics.used.percent':'28',
            'kernel.files.allocated': '41',
            'kernel.files.left':'42',
            'kernel.maxfiles':'43',
            'kernel.maxproc':'44',
            'mem.memfree.percent':'61',
            'mem.swapfree.percent':'62',
            'mem.swapused.percent':'63',
            'load.5min':'80',
            'load.15min':'90',
            'load.1min':'100',
        }
        self.dictionarylist = self.dictionary.keys()
        f.close()

    def GetTxtData(self):
        return self.wa_data

    def WarningID(self):
        # 最外层的报警id
        # "id":"s_14_7e90df919960ebe8ba296a2f3e7fcce4",
        s = r'd\":\"[0-9,A-z]+\",'
        pattern = re.compile(s,re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        point_id = []
        i = 0
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[6:listlen-1]
            #将报警终端转换为报警终端的id
            if warn_list not in point_id:
                point_id.append(warn_list)
                i += 1
            warn_lists.append(point_id.index(warn_list)+1)
        return warn_lists

    def StrategyID(self):
        # 报警策略的id
        # "strategy":{"id":14,"metric
        #,"strategy":{"id":12,"me
        s = r'y\":{\"id\":[0-9]+,\"m'
        pattern = re.compile(s,re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[9:listlen-3]
            warn_lists.append(warn_list)
        return warn_lists

    def Metric(self):
        # 报警策略的监控对象
        # "metric":"cpu.idle",
        s = r'ic\":\"[a-z|0-9|.]+\"'
        pattern = re.compile(s,re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[5:listlen-1]
            if warn_list in self.dictionarylist:
                warn_list = self.dictionary[warn_list]
            warn_lists.append(warn_list)
        return warn_lists

    def TqlID(self):
        # 报警群组的id
        # "tpl":{"id":13,"n
        s = r'tpl\":{\"id\":[0-9]+,\"n'
        pattern = re.compile(s,re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[11:listlen-3]
            warn_lists.append(warn_list)
        return warn_lists

    def EndPoint(self):
        # 报警终端
        # "endpoint":"VM-0-17-ubuntu",
        s = r'nt\":\"[^,]+,'
        pattern = re.compile(s, re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        point_id = []
        i = 0
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[5:listlen-2]
            #将报警终端转换为报警终端的id
            if warn_list not in point_id:
                point_id.append(warn_list)
                i += 1
            warn_lists.append(point_id.index(warn_list)+1)
        return warn_lists

    '''def EventTime(self):
        # 报警时间
        # "eventTime\":1588667880,\
        s = r'ime\\":[0-9]+,'
        pattern = re.compile(s, re.I)
        all_list = pattern.findall(self.wa_data)
        warn_lists = []
        for warn_list in all_list:
            listlen = len(warn_list)
            warn_list = warn_list[7:listlen-1]
            warn_lists.append(warn_list)
        return warn_lists'''

    def GetWarn(self):
        # 获得处理完的报警数据
        WID = self.WarningID()
        SID = self.StrategyID()
        Met = self.Metric()
        TID = self.TqlID()
        EPt = self.EndPoint()
        # ETe = self.EventTime()
        length = len(WID)
        if length == 0:
            return np.array(0)
        warn = np.array([WID[0], SID[0], Met[0], TID[0], EPt[0]])
        i = 1
        while i < length:
            row = np.array([WID[i],SID[i],Met[i],TID[i],EPt[i]])
            warn = np.row_stack((warn, row))
            i += 1
        return warn



    def returnwarn(self,order:list):
        f = open(self.filename,'r',encoding='UTF-8')
        line_data =[]
        for line in f:
            line_data.append(line)
        i = 0
        clu_data = []
        while i < len(order):
            clu_data.append(line_data[order[i]])
            i += 1
        return clu_data





if __name__ == "__main__":
    GetD = DataTreating('event_t2.txt')
    #print(GetD.GetTxtData())
    #print(GetD.WarningID())
    #print(GetD.StrategyID())
    #print(GetD.Metric())
    #print(GetD.TqlID())
    #print(GetD.EndPoint())
    print(GetD.GetWarn())
    #print(GetD.returnwarn([0,3,6]))

