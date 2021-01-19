import pickle
import tempfile

#pickling and unpickling  should be done using binary file since they support bytestream
#to store structured data in a file
 
# pickle.dump(object, file) <- converts object to binary file

def storePickle():
    sagar = {'key': 'Sagar', 'name': 'Sagar Paul', 'age': 24, 'iq' : 10}
    nandini = {'key': 'Nandini', 'name': 'Nandini Chaudhary', 'age': 24, 'iq' : 60}

    dbase = {}
    dbase['Sagar'] = sagar
    dbase['Nandini'] = nandini

    try:
        dbFile = open('tryPickle', 'ab')
        pickle.dump(dbase, dbFile)
    finally:
        dbFile.close()

def storePickleTemp():
    sagar = {'key': 'Sagar', 'name': 'Sagar Paul', 'age': 24, 'iq' : 10}
    nandini = {'key': 'Nandini', 'name': 'Nandini Chaudhary', 'age': 24, 'iq' : 60}

    temp = tempfile.TemporaryFile()
   
    dbase = {}
    dbase['Sagar'] = sagar
    dbase['Nandini'] = nandini

    try:
        temp.write(pickle.dumps(dbase))
        temp.seek(0)
        print(temp.read())
    finally:
        temp.close()


def loadPickle():
    dbfile = open('tryPickle', 'rb')

    dbase = pickle.load(dbfile)
    for k in dbase:
        print(k, dbase.get(k))

    dbfile.close()

if __name__ == "__main__":
    storePickle()
    loadPickle()
    


