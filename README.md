# Meme packer
### Problem
Due to Article 13 memes became illegal so people started using USB sticks as a storage of memes and selling them for caps. Every meme is identified by a name, a size, given in MiB, and its market price. Help people who sells USB sticks with memes and write a function to maximize their profit. 
### Solution 
This task is example of knapsack problem for which many of implementations can be found on the Internet. I decided not to solve this problem using these implementantions and I approached the problem differently. I used inbuilt function combinations from itertools module. Unfortunately, this approach is not the best one and its complexity is O(n<sup>k</sup>). There are better alternatives such as bottom-up or top-down recursive approach to the problem. Dynamic programming would be the best choice here. 
### Steps
Firstly, I convert USB size from GiB to MiB and filter meme database out from duplicates using set() and then I restore list
```python
usb_size *= 1024
memes = list(set(memes))
```
I sort the list by profitability
```
memes.sort(key=lambda item: item[2]/item[1], reverse=True)
```
Then, I create list of all possible combinations except the ones which would not fit in a USB stick.
This stage could be optimisied due to huge impact on the speed of the code.
```python
filtred_memes = []
for index, meme in enumerate(memes):
    filtered_memes.append([list(combination) for combination in combinations(memes, len(memes)-index) if
                          sum([meme[1] for meme in list(combination)]) <= usb_size])
```
Afterwards, memes are sorted by the total cost.
```python
sorted_memes = []
for memes in filter(lambda list_of_memes: list_of_memes, filtered_memes):
    [sorted_memes.append(meme) for meme in memes]
sorted_memes.sort(key=lambda item: sum([i[2] for i in item]), reverse=True)
```
And lastly,  tuple with the total price and set of meme names is returned
```python
return sum([i[2] for i in sorted_memes[0]]), {i[0] for i in sorted_memes[0]}
```

### Installation
Git clone repository on your computer and run main.py.
If you want to test the program I recommend using venvwrapper in order to avoid getting conflicts with your local projects and then installing test dependencies from requirements_test.py. 

### Things to optimize
There is a problem with this code due to quantity od combinations in some cases. 
For example, for this data probe which doesn't hold any duplicates number of combinations become big number:
```python
1,      # usb size
[       # memes
    ('rollsafe.jpg', 205, 6),        
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 126, 11),
    ('I_got_an_arrow.jpg', 584, 20),
    ('sad_adventurer.gif', 320, 25),
    ('be_like_bill.avi', 175, 16),
    ('But_Thats_None_of_My_Business.jpg', 105, 10),
    ('grumpy_cat.gif', 210, 19),
    ('old_spice_guy.avi', 105, 14),
    ('rickroll.jpg', 265, 9),
    ('doge_the_dog.gif', 320, 15),
    ('leekspin.avi', 635, 11)
]
```
cProfile shows this for mentioned data probe:
Fortunately, these extraordinary ncalls are used to lower number of future unneeded usage and it can also be seen underneath. After filtering out number of calls decreased by 85% leaving only needed calls.
```python
         10194 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        1    0.000    0.000    0.006    0.006 main.py:1(<module>)
       12    0.000    0.000    0.000    0.000 main.py:14(<lambda>)
       12    0.003    0.000    0.005    0.000 main.py:18(<listcomp>)
     4095    0.002    0.000    0.002    0.000 main.py:19(<listcomp>)
       12    0.000    0.000    0.000    0.000 main.py:24(<listcomp>)
      483    0.000    0.000    0.000    0.000 main.py:25(<lambda>)
      483    0.000    0.000    0.000    0.000 main.py:25(<listcomp>)
        1    0.000    0.000    0.000    0.000 main.py:27(<listcomp>)
        1    0.000    0.000    0.000    0.000 main.py:27(<setcomp>)
        1    0.000    0.000    0.006    0.006 main.py:4(calculate)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
       12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     4579    0.001    0.000    0.001    0.000 {built-in method builtins.sum}
      495    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.001    0.000 {method 'sort' of 'list' objects}
```
