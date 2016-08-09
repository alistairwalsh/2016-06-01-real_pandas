
# Where are we?

http://nbviewer.jupyter.org/github/kikocorreoso/PyConES14_talk-Hacking_the_Notebook/tree/master/notebooks/

# The Jupyter Notebook

### A web browser interface for the Python language

- A rich multimedia environment.
- The display and the interpreter are seperate.
- Ideal for science/research, just like a lab book.

#### Some shortcuts

  keys |  action       |  mode
:-----:|:-------------:|:-----:
`esc`  | blue surround | command
`return`| green surround | edit
**h**    | show help| command
**b** | cell below | command
**a** | cell above | command
**x** | cell delete | command
**m** | markdown | command
**y** | code cell | command
**n** | line numbers | command
`[ & ]`|move block | edit

### Style counts


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




```python
from IPython.core.display import Image
Image(url= 'http://katrinarasbold.com/wp-content/uploads/2013/03/Jacob.jpg')
```




<img src="http://katrinarasbold.com/wp-content/uploads/2013/03/Jacob.jpg"/>



# Solid Ground


```python
x = 0b1111111111111111111111111111110
```


```python
y = 0b0000000000000000000000000000001
```


```python
bin(x + y)
```




    '0b1111111111111111111111111111111'



### Math Operators from Highest to Lowest Precedence

operator|example|evaluates to...
:-----:|:------:|:------:
** | 2 ** 3 | 8
% | 22 % 8 | 6
// | 22 // 8 | 2
/ | 22 / 8 | 2.75
* | 3 * 5 | 15
- | 5 - 2 | 3
+ | 2 + 2 | 4

### Basic io


```python
print()
```


```python
input()
```


```python
len()
```

### The Integer, Floating-Point, and String Data Types


```python
type()
```


```python
int()
```


```python
float() 
```


```python
str()
```

<p>One way to remember how slices work is to think of the indices as pointing
<em>between</em> characters, with the left edge of the first character numbered 0.
Then the right edge of the last character of a string of <em>n</em> characters has
index <em>n</em>, for example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span> <span class="o">+---+---+---+---+---+---+</span>
 <span class="o">|</span> <span class="n">P</span> <span class="o">|</span> <span class="n">y</span> <span class="o">|</span> <span class="n">t</span> <span class="o">|</span> <span class="n">h</span> <span class="o">|</span> <span class="n">o</span> <span class="o">|</span> <span class="n">n</span> <span class="o">|</span>
 <span class="o">+---+---+---+---+---+---+</span>
 <span class="mi">0</span>   <span class="mi">1</span>   <span class="mi">2</span>   <span class="mi">3</span>   <span class="mi">4</span>   <span class="mi">5</span>   <span class="mi">6</span>
<span class="o">-</span><span class="mi">6</span>  <span class="o">-</span><span class="mi">5</span>  <span class="o">-</span><span class="mi">4</span>  <span class="o">-</span><span class="mi">3</span>  <span class="o">-</span><span class="mi">2</span>  <span class="o">-</span><span class="mi">1</span>
</pre></div>
</div>

[The programming World](Beginner_Python_framework_Basics-Copy1.ipynb)


```python
word = 'alphabet'
```


```python
word[1]
```




    'l'




```python
word[1:4]
```




    'lph'




```python
word[:-3]
```




    'alpha'




```python
word[:]
```




    'alphabet'




```python
word[:3000000031263839]
```




    'alphabet'




```python
from IPython.display import FileLink
FileLink('Beginner_Python_framework_Basics_2.ipynb')
```




<a href='Beginner_Python_framework_Basics_2.ipynb' target='_blank'>Beginner_Python_framework_Basics_2.ipynb</a><br>




```python

```
