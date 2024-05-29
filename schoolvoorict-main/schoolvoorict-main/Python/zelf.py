import csv
lijst = []
apppath='klanten.csv'
with open(apppath,mode="r",newline='') as fileopen:
    fileread= csv.reader(fileopen)
    next(fileread)
    for lezer in fileread:
        lijst.append(lezer)
while True:
    vraag = input("van wie wilt je de factuur zien typ naam: ")
    totaalprijs = 0
    for regel in lijst:
        factuur=[]
        if vraag == regel[1]:
            producten=regel[3].split(',')
            for product1 in producten:
                prijs= product1.split('$')[1]
                prijs = prijs.split(')')[0]
                totaalprijs += float(prijs)

                naam = product1.split('(')[0]
                factuur.append((naam,prijs))
                print(naam,prijs)
            print("totaalprijs:",totaalprijs)