#map() example
#map applies a function to all the items from a list
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


print(squared)

#more pythonic way
sqaured =[x**2 for x in items]

print(squared)


#filter() example
#filter creates a list of elements for whitch a function returns true
diff=list(filter(lambda x: x<4,items))

print(diff)

#more pythonic way
diff= [x for x in items if x<4]

print(diff)

