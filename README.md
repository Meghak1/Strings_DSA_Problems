# Strings_DSA_Problems
# Python Dictionaries (`dict`) — Complete Interview Notes

A **dictionary** is a built-in data structure that stores data as **key-value pairs**.

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
```

* Key → unique identifier
* Value → data associated with the key
* Mutable ✅
* Ordered (Python 3.7+) ✅
* Keys must be immutable (str, int, tuple, etc.) ✅

---

# 1. Creating Dictionaries

## Empty Dictionary

```python
d = {}
```

or

```python
d = dict()
```

Output:

```python
{}
```

---

## With Values

```python
student = {
    "name": "John",
    "age": 20
}
```

---

## Using `dict()`

```python
student = dict(name="John", age=20)
```

Output:

```python
{'name': 'John', 'age': 20}
```

---

# 2. Accessing Values

## Using `[]`

```python
student = {"name": "John"}

student["name"]
```

Returns:

```python
'John'
```

⚠️ Error if key doesn't exist

```python
student["age"]
```

Returns:

```python
KeyError
```

---

## Using `get()`

### Syntax

```python
dict.get(key, default)
```

### Parameters

| Parameter | Meaning                         |
| --------- | ------------------------------- |
| key       | Key to search                   |
| default   | Value returned if key not found |

### Returns

* Value if key exists
* Default value otherwise

Example:

```python
student.get("name")
```

Returns:

```python
'John'
```

Example:

```python
student.get("age")
```

Returns:

```python
None
```

Example:

```python
student.get("age", 0)
```

Returns:

```python
0
```

---

# 3. Adding / Updating Elements

```python
student["age"] = 21
```

If key exists → updates

If key doesn't exist → creates

---

Example

```python
student = {}

student["name"] = "John"
```

Output:

```python
{'name': 'John'}
```

---

# 4. Removing Elements

## `pop()`

### Syntax

```python
dict.pop(key, default)
```

### Returns

Value removed

Example

```python
student = {"name":"John"}

student.pop("name")
```

Returns:

```python
'John'
```

Dictionary becomes:

```python
{}
```

---

## `popitem()`

Removes last inserted pair.

```python
d = {"a":1,"b":2}

d.popitem()
```

Returns:

```python
('b',2)
```

---

## `del`

```python
del d["a"]
```

Removes key permanently.

---

## `clear()`

```python
d.clear()
```

Returns:

```python
None
```

Dictionary becomes:

```python
{}
```

---

# 5. Checking Keys

## `in`

```python
"name" in student
```

Returns:

```python
True
```

---

## `not in`

```python
"salary" not in student
```

Returns:

```python
True
```

---

# 6. Dictionary Length

## `len()`

```python
len(student)
```

Returns number of keys.

Example:

```python
{"a":1,"b":2}
```

Returns:

```python
2
```

---

# 7. Iterating Over Dictionary

---

## Loop Over Keys

```python
for key in d:
    print(key)
```

Output:

```python
a
b
c
```

---

## `keys()`

### Syntax

```python
dict.keys()
```

### Returns

```python
dict_keys
```

Example

```python
d = {"a":1,"b":2}

d.keys()
```

Returns:

```python
dict_keys(['a','b'])
```

---

## Loop Keys

```python
for key in d.keys():
    print(key)
```

---

# 8. `values()`

### Syntax

```python
dict.values()
```

### Returns

```python
dict_values
```

Example

```python
d.values()
```

Returns:

```python
dict_values([1,2])
```

---

## Loop Values

```python
for value in d.values():
    print(value)
```

Output:

```python
1
2
```

---

# 9. `items()` ⭐ Important

Most asked in interviews.

### Syntax

```python
dict.items()
```

### Returns

```python
dict_items
```

containing

```python
(key, value)
```

pairs.

Example

```python
d = {
    "a":1,
    "b":2
}
```

```python
d.items()
```

Returns:

```python
dict_items([
    ('a',1),
    ('b',2)
])
```

---

## Loop with Items

```python
for key, value in d.items():
    print(key, value)
```

Output:

```python
a 1
b 2
```

---

# 10. `update()`

Merge dictionaries.

### Syntax

```python
dict.update(other_dict)
```

Example

```python
d1 = {"a":1}
d2 = {"b":2}

d1.update(d2)
```

Output:

```python
{'a':1,'b':2}
```

---

# 11. `copy()`

Creates shallow copy.

```python
d2 = d1.copy()
```

Example

```python
d1 = {"a":1}

