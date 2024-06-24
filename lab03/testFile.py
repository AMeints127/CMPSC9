from lab03 import *

def multiply_test():
    assert multiply(500,4) == 2000
    assert multiply(23,17) == 391
    assert multiply(5,0) == 0

def collectMultiples_test():
    assert collectMultiples([1,2,4,5,7], 3) == []
    assert collectMultiples([3,3,3,3], 3) == [3,3,3,3]
    assert collectMultiples([], 3) == []

def countVowels_test():
    assert countVowels("Counting vowels") == 5
    assert countVowels("Hello World") == 3
    assert countVowels("Computer science") == 6
    assert countVowels("Sty") == 0
def reverseVowels_test():
    assert reverseVowels("AEIOU") == "UOIEA"
    assert reverseVowels("AaEeIiOoUu") == "uUoOiIeEaA"
    assert reverseVowels("Stairs") == "ia"

def removeSubString_test():
    assert removeSubString("Hello Yellow", "ll") == "Heo Yeow"
    assert removeSubString("Hahahahah", "ha") == "Hah"
    assert removeSubString("Nice", "Nice") == ""

multiply_test()
collectMultiples_test()
countVowels_test()
reverseVowels_test()
removeSubString_test()
