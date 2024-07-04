from tabulate import tabulate

class Express:
    def __init__(self):
        self.Route={
        "Minstowe" : {"Cowstone": 3},
        "Oldcastle" : {"New North": 5, "Freeham": 2},
        "Cowstone": {"New North": 4, "Bingborough": 6, "Donningpool": 7, "HighBrook": 5},
        "New North": {"Bingborough": 3, "Donningpool": 6, "Wington": 4, "Highbrook": 2},
        "Freeham": {"Cowstone": 2, "Donningpool": 3, "Wingtown": 5},
        "Bingborough": {"Donningpool": 2, "Highbrook":1},
        "Donningpool": {"Wingtown": 4,"Highbrook": 5, "Old Mere": 2}
        }
        
        self.Train = {
            "Economy" : [25, 20],
            "Business" : [30, 30],
            "Exclusive" : [35, 40]
        }
        
        self.Home()
        
    def Home(self):
        while True:
            print()
            print("Welcome to Ajarin Dong Puh Express")
            print("="*20)
            print("1. Order Ticket")
            print("2. View Routes")
            print("3. View Train")
            print("4. Exit")
            print("="*20)
            menuchoice = input("Choose(1 - 4): ")
            if int(menuchoice) < 1 or int(menuchoice) > 4:
                print("Menu yang Anda masukkan tidak sesuai")
            else:
                if menuchoice == '1':
                    self.OrderTickets()
                if menuchoice == '2':
                    self.ShowRoutes()
                if menuchoice == '3':
                    self.ViewTrain()
                if menuchoice == '4':
                    print("Anjazzzz Slebew")
                    break

    def OrderTickets(self):
        print("menu satu jalan")
        n = input()
    
    def ShowRoutes(self):
        while True:
            print("Menu dua jalan")
            print("cost = $15/hour")
            untuk= []
            for dari, dicttujuan in self.Route.items():
                for tujuan, weight in dicttujuan.items():
                    untuk.append([f"{dari} -- {tujuan}", weight])
            table = tabulate(untuk, headers= ["Routes (2-ways)", "Jaraklah", "Duration(hours)"], tablefmt = "psql", colalign=("left", "center"))
            print(table)
            print("Take Your Route")
            print("=" *10)
            dari = input("From: ")
            kemana = input("To: ")
            print("See another Route?")
            menu2choice = input("Yes/No = ").lower()
            if menu2choice == "no": break
            
    def ViewTrain(self):
        while True:
            data = []
            for kelas  in self.Train.items():
                data.append([kelas[0], kelas[1][0], kelas[1][1]])
            table = tabulate (data, headers= ["Class", "Max Capacity (kg)", "Cost ($)"], tablefmt = "psql", colalign=("left", "center", "center"))
            print(table)
            
            print("We can help you choose what to bring, do you want to try?")
            choose = input("Yes/No = ").lower()
            
            if choose == "yes":
                item_take = []
                total_weight = 0
                item = []
                
                while True:
                    kelas_pilihan = input("Choose Class: ").capitalize()
                    if kelas_pilihan in self.Train:
                        break
                    print(f"Kelas {kelas_pilihan} Tidak Ditemukan")
                
                weight_current = self.Train[kelas_pilihan][0]
                print("Give your item priority scale from 1 (very inportant) to 5 (not important)")
                
                n = int(input("How many things you want to bring?"))
                for i in range(n):
                    name = input(f"Item - {i + 1} : ")
                    weight = int(input(f"Weight(kg) : "))
                    priority = int(input(f"Priority : "))
                    item.append([name,weight,priority])
                    print()
                
                choice = input("Can Your Items be Divided Into Parts ? (Yes / No) : ").lower()
                print("We Recommend You To Bring")
                if choice == "no":
                    item.sort(key = lambda x : (x[2], x[1]))
                    for i in range(n):
                        if weight_current >= item[i][1]:
                            weight_current -= item[i][1]
                            total_weight += item[i][1]
                            item_take.append(item[i][0])
                    if len(item_take) != len(item):
                        for i in range(len(item_take)):
                            print(f"{i + 1}. {item_take[i]}")
                        
                elif choice == "yes":
                    item.sort(key = lambda x : (-(x[1] / x[2]), x[2]))
                    for i in range(n):
                        if weight_current >= item[i][1]:
                            weight_current -= item[i][1]
                            total_weight += item[i][1]
                            item_take.append((item[i][0], "WHOLE"))
                        elif weight_current < item[i][1] and weight_current != 0:
                            item_take.append((item[i][0], f"{weight_current}/{item[i][1]}"))
                            total_weight += weight_current
                            weight_current -= weight_current
                            
                    if len(item_take) != len(item):
                        for i in range(len(item_take)):
                            print(f"{i + 1}. {item_take[i][0]} ({item_take[i][1]})")
                
                print(f"With Total Weight : {total_weight}")
                if len(item) == len(item_take): print(f"You Can Carry All of Your Items")
                else: print("You Can Use Our Recommendation or Choose Another Class to Carry More")
                loop = input("\nTry Another Class ? (Yes / No) : ").lower()
                if loop == "no": break
                    
            else: break

Express()

'''
3
yes
economy
5
Books
10
1
Clothes
12
1
Snacks
4
4
Souvenir
3
2
Cosmetic
1
3
no

#2
3
yes
economy
5
Books
10
1
CLothes
12
1
Snacks
4
4
Cosmetic
2
2
Souvenir
1
3
yes
'''