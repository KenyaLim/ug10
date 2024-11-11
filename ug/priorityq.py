class PriorityQueue:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            return
        return self.data[0]

    def enqueue(self, prioritas, data):
        self.data.append((prioritas, data))
        self.data.sort(reverse=True)


    def dequeue(self):
        if self.is_empty():
            return
        return self.data.pop(0)

    def write_all_data(self):
        print(self.data)

def print_pasien(pq : PriorityQueue):
    data = pq.data
    prioritas = ""
    pasien = ""
    n = 1
    for p, pasien in data:
        if p == 3:
            prioritas = "Sudah meninggal"
        elif p == 2:
            prioritas = "Merah"
        elif p == 1:
            prioritas = "Kuning"
        else:
            prioritas = "Invalid status"
        print(f"{n}. {pasien}, status: {prioritas}")
        n += 1

if __name__ == "__main__":
    #pass
    pq = PriorityQueue()
    print("Masukkan 3 pasien")
    for i in range(3):
        pasien = input("Masukkan nama pasien: ")
        kec = input("Kecepatan respirasi per menit: ")
        if kec == "0":
            pq.enqueue(3, pasien)
            continue
        nadi = input("Denyut lemah/tidak terasa y/n: ")
        if nadi == "y":
            pq.enqueue(2, pasien)
            continue
        abab = input("Apakah bisa diperintah y/n: ")
        if abab == "y":
            pq.enqueue(1, pasien)
        else:
            pq.enqueue(2, pasien)
    print_pasien(pq)
            