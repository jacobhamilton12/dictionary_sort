# dictionary_sort
Data structure I made to see if it will be faster than heapq. Currently it is not, though there are some optimizations that can be made

Run tests with ```poetry run pytest -v -s```


## General Idea
Sort of a mash up between counting sort and fenwick tree. Each level is for number of digits. It will pop the top smallest numbers first.

Ex, 
```python
[54, 13, 667, 98, 1] ->                   [{1: {}}
                           {5: {4: {}}, 9: {8: {}}, 1: {3: {}}}
                                       {6: {6: {7: {}}}}]
```
