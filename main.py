#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QFileDialog
from PyQt5 import QtGui, uic

qtCreatorFile = "dialog.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class adfgvx(QMainWindow, Ui_MainWindow):
    fullAbc={False: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", True: "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"}
    tablecord=[]
    tableLable=[]
    abcLoaded=[]
    lang="W"
    adfgvx=False

    def LableInit(self):
        self.tableLable = [
            [self.cl00,self.cl01,self.cl02,self.cl03,self.cl04,self.cl05],
            [self.cl10,self.cl11,self.cl12,self.cl13,self.cl14,self.cl15],
            [self.cl20,self.cl21,self.cl22,self.cl23,self.cl24,self.cl25],
            [self.cl30,self.cl31,self.cl32,self.cl33,self.cl34,self.cl35],
            [self.cl40,self.cl41,self.cl42,self.cl43,self.cl44,self.cl45],
            [self.cl50,self.cl51,self.cl52,self.cl53,self.cl54,self.cl55]
        ]
    def NullTable(self):
        for i in range(0,len(self.tableLable)):
            for j in range(0,len(self.tableLable[i])):
                self.tableLable[i][j].setText("")
    def IsLetterThere(self,letter):
        no = False
        for j in range(0,len(self.abcLoaded)):
            if letter == self.abcLoaded[j]:
                no = True
                continue
        return no
    def FillTable(self):
        localAbc = self.CookRawString(self.fullAbc[self.adfgvx])
       
        for i in range(0,len(self.fullAbc[self.adfgvx])):
            letter = self.CookRawString(localAbc[i])

            if(not self.IsLetterThere(letter)):
                self.abcLoaded.append(localAbc[i])
    def LoadAbc(self):
        self.abcLoaded = []
        tempAbc = self.CookRawString(self.abc.text())
        for i in range(0,len(tempAbc)):
            # Check for duplications

            if(not self.IsLetterThere(tempAbc[i])):
                self.abcLoaded.append(tempAbc[i])

        self.FillTable()
        size = 5
        if self.adfgvx:
            size = 6
        for i in range(0, len(self.abcLoaded)):
            self.tableLable[math.floor(i/size)][i%size].setText(self.abcLoaded[i])

    def TableSize(self): #Checkbox
        if self.adfgvx:
            self.tablecord=["AA","AD","AF","AG","AX","DA","DD","DF","DG","DX","FA","FD","FF","FG","FX","GA","GD","GF","GG","GX","XA","XD","XF","XG","XX"]
        else:
            self.tablecord=["AA","AD","AF","AG","AV","AX","DA","DD","DF","DG","DV","DX","FA","FD","FF","FG","FV","FX","GA","GD","GF","GG","GV","GX","VA","VD","VF","VG","VV","VX","XA","XD","XF","XG","XV","XX"]
    
    def CookRawString(self,rawstring):
            cookedstring=""
            reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
            forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            for i in range(0,len(rawstring)):
                if rawstring[i]<"A" or rawstring[i]>"Z":
                    if rawstring[i]==" ":
                        cookedstring+="MEZERA"
                    else:
                        if rawstring[i]==chr(ord(self.lang)+32) and (not self.adfgvx):
                            if self.lang=="W":
                                cookedstring+="V"
                            if self.lang=="J":
                                cookedstring+="I"
                        elif rawstring[i].isnumeric() and self.adfgvx: 
                            cookedstring+=rawstring[i];       
                        else:
                            for j in range(0, len(reple)):
                                if rawstring[i] in reple[j]:
                                    cookedstring+=forThing[j]
                else:
                    if rawstring[i]==self.lang and (not self.adfgvx):
                        if self.lang=="W":
                            cookedstring+="V"
                        if self.lang=="J":
                            cookedstring+="I"
                    else:
                        cookedstring+=rawstring[i]
            return cookedstring
        
    
    def Sifrovat(self):
        table = self.abcLoaded
        cookedstring=self.CookRawString(self.input.toPlainText())
        #substituce
        burnedstring=""
        for i in range(0,len(cookedstring)):
            for j in range(0,len(table)):
                if cookedstring[i]==table[j]:
                    burnedstring+=self.tablecord[j]
                    break
        print(burnedstring)
        key=self.CookRawString(self.key.text())
        #transpozice
        x=len(key)
        keyL=[]
        sloupce=[]
        for i in range(0,x):
            keyL.append(key[i])
        for i in range(0,x):
            sloupce.append([])
        for i in range(0,len(burnedstring)):
            for j in range(0,x):
                if i%x==j:
                    sloupce[j]+=burnedstring[i]
        print(sloupce)
        while len(sloupce[-1])==0:
            sloupce.pop()
            keyL.pop()
        for i in range(1,len(keyL)):
            for j in range(0,i):
                if keyL[i]<keyL[j]:
                    keyL.insert(j,keyL.pop(i))
                    sloupce.insert(j,sloupce.pop(i))
        burnedstring=""
        for i in range(0,len(sloupce)-1):
            for j in range(0,len(sloupce[i])):
                burnedstring+=sloupce[i][j]
            burnedstring+=" "
        for j in range(0,len(sloupce[-1])):
                burnedstring+=sloupce[-1][j]
        #return [sloupce,keyL]
        #print(sloupce)
        self.output.setText(burnedstring)
        #return burnedstring
    
    def Desifrovat(self,instring):
        table = self.abcLoaded
        instring = self.input.toPlainText()
        #instring=self.CookRawString(instring)
        key=self.CookRawString(self.key.text())
        x=(len(instring)-instring.count(" "))
        if x<len(key):
            key=key[0:x]
        x=len(key)
        sloupce=[]
        for i in range(0,x):
            sloupce.append([])
        j=0
        for i in range(x):
            while instring[j]!=" ":
                sloupce[i].append(instring[j])
                j+=1
                if j==len(instring):
                    break
            j+=1
        keyL=[]
        for i in range(0,x):
            keyL.append(key[i])
        keyL.sort()
        #transpozice
        x=len(key)
        for i in range(0,x):
            for j in range(i,x):
                if key[i]==keyL[j]:
                    keyL.insert(i,keyL.pop(j))
                    sloupce.insert(i,sloupce.pop(j))
                    break
        string=""
        for i in range(0,len(sloupce[0])):
            while len(sloupce[-1])==0:
                sloupce.pop()
            for j in range(0,len(sloupce)):
                string+=sloupce[j].pop(0)
        #print(string)
        #substituce
        outstring=""
        for i in range(0,len(string),2):
            outstring+=table[self.tablecord.index(string[i]+string[i+1])]
        self.output.setText(outstring)

    def switchLangAction(self):
        if self.lang == "W":
            self.lang = "J"
            self.switchLang.setText("Přepnout do CZ")
            
        else:
            self.lang ="W"
            self.switchLang.setText("Přepnout do EN")
        self.LoadAbc()
        self.abc.setText("".join(self.abcLoaded))
        
    def switchSizeAction(self):
        self.NullTable()
        if self.adfgvx:
            self.switchSize.setText("Přepnout do ADFVGX")
        else:
            self.switchSize.setText("Přepnout do ADFGX")

        self.adfgvx = not self.adfgvx
        self.LoadAbc()
        self.abc.setText("".join(self.abcLoaded))

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.LableInit()
        self.TableSize()
        self.abc.textChanged.connect(self.LoadAbc)
        self.switchLang.clicked.connect(self.switchLangAction)
        self.switchSize.clicked.connect(self.switchSizeAction)
        self.code.clicked.connect(self.Sifrovat)
        self.decode.clicked.connect(self.Desifrovat)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = adfgvx()
    window.show()
    sys.exit(app.exec_())
####
