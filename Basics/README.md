### [Working with Numbers](https://github.com/ehime/python-primers/blob/master/Basics/001-numerical.py)

Python provides arithmetic operations for manipulating numbers to a straightforward manner that is similar to that used in other programming languages.
the following example assigns numbers to two variables and computes their product:

    >>> x = 3
    >>> y = 7
    >>> x * y
    28

The following examples demonstrate other arithmetic operations involving integers:

    >>> 2+2
    4
    >>> 4/3
    1
    >>> 3-8
    -5

Notice that the division ("/") of two integers is actually a truncation in which only the integer portion of the result is retained. The following example converts a floating-point nymber into an exponential form:

    >>> fnum = 0.00012345689000007
    >>> "%.14e"%fnum
    '1.123456890000070e-04'

You can use the `int()` function and the `float()` function to convert strings to numbers:

    word1 = "123"
    word2 = "456.78"
    var01 = int(word1)
    var02 = float(word2)
    print "var01: " ,var01, " var02: ",var02

The output from the preceding code block is here:

    var01: 123 var02 456.78

Alternatively, you can use the `eval()` function:

    word1 = "123"
    word2 = "456.78"
    var01 = eval(word1)
    var02 = eval(word2)
    print "var01: " ,var01, " var02: ",var02

If you attempt to convert a string that is not a valid integer of a floating-point number, Python rauses an exception, so ut;s advisable to place your code in a `try/catch` block.