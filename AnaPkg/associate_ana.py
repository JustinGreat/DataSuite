#encoding=utf-8
from data_analysis import *
from itertools import combinations
def comb(lst):
    ret=[]
    for i in range(1,len(lst)+1):
        ret+=list(combinations(lst,i))
    return ret
class AprLayer(object):
    d=dict()
    def __init__(self):
        self.d=dict()
class AprNode(object):
    s=set()
    size=0
    num=0
    lnk_nodes=dict()
    def __init__(self,node):
        self.s=set(node)
        self.size=len(self.s)
        self.lnk_nodes=dict()
        self.num=0
    def __hash__(self):
        return hash("__".join(sorted([str(itm) for itm in list(self.s)])))
    def __eq__(self, other):
        if "__".join(sorted([str(itm) for itm in list(self.s)]))=="__".join(sorted([str(itm) for itm in list(other.s)])):
            return True
        return False
    def isSubnode(self,node):
        return self.s.issubset(node.s)
    def incNum(self,num=1):
        self.num+=num
    def addLnk(self,node):
        self.lnk_nodes[node]=node.s

class AprBlk():
    apr_layers=dict()
    data_num=0
    def __init__(self,data):
        cnt=0
        self.data_num=len(data)
        for datum in data:
            cnt+=1
            datum=comb(datum)
            nodes=[AprNode(da) for da in datum]
            for node in nodes:
                if not node.size in self.apr_layers:
                    self.apr_layers[node.size]=AprLayer()
                if not node in self.apr_layers[node.size].d:
                    self.apr_layers[node.size].d[node]=node
                self.apr_layers[node.size].d[node].incNum()
            for node in nodes:
                if node.size==1:
                    continue
                for sn in node.s:
                    sub_n=AprNode(node.s-set([sn]))
                    self.apr_layers[node.size-1].d[sub_n].addLnk(node)
            #
            #max_size=max(list(self.apr_layers.keys()))
            #for i in range(1,max_size):
            #    for subnode in self.apr_layers[i].d:
            #        for bignode in self.apr_layers[i+1].d:
            #            if subnode.isSubnode(bignode):
            #                subnode.addLnk(bignode)
    def getFreqItems(self,thd=1,hd=1):
        freq_items=[]
        for layer in self.apr_layers:
            for node in self.apr_layers[layer].d:
                if self.apr_layers[layer].d[node].num<thd:
                    continue
                freq_items.append((self.apr_layers[layer].d[node].s,self.apr_layers[layer].d[node].num))
        freq_items.sort(key=lambda x:x[1],reverse = True)
        return freq_items[:hd]

    def getConf(self,low=True, h_thd=10, l_thd=1, hd=1):
        confidence = []
        for layer in self.apr_layers:
            for node in self.apr_layers[layer].d:
                if self.apr_layers[layer].d[node].num < h_thd:
                    continue
                for lnk_node in node.lnk_nodes:
                    if lnk_node.num < l_thd:
                        continue
                    conf = float(lnk_node.num) / float(node.num)
                    confidence.append([node.s, node.num, lnk_node.s, lnk_node.num, conf])

        confidence.sort(key=lambda x: x[4])
        if low:
            return confidence[:hd]
        else:
            return confidence[-hd::-1]

class AssctAnaClass(DataAnaClass):
    data=[]
    apr_blk=""
    def __init__(self,data):
        self.data=data
        self.apr_blk=AprBlk(data)
    def processData(self,cmd,thd=1,hd=1):
        if not cmd in ["freq_item","low_conf","high_conf"]:
            print("CMD Error!")
            return
        if cmd=="freq_item":
            return self.apr_blk.getFreqItems(thd=thd,hd=hd)
        if cmd=="low_conf":
            return self.apr_blk.getConf(h_thd=thd,l_thd=thd,hd=hd)
        if cmd=="high_conf":
            return self.apr_blk.getConf(low=False,h_thd=thd,l_thd=thd)