# Other Base operations

# Base conversion operations
print 'x = 1234 ' ; x = 1234                # all numbers are base10 derivs
print 'bin(x) '   , bin(x)                  # '0b10011010010'
print 'oct(x) '   , oct(x)                  # '02322' -> missing prefix??? expected: 0o02322???
print 'hex(x) '   , hex(x)                  # '0x4d2'

# Using the format() function to suppress prefixes
print 'format(x, \'b\')' , format(x, 'b')   # bin conversion
print 'format(x, \'o\')' , format(x, 'o')   # oct conversion
print 'format(x, \'x\')' , format(x, 'x')   # hex conversion
