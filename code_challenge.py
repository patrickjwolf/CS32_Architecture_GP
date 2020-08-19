dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}


      
sum = 0
for i in dict.values():
    if type(i) == int: 
        sum += i 
print(sum)
  
a = 0xABCDEF
b = 0x2a
print(a, b)