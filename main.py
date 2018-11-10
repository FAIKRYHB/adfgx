class adfgvx():
    tablecord=[]
    lang="W"
    def TableSize(self,bit): #Checkbox
        if bit:
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
                        if self.tablecord==25 and rawstring[i]==chr(ord(self.lang)+32):
                            if self.lang=="W":
                                cookedstring+="V"
                            if self.lang=="J":
                                cookedstring+="I"
                        else:
                            for j in range(0, len(reple)):
                                if rawstring[i] in reple[j]:
                                    cookedstring+=forThing[j]
                else:
                    if self.tablecord==25 and rawstring[i]==self.lang:
                        if self.lang=="W":
                            cookedstring+="V"
                        if self.lang=="J":
                            cookedstring+="I"
                    else:
                        cookedstring+=rawstring[i]
            return cookedstring
        
    
    def Sifrovat(self,cookedstring,key,table):
        #substituce
        burnedstring=""
        for i in range(0,len(cookedstring)):
            for j in range(0,len(table)):
                if cookedstring[i]==table[j]:
                    burnedstring+=self.tablecord[j]
                    break
        #print(burnedstring)
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
        #print(sloupce)
        for i in range(1,x):
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
        return burnedstring
    
    def Desifrovat(self,instring,key,table):
        x=len(key)
        sloupce=[]
        for i in range(0,x):
            sloupce.append([])
        len(testoutdva)
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
        return outstring

####
testin="ahojpepojaksemas"
testinstance=adfgvx()
testinstance.TableSize(True)
testout=testinstance.CookRawString(testin)
testtable="ERHPQZBGFOAMLNYXSDITVCKJU"
testoutdva=testinstance.Sifrovat(testout,"KOLOTOC",testtable)
Detest=testinstance.Desifrovat(testoutdva,"KOLOTOC",testtable)