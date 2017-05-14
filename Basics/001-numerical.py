# Numerical operations

# Arithmetic operations involving assignment
print 'x = 4 '  ; x = 4
print 'y = 7 '  ; y = 7
print 'x * y '  , x * y   # Variable setting

# Arithmetic operations involving integers
# NOTE: the division operation is a truncation in which only the integer portion is retained
print '4 / 3  ' , 4/3     # Division    (no float)
print '2 + 2  ' , 2+2     # Addition
print '3 - 8 '  , 3-8     # Subtraction (negatives)
print '9 * 7 '  , 9*7     # Multiplication

# Arithmetic operation on float points
print 'fnum = 0.001234567890000007' ; fnum = 0.001234567890000007
print '"%.14e"%fnum' , "%.14e"%fnum

# Using internal int() and float() functions to convert numbers
print 'word1 = "123"'        ; word1 = "123"
print 'word2 = "456.78"'     ; word2 = "456.78"
print 'var01 = int(word1)'   ; var01 = int(word1)
print 'var02 = float(word2)' ; var02 = float(word2)
print "var01 is " , var01 ,  \
      "var02 is " , var02

var01 ,      \
var02 = None \
      , None             # Clearing variable value

# Alternatively with eval()
print 'var01 = eval(word1)' ; var01 = eval(word1)
print 'var02 = eval(word2)' ; var02 = eval(word2)
print "var01 is " , var01 , \
      "var02 is " , var02
