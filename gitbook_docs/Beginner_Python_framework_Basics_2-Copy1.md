

```python
from IPython.core.display import HTML, Image
css = open('style/style-table.css').read() + open('style/style-notebook.css').read()
HTML('<style>{}</style>'.format(css))
```




<style>body {
    margin: 0;
    font-family: Helvetica;
}
table.dataframe {
    border-collapse: collapse;
    border: none;
}
table.dataframe tr {
    border: none;
}
table.dataframe td, table.dataframe th {
    margin: 0;
    border: 1px solid white;
    padding-left: 0.25em;
    padding-right: 0.25em;
}
table.dataframe th:not(:empty) {
    background-color: #fec;
    text-align: left;
    font-weight: normal;
}
table.dataframe tr:nth-child(2) th:empty {
    border-left: none;
    border-right: 1px dashed #888;
}
table.dataframe td {
    border: 2px solid #ccf;
    background-color: #f4f4ff;
}
h3 {
    color: white;
    background-color: black;
    padding: 0.5em;
}
</style>



# The programming world

### Variables

- The assignment operator
- valid names
- assigning the output of an expression


### The magical list

- creating
- slicing
- adding, deleting, insert, append


```python
nums = [1,2,3,45]
```


```python
nums[:2]
```




    [1, 2]




```python
nums[1] = 'hello'
```


```python
nums
```




    [1, 'hello', 3, 45]




```python
nums2 = ['a','b','c']
```


```python
nums + nums2
```




    [1, 'hello', 3, 45, 'a', 'b', 'c']




```python
word = 'alptabet'
```

### Can a str be changed?


```python
word[3] = 'h'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-e0ec55d1a414> in <module>()
    ----> 1 word[3] = 'h'
    

    TypeError: 'str' object does not support item assignment



```python
word2 = 'zebra'
```


```python
information = {'name':'Alistair',
 'age':'mind your own business',
 'address':'Brunswick','age':42}
```


```python
information
```




    {'address': 'Brunswick', 'age': 42, 'name': 'Alistair'}




```python
information['eye colour'] = 'blue'
```


```python
information[2] = 'hello'
```


```python
information
```




    {'age': 42,
     'address': 'Brunswick',
     'eye colour': 'blue',
     'name': 'Alistair',
     2: 'hello'}



### The mysterious dictionary

- suitable data types
- hashable


```python
from IPython.display import FileLink
FileLink('treasure_hunt/treasure_hunt.ipynb')
```




<a href='treasure_hunt/treasure_hunt.ipynb' target='_blank'>treasure_hunt/treasure_hunt.ipynb</a><br>



### The immutable tuple

- why immutable?

### The strict set

- no repeats
- like a Venn diagram


```python
Image('images/venn-pbpython2.png')
```




![png](output_28_0.png)



Operation| Equivalent |	Result
---------|------------|---------
len(s)	 |	|number of elements in set s (cardinality)
x in s	 |	| test x for membership in s
x not in s	| 	|test x for non-membership in s
s.issubset(t)	|s <= t	|test whether every element in s is in t
s.issuperset(t)| s >= t	|test whether every element in t is in s
s.union(t)|	s &#124; t |	new set with elements from both s and t
s.intersection(t)|	s & t	| new set with elements common to s and t
s.difference(t)|	s - t	| new set with elements in s but not in t
s.symmetric_difference(t)|	s ^ t	| new set with elements in either s or t but not both
s.copy()|	 	|new set with a shallow copy of s

# Program control

### Automate the boring stuff

### for loops

As we have seen, we can index a list to select the individual characters by using indexing


```python
word = 'lead'
print(word[0])
print(word[1])
print(word[2])
print(word[3])

```

    l
    e
    a
    d


But this code doesn't work if the word is a different length


```python
word = 'tin'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
```

    t
    i
    n



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-14-a51226538da7> in <module>()
          3 print(word[1])
          4 print(word[2])
    ----> 5 print(word[3])
    

    IndexError: string index out of range


### The `for` loop


```python
word = 'oxygen'
for i in word:
    print(i)
print(i)
```

    o
    x
    y
    g
    e
    n
    n



```python
for i in ['1','2','3']:
    print(i)
