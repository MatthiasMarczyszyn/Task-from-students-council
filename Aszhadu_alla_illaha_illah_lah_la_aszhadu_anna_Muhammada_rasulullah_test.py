import unittest

import Aszhadu_alla_illaha_illah_lah_la_aszhadu_anna_Muhammada_rasulullah as ash


class TestPalindrome(unittest.TestCase):
    """
    Test for if_palindrom function. I made a few simple test for checking all possiblity of function behavior.
    I used some normal words , empty string, string with numbers and strings with random letters.
    """

    def test_if_palindrome(self):
        self.assertEqual(ash.if_palindrome("bob"), True)
        self.assertEqual(ash.if_palindrome("Allah"), True)
        self.assertEqual(ash.if_palindrome("to"), False)
        self.assertEqual(ash.if_palindrome("jedyny"), False)
        self.assertEqual(ash.if_palindrome("Bog"), False)
        self.assertEqual(ash.if_palindrome("Papiez"), False)
        self.assertEqual(ash.if_palindrome("polak"), False)
        self.assertEqual(ash.if_palindrome("gwalcil"), False)
        self.assertEqual(ash.if_palindrome("male"), False)
        self.assertEqual(ash.if_palindrome("dzieci"), False)
        self.assertEqual(ash.if_palindrome("konstantynopolitanczykowianeczka"), False)
        self.assertEqual(ash.if_palindrome(""), False)
        self.assertEqual(ash.if_palindrome("h"), True)
        self.assertEqual(ash.if_palindrome("hhhaabbkkll"), True)
        self.assertEqual(ash.if_palindrome("fffggg"), False)
        self.assertEqual(ash.if_palindrome("hhhaabbkkll11"), True)
        self.assertEqual(ash.if_palindrome("fffggg23"), False)


if __name__ == "__main__":
    unittest.main()
