

```python
from IPython.core.display import HTML, Image
css = open('/home/researcher/2016-06-01-real_pandas/style/style-table.css').read() + open('/home/researcher/2016-06-01-real_pandas/style/style-notebook.css').read()
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
pwd
```




    '/home/researcher'




```python
3 *994857

```




    2984571



# Python Workshop

--------------

- Shell
- Python
- iPython
- **Jupyter Notebook**

1. get stuff into a program
2. manipulate it
3. output something

![](http://i.imgur.com/uk2uq.jpg)


```python
type("hello isn't it a lovely day?")
```




    str




```python
type(45)
```




    int




```python
type(16.4)
```




    float




```python
int()
```


```python
float()
```


```python
str()
```


```python
input('type a number')
```

    type a number42





    '42'




```python
int('42')
```




    42




```python
number = '42'
```


```python
number
```




    '42'




```python
type(number)
```




    str




```python
number = input('type a number')
```

    type a number42



```python
number
```




    '42'




```python
number
```




    '42'




```python
'hello'+'hello'
```




    'hellohello'




```python
'hello'-'hello'
```


    

    TypeErrorTraceback (most recent call last)

    <ipython-input-22-85fe99bfc8d4> in <module>()
    ----> 1 'hello'-'hello'
    

    TypeError: unsupported operand type(s) for -: 'str' and 'str'



```python
number = int(number+number)
```


```python

```
