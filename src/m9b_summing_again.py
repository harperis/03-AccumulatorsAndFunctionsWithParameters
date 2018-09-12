"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Isaac Harper.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')
    expected = 3.80826
    actual = sum_powers(5, -0.3)
    print('expected', expected)
    print('actual', actual)
    expected = '????'
    answer = sum_powers(4, .8)
    print('expected', expected)
    print('answer', answer)
    expected = "?????"
    answer = sum_powers(10, -0.5)
    print('expected', expected)
    print('answer', answer)
    expected = '????'
    answer = sum_powers(8, 1.3)
    print('expected', expected)
    print('answer', answer)



def sum_powers(n, p):
    total = 0
    power = p
    for k in range(n):
        total = total + ((k + 1) ** power)
    return total
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')
    expected = 142.384776
    answer = sum_powers_in_range(3, 100, 0.1)
    print('Test 1 expected', expected)
    print('Test 1 answer', answer)
    expected = '????'
    answer = sum_powers_in_range(5, 25, 0.7)
    print('expected', expected)
    print('answer', answer)
    expected = '?????'
    answer = sum_powers_in_range(7, 15, -0.4)
    print('expected', expected)
    print('answer', answer)
    expected = '????'
    answer = sum_powers_in_range(27, 63, 0.2)
    print('expected', expected)
    print('answer', answer)


def sum_powers_in_range(m, n, p):
    total = 0
    power = p
    for k in range(m, n + 1):
        total = total + ((k) ** power)
    return total


    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
    """
main()