from Apartment import *

def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0 # index for lefthalf sublist
        j = 0 # index for righthalf sublist
        k = 0 # index for alist

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
            

def ensureSortedAscending(apartmentList):
    i = 0
    j = 1
    while j < len(apartmentList):
        if apartmentList[i] < apartmentList[j]:
            i +=1
            j += 1
        else:
            return False
        
    return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    affordableApartments = ''
    affordList = []
    mergesort(apartmentList)
    for i in apartmentList:
        if (i.getRent() <= budget):
            affordList.append(i)

    k = 0
    for j in affordList:
        if k < (len(affordList) - 1):
            affordableApartments += j.getApartmentDetails() + '\n'
        else:
            affordableApartments += j.getApartmentDetails()
        k += 1
                
    return affordableApartments


