# Define the multiplier
multiplier = [1,0,1,1]  # Example multiplier in binary, change as needed
N = 16  # Example value of N, change as needed

# Method 1: Using bitwise left shift
#temp_buffer = (multiplier[3] & 1) << N

# Method 2: Using bitwise OR and left shift
temp_buffer = (multiplier[3] & 1) | ((multiplier[3] & 1) << 1)
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2
temp_buffer |= temp_buffer << 2

print(bin(temp_buffer))  # Print the result in binary format