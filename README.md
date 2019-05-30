# Meme packer
### Problem
Due to Article 13 memes became illegal so people started using USB sticks as a storage of memes and selling them for caps. Every meme is identified by a name, a size, given in MiB, and its market price. Help people who sells memes and write a function to maximize the profit. 
### Solution 
This task is example of knapsack problem for which many of implementations can be found on the Internet. I decided not to solve this problem using these implementantions and I approached the problem differently. I used inbuilt function combinations from itertools module.
### Steps
Firstly, I convert USB size from GiB to MiB and filter meme database out from duplicates using
```python
usb_size = usb_size*(1024)
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
for i, meme in enumerate(memes):
    filtred_memes.append([list(i) for i in combinations(memes, len(memes) - i) if
                          sum([k[1] for k in list(i)]) < usb_size])
```
Afterwards, memes are sorted by the total cost.
```python
sorted_memes = []
for i in filtred_memes:
    if i is not None:
        [sorted_memes.append(j) for j in i]
sorted_memes.sort(key=lambda item: sum([i[2] for i in item]), reverse=True)
```
And lastly,  tuple with the total price and set of meme names is returned
```python
return sum([i[2] for i in sorted_memes[0]]), {i[0] for i in sorted_memes[0]}
```

## Installation
Git clone repository on your computer and run main.py.
If you want to test the program I recommend using venvwrapper in order to avoid getting conflicts with your local projects and then installing test dependencies from requirements_test.py. 
