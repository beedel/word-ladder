import unittest
from main import main


class TestWordLadder(unittest.TestCase):
    
    def test_wordLadder(self):
        self.assertEqual(main("hot,dot,dog,lot,log,arm,cat,man", "hit", "cog"), 5, "from hit to cog should be 5") 
        self.assertEqual(main("dot,dog,log", "lag", "cog"), 3, "from lag to log should be 3")
        self.assertEqual(main("came,case,cast", "same", "cost"), 5, "from same to cost should be 5")
        self.assertEqual(main("cord,card,ward", "cold", "warm"), 5, "from cold to warm should be 5")

        
if __name__ == "__main__":
    unittest.main()
