
# Case 1: try + except
print("Case 1: try + except")
try:
    value = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print(" -> Caught division by zero\n")

# Case 2: try + except + else
print("Case 2: try + except + else")
try:
    value = 10 / 2  # No error here
except ZeroDivisionError:
    print(" -> Error occurred")
else:
    print(" -> No error, result =", value, "\n")

# Case 3: try + finally
print("Case 3: try + finally")
try:
    print(" -> Trying risky action...")
    x = 5 / 1
finally:
    print(" -> Finally block always runs\n")

# Case 4: try + except + finally
print("Case 4: try + except + finally")
try:
    numbers = [1, 2, 3]
    print(" -> Accessing element at index 5...")
    print(numbers[5])  # IndexError
except IndexError:
    print(" -> Caught index error")
finally:
    print(" -> Cleanup in finally\n")

# Case 5: try + multiple except blocks
print("Case 5: try + multiple except blocks")
try:
    text = int("hello")  # Raises ValueError
except ValueError:
    print(" -> ValueError caught")
except TypeError:
    print(" -> TypeError caught")
print()

# Case 6: try + except (catching any exception)
print("Case 6: try + except (catch-all)")
try:
    result = 10 / 0
except Exception as e:
    print(" -> Caught any error:", e)
print()

# Case 7: try + except with custom error message
print("Case 7: try + except with custom message")
try:
    import non_existing_module
except ImportError as e:
    print(" -> Failed to import module:", e)
print()
