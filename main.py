class adfgvx():
    lang="W"
    def CookRawString(self,rawstring):
            cookedstring=""
            reple = [["a","á","ä","Á","Ä"],["b"],["č","ć","c","Č","Ć"],["d","ď","Ď"],["ě","é","e","ë","Ě","É","Ë"],["f"],["g"],["h"],["i","í","ï","Í","Ï"],["j"],["k"],["l","ĺ","Ĺ"],["m"],["n","ň","ń","Ň","Ń"],["o","ó","ö","Ó","Ö"],["p"],["q"],["r","ř","ŕ","Ř","Ŕ"],["š","ś","s","Š","Ś"],["t","ť","Ť"],["u","ú","ů","Ů","Ú"],["v"],["w"],["x"],["y","ý","ÿ","Ý","Ÿ"],["z","ž","ź","Ž","Ź"]]
            forThing = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            for i in range(0,len(rawstring)):
                if rawstring[i]<"A" or rawstring[i]>"Z":
                    if rawstring[i]==" ":
                        cookedstring+="MEZERA"
                    else:
                        if rawstring[i]==chr(ord(self.lang)+32):
                            if self.lang=="W":
                                cookedstring+="V"
                            if self.lang=="J":
                                cookedstring+="I"
                        else:
                            for j in range(0, len(reple)):
                                if rawstring[i] in reple[j]:
                                    cookedstring+=forThing[j]
                else:
                    if rawstring[i]==self.lang:
                        if self.lang=="W":
                            cookedstring+="V"
                        if self.lang=="J":
                            cookedstring+="I"
                    else:
                        cookedstring+=rawstring[i]
            return cookedstring
        
    
    def Substituce(self,cookedstring,table):
        burnedstring=""
        tablecord=["AA","AD","AF","AG","AX","DA","DD","DF","DG","DX","FA","FD","FF","FG","FX","GA","GD","GF","GG","GX","XA","XD","XF","XG","XX"]
        tablecordV=["AA","AD","AF","AG","AV","AX","DA","DD","DF","DG","DV","DX","FA","FD","FF","FG","FV","FX","GA","GD","GF","GG","GV","GX","VA","VD","VF","VG","VV","VX","XA","XD","XF","XG","XV","XX"]
        for i in range(0,len(cookedstring)):
            for j in range(0,len(table)):
                if cookedstring[i]==table[j]:
                    burnedstring+=tablecord[j]
                    break
        return burnedstring
    
    def Transpozice(self,key,burnedstring):
        x=len(key)
        keyL=[]
        sloupce=[]
        for i in range(0,x):
            keyL.append([key[i]])
        for i in range(0,x):
            sloupce.append([])
        for i in range(0,len(burnedstring)):
            for j in range(0,x):
                if i%x==j:
                    sloupce[j]+=burnedstring[i]
        print(sloupce)
        for i in range(1,x):
            for j in range(0,i):
                if keyL[i]<keyL[j]:
                    keyL.insert(j,keyL.pop(i))
                    sloupce.insert(j,sloupce.pop(i))
        return sloupce
                
                
####
testin="ahojpepojaksemas"
testinstance=adfgvx()
testout=testinstance.CookRawString(testin)
testtable="ERHPQZBGFOAMLNYXSDITVCKJU"
testoutdva=testinstance.Substituce(testout,testtable)
testouttri=testinstance.Transpozice("KOLOTOC",testoutdva)