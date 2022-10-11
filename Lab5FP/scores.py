from datetime import date

class Score:
    def __init__(self,f):
        self.__f = f

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self,f):
        self.__f = f

    def add_score(self,round,name,money):
        f2 = open(self.__f,"a")
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        text2 = str(d1) + "," + str(round) + "," + str(name) + "," + str(money) + "\n"
        f2.write(text2)
        f2.close()

    def write_scores(self):
        f2 = open(self.__f,"r")
        lines = f2.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()
        lines.sort(key = lambda x:int(x.split(",")[3]),reverse=True)
        """
        for i in range(len(lines)):
            for j in range(i+1,len(lines)):
                x1 = lines[i].split(",")[3]
                x2 = lines[j].split(",")[3]
                if int(x1) < int(x2):
                    aux = lines[i]
                    lines[i] = lines[j]
                    lines[j] = aux
                    print(x1,x2)
                print(x1)
                print(x2)
        """
        for x in lines:
            print(x)
