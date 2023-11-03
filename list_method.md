
### append() method

-adds the element at the end of a list.

~~~
motorcycles=['ducati','honda','yamaha']
motorcycles.append('bmw')
print(motorcycles)
~~~

### insert() method- you can add an element at any position by specifying the index of the new element and the value of the new item
~~~
motorcycles=['ducati','honda','yamaha']
motorcycles.insert(0,'suzuki')
print(motorcycles)
~~~

### Removing items from a list
<b>1.Using del  </b>-This permanently removes an item from a list. Removes an element from a list by specifying it's position using index.
~~~
motorcycles=['ducati','honda','yamaha']

del motorcycles[1]
print(motorcycles)
~~~
<b>2.Using pop() method</b>-this method removes the last item in the list, but it lets you work with that item after removing
~~~
motorcycles=['ducati','honda','yamaha']

mod_motorcycles=motorcycles.pop()

print(mod_motorcycles)
print(motorcycles)
~~~
- Popping items from any position in a list by specifying the index
~~~
motorcycles=['ducati','honda','yamaha']


first_motorcycle=motorcycles.pop(0)
print(f"My first motorcycle was {first_motorcycle}")
~~~
<b>3.Removing an item by value</b>
~~~
motorcycles=['ducati','honda','yamaha']

motorcycles.remove('honda')
print(motorcycles)
~~~