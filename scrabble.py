#how will this affect git? Let's find out!
import itertools

SCRABBLE_DICTIONARY = ['sour', 'spur', 'spud', 'stud', 'stun', 'a', 'dog', 'terrible', 'hopeless']
INTEGER = 4

class Word():

    LETTER_SCORE_DICTIONARY = {
                'a': 1, 'b': 3, 'c': 3,  'd': 2,
                'e': 1, 'f': 4, 'g': 2, 'h':4,
                'i': 1, 'j': 8, 'k': 5, 'l':1,
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10,
                'r':1, 's':1, 't':1, 'u':1, 'v':4,
                'w':4, 'x':8, 'y':4, 'z':10
                }

    def __init__(self, str1):
        self.word = str1.lower()
        self.value = self.__calculate_value()

    def __calculate_value(self):
        score = 0
        for letter in self.word:
            score += self.LETTER_SCORE_DICTIONARY[letter]
        return score

    def __str__(self):
        return self.word + ", " + str(self.value)

class Dictionary():

    def __init__(self, list1, int1):
        self.list1 = list1
        self.int1 = int1
        self.words = [Word(word) for word in self.__filter_on_wordlength()]

    def __filter_on_wordlength(self):
        return [word for word in self.list1 if len(word) == self.int1]

    def contains(word):
        if word in self.words:
            return True
        return False


class Ladder():

    def __init__(self, initial_ladder):
        self.ladder = initial_ladder
        self.descending = False
        self.length = 0

    def is_scrabble_ladder(self):
        #if self.length > 0 and self.length == len(self.ladder):
            #return True
        #return False
        if len(self.ladder) < 3 or len(self.ladder) % 2 != 1:
            return False
        peak = len(self.ladder) / 2 - 1
        for n in range(len(self.ladder) - 1):
            if n <= peak:
                if not self.ladder[n].value < self.ladder[n + 1].value:
                    return False
            elif n > peak:
                if not self.ladder[n].value > self.ladder[n + 1].value:
                    return False
        return True
        
        if self.length > 0 and self.length == len(self.ladder):
            return True
        return False

    def add_word(self, word):
        if self.word_is_valid_addition(word):
            self.ladder.append(word)
            if len(self.ladder) > 1 and not self.descending and word.value < self.ladder[-2].value:
                self.descending = True
                self.length = len(self.ladder) * 2 - 3

    def word_is_valid_addition(self, word):
        # the ladder is empty, so any word works
        if len(self.ladder) == 0:
            return True
        # Ladder is complete
        if self.length > 0 and self.length == len(self.ladder):
            return False
        # check similarity of words
        difference = False
        for n in range(len(word.word)):
            if word.word[n] != self.ladder[-1].word[n]:
                if difference:
                    return False
                else:
                    difference = True
        # Ladder already contains the word
        for n in range(len(self.ladder)):
            if self.ladder[n].word == word.word:
                return False
        # New word's value is greater, and the ladder hasn't reached the "peak" yet
        if word.value > self.ladder[-1].value and not self.descending:
            return True
        # New word's value is less, and the ladder is past the "peak"
        if word.value < self.ladder[-1].value and self.descending:
            return True
        # Word has a lower value.
        if word.value < self.ladder[-1].value and len(self.ladder) > 1:
            return True
        return False

    def score(self):
        score = 0
        for word in self.ladder:
            score += word.value
        return score

    def equals(self, ladder1):
        if len(self.ladder) != len(ladder1.ladder):
            return False
        flag1 = True
        for n in range(len(self.ladder)):
            if self.ladder[n].word != ladder1.ladder[n].word:
                flag1 = False
        a_list = list(ladder1.ladder)
        flag2 = True
        for n in range(len(self.ladder)):
            if self.ladder[n].word != a_list[n].word:
                flag1 = False
        return flag1 or flag2


    def __str__(self):
        return_string = "This Ladder contains: "
        for word in self.ladder:
            return_string += str(word) + ", "
        return return_string

    def __repr__(self):
        return self.__str__()

class Ladders():

    #HIGHEST_SCORE = 0
    #HIGHEST_SCORE_LADDERS = []

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.HIGHEST_SCORE = 0
        self.HIGHEST_SCORE_LADDERS = []

    def calculate_highest_score(self):

        def method_helper(dictionary, ladder):
            print(ladder)
            #base case
            if ladder.is_scrabble_ladder():
                print("found one")
                if ladder.score() == self.HIGHEST_SCORE:
                    #check for reverse duplicates
                    for ladder1 in self.HIGHEST_SCORE_LADDERS:
                        if ladder1.equals(ladder):
                            print("DUPLICATE")
                            return
                    self.HIGHEST_SCORE_LADDERS.append(ladder)
                    print("ADDED ONE")
                if ladder.score() > self.HIGHEST_SCORE:
                    print("NEW HIGH SCORE")
                    self.HIGHEST_SCORE = ladder.score()
                    self.HIGHEST_SCORE_LADDERS = [ladder]
                return
            #if the ladder isn't complete, check more combinations
            for word in dictionary.words:
                if ladder.word_is_valid_addition(word):
                    #print(list(ladder.ladder))
                    #print(list(ladder.ladder).append(word))
                    a_list = list(ladder.ladder)
                    a_list.append(word)
                    #print(a_list)
                    #method_helper(dictionary, Ladder(list(ladder.ladder).append(word)))
                    method_helper(dictionary, Ladder(a_list))


        #for ladder in ladders:
            #if ladder.is_scrabble_ladder():
                #if ladder.score() > highest_score:
                    #highest_score = ladder.score()
            #else:
                #pass
        #return highest_score

        #ladders = []
        #for word in self.dictionary.words:
            #ladders.append(Ladder(itertools.product([word], self.dictionary)))
            #ladders.append(Ladder([word]))
        #for ladder in ladders:
        method_helper(self.dictionary, Ladder([]))
        print(self.HIGHEST_SCORE)
        #print(self.HIGHEST_SCORE_LADDERS)
        for ladder in self.HIGHEST_SCORE_LADDERS:
            print(ladder)

dictionary = Dictionary(SCRABBLE_DICTIONARY, 4)

ladder1 = Ladder([Word("sour")])
ladder2 = Ladder([Word("sour"), Word("spur")])
ladder3 = Ladder([Word("sour"), Word("spur"), Word("spud")])
ladder4 = Ladder([Word("sour"), Word("spur"), Word("spud"), Word("stud")])
ladder5 = Ladder([Word("sour"), Word("spur"), Word("spud"), Word("stud"), Word("stun")])
ladders = [ladder1, ladder2, ladder3, ladder4, ladder5]


bla = Ladders(dictionary)
bla.calculate_highest_score()
aladder = Ladder([])
print(aladder.length)
aladder.add_word(Word("sour"))
print(aladder.length)
aladder.add_word(Word("spur"))
print(aladder.length)
aladder.add_word(Word("spud"))
print(aladder.length)
aladder.add_word(Word("stud"))
print(aladder.length)
aladder.add_word(Word("stun"))
print(aladder.length)
