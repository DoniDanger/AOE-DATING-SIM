# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Eugene = Character('Eugene', color="#E03B8B")
default Zeil = Character('Zeil', color="#E03B8B")     

# The game starts here.
label start:
    play music "audio/bgm_village_dance.mp3" fadein 1.0 volume 0.5
    "During the War of the Spanish Succession…"
    scene bg road
    show eugene smile
    "Eugene" "Greetings! I am Eugene of Savoy, but you may call me Eugene."
    "Eugene" "I'm afraid that war has once again found the  \"Hasburg Empire\"."
label sprites:
    "Eugene"  "But wait, who are you?"
    show eugene delighted
    "Eugene"  "Oh! You're from a diplomatic delegation!"
    show eugene angry
    "Eugene" "Please excuse my brusqueness."
    show extra normal at right
    "Austrian Soldier" "Sir..."
    hide extra
    "Eugene" "..."
label character:
    show eugene bored
    "Eugene" "Well, this is no way to treat such an important man."
    show eugene smile with dissolve
    "Eugene" "I want the proud colors of the Habsburgs on display!"
    Eugene "Wonderful!"    
label background:
    Eugene "Come now! Let's go to a more suitable venue for a delegation."
    scene bg town
    with fade
    
    show eugene smile at left
    Eugene "It seems we've arrived earlier than expected!"  
label bgm:
    play music "audio/bgm_air.mp3" fadein 1.0 volume 0.5
    Eugene "Oh, the musicians are playing baroque?"
    Eugene "It's too ghastly for my tastes. I'm afraid I'll have to meet you somewhere else it seems."
    
    stop music fadeout 1.0
    scene bg castle hall
    with fade
    
label sfx:
    play sound "audio/bgm_flute_concerto.mp3"
    Eugene "Oh, is it already time for our meeting?"


label choices:
    default learned = False
    Eugene "Do you have any interest in aligning with us against the French?"
menu:
    "The French are clearly trying to stir up trouble. Austria has our support!":
        jump choices1_a
    "I have my doubts about an alliance for now. I need more time to think about it.":
        jump choices1_b
label choices1_a:
    show eugene delighted
    Eugene "Good man!"
    $ learned = True
    jump choices1_common

label choices1_b:
    show eugene annoyed
    Eugene "Very well. Austria will not force war upon you, but the French very much will."
    jump choices1_common

label choices1_common:
    Eugene "I think that is enough diplomacy for tonight."
    Eugene "You should get your rest."

label flags:
    if learned:
        Eugene "The French will realize their folly now!"
    else:
        Eugene "You should realize the implications of a French-dominated Europe!"
    stop music fadeout 1.0
    return
