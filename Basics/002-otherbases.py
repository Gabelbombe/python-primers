# Other Base operations

# Base conversion operations
print 'x = 1234 ' ; x = 1234                # all numbers are base10 derivs
print 'bin(x) '   , bin(x)                  # '0b10011010010'
print 'oct(x) '   , oct(x)                  # '02322' -> tracking octal misrepresentation at: https://goo.gl/Hab1e1
print 'hex(x) '   , hex(x)                  # '0x4d2'

# NOTE: baked in oct() should be superceded with `octal = '{:#o}'.format` if 0oXXX denomination is to be required
# NOTE: both 0oXXX and 0XXX WILL EVALUATE CORRECTLY

# Example:
# ⌘ python -c "print \"%d\" % 0o2322" '1234'
# ⌘ python -c "print \"%d\" % 02322"  '1234'

# Using the format() function to suppress prefixes
print 'format(x, \'b\')' , format(x, 'b')   # bin conversion
print 'format(x, \'o\')' , format(x, 'o')   # oct conversion
print 'format(x, \'x\')' , format(x, 'x')   # hex conversion
