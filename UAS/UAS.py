from tabulate import tabulate
import math
import random
import string
import sys

class Express:
    def __init__(self):
        self.Route={
        "Minstowe" : {"Cowstone": 3},
        "Oldcastle" : {"New North": 5, "Freeham": 2},
        "Cowstone": {"New North": 4, "Bingborough": 6, "Donningpool": 7, "HighBrook": 5},
        "New North": {"Bingborough": 3, "Donningpool": 6, "Wington": 4, "Highbrook": 2},
        "Freeham": {"Cowstone": 2, "Donningpool": 3, "Wington": 5},
        "Bingborough": {"Donningpool": 2, "Highbrook":1},
        "Donningpool": {"Wington": 4,"Highbrook": 5, "Old Mere": 2}
        }
        
        self.FullRoute = {
            "Minstowe" : {"Cowstone": 3},
            "Oldcastle" : {"New North": 5, "Freeham": 2},
            "Cowstone": {"New North": 4, "Bingborough": 6, "Donningpool": 7, "Highbrook": 5, "Minstowe": 3, "Freeham": 2},
            "New North": {"Bingborough": 3, "Donningpool": 6, "Wington": 4, "Highbrook": 2, "Oldcastle": 5, "Cowstone": 4},
            "Freeham": {"Cowstone": 2, "Donningpool": 3, "Wington": 5, "Oldcastle": 2},
            "Bingborough": {"Donningpool": 2, "Highbrook":1, "Cowstone": 6, "New North": 3},
            "Donningpool": {"Wington": 4,"Highbrook": 5, "Old Mere": 2, "Cowstone": 7, "New North": 6, "Freeham": 3, "Bingborough": 2},
            "Highbrook": {"Cowstone": 5, "New North": 2, "Bingborough":1, "Donningpool": 5 },
            "Wington": {"New North": 4, "Freeham": 5, "Donningpool":4},
            "Old Mere": {"Donningpool": 2}
        }
        
        self.Train = {
            "Economy" : [25, 20],
            "Business" : [30, 30],
            "Exclusive" : [35, 40]
        }
        
        self.Home()
    
    class Graph:
        def __init__(self, nodes, init_graph):
            self.nodes = nodes
            self.graph = self.construct_graph(nodes, init_graph)

        def construct_graph(self, nodes, init_graph):
            graph = {node: {} for node in nodes}
            graph.update(init_graph)

            for node, edges in graph.items():
                for adjacent_node, value in edges.items():
                    if not graph[adjacent_node].get(node, False):
                        graph[adjacent_node][node] = value
            return graph

        def get_nodes(self):
            return self.nodes

        def get_outgoing_edges(self, node):
            return list(self.graph[node].keys())
        
        def value(self, node1, node2):
            return self.graph[node1][node2]

    def dijkstra(self, graph, start_node, target_node):
        unvisited_nodes = list(graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize

        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
            
            if current_min_node == target_node:
                break

            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path
    
    def print_result(self, previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        path.append(start_node)
        print(" -> ".join(reversed(path)))
        print(f"Duration: {shortest_path[target_node]} hours")
        
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
            if menuchoice.isdigit():
                if int(menuchoice) < 1 or int(menuchoice) > 4:
                    print("Menu yang Anda masukkan tidak sesuai")
                else:
                    if menuchoice == '1':
                        self.OrderTickets()
                    elif menuchoice == '2':
                        self.ShowRoutes()
                    elif menuchoice == '3':
                        self.ViewTrain()
                    elif menuchoice == '4':
                        print('='*30)
                        print("||        TERIMAKASIH       ||")
                        print("|| MADE BY AJARIN DONG PUH  ||")
                        print('='*30)
                        enter = input()
                        return
                    else:
                        print('='*30)
                        print("|| FITUR TERSEBUT TIDAK ADA ||")
                        print('='*30)
                        print()
                        enter = input()
            else:
                print("Menu yang Anda masukkan tidak sesuai")

    def OrderTickets(self):
        while True:
            print("Make sure you already check your route before order the ticket.")
            print("Where do you wanna go?")
            
            while True:
                asal = input("From : ").title()
                tujuan = input("To : ").title()
                if asal in self.FullRoute and tujuan in self.FullRoute:
                    break
                else:
                    print("Your Routes Didn't Match")
                
            print(f"\nHere is the route from {asal} to {tujuan}: ")
            graph = self.Graph(self.FullRoute.keys(), self.FullRoute)
            previous_nodes, shortest_path = self.dijkstra(graph, asal, tujuan)
            self.shortest_path = shortest_path
            self.print_result(previous_nodes, shortest_path, asal, tujuan)
            
            while True:
                print("\nMake sure you already check your belongings before choosing class")
                kelas = input("Choose class (Economy, Business, Exclusive): ").capitalize()
                if kelas in self.Train.keys():
                    break
                else:
                    print(f"There are no {kelas} class")
            
            while True:
                print("\nPlease insert your data:")
                name = input("Name\t\t\t  : ")
                while True:
                    departdate = input("Departure date(DD/MM/YYYY): ")
                    if len(departdate) == 10:
                        try:
                            hari1, bulan1, tahun1 = map(int, departdate.split('/'))
                            break
                        except ValueError:
                            print("Wrong format, please enter a valid date.")
                    else:
                        print("Wrong format")
                while True:
                    departtime = input("Departure time(HH.MM)\t  : ")
                    if len(departtime) == 5:
                        try:
                            jam1, menit1 = map(int, departtime.split('.'))
                            break
                        except ValueError:
                            print("Input yang benar")
                    else:
                        print("Wrong format")
                confirm = input("Are you sure about all the data above?(yes/no) : ").lower()
                print()
                if confirm == "no":
                    continue
                else:
                    duration = shortest_path[tujuan]
                    totalCost = duration * 15 + self.Train[kelas][1]
                    jam = jam1 + duration
                    menit = menit1
                    hari = hari1
                    bulan = bulan1
                    tahun = tahun1

                    while jam >= 24:
                        jam -= 24
                        hari += 1
                        if bulan in [1, 3, 5, 7, 8, 10, 12] and hari > 31:
                            hari = 1
                            bulan += 1
                        elif bulan in [4, 6, 9, 11] and hari > 30:
                            hari = 1
                            bulan += 1
                        elif bulan == 2:
                            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):  # Leap year
                                if hari > 29:
                                    hari = 1
                                    bulan += 1
                            else:
                                if hari > 28:
                                    hari = 1
                                    bulan += 1
                        if bulan > 12:
                            bulan = 1
                            tahun += 1

                    date2 = f"{hari:02}/{bulan:02}/{tahun}"
                    time2 = f"{jam:02}:{menit:02}"

                    print(f"+{'-' * 63}+")
                    print(f"| TRAIN TICKET \t\t\t\t\t\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"| Origin\t| {asal}\t\t\t\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"| Date\t\t: {departdate}\t\tTIME\t: {departtime}\t\t|")
                    train = f"{random.randint(100, 999)}-{random.choice(string.ascii_uppercase)}"
                    print(f"| Train#\t: {train}\t\t\tCLASS\t: {kelas}\t|")
                    platform = f"{random.randint(1, 10):02}"
                    seat = f"{random.randint(1, 50):02}"
                    print(f"| PLATFORM\t: {platform}\t\t\tSEAT\t: {seat}\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"| DESTINATION\t| {tujuan}\t\t\t\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"| DATE\t: {date2}\t\t\tTIME\t: {time2}\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"| Passenger Name : {name}\t\t\t\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"Total Cost\t: ${totalCost}")

                    other = input("\nOrder another ticket? (yes/no) : ")
                    if other == "no":
                        return
                    else:
                        break
    
    def ShowRoutes(self):
        while True:
            print("cost = $15/hour")
            untuk= []
            for dari, dicttujuan in self.Route.items():
                for tujuan, weight in dicttujuan.items():
                    untuk.append([f"{dari} -- {tujuan}", weight])
            table = tabulate(untuk, headers= ["Routes (2-ways)", "Duration(hours)"], tablefmt = "psql", colalign=("left", "center"))
            print(table)
            print("Take Your Route")
            print("=" *10)
            asal = input("From : ").title()
            tujuan = input("To : ").title()
            
            if asal in self.FullRoute and tujuan in self.FullRoute:
                print(f"Here is the shortest route from {asal} to {tujuan}: ")
                graph = self.Graph(self.FullRoute.keys(), self.FullRoute)
                previous_nodes, shortest_path = self.dijkstra(graph, asal, tujuan)
                self.print_result(previous_nodes, shortest_path, asal, tujuan)
                print("\nSee another Route?")
                menu2choice = input("Yes/No = ").lower()
                if menu2choice == "no":
                    break
            else:
                print("Your Routes Didn't Match")
                space = input()
            
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
                item_all = True
                
                while True:
                    kelas_pilihan = input("Choose Class: ").capitalize()
                    if kelas_pilihan in self.Train:
                        break
                    print(f"Kelas {kelas_pilihan} Tidak Ditemukan")
                
                weight_current = self.Train[kelas_pilihan][0]
                print("Give your item priority scale from 1 (very inportant) to 5 (not important)")
                
                n = int(input("How many things you want to bring ? "))
                for i in range(n):
                    name = input(f"Item - {i + 1} : ")
                    weight = int(input(f"Weight(kg) : "))
                    priority = int(input(f"Priority : "))
                    item.append([name,weight,priority])
                    print()
                
                choice = input("Can Your Items be Divided Into Parts ? (Yes / No) : ").lower()
                
                if choice == "no":
                    item.sort(key = lambda x : (x[2], x[1]))
                    for i in range(n):
                        if weight_current >= item[i][1]:
                            weight_current -= item[i][1]
                            total_weight += item[i][1]
                            item_take.append(item[i][0])
                        else:
                            item_all = False
                    if not item_all and len(item_take) != 0:
                        print("We Recommend You To Bring :")
                        for i in range(len(item_take)):
                            print(f"{i + 1}. {item_take[i]}")
                        
                elif choice == "yes":
                    item.sort(key = lambda x : (-(x[1] / x[2]), x[2], x[1]))
                    for i in range(n):
                        if weight_current >= item[i][1]:
                            weight_current -= item[i][1]
                            total_weight += item[i][1]
                            item_take.append((item[i][0], "Whole"))
                        elif weight_current < item[i][1] and weight_current != 0:
                            item_all = False
                            fpb = math.gcd(weight_current, item[i][1])
                            item_take.append((item[i][0], f"{int(weight_current / fpb)}/{int(item[i][1] / fpb)}"))
                            total_weight += weight_current
                            weight_current -= weight_current
                    if not item_all and len(item_take) != 0:    
                        print("We Recommend You To Bring :")
                        for i in range(len(item_take)):
                            print(f"{i + 1}. {item_take[i][0]} ({item_take[i][1]} Parts)")
                        print(f"With Total Weight : {total_weight} Kg")
                    
                if len(item_take) == 0: 
                    print("You Can't Carry All of Your Belongings")
                    print("You Can Use Our Recommendation or Choose Another Class to Carry More")
                elif len(item) == len(item_take) and item_all: 
                    print(f"You Can Carry All of Your Items")
                else: 
                    print("You Can Use Our Recommendation or Choose Another Class to Carry More")
                loop = input("\nTry Another Class ? (Yes / No) : ").lower()
                
                if loop == "no": 
                    break
                    
            else: 
                break

Express()
