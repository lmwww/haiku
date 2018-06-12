import random;

class Dictionary:
  def getWord(self, type, syllables):
    # For now, a giant if block
    if type == 'verb':
      if syllables == 1:
        options = [
          {
            'text': 'fall',
            'syllables': 1
          },
          {
            'text': 'sit',
            'syllables': 1
          },
          {
            'text': 'walk',
            'syllables': 1
          },
          {
            'text': 'work',
            'syllables': 1
          },
          {
            'text': 'end',
            'syllables': 1
          },
          {
            'text': 'climb',
            'syllables': 1
          },
          {
            'text': 'dream',
            'syllables': 1
          },
          {
            'text': 'sleep',
            'syllables': 1
          },
          {
            'text': 'write',
            'syllables': 1
          }
        ];
      elif syllables == 2:
        options = [
          {
            'text': 'explode',
            'syllables': 2
          },
          {
            'text': 'finish',
            'syllables': 2
          },
          {
            'text': 'follow',
            'syllables': 2
          },
          {
            'text': 'shuffle',
            'syllables': 2
          },
          {
            'text': 'create',
            'syllables': 2
          },
          {
            'text': 'update',
            'syllables': 2
          },
          {
            'text': 'dissolve',
            'syllables': 2
          },
          {
            'text': 'cover',
            'syllables': 2
          },
          {
            'text': 'enter',
            'syllables': 2
          },
          {
            'text': 'shiver',
            'syllables': 2
          },
          {
            'text': 'collect',
            'syllables': 2
          },
          {
            'text': 'dissolve',
            'syllables': 2
          },
          {
            'text': 'revolve',
            'syllables': 2
          }
        ];
      else:
        options = [
          {
            'text': 'disappear',
            'syllables': 3
          },
          {
            'text': 'surrender',
            'syllables': 3
          },
          {
            'text': 'animate',
            'syllables': 3
          },
          {
            'text': 'overcome',
            'syllables': 3
          },
          {
            'text': 'escalate',
            'syllables': 3
          },
          {
            'text': 'examine',
            'syllables': 3
          },
          {
            'text': 'multiply',
            'syllables': 3
          }
        ]

    elif type == 'object':
      if syllables == 1:
        options = [
          {
            'text': 'truck',
            'syllables': 1
          },
          {
            'text': 'road',
            'syllables': 1
          },
          {
            'text': 'shoe',
            'syllables': 1
          },
          {
            'text': 'lake',
            'syllables': 1
          },
          {
            'text': 'bag',
            'syllables': 1
          },
          {
            'text': 'cloud',
            'syllables': 1
          },
          {
            'text': 'duck',
            'syllables': 1
          },
          {
            'text': 'grass',
            'syllables': 1
          },
          {
            'text': 'dog',
            'syllables': 1
          },
          {
            'text': 'cat',
            'syllables': 1
          },
          {
            'text': 'wind',
            'syllables': 1
          },
          {
            'text': 'sky',
            'syllables': 1
          },
          {
            'text': 'air',
            'syllables': 1
          },
          {
            'text': 'waves',
            'syllables': 1
          },
          {
            'text': 'ground',
            'syllables': 1
          }
        ];
      elif syllables == 2:
        options = [
          {
            'text': 'pumpkin',
            'syllables': 2
          },
          {
            'text': 'window',
            'syllables': 2
          },
          {
            'text': 'water',
            'syllables': 2
          },
          {
            'text': 'lighthouse',
            'syllables': 2
          },
          {
            'text': 'picture',
            'syllables': 2
          },
          {
            'text': 'cherry',
            'syllables': 2
          },
          {
            'text': 'apple',
            'syllables': 2
          }
        ];
      else:
        options = [
          {
            'text': 'olive tree',
            'syllables': 3
          },
          {
            'text': 'butterfly',
            'syllables': 3
          },
          {
            'text': 'wallpaper',
            'syllables': 3
          },
          {
            'text': 'paper plate',
            'syllables': 3
          },
          {
            'text': 'balcony',
            'syllables': 3
          },
          {
            'text': 'potato',
            'syllables': 3
          },
          {
            'text': 'photograph',
            'syllables': 3
          },
          {
            'text': 'wilderness',
            'syllables': 3
          },
          {
            'text': 'waterfall',
            'syllables': 3
          }
        ];


    elif type == 'concept':
      if syllables == 1:
        options = [
          {
            'text': 'hope',
            'syllables': 1
          },
          {
            'text': 'fear',
            'syllables': 1
          },
          {
            'text': 'death',
            'syllables': 1
          },
          {
            'text': 'change',
            'syllables': 1
          },
          {
            'text': 'pain',
            'syllables': 1
          }
        ];
      elif syllables == 2:
        options = [
          {
            'text': 'hunger',
            'syllables': 2
          },
          {
            'text': 'nonsense',
            'syllables': 2
          }
        ];
      else:
        options = [
          {
            'text': 'emptiness',
            'syllables': 3
          },
          {
            'text': 'memory',
            'syllables': 3
          },
          {
            'text': 'sacrifice',
            'syllables': 3
          },
          {
            'text': 'elation',
            'syllables': 3
          },
          {
            'text': 'acceptance',
            'syllables': 3
          }
        ];

    #############
    elif type == 'place':
      if syllables == 1:
        options = [
          {
            'text': 'here',
            'syllables': 1
          },
          {
            'text': 'lost',
            'syllables': 1
          },
          {
            'text': 'there',
            'syllables': 1
          },
          {
            'text': 'up',
            'syllables': 1
          }
        ];
      elif syllables == 2:
        options = [
          {
            'text': 'outside',
            'syllables': 2
          },
          {
            'text': 'at home',
            'syllables': 2
          },
          {
            'text': 'beneath',
            'syllables': 2
          },
          # {
          #   'text': 'alone',
          #   'syllables': 2
          # },
          # {
          #   'text': 'planted',
          #   'syllables': 2
          # },
          # {
          #   'text': 'fallen',
          #   'syllables': 2
          # }
        ];
      elif syllables == 3:
        options = [
          {
            'text': 'on a chair',
            'syllables': 3,
            'period': True
          },
          {
            'text': 'underneath',
            'syllables': 3
          },
          {
            'text': 'over there',
            'syllables': 3
          },
          {
            'text': 'underfoot',
            'syllables': 3
          }
        ];
      else:
        options = [
          {
            'text': 'far, far away',
            'syllables': 4,
          },
          {
            'text': 'underwater',
            'syllables': 4,
          }
        ];

    elif type == 'adjective':
      if syllables == 3:
          options = [
          {
            'text': 'simplistic',
            'syllables': 3
          },
          {
            'text': 'imminent',
            'syllables': 3
          },
          {
            'text': 'curious',
            'syllables': 3
          },
          {
            'text': 'natural',
            'syllables': 3
          },
          {
            'text': 'fluttering',
            'syllables': 3
          }
        ];
      elif syllables == 2:
        options = [
          {
            'text': 'liquid',
            'syllables': 2
          },
          {
            'text': 'lovely',
            'syllables': 2
          },
          {
            'text': 'empty',
            'syllables': 2
          },
          {
            'text': 'broken',
            'syllables': 2
          },
          {
            'text': 'upright',
            'syllables': 2
          },
          {
            'text': 'bleeding',
            'syllables': 2
          },
          {
            'text': 'icy',
            'syllables': 2
          },
          {
            'text': 'taken',
            'syllables': 2
          }
        ];
      else:
        options = [
          {
            'text': 'blue',
            'syllables': 1
          },
          {
            'text': 'deep',
            'syllables': 1
          },
          {
            'text': 'full',
            'syllables': 1
          },
          {
            'text': 'swift',
            'syllables': 1
          },
          {
            'text': 'torn',
            'syllables': 1
          },
          {
            'text': 'green',
            'syllables': 1
          },
          {
            'text': 'free',
            'syllables': 1
          },
          {
            'text': 'lost',
            'syllables': 1
          },
          {
            'text': 'found',
            'syllables': 1
          },
          {
            'text': 'short',
            'syllables': 1
          },
          {
            'text': 'grown',
            'syllables': 1
          },
          {
            'text': 'false',
            'syllables': 1
          },
          {
            'text': 'square',
            'syllables': 1
          }
        ];


    else:
      options = [
        {
          'text': 'null',
          'syllables': 1
        }
      ];

    return random.choice(options);
