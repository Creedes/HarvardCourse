# create a new empty set
s = set() 

# adding to set (value)
s.add(1)
s.add(3)
s.add(0)
s.add(42)
s.add(12)
# no element appears twice 
s.add(3)


#remove elements (value)
s.remove(12)

print(s)

# len()
print(f"length of s: {len(s)}")