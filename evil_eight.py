#! /usr/bin/env python3

# welcome to evil_eight - a spooky take on the classic magic 8 ball

# made by fiolet in honor of her second favorite holiday

# to use: ./evil_eight.py <question>

import random

class color:
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

question = color.BOLD + color.RED + "What is Your Question Mortal?" + color.END
ans = input("\n" + question + "\n")
ans_low = ans.lower()


who = "who"
what = "what"
when = "when"
where = "where"
why = "why"
how = "how"
will = "will"


who_list = ["A Ghouly, Gruesome Ghost", "Your Zombie Mother and Father", "The Devil Himself", "Frankenstein and his Monster", "Evil Elves to Steal Your Shoes", "A Slime Monster from the Black Lagoon", "Your Worst Nightmare"]
what_list = ["You Will Surely Die", "Your Limbs Will Rot", "The Hounds Will Find You", "A Cauldron Will Fall on Your Head", "The Seer Requests a Smarter Question", "All You Love Will Dessicate"]
when_list = ["The Seer Sees no Future Here", "After The Mountains Turn to Dust", "Once the Hounds Have Eaten Their Fill", "When the Great Pumpkin Rises", "Never, you Fool", "At the Stroke of Midnight"]
where_list = ["In the Shrieking Hall of the Haunted Library", "Under the Rotted Apple Tree by the Cemetery", "Beneath the Coffin of Dracula", "It's All in Your Head, Mwahaha", "Within the Fold of the Mummy's Wrap", "Hidden in the Cyrpts"]
why_list = ["Because You Should Know Your Death", "All Good Things Must Eventually Die", "You Should Have Not Opened the Coffin", "To Steal Your Soul", "The Evil Wrongs Need to be Corrected - With Your Death", "To Plunder the Earth and Spill Blood"]
how_list = ["With Bat Saliva and Elbow Grease (Made From Elbows, of Course)", "With Three Turns of the Witches Broom", "Using the Blood of Twenty Virgins", "Your Question Is Irrelevant, Ask Again", "With Screams, of Course", "With a Flabled Dark Curse"]
will_list = ["It Will Never Happen Unless it is a Full Moon.", "Only if you Defeat the Vampires", "Should the Witches Agree, then Yes", "On the Third Night After the Ghouls Rise", "Not With a Stuid Question Like That, Ask Again"]
other_list = ["Question Unclear, Try Again Meatbag", "You Never Know With These Things, Try Boiling It", "Deadly Nightshade Usually Works", "After You Choke, Of Course", "Try Brains, They Might Satisfy Your Cravings", "Zombies Might Eat You, But You Should Try Anyways"]


who_random = random.choice(who_list)
what_random = random.choice(what_list)
when_random = random.choice(when_list)
where_random = random.choice(where_list)
why_random = random.choice(why_list)
how_random = random.choice(how_list)
will_random = random.choice(will_list)
other_random = random.choice(other_list)


def question():
    if who in ans_low:
        print("\n" + who_random + "\n")
    elif what in ans_low:
        print("\n" + what_random + "\n")
    elif when in ans_low:
        print("\n" + when_random + "\n")
    elif where in ans_low:
        print("\n" + where_random + "\n")
    elif why in ans_low:
        print("\n" + why_random + "\n")
    elif how in ans_low:
        print("\n" + how_random + "\n")
    elif will in ans_low:
        print("\n" + will_random + "\n")
    else:
        print("\n" + other_random + "\n")



def main():
    question()

main()
