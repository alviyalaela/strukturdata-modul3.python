from collections import deque

class latihan2:
    def contohQueue(self):
        baris = deque()
        baris.append("Java")
        baris.append("DotNet")
        baris.append("PHP")
        baris.append("HTML")
        print("popleft : ", baris.popleft())
        print("leftmost element : ", baris[0])
        print("pop : ", baris.pop())
        print("leftmost element : ", baris[0])

if __name__ == '__main__':
    s = latihan2()
    s.contohQueue()