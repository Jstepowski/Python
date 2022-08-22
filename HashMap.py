class HashMap:
    def __init__(self):
        self.Max = 100
        self.arr = [None for num in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max 

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


        
hash = HashMap()
hash['March 6'] = 130

print (hash['March 6'])
# hash.add("March 6", 130)
# hash_num = hash.get_hash("March 6")
# print (hash.arr)
# print (hash.get("March 6"))
    
