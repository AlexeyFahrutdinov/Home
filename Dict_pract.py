my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
print(my_dict["key1"])

prices = {"apples" : 2.99, "oranges" : 3.99, "milk" : 5.80}
print(prices["apples"])

key = {"k1" : 123, "k2" : [1, 2, 3], "k3" : {"insidekey": 123}}

print(key)
print(key["k1"])
print(key["k2"])
print(key["k2"][2])
print(key["k3"])
print(key["k3"]["insidekey"])

print(key.keys())
print(key.values())
print(key.items())