d2 = d1.copy()
```

Output:

```python
{'a':1}
```

---

# 12. `setdefault()`

Very important for frequency counting.

### Syntax

```python
dict.setdefault(key, default)
```

### Returns

* Existing value if key exists
* Inserts default value otherwise

Example

```python
d = {}

d.setdefault("a",0)
```

Returns:

```python
0
```

Dictionary:

```python
{'a':0}
```

---

Example

```python
d = {"a":5}

d.setdefault("a",0)
```

Returns:

```python
5
```

Dictionary unchanged.

---

# 13. Frequency Counting Pattern ⭐

Most important interview pattern.

Without `Counter`

```python
freq = {}

for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1
```

Output:

```python
{
 'b':1,
 'a':3,
 'n':2
}
```

---

### Why `get()`?

Without it:

```python
freq[ch] += 1
```

fails for first occurrence.

`get(ch,0)` provides default count.

---

# 14. Dictionary Comprehension

### Syntax

```python
{
    key:value
    for item in iterable
}
```

Example

```python
squares = {
    x:x*x
    for x in range(5)
}
```

Output

```python
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

---

# 15. Nested Dictionaries

```python
students = {
    1:{
        "name":"John",
        "age":20
    },
    2:{
        "name":"Alice",
        "age":21
    }
}
```

Access:

```python
students[1]["name"]
```

Returns:

```python
John
```

---

# 16. `fromkeys()`

### Syntax

```python
dict.fromkeys(iterable, value)
```

Example

```python
dict.fromkeys(
    ["a","b","c"],
    0
)
```

Returns:

```python
{
 'a':0,
 'b':0,
 'c':0
}
```

---

# 17. Sorting Dictionary

By key

```python
sorted(d)
```

Returns sorted keys.

---

By value

```python
sorted(
    d.items(),
    key=lambda x:x[1]
)
```

Example

```python
d = {
    'a':3,
    'b':1,
    'c':2
}
```

Returns:

```python
[
 ('b',1),
 ('c',2),
 ('a',3)
]
```

---

# 18. Counter (Advanced Dictionary)

```python
from collections import Counter
```

Example

```python
Counter("banana")
```

Returns

```python
Counter({
 'a':3,
 'n':2,
 'b':1
})
```

---

## Most Common

```python
freq.most_common(2)
```

Returns:

```python
[
 ('a',3),
 ('n',2)
]
```

---

# 19. Time Complexities

| Operation  | Complexity |
| ---------- | ---------- |
| Access     | O(1)       |
| Insert     | O(1)       |
| Delete     | O(1)       |
| Search Key | O(1)       |
| Iterate    | O(n)       |
| Copy       | O(n)       |
| Compare    | O(n)       |

Average-case complexities due to hashing.

---

# 20. Interview Patterns Using Dictionaries

### Frequency Count

```python
freq[ch] = freq.get(ch,0)+1
```

Problems:

* Valid Anagram
* Ransom Note
* First Unique Character

---

### Hash Map Lookup

```python
seen = {}
```

Problems:

* Two Sum
* Contains Duplicate

---

### Grouping

```python
groups = {}
```

Problems:

* Group Anagrams
* Categorizing Data

---

### Counting

```python
count = {}
```

Problems:

* Top K Frequent Elements
* Majority Element

---

# Quick Cheat Sheet

| Function              | Takes        | Returns             |
| --------------------- | ------------ | ------------------- |
| `d[key]`              | key          | value               |
| `get(key,default)`    | key          | value/default       |
| `keys()`              | nothing      | all keys            |
| `values()`            | nothing      | all values          |
| `items()`             | nothing      | `(key,value)` pairs |
| `pop(key)`            | key          | removed value       |
| `popitem()`           | nothing      | last pair           |
| `update(dict)`        | dictionary   | None                |
| `copy()`              | nothing      | shallow copy        |
| `clear()`             | nothing      | None                |
| `setdefault(key,val)` | key,val      | existing/new value  |
| `fromkeys(iter,val)`  | iterable,val | new dictionary      |
| `len(d)`              | dictionary   | number of keys      |
| `sorted(d)`           | dictionary   | sorted keys list    |

### Most Important Interview Methods

1. `get()`
2. `items()`
3. `keys()`
4. `values()`
5. `update()`
6. `pop()`
7. `setdefault()`
8. `Counter()`
9. Dictionary comprehension
10. Frequency counting pattern (`freq[ch] = freq.get(ch,0)+1`)

