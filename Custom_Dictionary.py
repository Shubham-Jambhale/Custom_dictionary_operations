def custom_dict(queries,values):
    dicti = {}
    key = 0
    result=[]
    value = 0
    
    #Queries are addressed in O(1) time as iterating over the array only once.
    for i in range(len(queries)):
        givenCommand = queries[i]
        v = values[i]
        if givenCommand == "Add":
            k,dicti = add(v,dicti,key,value)
            
        elif givenCommand == "Add_to_vals":
            value = add_to_vals(v,value)
            
        elif givenCommand == "Add_to_keys":
            key = add_to_keys(v,key)
        else:
            k = v[0]
            k=k-key
            total = dicti[k] + value
            result.append(total)
    return result
            
def add(v,dicti,key,value):
    k,v = v[0],v[1]
    dicti[k-key]=v-value
    return k,dicti

def add_to_vals(v,value):
    k = v[0]
    value = k + value
    return value
    
def add_to_keys(v,key):
    k = v[0]
    key = k + key
    return key
   
print("---Output Begins --- ")
print()
output=custom_dict(['Add','Add_to_vals','Return','Add','Add_to_keys','Add_to_vals','Return'],[[1,2],[2],[1],[2,3],[1],[-1],[3]])
print("Output:",output)
print()