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
        "Cowstone": {"New North": 4, "Bingborough": 6, "Donningpool": 7, "Highbrook": 5},
        "New North": {"Bingborough": 3, "Donningpool": 6, "Wingtown": 4, "Highbrook": 2},
        "Freeham": {"Cowstone": 2, "Donningpool": 3, "Wingtown": 5},
        "Bingborough": {"Donningpool": 2, "Highbrook":1},
        "Donningpool": {"Wingtown": 4,"Highbrook": 5, "Old Mere": 2}
        }
        
        self.FullRoute = {
            "Minstowe" : {"Cowstone": 3},
            "Oldcastle" : {"New North": 5, "Freeham": 2},
            "Cowstone": {"New North": 4, "Bingborough": 6, "Donningpool": 7, "Highbrook": 5, "Minstowe": 3, "Freeham": 2},
            "New North": {"Bingborough": 3, "Donningpool": 6, "Wingtown": 4, "Highbrook": 2, "Oldcastle": 5, "Cowstone": 4},
            "Freeham": {"Cowstone": 2, "Donningpool": 3, "Wingtown": 5, "Oldcastle": 2},
            "Bingborough": {"Donningpool": 2, "Highbrook":1, "Cowstone": 6, "New North": 3},
            "Donningpool": {"Wingtown": 4,"Highbrook": 5, "Old Mere": 2, "Cowstone": 7, "New North": 6, "Freeham": 3, "Bingborough": 2},
            "Highbrook": {"Cowstone": 5, "New North": 2, "Bingborough":1, "Donningpool": 5 },
            "Wingtown": {"New North": 4, "Freeham": 5, "Donningpool":4},
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
                    
    def OrderTickets(self):

        while True:
            print("Make sure you already check your route before order the ticket.")
            print("Where do you wanna go?")
            asal=input("From:")
            tujuan=input("To:")
            print(f"\nHere is the route from {asal} to {tujuan}: ")
            graph = self.Graph(self.FullRoute.keys(), self.FullRoute)
            previous_nodes, shortest_path = self.dijkstra(graph, asal, tujuan)
            self.shortest_path = shortest_path
            self.print_result(previous_nodes, shortest_path, asal, tujuan)
            while True:
                print("\nMake sure you already check your belongings before choosing class")
                kelas = input("Choose class (Economy, Business, Exclusive): ")
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
                    departtime = input("Departure time(HH:MM)\t  : ")
                    if len(departtime) == 5:
                        try:
                            jam1, menit1 = map(int, departtime.split('.'))
                            break
                        except ValueError:
                            print("Input yang benar")
                    else:
                       print("Input yang benar")
                confirm = input("Are you sure about all the data above?(yes/no):")
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
                    print(f"|Passenger Name:{name}\t\t\t\t\t\t|")
                    print(f"+{'-' * 63}+")
                    print(f"Total Cost\t: ${totalCost}")

                    other = input("\nOrder another ticket?(yes/no):")
                    if other == "no":
                        break
                    else:
                        self.OrderTickets()
                        
    def ShowRoutes(self):
        while True:
            print("Cost = $15/hour")
            untuk= []
            for asal, dicttujuan in self.Route.items():
                for tujuan, weight in dicttujuan.items():
                    untuk.append([f"{asal} -- {tujuan}", weight])
            table = tabulate(untuk, headers= ["     Routes (2-ways)", "Duration(hours)"], tablefmt = "psql", colalign=("left", "center"))
            print(table)
            print("Take Your Route")
            print("=" *10)
            asal = input("From : ")
            tujuan = input("To : ")
            print(f"Here is the shortest route from {asal} to {tujuan}: ")
            graph = self.Graph(self.FullRoute.keys(), self.FullRoute)
            previous_nodes, shortest_path = self.dijkstra(graph, asal, tujuan)
            self.print_result(previous_nodes, shortest_path, asal, tujuan)
            print("See another Route?")
            menu2choice = input("Yes/No = ").lower()
            if menu2choice == "no":
                break
            
    def ViewTrain(self):
        while True:
            data = []
            for kelas  in self.Train.items():
                data.append([kelas[0], kelas[1][0], kelas[1][1]])
            table = tabulate (data, headers= ["  Class", "Max Capacity (kg)", "Cost ($)"], tablefmt = "psql", colalign=("left", "center", "center"))
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
                
                n = int(input("How many things you want to bring?:"))
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
                    if len(item_take) != len(item):
                        print("We Recommend You To Bring :")
                        for i in range(len(item_take)):
                            print(f"{i + 1}. {item_take[i]}")
                        print(f"With Total Weight : {total_weight} Kg")
                        
                elif choice == "yes":
                    item.sort(key = lambda x : (-(x[1] / x[2]), x[2]))
                    for i in range(n):
                        if weight_current >= item[i][1]:
                            weight_current -= item[i][1]
                            total_weight += item[i][1]
                            item_take.append((item[i][0], "Whole"))
                        elif weight_current < item[i][1] and weight_current != 0:
                            fpb = math.gcd(weight_current, item[i][1])
                            item_take.append((item[i][0], f"{int(weight_current / fpb)}/{int(item[i][1] / fpb)}"))
                            total_weight += weight_current
                            weight_current -= weight_current
                            
                    print("We Recommend You To Bring :")
                    for i in range(len(item_take)):
                        print(f"{i + 1}. {item_take[i][0]} ({item_take[i][1]} Parts)")
                    print(f"With Total Weight : {total_weight} Kg")
                    
                if len(item_take) == 0: print("You Can't Carry All of Your Belongings")
                elif len(item) == len(item_take): print(f"You Can Carry All of Your Items")
                else: print("You Can Use Our Recommendation or Choose Another Class to Carry More")
                loop = input("\nTry Another Class ? (Yes / No) : ").lower()
                if loop == "no":
                    break
                    
            else: 
                break

Express()

'''
Algoritma:

1. import tabulate untuk membuat data dlm bentuk tabel
2. import math untuk operasi mtk
3. import random untuk membuat data inputan acak di train
4. import string untuk mendapatkan semua huruf kapital dalam alfabet.
5. import sys untuk dpt nilai max dari dijkstra
6. buatkan class express untuk kode program utama
7. buatkan fungsi dengan parameter self
8. menginisialisasi data rute kereta dalam bentuk dictionary utk menampung self.route
9. menginisialisasi data rute kereta dalam bentuk dictionary utk menampung self.FullRoutes
10. menginisialisasi data kelas kereta beserta kapasitas dan biaya dalam bentuk dictionary untuk menampung jenis kereta beserta kapasitas dan juga harganya di self.train
11. buatkan class graph
12. buatkan fungsi dengan parameter node dan juga graph
13. buatkan self.node untuk menyimpan node dlm graph
14. buatkan self.graph untuk menyimpan graph dlm graph
15. buatkan fungsi construct_graph utk merepresentasi graf
16. inisialisasa graf kosong agar setiap node memiliki edges
17. perbarui graph dgn init graph
18. buatkan perulangan setiap node dlm graph
19. buatkan perulangan setiap node beradjacency dgn node sekarang
20. jika tidak maka tambahkan ke value
21. balikan graph
22. buatkan fungsi get nodes dengan parameter self
23. kembalikan node yang ada dlm graph
24. buatkan fungsi get edges dengan parameter self dan juga nodenya
25. kembalikan list daftar node
26. buatkan fungsi value utk dpt nilai dari node dlm graph
27. kembalikan nilai dari node1 dan node2
28. buatkkan fungsi dijkstra dgn paramater graph, start node dan target node
29. inisialisasi unvisited node dgn list dan dgn memanggil fungsi get node
30. inisialisasi shortest path dgn dict
31. inisialisasi previous node dgn dict
32. inisialisasi max value dgn sys.maxsize
33. buatkakn perulangan setiap node dlm unvisited node
34. inisialisasi afar setiap node dlm unvisited node dgn maxvaalue
35. node awal dlm jalur pendek dibuat jdi 0
36. buatkan perulangan whilejika ada node yg blm dikunjungin
37. inisialisasi current_min_node dgn none
38. buatkan perulangan setiap node dlm unvisited node
39. buatkan prlangan utk setiap node yg blm dikunjungin
40. jika current_min_Node masih bernilai none
41. buatkan agar node menjadi current_min_node
42. jika nilai shortest path si node lebih kecil dari shortest path si currenct_min_node maka buatkan current_min_node jdi node
43. jika nilai current_min_node mencapai si target maka break
44. neighbors diambil dari fungsi get_outgoing_edges 
45. buatkan perulangan setiap edge dlm neighbors
46. tentative_value=nilai dari shortest_oath ditambah si value dlm graph yaitu current_min_node dan neighbor
47. jika tentative_value lebih kecil dari shortest path dgn node neighbor 
48. maka buatkan shortest path dgn node neighbor jdi tentative_value
49. maka buatkan previous dgn node neighbor jdi node
50. jika sdh dikunjungi maka hapus current_min_node dari unvisited_node
51. kembalikan si previous_nodes dan shortest_path
52. buatkan fungsi print_result dgn parameter previous_nodes, shortest_path, start node dan target_npde
52. inisialisasi path dgn list kosong
53. buatkan node sebagai target node
54. buatkan perulangan while node tidak sama dengan start node
55. maka node di append ke path
56. buatkan node sebagai previous_node
57. buatkan start_node ke di append le path
58. buatkan jalur terpendek dari start_node ke target _node dan durasinya
59. buatkan fungsi home
60. buatkan perulangan while True
61. print "Welcome to Ajarin Dong Puh Express
62. peint "1. Order Ticket"
63. print "2. View Ticket"
64. print "3. View Train"
65. print "4. Exit"
66. buaktkkan menuchoice sbg inputan ke user
67. jika inputan user lebih kecil dari 1 dan lebih besar dari 4 maka print "Menu yang Anda masukkan tidak sesuai"
68. jika inputan user 1 maka panggil fungsi self.OrderTickets()
69. jika inputan user 2 maka panggil fungsi self.ViewTicket()
70. jika inputan user 3 maka panggil fungsi self.ViewTrain()
71. jika inputan user 4 maka print "Terima kasih telah menggunakan Ajarin Dong Puh Express"
72. buatkan fungsi orderTickets
73. buatkan perulangan while True
74. print "Make sure you already check your route before order the ticket."
75. print"Where do you wanna go?"
76. buatkan asal utk inputan From
77. buatkan tujuan utk inputan To
79. print route dri asla ke tujjuan
80. buatkan graph dzari class graph dgn full.route
81. buatkan agar previous node dan shortest graph dn dijkstra asal dan tujuan
82. print hasil rute
83. buatkan perulangan while true
84. print "Make sure you already check your belongings before choosing class"
85. buatkan kelas sbg inputan ke user
86. jika kelas tdk dlm self.train.keys maka print "Kelas yang Anda masukkan tidak sesuai"
87. jika kelas dlm self.train.keys maka masuk ke perulangan while true
88. print "Please insert your data:"
89. buatkan nama sbg inputan ke user
90. buatkan perulangan while true
91. buatkan departdate sbg inputan ke user
92. jika panjang dari departdate==10
93. buatkan hari, bulan, dan tahun sebagai map(int, input())
94. buatkan pesan error jika slah inputan
94. buatkan perulangan while true
95. buatkan departtime sbg inputan ke user
96. jika panjang dari departtime==5
93. buatkan jam dan menit sebagai map(int, input())
94. buatkan pesan error jika slah inputan
95. buatkan confirm sbg inputan ke user("Are you sure about all the data above?(yes/no):")
96. jika confirm == "no" maka akan kembali ke inseert data
97. jika confirm == "yes" maka akan lanjut untuk mengecek durasi, totalCost, waktu dan juga hari
98. duration diambil dari shortest path yg tadi
99. totalCost diambil dari nilai dari duration dikalikan dgn 15+ cost dlm self.train
100. waktunyaa didapat dri wajtu ketika inputan ditambah dgn duration
101. buatkan agar tgl menyesuaikan dgn jam
102. jika jam lebih dari 24 maka jam akan berkurang dan hari bertmbah 1
103. buatkan untuk bulan 31 hari
104. buatkan untuk bulan 30 hari
105. jika pada bulan 2 diperiksa apakah dia pada tahun kabisat atau tidak 
106. jika dia pada tahun kabisat maka dia akan bertambah bukannya menjadi 29
107. jika dia tidak pada tahun kabisat maka dia akan bertambah bukannya menjadi 28
108. inisialisasi date2 utk hari ketika dia sampai
108. inisialisasi time2 utk waktu ketika dia sampai
109. print judul yaitu "Train Ticket"
110. print asal, waktu, nomor kereta, platform, waktu keberangkatan, kelasnya, kursinya, tujuan, waktu dan tanggal tiba, nama penumpang, dan juga harganya
111. buatkan other sbg inputan user("Order another ticket?(yes/no):")
112. jika other==no maka akan kluar dari perulangan
113. jika other==yes maka akan memanggil fungsi OrdeerTickets
114. buatkan fungsi ShowRoutes
115. buatkan perulangan while True
116. print Cost = $15/hour utk biaya perjam
117. buatkan untuk sbg list kosong
118. utk setiap asal dan tujuan di append
119. gunakan tabulate utk hasil dari data yg berisi route dan duration
120. print "Take Your Route"
121. buatkan asal sbg inputan ke user
122. buatkan tujuan sbg inputan ke user
123. print route dri asla ke tujjuan
124. buatkan graph dzari class graph dgn full.route
125. buatkan agar previous node dan shortest graph dn dijkstra asal dan tujuan
126. print hasil rute
127. print "See another Route?"
128. buatkan menu2choice sbg inputan user("Yes/No")
129. jika menu2choice == "no maka kluar dri loop

lanjut ke rara

'''

'''




#1
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

#3
3
yes
economy
1
Books
10
1
no
'''
