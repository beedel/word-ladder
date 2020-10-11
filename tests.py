import unittest
from bfs import traverse


class TestBracketMatching(unittest.TestCase):

    def test_bracketMatching(self):
        self.assertEqual(bracketMatching("()"), True, "() should be true")
        self.assertEqual(bracketMatching("())"), False, "'())' should be false")  
        self.assertEqual(bracketMatching("a (dog)"), True, "'a (dog)' should be true")
        self.assertEqual(bracketMatching("a (dog"), False, "'a (dog' should be false")    

        self.assertEqual(bracketMatching("{}"), True, "{} should be true")
        self.assertEqual(bracketMatching("{})"), False, "{}) should be false")  
        self.assertEqual(bracketMatching("a {dog}"), True, "'a {dog}' should be true")
        self.assertEqual(bracketMatching("a {dog"), False, "'a {dog' should be false")   

        self.assertEqual(bracketMatching("[]"), True, "[] should be true")
        self.assertEqual(bracketMatching("[])"), False, "[]) should be false")  
        self.assertEqual(bracketMatching("a [dog]"), True, "'a [dog]' should be true")
        self.assertEqual(bracketMatching("a [dog"), False, "'a [dog' should be false")     

if __name__ == "__main__":
    unittest.main()