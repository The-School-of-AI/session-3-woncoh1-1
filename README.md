# Session 3 - Numeric Types: Part I

## 1. Assignment Instructions

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
### 1. `encoded_from_base10`
### 2. `float_equality_testing`
### 3. `manual_truncation_function`
### 4. `manual_rounding_function`
### 5. `rounding_away_from_zero`

    'int',
    'encoded_from_base10',
    'digit_map',
    'ValueError',
    'math',
    'isclose',
    'absolute',
    'relative',
    'tolerance',
    'bin(',
    'hex(',
    'round',
    'truncation',
    'error',
    'equality',
    'zero',
    'away'



## 0. Assignment Instructions

1. Garbage collection of cyclical reference
    - Here in this code we will be leaking memory because we are creating cyclic reference. 
    - Find that we are indeed making cyclic references. 
    - Eventually memory will be released, but that is currently not happening immediately. 
    - We have added a function called "clear_memory" but it is not able to do it's job. Fix it. 
    - Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that this code is sub-optimal.

2. Efficient equality and membership testing of strings
    - Here we are suboptimally testing whether two strings are exactly same or not. 
    - After that we are trying to see if we have a particular character in that string or not. 
    - Currently the code is suboptimal. 
    - Write it in such a way that it takes 1/10 the current time.

<a name="cyclical"/>

## 1. Garbage Collection of Cyclical Reference

### 1-1 Parts List

#### Classes

1. `Something`
    - This is a simple class with a constructor that assigns `None` to the sole class variable `something_new`.
    
2. `SomethingNew`
    - Here the `__init__` constructor accepts an argument of type `Something`, whose default is set to `None`.
    - The assignment `self.something = something` forebodes potential cyclical reference. 

#### Functions

1. `add_something`
    - Clear cyclical reference: 
        - `something = Something()`
        - `something.something_new = SomethingNew(i, something)`
    - The resulting `something` gets added to the collection.

2. `clear_memory`
    - This functions is intended to delete all elements from the list and free up memory.
    - But we need to modify the body of this function in order to make it work properly.

3. `critical_function`
    - This is the function at brings together all the ingredients, namely `collection`, `add_something` and `clear_memory`, and put them to heavy work.
