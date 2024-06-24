from BookCollectionNode import *
from Book import *

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
                

    def getBooksByAuthor(self, author):
        temp = self.head
        authorList = ''
        while temp != None:
            if temp.getData().getAuthor().upper() == author.upper():
                authorList += temp.getData().getBookDetails() + '\n'
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return authorList

    def getAllBooksInCollection(self):
        temp = self.head
        bookList = ''
        while temp != None:
            bookList += temp.getData().getBookDetails() + '\n'
            temp = temp.getNext()
            
        return bookList

    def removeAuthor(self, author):
        temp = self.head

        if temp == None: 
            return
        
        previous = None

        while temp != None:
            if temp.getData().getAuthor().upper() == author.upper():
                if previous == None:
                    self.head = temp.getNext()

                if previous != None:
                    previous.setNext(temp.getNext())

                temp = temp.getNext()

            else:
                previous = temp
                temp = temp.getNext()

            


    def recursiveSearchTitle(self, title, bookNode):
        temp = bookNode

        if temp == None:
            return False


        if temp.getData().getTitle().upper() == title.upper():
            return True
        else:
            temp = temp.getNext()
            return self.recursiveSearchTitle(title, temp)



    
    
