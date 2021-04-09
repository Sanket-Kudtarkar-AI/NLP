from actions_parser import imperative_parser

sentences = ['Bring me a glass of water.',
             'Don’t ever touch my phone.',
             'Give me a pen and a pencil.',
             'Play with intensity and courage.',
             'Remember me when we are parted.',
             'Never forget the person who loves you.',
             'Take a step and don’t move.',
             'Don’t be excited about everything without reason.',
             'Don’t rush or you will fall.',
             'Read a lot to improve your writing skill.',
             'Write whenever you get a chance.',
             'Don’t stay out at night.',
             'Please open the door quickly.',
             'Have a cup of cappuccino.',
             'You wash your hand first and then eat.',
             'Kindly bring the book to me.',
             'Please forgive my meticulousness but you have spelled it wrong.',
             'Don’t ever call me a loser.',
             'Watch your step before taking it.',
             'Please grant me a loan.']

for sentence in sentences:
    imperative_parser(sentence)

sentences_2 = ["Pass the salt.",
               "Move out of my way!",
               "Shut the front door.",
               "Find my leather jacket.",
               "Be there at five.",
               "Clean your room.",
               "Complete these by tomorrow.",
               "Consider the red dress.",
               "Wait for me.",
               "Get out!",
               "Make sure you pack warm clothes.",
               "Choose Eamonn, not Seamus.",
               "Please be quiet.",
               "Be nice to your friends.",
               "Play ball!",
               "Sir, call me this weekend."]

for sentence in sentences_2:
    imperative_parser(sentence)

sentences_3 = ["He runs.",
               "She sings.",
               "I like climbing.",
               "Fran is sad.",
               "My cat is black.",
               "Dogs are cute.",
               "He is eight years old.",
               "The sky is blue.",
               "He loves pizza.",
               "The car is white.",
               "Ice is cold.",
               "He talks very fast",
               "Buy this and you will be in profit"]

for sentence in sentences_3:
    imperative_parser(sentence)