```

    1
    2
    3



```python
letter ='z'
for letter in 'abc':
    print(letter)
print(letter)
```

    a
    b
    c
    c



```python
count = 0
for num in [1,2,3]:
    count = count + 1
    print(num)
print('the number of elements in the list is ',count)
```

    1
    2
    3
    the number of elements in the list is  3



```python
print(len([1,2,3]))
```

    3


### conditionals


```python
num = 105
if (num > 100) and (num < 110):
    print('greater than 100 and less than 110')
elif num < 100:
    print('less than')
else:
    print('is neither')

print('done')
```

    greater than 100 and less than 110
    done



```python
if (1>0) and (-1<0):
    print('both true')
else:
    print('at least one part if false')
```

    both true



```python
x = 'apple'
if x is not 'apple':
    print('x is not apple')
else:
    print('x is apple')
```

    x is apple



```python
if '2' is 2:
    print('true')
else:
    print('false')

```

    false



```python

```




    True




```python

```

- if
- elif
- else

Operation |	Meaning
----------|-----------
<	| strictly less than
<=	| less than or equal
>	| strictly greater than
>=	| greater than or equal
==	| equal
!=	| not equal
is	| object identity
is not	| negated object identity

### booleans or `truth` statements


```python
if True:
    print('True is True')
if False:
    print('False is not True')
if 'hello':
    print('hello is True')
if '':
    print('An empty string is not True')
if [1,2,3]:
    print('A list with values is True')
if []:
    print('What about an ampty list')
if {1:'answer'}:
    print('What about a full dict')
if {}:
    print('What about an ampty dict')
if 1:
    print('1 is True')
if 0:
    print("0 isn't")
```

    True is True
    hello is True
    A list with values is True
    What about a full dict
    1 is True



```python
def this_function_does_nothing():
    '''
    This function takes no input, does nothing and produces no output
    '''
    pass
    
```


```python
this_function_does_nothing()
```

    Help on function this_function_does_nothing in module __main__:
    
    this_function_does_nothing()
        This function takes no input, does nothing and produces no output
    



```python
this_function_does_nothing()
```

    Help on function this_function_does_nothing in module __main__:
    
    this_function_does_nothing()
        This function takes no input, does nothing and produces no output
    



```python
potatoes = ['desire','kipfler','red','russet','petite','Mr. Potatoe Head']
```


```python
potatoes
```




    ['desire', 'kipfler', 'red', 'russet', 'petite', 'Mr. Potatoe Head']




```python
def peel_em(name_list):
    '''
    this function takes a list of strings and 
    removes the first and last letter from each element of
    the list and returns the shortened list of strings
    '''
    full_list = []
    
    for potato in name_list:
        answer = potato[1:-1]
        full_list.append(answer)
    
    return full_list
```


```python
peel_em(potatoes=['a','c'])
```




    ['esir', 'ipfle', 'e', 'usse', 'etit', 'r. Potatoe Hea']



# Writing programs

### Functions

### Tests

- assert
- try, except


```python

```

### Getting help

When asking programming questions, remember to do the following:
- Explain what you are trying to do, not just what you did. This lets your helper know if you are on the wrong track.

- Specify the point at which the error happens. Does it occur at the very start of the program or only after you do a certain action?

- Copy and paste the entire error message and your code to http://pastebin.com/ or http://gist.github.com/.
These websites make it easy to share large amounts of code with people over the Web, without the risk of losing any text formatting. You can then put the URL of the posted code in your email or forum post. For example, here some pieces of code I’ve posted: http://pastebin.com/SzP2DbFx/ and https://gist.github.com/asweigart/6912168/.

- Explain what you’ve already tried to do to solve your problem. This tells people you’ve already put in some work to figure things out on your own.

- List the version of Python you’re using. (There are some key differences between version 2 Python interpreters and version 3 Python interpreters.) Also, say which operating system and version you’re running.

- If the error came up after you made a change to your code, explain exactly what you changed.

- Say whether you’re able to reproduce the error every time you run the program or whether it happens only after you perform certain actions. Explain what those actions are, if so.
