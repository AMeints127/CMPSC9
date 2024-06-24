from Book import *
from BookCollection import *
from BookCollectionNode import *

#Book
def test_getTitle():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getTitle() == "Cujo"
def test_getAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getAuthor() == "King, Stephen"
def test_getYear():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getYear() == 1981
def test_getBookDetails():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getBookDetails() == "Title: Cujo, Author: King, Stephen, Year: 1981" 
def test_gt_():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    assert b0.__gt__(b1) == True

#BookCollectionNode
def test_getData():
    b0 = Book("Cujo", "King, Stephen", 1981)
    n = BookCollectionNode(b0)
    assert n.getData() == b0
def test_getNext():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    n = BookCollectionNode(b0)
    n1 = BookCollectionNode(b1)
    n.setNext(n1)
    assert n.getNext() == n1
def test_setData():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    n = BookCollectionNode(b0)
    n.setData(b1)
    assert n.getData() == b1
def test_setNext():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    n = BookCollectionNode(b0)
    n.setNext(b1)
    assert n.getNext() == b1

#BookCollection
def test_isEmpty():
    bc = BookCollection()
    assert bc.isEmpty() == True
    b0 = Book("Cujo", "King, Stephen", 1981)
    bc.insertBook(b0)
    assert bc.isEmpty() == False
def test_getNumberOfBooks():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    assert bc.getNumberOfBooks() == 0
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4
def test_insertBook():
    b0 = Book("Cujo", "King, Stephen", 1981)
    bc = BookCollection()
    bc.insertBook(b0)
    assert bc.getAllBooksInCollection() == "Title: Cujo, Author: King, Stephen, Year: 1981\n"
def test_getBooksByAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    assert bc.getBooksByAuthor("CLINE, ERNEST") == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
def test_getAllBooksInCollection():
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b1)
    assert bc.getAllBooksInCollection() == "Title: The Shining, Author: King, Stephen, Year: 1977\n"
def test_removeAuthor():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("King, Stephen")
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
def test_recursiveSearchTitle():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False





    
