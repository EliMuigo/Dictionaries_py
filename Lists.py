"""#list- are mutable 
courses=['History','Math','Physics','CompSci']

#to print out items from index 0 to 1
print(courses[0:2])

#to print out the last 2 items
print(courses[2:])

#to print out an item using index
print(courses[2])

#adding an item to a list
courses.append('Art')
print(courses)

#adding a list to another list use extend method
course_2=['Science','Education']
courses.extend(course_2)
print(courses)

#removing values from a list
courses.pop(2)
print(courses)

#OR
popped=courses.pop(1)
print(popped)


#sorting
courses.reverse()
print(courses)

courses.sort()

#OR
sorted_courses=sorted(courses)
print(sorted_courses)

nums =[1,3,2,4,6,5]
nums.sort()
print(nums)
nums.sort(reverse=True)#used to reverse the sort method 

print(nums)

#Finding values
print(courses.index("CompSci"))#finding the index of a value in a list

print('Art' in courses)
 
 #looping through values
for course in courses:
    print(course)

#getting index and values
for item in enumerate(courses):
 print(item)


for index,course in enumerate(courses,start=1):
    print(index,course)


#splitting values
course_str=' , '.join(courses)
print(course_str)

new_list=course_str.split( '-' )
print(new_list)


bicycles=['Trek','specialized','scotts','redline']
#To access redline we use index
print(bicycles[2])
#using the title() method
print(bicycles[2].title())


#Negative Indexing-used in accessing  the last element in a list.
bicycles=['Trek','specialized','scotts','redline']
print(bicycles[-1])

#A short program
names=['Vince','Terry','Austin','Vicky','Eli']
for names in names:
    print(f"hello {names}")

#Changing,removing, and adding elements

#append() method-adds the element at the end of a list.
motorcycles=['ducati','honda','yamaha']
motorcycles.append('bmw')
print(motorcycles)

#insert()- you can add elements at any position in the list by specifying the index
motorcycles=['ducati','honda','yamaha']
motorcycles.insert(0,'suzuki')
print(motorcycles)

#removing elements from a list 

#del statement- removes an element from a list by specifying it's position
motorcycles=['ducati','honda','yamaha']

del motorcycles[1]
print(motorcycles)

# pop () method - this method removes the last item in the list, but it lets you work with that item after removing
motorcycles=['ducati','honda','yamaha']

mod_motorcycles=motorcycles.pop()

print(mod_motorcycles)
print(motorcycles)

#popping items from any position in a list
motorcycles=['ducati','honda','yamaha']


first_motorcycle=motorcycles.pop(0)
print(f"My first motorcycle was {first_motorcycle}")"""

#removing an item by value
motorcycles=['ducati','honda','yamaha']

motorcycles.remove('honda')
print(motorcycles)



















