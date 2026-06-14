# Remove Outermost Parentheses

## Problem Statement

Given a valid parentheses string `s`, remove the outermost parentheses from every primitive substring and return the resulting string.

### Example

```python
Input: s = "(()())(())"

Output: "()()()"
```

Explanation:

```text
(()())  -> ()()
(())    -> ()
```

Combining them gives:

```text
()()()
```

---

# Approach

The key idea is to keep track of the current nesting level using a variable called `depth`.

* When we encounter `'('`, we increase the depth.
* When we encounter `')'`, we decrease the depth.
* The outermost opening parenthesis is encountered when `depth == 0`.
* The outermost closing parenthesis is encountered when depth becomes `0` after decrementing.

We append only the parentheses that are not part of the outermost layer.

---

# Algorithm

1. Initialize:

   * `res = []` to store the answer.
   * `depth = 0` to track nesting level.

2. Traverse each character in the string.

3. If the character is `'('`:

   * If `depth > 0`, append it to the result.
   * Increase `depth` by 1.

4. If the character is `')'`:

   * Decrease `depth` by 1.
   * If `depth > 0`, append it to the result.

5. Join the characters in `res` and return the final string.

---

# Why Do We Decrement First for `')'`?

Consider:

```text
(()())
     ^
```

The last `)` is the outermost closing parenthesis and must be removed.

Before processing it:

```python
depth = 1
```

If we checked first:

```python
if depth > 0:
    res.append(')')
```

the outermost `)` would be incorrectly added.

Instead:

```python
depth -= 1
```

Now:

```python
depth = 0
```

Since:

```python
if depth > 0
```

is false, the outermost closing parenthesis is skipped.

This is why decrementing comes before the check.

---

# Dry Run

Input:

```python
s = "(()())"
```

Initial state:

```python
res = []
depth = 0
```

| Character | Action             | Depth | Result |
| --------- | ------------------ | ----- | ------ |
| (         | Skip, depth += 1   | 1     | ""     |
| (         | Append, depth += 1 | 2     | "("    |
| )         | depth -= 1, append | 1     | "()"   |
| (         | Append, depth += 1 | 2     | "()("  |
| )         | depth -= 1, append | 1     | "()()" |
| )         | depth -= 1, skip   | 0     | "()()" |

Final answer:

```python
"()()"
```

---

# Code

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0

        for ch in s:

            if ch == '(':
                if depth > 0:
                    res.append(ch)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    res.append(ch)

        return ''.join(res)
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

We traverse the string once.

### Space Complexity

```text
O(n)
```

The result list may store up to `n` characters.

---

# Key Observation

For opening parentheses:

```python
if depth > 0:
    res.append('(')

depth += 1
```

We check before increasing depth so that the first outermost `'('` is skipped.

For closing parentheses:

```python
depth -= 1

if depth > 0:
    res.append(')')
```

We decrease depth before checking so that the last outermost `')'` is skipped.

This symmetry allows us to remove only the outermost pair of every primitive substring.
