#Author: Tristan J. Flynn

#Date: 5/11/22

#Description: Class declaration to describe mnemonic phrase
import random

class MnemonicPhrase:
    #Student class defines the attributes of higher education students
    def __init__(self, numWords, firstLetters, listWords, mnemonicPhrase = []):
        self.numWords = numWords
        self.firstLetters = firstLetters
        self.mnemonicPhrase = mnemonicPhrase
        self.listWords = listWords


    def createInitialPhrase(self,firstLetters, listWords):
        i = 0

        mnemonicPhrase = []
        for letter in firstLetters:
            mnemonicPhrase.append(listWords[i][random.randint(0,len(listWords[i]))])
            i += 1

        return mnemonicPhrase

    def displayPhraseNums(self, firstLetters, listWords, mnemonicPhrase):

        i = 0

        print("Your current phrase is:")

        for item in mnemonicPhrase:
            print(i + 1, ")", mnemonicPhrase[i])
            i += 1

    def displayFinalPhrase(self, mnemonicPhrase = []):
        i = 0
        for item in mnemonicPhrase:
            mnemonicPhrase[i] = mnemonicPhrase[i].title()
            i += 1
        print("Thank you for using the Mnemonic Phrase Generator!")
        print("Your final phrase is:", *mnemonicPhrase, sep=' ')



    def shufflePhrase(self, mnemonicPhrase, listWords):
        shuffleWord = int(0)

        while shuffleWord != -1:
            try:
                print("Enter the number for the word you would like to shuffle (0 to stop):")
                shuffleWord = int(input()) - 1

                while shuffleWord > len(mnemonicPhrase) - 1 or shuffleWord < -1:
                    print("ERROR: Input must be numeric and must correspond with a word above")
                    print("Enter the number for the word you would like to shuffle (0 to stop):")
                    shuffleWord = int(input()) - 1

            except ValueError:
                print("ERROR: Input must be numeric, trying again...")
                shuffleWord = int(0)
                continue

        #-1 is specified as the sentinel value because we are subtracting one from
        #shuffleWord in order to use it as an accurate index value

        #Must break the loop on sentinel value to prevent index -1 to be removed a replaced
            if shuffleWord == -1:
                break


        #shuffleWord is used to remove and insert at the specified index

            mnemonicPhrase.remove(mnemonicPhrase[shuffleWord])
            mnemonicPhrase.insert(shuffleWord,listWords[shuffleWord][random.randint(0,len(listWords[shuffleWord])- 1)])
            print("Your phrase has become:")
            i = 0
            for word in mnemonicPhrase:
                print(i + 1, ")", mnemonicPhrase[i])
                i += 1

    def insertCustomWord(self, mnemonicPhrase):
        i = 0
        stop = ''
        print("Your current phrase is:")
        for word in mnemonicPhrase:
            print(i + 1, ")", mnemonicPhrase[i])
            i += 1
        while stop != 'n' or stop != 'N':

            try:
                print("Enter the number of the word you would like to replace with a custom word:")
                shuffleWord = int(input()) - 1

                while shuffleWord > len(mnemonicPhrase) - 1 or shuffleWord < 0:
                    print("ERROR: Input must be numeric and must correspond with a word above")
                    print("Enter the number of the word you would like to replace with a custom word:")
                    shuffleWord = int(input()) - 1

                print("Enter the word you would like to insert into the phrase:")
                #This is the only input that is not validated
                #No validation allows user to enter anything into their phrase
                insertedWord = str(input())
                mnemonicPhrase.remove(mnemonicPhrase[shuffleWord])
                mnemonicPhrase.insert(shuffleWord,insertedWord)
                print("Your phrase has become:")

                i = 0

                for word in mnemonicPhrase:
                    print(i + 1, ")", mnemonicPhrase[i])
                    i += 1

                print("Would you like to continue inputting custom words? (Y/N)")
                stop = input(str())

                if stop == 'n' or stop == 'N':
                    break

            except ValueError:
                print("ERROR:Input must be numeric")
                continue

    def set_numWords(self, numWords):
        self.numWords = numWords

    def set_firstLetters(self, firstLetters):
        self.firstLetters = firstLetters

    def set_mnemonicPhrase(self, mnemonicPhrase, createInitialPhrase):
        mnemonicPhrase = createInitialPhrase(firstLetters, listWords)
        self.mnemonicPhrase = mnemonicPhrase

    def set_listWords(self, listWords):
        self.listWords = listWords

    def get_numWords(self):
        return self.numWords

    def get_firstLetters(self):
        return self.firstLetters

    def get_mnemonicPhrase(self):
        return self.mnemonicPhrase

    def get_listWords(self):
        return self.listWords
