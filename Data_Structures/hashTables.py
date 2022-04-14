class hashTable():
    def __init__(self, size):
        self.keyMap = [0 for i in range(size)]
        
    def _hash(self, key):
        total = 0
        weird_prime = 31
        for i in range(0, min(100, len(key))):
            char = key[i]
            value = abs(ord(char) - 96)
            total = (total * weird_prime + value) % len(self.keyMap)
        return total
        
    def set(self, key, value):
        hashh = self._hash(key)
        if self.keyMap[hashh] == 0:
            self.keyMap[hashh] = []
            self.keyMap[hashh].append([key, value])
        else:
            self.keyMap[hashh].append([key, value])
            
    def get(self, key):
        position = self._hash(key)
        if self.keyMap[position] != 0:
            for element in self.keyMap[position]:
                if element[0] == key:
                    print(element[0])
                    return element[1]
        return -1
        
    def keys(self):
        kys = []
        for position in self.keyMap:
            if position!= 0:
                for element in position:
                    if(not element[0] in kys):
                        kys.append(element[0])
        return kys
        
    def values(self):
        vls = []
        for position in self.keyMap:
            if position!= 0:
                for element in position:
                    if(not element[1] in vls):
                        vls.append(element[1])
        return vls

hs = hashTable(10)
hs.set("darkblue", "#00008b")
hs.set("salmon", "#fa8072")
hs.set("red", "#ffffff")
hs.set("red", "#ffffff")
print(hs.get("darkblue"))
print(hs.get("saoksoaksoaksokaepmkemsakmeaosemasoemaosm"))
print("Keys = "+str(hs.keys()))
print("Values = "+str(hs.values()))
