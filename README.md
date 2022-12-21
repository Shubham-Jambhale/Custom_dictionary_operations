# Custom_dictionary_operations

# Question 

There exists a custom dictionary that supports the following operations:

a) Add(key_k,val_v): If no key exists in the dictionary with value key_k, add the (key_k,value_v)
pair to the dictionary. Else update the value corresponding to the key key_k to value_v

b) Add_to_keys(diff): Adds diff to every key in the dictionary at that point of time.

c) Add_to_vals(diff): Adds diff to every value in the dictionary at that point of time.

d) Return(key_k): Returns the value corresponding to the key key_k from the dictionary.

Now the custom dictionary is initially empty and you are given two lists queries and values
of equal length n.

Every element in queries belongs to the set of strings {‘Add’,’Add_to_keys’,’Add_to_vals’,’Return’}.
For 0<=i<n, if queries[i]==‘Add’ values[i] is a list of two integers key_k as values[i][0] and val_v
as values[i][1], else if queries[i]!=‘Add’ values[i] is a list of 1 integer.
You have to traverse the queries and values list from 0 to n-1 and address each index by performing the operation at queries[i] with parameters as values[i].
If there are m elements with value ‘Return’ in list queries, your task is to return a list ’result’ of
length m where the first element is the returned value of the operation ’d’(given above) when
it is called by list queries for the first time and the second element is the returned value of the
operation ’d’ when it is called by list queries for the second time and so on.

Now each type of query is supposed to be addressed in O(1) time(not amortized) complexity.
Given the task is very brute and requires very less logic if the time constraint is compromised,
40% of the score would be awarded for the problem if any of the functions do not meet the time
complexity requirement

# Example

queries= [’Add’,’Add_to_vals’,’Return’,’Add’,’Add_to_keys’,’Add_to_vals’,’Return’]

values= [ [1,2],[2],[1],[2,3],[1],[-1],[3] ]

Output: result=[4,2]
