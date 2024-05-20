A = 14975
B = 31389
# Step 1: Split the 16-bit numbers into two 8-bit halves
A_high = A >> 8
A_low = A & 0xFF
B_high = B >> 8
B_low = B & 0xFF

# Step 2: Compute the partial product
#A_low1 = A & 0xF0 # 0000 0000 1111 0000
#A_low2 = A & 0x0F # 0000 0000 0000 1111
#B_low1 = B & 0xF0 # 0000 0000 1111 0000
#B_low2 = B & 0x0F # 0000 0000 0000 1111
A_low1 = A_low >> 4
A_low2 = A_low & 0x0F
B_low1 = B_low >> 4
B_low2 = B_low & 0x0F

# partial1 = A_low * B_low # both 8 bits 
# Compute partial products
partialL1 = A_low1 * B_low1
partialL2 = A_low1 * B_low2 << 4
partialL3 = A_low2 * B_low1 << 4
partialL4 = A_low2 * B_low2

partial1 = partialL1 + partialL2 + partialL3 + partialL4 

partial2 = (A_low * B_high) << 8
partial3 = (A_high * B_low) << 8
partial4 = (A_high * B_high) << 16

# Step 3: Align the partial products
# Already aligned

# Step 4: Add the aligned partial products
result = partial1 + partial2 + partial3 + partial4
print("Result: ", result)
print("Actual: ", 14975 * 31389)