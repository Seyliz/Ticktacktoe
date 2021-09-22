import TickTackToe

class Collection:

    def collection_menu(self):

        while True:
            try:
                stance = int(input("-----MAINMENU-----\n------------------\n---Enter number---\n----to select-----\n------------------\n--1--TickTackToe--\n--2--Exit Game----\n------------------\n"))
            except:
                print("2Wrong Input\n Try Again")

            if stance == 1:
                TickTackToe.run_game()
            elif stance == 2:
                exit()
            else:
                print("1Wrong Input\n Try Again")

def run_collection():
    collection = Collection()
    collection.collection_menu()            

run_collection()