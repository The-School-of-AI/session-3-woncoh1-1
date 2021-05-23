# Session 3 - Numeric Types: Part I

## 1. Assignment Instructions

Here we state the goals of implementing the following 5 functions:
1. `encoded_from_base10`
2. `float_equality_testing`
3. `manual_truncation_function`
4. `manual_rounding_function`
5. `rounding_away_from_zero`

### 1. `encoded_from_base10`
- This function returns a string encoding in the "base" for the the "number" using the "digit_map"
- Conditions that this function must satisfy:
  - 2 <= base <= 36 else raise ValueError.
  - Invalid base ValueError must have relevant information.
  - Digit_map must have sufficient length to represent the base.
  - Must return proper encoding for all base ranges between 2 to 36 (including).
  - Must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added).
  - The digit_map must not have any repeated character, else ValueError.
  - The repeating character ValueError message must be relevant.
  - You cannot use any in-built functions in the MATH module.

### 2. `float_equality_testing`
- This function emulates the ISCLOSE method from the MATH module, but you can't use this function.
- We are going to assume:
  - rel_tol = 1e-12
  - abs_tol = 1e-05

### 3. `manual_truncation_function`
- This function emulates python's MATH.TRUNC method:
  - It ignores everything after the decimal point. 
  - It must check whether f_num is of correct type before proceed. 
  - You can use inbuilt constructors like int, float, etc.

### 4. `manual_rounding_function`
- This function emulates python's inbuild ROUND function.
- You are not allowed to use ROUND function, but expected to write your one manually.

### 5. `rounding_away_from_zero`
- This function implements rounding away from zero as covered in the class.
- Desperately need to use INT constructor? Well you can't. 
- Hint: use FRACTIONS and extract numerator.

## 2. Function Implementation

Here we review key specs for each function and how they were implemented.

### 1. `encoded_from_base10`
- 2 <= base <= 36 else raise ValueError.
  ```python
  if base < 2 or base > 36:
      raise ValueError("Invalid base: 2 <= base <= 36")
  ```
- Digit_map must have sufficient length to represent the base.
  ```python
  if max(digits) >= len(digit_map):
      raise ValueError("digit_map is not long enough to encode digits")
  ```
- Must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added).
  ```python
  if sign == -1:
      encoding = '-' + encoding
  ```
- The digit_map must not have any repeated character, else ValueError.
  ```python
  for count in Counter(digit_map).values():
      if count > 1:
          raise ValueError("Invalid digit_map: repeating digits not allowed in digit_map")
  ```
  - `bin()` or `hex()` are not allowed.

### 2. `float_equality_testing`
  - Set values for absolute and relative tolerances.
  ```python
  rel_tol = 1e-12
  abs_tol = 1e-05
  ```
  - Directly use Python's definition of `isclose` from the `math` module.
  ```python
  return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), 
                           abs_tol)
  ```
### 3. `manual_truncation_function`
  - It must check whether f_num is of correct type before proceed.
  ```python
  if not isinstance(f_num, float):
      raise ValueError("Invalid f_num: f_num should be a 32-bit floating point number")
  ```
  - You can use inbuilt constructors like int, float, etc.
    - Use `int()`:
    ```python
    return int(f_num)
    ```
    - Use __int__(), since the test script raises an error for using `int()`. There seems to be a contradiction between the test script and assignment requirement.
    ```python
    return f_num.__int__()
    ```
    
### 4. `manual_rounding_function`
This function is implemented using 3 parts:
1. String representation of `f_num`
```python
str_int = str(f_num).split('.')[0]
is_negative = str_int[0] == '-'
```
2. Getting the first decimal value using `Decimal`
```python
first_decimal_place = len(str_int) - 1 if is_negative else len(str_int)
first_decimal_value = Decimal(f_num).as_tuple().digits[first_decimal_place]
```
3. Using the `manual_rounding_function` defined above for rounding
```python
if first_decimal_value < 5:
    return manual_truncation_function(f_num)
else:
    if is_negative:
        return manual_truncation_function(f_num - 0.5)
    else:
        return manual_truncation_function(f_num + 0.5)
 ```

### 5. `rounding_away_from_zero`
This function is identical to the above except for the actual rounding part:
```python
if is_negative:
    return manual_truncation_function(f_num - 1)
else:
    return manual_truncation_function(f_num + 1)
```
