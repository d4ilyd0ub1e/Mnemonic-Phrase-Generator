#Author: Tristan J. Flynn
#Date: 4/30/22
#Description: Program creates a mnemonic phrase and allows user to choose the number

#of words, starting letter for each word, and swap out words from the initially generated

#phrase using a dictionary file

import random
import m16_module

def main():
    try:
        firstLetters = []

        print("How many words are required for your mnemonic phrase?")

        while True:
            try:
                numWords = int(input())
                #Input validation checks for integer and does not allow values

                #0 or lower or higher than 20
                while numWords <= 0 or numWords > 20:
                    print("Number of words cannot be 0 or more than 20", "\n")
                    print("How many words are required for your mnemonic phrase?")
                    numWords = int(input())

            except ValueError:
                print("ERROR: Input must be numeric","\n", "How many words are required for your mnemonic phrase?")
                continue
            else:
                break

        i = 0

        while numWords > 0:
            print("Enter the first letter of the word in position", i + 1, ":")
            inputLetter = str(input())

            #Input validation checks for alphabetic input and ensures only one

            #character is accepted
            while inputLetter.isalpha() == False or len(inputLetter) > 1 or len(inputLetter) <= 0:
                print("ERROR: Input must be alphabetic and cannot be more than one letter")
                print("Enter the first letter of the word in position", i + 1, ":")
                inputLetter = str(input())
            #Insert the inputted letter into the list firstLetters
            firstLetters.append(inputLetter)
            numWords -= 1
            i += 1


    except TypeError as e:
        print("ERROR: Incorrect data type")
    else:
        phraseGenerator(numWords, firstLetters)


def phraseGenerator (numWords, firstLetters):


    mnemonicPhrase = []
    dictList = []

    i = 0
    try:
        #Open file and read into list
        dictFile = open('wordlist.txt', 'r')
        #Remove newline delimeter
        for word in dictFile:
            word = word.rstrip('\n')
            dictList.insert(i, word)


#Create a list of lists of variable size based on how many words are needed
        numOfLists = len(firstLetters)
        listWords = [[] for i in range(numOfLists)]

#Populate the list with words that start with the selected letters
#There is a list for each letter chosen for firstLetters
        for item in listWords:
            for word in dictList:
                if word.startswith(firstLetters[i]) == True:
                    listWords[i].append(word)
            i += 1
        i = 0



        #Object creation
        thePhrase = m16_module.MnemonicPhrase(numWords, firstLetters, mnemonicPhrase, listWords)
        #Create the initial phrase by declaring mnemonicPhrase
        mnemonicPhrase = thePhrase.createInitialPhrase(firstLetters, listWords)
        #Method call the display the first version of the phrase
        thePhrase.displayPhraseNums(firstLetters, listWords, mnemonicPhrase)
        #Method call to shuffle words in the phrase
        thePhrase.shufflePhrase(mnemonicPhrase, listWords)
        print("Would you like to insert any custom words? (Y/N)")
        insertYes = str(input())
        if insertYes == 'Y' or insertYes == 'y':
            thePhrase.insertCustomWord(mnemonicPhrase)

        thePhrase.displayFinalPhrase(mnemonicPhrase)


    except IndexError:
        print("INDEX ERROR")

    except IOError:
        print("FILE ERROR")

    except TypeError:
        print("ERROR: Incorrect Data type")

    except Exception as e:
        print("A general exception has occurred:", e)


#Call main
main()
