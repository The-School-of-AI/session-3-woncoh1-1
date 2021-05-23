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
