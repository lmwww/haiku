import random;
import re;
from dictionary import Dictionary;

##############################################################
# Main Haiku class
##############################################################
class Haiku:
  def generateHaiku(self):
    lne = self.generateLine(5);
    lne = self.generateLine(7);
    lne = self.generateLine(5);

  ###
  # Generate a line of a given length
  #
  #   length | int | Number of syllables
  ###
  def generateLine(self, length):
    lne = Line(length);
    lne.populate();
    print lne.getText();

##############################################################
# Line class - handles building up a line of a given syllable length
##############################################################
class Line:
  # maxLength
  # remainingLength
  # text
  def __init__(self, length):
    self.maxLength = length;
    self.remainingLength = length;
    self.wordList = [];
    self.text = '';

  def populate(self):
    if self.maxLength == 5:
      possibleMoves = ['objectPlaceObject', 'objectVerbOptionalExtra'];
    elif self.maxLength == 7:
      possibleMoves = ['verbAdjectiveObject', 'adjectiveObjectVerbPlace'];

    mve = random.choice(possibleMoves);
    eval('self.' + mve + '()');

    # on the off chance we still have spaces
    while self.remainingLength > 0:
      if self.randomTrueOrFalse():
        self.pullWord('object');
      else:
        self.pullWord('place');
      self.periodify();


  # 5 = object / place / object / object
  def objectPlaceObject(self):
      self.pullWord('object');
      self.pullWord('place');
      self.periodify();
      self.pullWord('object');
      self.periodify();

  def objectVerbOptionalExtra(self):
    if self.randomTrueOrFalse():
      self.pullWord('adjective');
    self.pullWord('object');
    self.pullWord('verb');

    # Randomize!
    random.shuffle(self.wordList);

    if self.remainingLength > 0:
      if self.randomTrueOrFalse():
        self.periodify();
        if self.pullWord('concept'):
          self.periodify();
      else:
        self.pullWord('place');
        self.periodify();
        if self.pullWord('adjective'):
          self.periodify();
    else:
      self.periodify();

  def verbAdjectiveObject(self):
    self.pullWord('verb');
    self.pullWord('adjective');
    self.pullWord('object');

    # If we still have some room, make the verb longer
    if self.remainingLength > 0:
      self.wordList[0].ingify(); # the verb was the first item

    self.periodify();

    # If we STILL have some room, add a period and another object
    if self.pullWord('concept'):
      self.periodify();


  def adjectiveObjectVerbPlace(self):
    self.pullWord('adjective');
    self.pullWord('object');
    self.pullWord('verb');

    if self.randomTrueOrFalse():
      self.periodify();

    if self.randomTrueOrFalse():
      self.pullWord('object');

    # If we STILL have some room, add a period and another object
    if self.pullWord('place'):
      if self.randomTrueOrFalse():
        self.pullWord('adjective');
      self.pullWord('object');
      self.periodify();


  ###
  # Pull a word of a given type to toss into a line of poetry. Optionally cap the syllables allowed
  #
  #   type | string | Type of word to pull (e.g. verb/object)
  ###
  def pullWord(self, type):

    # Double check we actually need to do anything and haven't filled the line
    if self.remainingLength == 0:
      return False;

    wrd = Word(type);
    wrd.populate(self.remainingLength);

    self.remainingLength -= wrd.getSyllables();
    self.wordList.append(wrd);

    return True;

  ###
  # Let's add a period to the currently last word
  ###
  def periodify(self):
    self.wordList[-1].periodify();

  ###
  # Get the text property
  ###    
  def getText(self):
    txt = ''; # TODO reduce
    for wrd in self.wordList:
      txt += wrd.getText();
      txt += ' ';
    return txt;

  def randomTrueOrFalse(self):
    return random.randint(1, 2) == 1;


##############################################################
# Word class - handles all word specific logic, largely based on type
##############################################################
class Word:
  def __init__(self, type):
    self.type  = type;
    self.isIng = False;
    self.dictionary = Dictionary();

  ###
  # For a verb, add -ing (adding syllable). Don't call for non-verbs
  ###
  def ingify(self):
    if self.type == 'verb':
      self.isIng = True;

  ###
  # Make sure a period comes after this word.
  ###
  def periodify(self):
    self.hasPeriod = True;

  ###
  # Pull word details, capping the syllables
  #
  #   maxSyllables | int | Maximum syllables, in case we have a lack of space
  ###
  def populate(self, maxSyllables):
    syllablesToUse = random.randint(1, maxSyllables);
    data = self.dictionary.getWord(self.type, syllablesToUse);
    self.text = data['text'];
    self.syllables = data['syllables'];
    self.hasPeriod = data['period'] if 'period' in data else False;

  ###
  # Get the text property
  ###    
  def getText(self):
    txt = self.text;
    # TODO better logic for parsing
    if self.isIng:
      txt = re.sub('[e|s]$', '', txt);
      txt += 'ing';

    # Print out a period after
    if self.hasPeriod:
      txt += '.';
    return txt;

  ###
  # Get the syllables property
  ###    
  def getSyllables(self):
    return self.syllables;


haiku = Haiku();
haiku.generateHaiku();
