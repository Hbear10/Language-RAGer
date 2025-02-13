vocab = open("GCSE - AQA german main vocab.csv","r",encoding="utf-8")
vocab_list = vocab.readlines()
vocab.close()
length = 1700

ind = 0


def get_ind():#get index at from file
    global ind
    index_file = open("index.txt","r")
    ind = int(index_file.read())
    index_file.close()
    print(ind)


def save_ind(x):#saves index to file
    index_file = open("index.txt","w")
    print(x, file=index_file)
    index_file.close()


def add_val(file,value):#adds a term to R,A or G file
    RAGfile = open(file, "a",encoding="utf-8")
    print(value[:-1], file=RAGfile)#output to file and remove \n
    RAGfile.close()

get_ind()

inp = None

while ind < length:
    print(vocab_list[ind][:-1])
    inp = input("~").lower()
    print("")
    if inp == "r":
        add_val("R.txt",vocab_list[ind])
    elif inp == "a":
        add_val("A.txt",vocab_list[ind])
    elif inp == "g":
        add_val("G.txt",vocab_list[ind])
    elif inp == "quit":
        quit()
    else:
        print("oh no")
        break

    ind+=1
    save_ind(ind)


