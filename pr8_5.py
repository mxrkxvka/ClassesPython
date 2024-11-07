class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)

    
str1 = RealString("Apple")
str2 = RealString("Яблоко")

print(str1 == str2)  
print(str1 >= str2)
print(str1 <= str2)  

print(str1)
print(str1 == "Apple")
print(str1 >= "Apple")
