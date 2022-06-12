# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Eugene = Character('Eugene', color="#FFD700")
define Me = Character('Me', color="#E03B8B")
define Frederick = Character('Frederick', color="#E03B8B")
default initiative = 0
default eugene_meter = 0

# The game starts here.
label start:
    play music "audio/bgm_haendel.mp3" fadein 1.0 volume 0.4
    "November 1st, 1700."
    "Charles II of Spain has died..."
    "...and Europe is now on the brink of war!"
    "The Spanish Empire hold grand posessions in the Netherlands, Italy, and the Americas under the Habsburg Charles II."
    "Spain's power served as a counterweight to the growing ambitions of the French under Louis XIV, upholding the balance of power."
    "However, with no heirs to Charles II's name, Spain has entered into a succession crisis that threatens to embroil all of Europe."
    "Bourbon and Habsburg claimants clash over the fate of the Spanish Empire, with outside powers taking either side."
    "In this fierece fight for the throne, all diplomatic overtures have failed."
    "With the recent failures of the Treaty of London, it seems more and more that the situation will escalate into war."
    "Charles II's death has already proved this."
    "On his deathbed, Charles II wrote in his will that the Bourbon Philip of Anjou will inherit the Spanish empire."
    "On Novemer 9th, the Spanish ambassadors formally offered the throne to Philip."
    "This news spells disaster for the balance of power in Europe."
    "The threat of French domination of Europe will soon become reality."
    "In these critical days, every second must be spent with care."
    "The Habsburgs will grow their alliances, the English and the Dutch will prepare their navies, and the Bourbons will ready their armies."
    "The spirit of war that engulfs the Swedes and Russians has come to collect its toll in Western Europe."
    "Although the fate of Europe is still uncertain, what will happen next is clear."
    "War is coming."
    "A war that will decide the fate of Europe for the century to come."
    "Being a close friend of Frederick I, along with a skilled diplomat and a colonel in the army, Frederick has entrusted you to lead negotiations with Austria."
    "Frederick has tasked you with guiding your nation of Prussia through this tumultuous era."
    "Through your negotiations, your decisions and ideals have the power to influence the war and the fate of Europe."
    "Will you side with the Grand Alliance in order to prevent French domination..."
    "...or will you side with the Bourbons and their right to inherit the Spanish throne."
    "Only time will tell what the best decision is for the future of Prussia."
    "May God ensure you success in whatever path you choose."
    stop music fadeout 1.0
    play music "audio/sfx_wagon_wheels.mp3" fadein 1.0 volume 0.4
    scene bg carriage inside
    with fade
    "The sound of the high-end carriage slogging through the hills of Bohemia filled the afternoon."
    "In just a few days time, the envoy will be in the seat of the Imperial Court in Vienna."
    "Although preparations were made in advance, the envoy still feels disorganized and rushed."
    "Important documents, letters, and seals are strewn about all over the seats opposite of me."
    "Despite the carriage and horses being of such high quality, the nature of the men in the envoy juxtapose the grandness on display."
    "The guards look fatigued yet they continue to march on wearily, putting on a tough act whenever I spot them."
    "The quartermaster is constantly agitated and has a sour face whenever he thinks I'm looking away." 
    "Even the carriage driver gives a dismissive smile whenever I suggest to slow the pace."
    "The rations given were ample, yet the men insist they only eat when on breaks."
    "Perhaps they too realize the urgency of arriving in Vienna as fast as possible."
    "The strength and willpower displayed makes me proud of my men, but also guilty as I look around the cozy carriage."
    "The interior of the carriage is luxurious, with expensive seating coated in fabulous colors. The door of the carriage looked to be crafted by an expert artisan."
    "There is ample space to rest and sleep, and protection from the cold outside."
    "Sitting in such a carriage while my men march through the cold fills me with guilt."
    "Hopefully, the urgency of the men will dissipate when we get closer to the Imperial Court."
    "Despite this hope, the situation of the men still lingers on in my mind."
    stop music fadeout 1.0
    "To take away from the worry of my men, I begin to reflect on what has influenced me the most. I begin to reflect on my..."
menu:
    "...upbringing and military career.":
        jump background1_a
    "...relationship with Frederick.":
        jump background1_b
    "...thoughts regarding current politics.":
        jump background1_c

label background1_a:
    play music "audio/bgm_follia.mp3" fadein 1.0 volume 0.4 
    "Perhaps remembering my youth would take my mind off things."
    "Although I was not the firstborn in my family, I was the oldest to survive to adulthood."
    "Of my three older brothers, all of them died at a young age due to pnuemonia."
    "As the remaining boy in the family, growing up a lot of pressure was placed on me. I was forced to raise my two younger siblings."
    "My parents were landed nobility, but they had little influence and meagre wealth."
    "My father was a strict, stern man, but could be loving at times."
    "I was never shown much love from him, but he always indirectly rewarded me with toys or treats for engaging in my studies."
    "As I was the eldest, most of his attention was drawn to me, and he cared little for my younger siblings."
    "My mother was the opposite of my father."
    "She was much more caring and loving, and since I was her first surviving son, she doted on me heavily. Too much."
    "Not a day I could spend playing in the courtyard without several attendants carefully observing me."
    "Despite her overattachment, she was a lovely mother and I held her opinion in high regard."
    "However, the same could not be said for my father."
    "In an effort to increase his standing, my father raised me with his idea of a noble upbringing."
    "His ambitions were high, for me to become a fine noble who would one day stand in the highest courts of Berlin, no matter what it took."
    "His stern approach to my studies made me loathe him, though. I saw him less as a father and more a strict caregiver."
    "Day and night, I was forced to my studies to read everything from the classics to history. However, the subject that most fascinated me was history."
    "The rise and falls of empires, the differing cultures and ideologies of civlizations, the movements and wars that shaped history."
    "Reading my lessons to enjoy the brilliance of ancient and modern tacticians made my studies bearable."
    "All of it engaged me, and I quickly took to learning history outside of my studies."
    "Books about the history of the great empires and leaders who shaped today filled my evenings."
    "The more I studied these leaders, the more I became disinterested with my other studies."
    "I never abandoned them and studied them attentively, but they would never answer the gap that history had left me with."
    "I began to think about what I truly wanted to become."
    "What mark I wanted to have on history." 
    "What mark I wanted to have on the world!"
    "Although this answer would not come to me until much later."
    "Through my parents efforts, I had become a fine, educated noble, but I never really enjoyed the high society that my father groomed me for."
    "Despite my noble upbringing, my taste in grand displays and decor were not as delicate as my peers."
    "I had many connections to other nobles through my parents, but rarely tried to pursue them."
    "In my youthful eyes, they were annoying, snobby, and judgemental. Hardly people I wanted to form anything meaningful with."
    "I continued like this for many years, dutifully engaging in my studies until I came of age."
    "By then, my parents decided that I was ready to attend an academy for the nobility, where I would probably fulfill my father's dreams."
    "Although the idea disheartened me, I believed I had no other options, and did not dissent with their decision."
    "I secretly dreaded the thought of going to such an academy, but I had no answer as to why?"
    "Was it because father wanted me to attend? Or perhaps I just had enough of my studies?"
    "But if I dread attending so much, what was the point of my studies in the first place? Why did I work so hard?"
    "These questions continued to plague me throughout the coming months, and my time of enrollment was almost nearing."
    "By this point, I had neither the bravery nor the will to protest, as it would bring nothing."
    "As I silently accepted my fate, an event would occur that would shape me into the man I became today."
    "To celebrate my coming of age, several relatives were called over, one of them being my uncle who I had only rarely met in my childhood."
    "He was a captain in the army, a free spirit, and he spent much of his time with me raving on about his stories in the military."
    "As the evening continued, his stories would only captivate me more and more, until I realized something."
    "I was not sure how or why, but I believed that I could find the answer to my purpose in the military."
    "After years of indecision and doubt, I discovered the path to make my mark."
    "I would enroll in the military academy."
    "When I told my parents about my wanting to enroll in the military academy, their protests could be heard around the entire estate!"
    "My father looked at me with a face mixed with anger and disappointment."
    "Father" "You're the eldest of our family, you can't die in some bloody battlefield for some mistaken idea of honor!"
    "Father" "Don't make all your studying and training for nothing!"
    "Father" "This is just some foolish idea planted in your head by your useless uncle. Don't make all my work for nothing."
    "My mother balled her eyes out, pleading that I don't go."
    "Mother" "Please, my son. Please do not go. I can't have another one of my children die so soon."
    "Although they continued to protest, I insisted on my enrollment, that I needed to find my place in the world."
    "After heavy argument and bitter debates, with a defeated look on his face, my father consented to my enrollment."
    "On the day of my leave, my family lined out to bid me my farewells."
    "With tears in their eyes, they vowed I promise to return safely. My father could only look at me solemnly."
    "Although I ensured them I would come home safely and with several victories to my name, in truth, I held a sliver of doubt about going."
    "With a heavy heart, I said my goodbyes before departing my family estate for the academy."
    "After a few days travel, I finally arrived to the Berlin Military Academy."
    "The first few months of the academy were brutal."
    "Adjusting to the style and attitude of the military after spending so much time with being trained with a different mindset took significant effort."
    "I was isolated at first, not having much connections or people to talk to. Although I was far from the only noble in the academy, I did not make much effort to speak to them."
    "Even when my peers gave me several opportunities to connect with them, I rejected them outright and was very hostile."
    "After all, weren't these the people I joined the academy to escape from?"
    "Most people in class were quick to ignore me soon after."
    "Despite all the hardships I faced at first, some self-inflicted, I never dismayed or lost hope in my goals. I continued to study like I had in my childhood."
    "With rigorous effort and persistent attitude, I began to assimilate into the culture of the academy."
    "Although my grades were mediocre, I never relented, and continued to study the art of war."
    "Eventually, my grades improved and I began to command some respect amongst my fellow cadets."
    "I began to connect to more people in my class and even started to respect them."
    "My peers may have had different backgrounds, ideas, and motivations for joining, but they all put in the same work and effort as I did."
    "With the confidence from my successes, I even tried to reconnect with nobles I previously avoided, not expecting much."
    "However, they did not hold any grudges against me for my past belligerence, and I enjoyed speaking with many of them."
    "After my conversations, I was confused on why I tried so much to avoid them in the past."
    "These people were just like me, with their own goals and dreams that they hope to achieve through the military."
    "So why did I hate them so much?"
    "I then came to the realization."
    "The nobility reminded me too much of my father."
    "The selfish, cold idea of nobility that my father had implanted into my belief of what a noble was had made me uncomfortable speaking to any of them."
    "I had dreaded going to the academy my father wanted me to because I was afraid that I would become like him, like his idea of nobility."
    "With this realization, my preujdice agaisnt nobles was toned down, although I still held some uncertainity in my heart whenever dealing with nobility."
    "I began connecting with other nobles more freely, and found many of them I could actually enjoy conversation with."
    "Walking the halls of the academy with fellow nobles was much more enoyable than spending them with the spoiled nobles of my childhood who never really shared my interests."
    "This was not to say that I didn't have my fair share of disagreements or quarrels with other nobles in the academy, but everything was mostly fine."
    "From then on, nothing of note occurred past my initial troubles."
    "I spent the next few years in the academy spending my youth how I wanted to. I committed to my studies in the day and went to parties and social gatherings when I had the chance."
    "After a few years, I had become well-respected amongst my peers and was a well-known figure among the seniors of the academy."
    "With my newly formed connections and high grades, I graduated from the academy as an officer."
    "From then on, I was free to do whatever I wanted."
    stop music fadeout 1.0
    jump background1_common
                       
label background1_b:
    "I did not finish this part lol"
    stop music fadeout 1.0
    jump background1_common
                                         
label background1_c: 
    play music "audio/bgm_symphony7.mp3" fadein 1.0 volume 0.7 
    "Considering the state of events, perhaps it would be best to recount the politics and diplomatic goals of Brandenburg-Prussia."
    "How is a statesmen supposed to negotiate foreign affairs if he can not remember the goals of his nation?"
    "Although the politics of Europe were something I generally ignored, it was hard for me to ignore the constant issues that plagued the Empire."
    "With the end of the Nine Years War, Prussia came out with little for how hard it had fought. Despite the best efforts of me and Frederick, we had failed."
    "By then, my spirits were crushed. Although I attended Ryswick, I failed to get any meaningful settlement for Prussia."
    "Brandenburg-Prussia still remained a dukedom, and Frederick was still not recognized as a King within the empire."
    "I remained in the circle of Frederick, but resigned myself from politics for a while, only caring for what Frederick assigned to me."
    "My ignorance of politics may have been short-sighted and even disatrous for a diplomat, but Frederick did not care for that."
    "To him, even the greatest of his diplomats had failed him at Ryswick, and so my misgivings were acceptable to him."
    "This habit of mine continued for a few years until the health of Charles II had failed considerably."
    "I had not paid much attention to the affair of the Spanish Succession, seeing how it the situation seemed to be so heavily contested."
    "Even then, if war was to break out between the Empire and the Bourbons, Prussia would likely not be rewarded for its service once again."
    "So, the matter for me was pointless."
    "This was until I had an evening dinner with Frederick like I always usually had."
    "Frederick was much paler in those days, and had an uneasy look about him."
    "He seemed to have something on his mind, but I did not know whether to pry about it or not."
    "After a few minutes of uneasy conversation, I decided to press the matter."
    Me "What's the issue Frederick?"
    Frederick "Karl Behncke, how knowledgeable are you on the situation in Spain?"
    Me "To be quite frank, I've barely paid it any mind."
    Frederick "You fool, what have you been doing these past few years!"
    Frederick "Living in ignorance because of one lost opportunity?!"
    Me "I-"
    "I could not come up with a reasonable response. Perhaps I had let my past failures consume me."
    "I thought that Frederick's toleration of my ignorance was approval of it, but I realize now that he simply just didn't want to reopen the wounds of Ryswick."
    "All I could do now was intently listen to Frederick's speech."
    Frederick "Listen, Karl. This affair is not just some war where Prussia will be used and discarded again."
    Frederick "A union between Spain and France will be disatrous for not just the Empire, but for Europe as a whole."
    Frederick "Ambitious as Louis XIV is, even he must realize that the powers of Europe will not stand for a Bourbon Spain."
    Frederick "I have a proposal for you."
    Me "A proposal?"
    Frederick "Yes. Would you like to head the delegation to Emperor Leopold regarding a military alliance?"
    Me "You want me to head the delegation? I'm sorry, Frederick but that's insane."
    Me "You've heard it from me yourself, I'm ignorant on the matter. I'm sure there are far more capable statesmen who have more interest in this matter than I."
    Me "I will have to decline."
    "Frederick's calm and collected demeanor was soon replaced with anger."
    Frederick "If you are ignorant, then you will learn. If you are incapable, you will become capable. This is the man I know you are, the man who I've trusted in so many battles before."
    Frederick "I come to you precisely because you hold no interest in fame or glory, no interest in boosting your career. Only serving your duty faithfully." 
    Frederick "\"Capable\" statesmen come and go, but trustworthy ones hold the most value to me."
    Me "But I've failed you before at Ryswick! How can you trust me again with such a monumental task?"
    Frederick "You were not the only one to fail at Ryswick! I failed at Ryswick, the entire delegation failed!" 
    Frederick "We failed not because we did not try our best, but because our allies failed to reward us."
    Frederick "Our allies thought us nothing more than mercenaries, and did not value our service because they believed they could afford to ignore us."
    Frederick "Unfortunately for them, reliable allies are a tough find nowadays, and any opportunity to find one can simply not be passed up."
    Frederick "Listen to my offer once more, Karl. Emperor Leopold is short on allies against the Bourbons, and now she is looking towards Prussia."
    Frederick "This is our chance to amend the failures of Ryswick. If we are successful, we can finally unite Brandenburg and Prussia into one, with me as king."
    Frederick "I entrust this to you because you are my greatest friend and my greatest negotiator."
    Frederick "So, will you accept my offer?"
    "After a few moments of great deliberation, I hesitatingly responded to her offer."
    Me "Yes, I think I will."
    Frederick "There's the man that fought with me at Bonn. I knew I could trust you."
    "It seems that the flurry of shocking news coming from Spain had been enough to set both me and Frederick into motion."
    "After our conversation, I took great effort to become the statesmen Frederick believed me capable of."
    "I went back into the habit of my studies, intently listening to every piece of news and intelligence coming from Spanish affair."
    "I observed the Treaty of London with great interest, but it soon became just another failed treaty."
    "By then, it was clear to me that war was inevitable."
    "I took to improving relations with our neighbors and setting up alliances to ensure Prussia could not be divided."
    "Although the Empire's war with France was certain, Prussia's involvement had not been set in stone yet."
    "Avoiding war with France could benefit Prussia more, especially with other fronts appearing."
    "With the Great Northern War raging, a rare opportunity presented itself to Prussia."
    Me "You know, Frederick. It's not too late to avoid the alliance with the Habsburgs."
    Me "If we assist the Danes in their war with Sweden, we'll be able to recover Pommerania."
    Frederick "Be that as it may, France becoming a union with Spain is a much more worrying matter."   
    Frederick "Although we can take advantage of this, the implications of the Empire losing this war are even greater than a victory over Sweden."
    Frederick "Continue preparing your envoy to Austria."
    Me "As you wish, Frederick."
    "With that, the Swedish affair was put on hold, at least for now."
    "With full control of the envoy, I believed that the timing of our envoy would be crucial."
    "Delaying the envoy to Austria until would have the most effect."
    "After all, coming to Austria before it was truly desperate would be a disadvantage in negotiations."
    "It would be better to hold off until the last critical junction to achieve our goals."
    "With this in mind, my preparations for the envoy continued as usual..."
    "..until drastic news came in from the Spain affair."
    "{u}Charles II is dead, and the Bourbon Philip of Anjou is named his successor.{/u}"
    "Before most could even process the news, my envoy immediately departed for Vienna."
    "At last, the critical junction has appeared."
    "8 days after Charles II's death, the Spanish ambassadors officially offered the crown to Philip."
    "Whether he accepts is uncertain, but now Austria is surely in need of strong allies."
    "Any negotiations with Leopold will surely bear fruit, so long as I take the initiative."
    "I will ensure that this will not be another Ryswick."
    stop music fadeout 1.0
    jump background1_common

label background1_common:
    "As I trailed off in my thoughts, I grew exhuasted for the night."
    "I told my officers to give the necessary orders to the men and took to my carriage."
    "After just a few moments I began to fall alseep."
    scene bg road
    with fade
    
    "As I woke up, I found myself inexplicably tired."
    "Perhaps even I've exhausted myself as much as my men and just haven't noticed it."
    "Either way, my reflections from last night seem to have made me much more cumbersome."
    "As I look out the window, I see plains."
    "We must no longer be in Bohemia, which means we're nearing Vienna."
    "The closer we get to Vienna, the more anxious I get myself regarding the negotiations."
    "Although I promised to Frederick and myself that the mistakes of Ryswick would never be repeated, ensuring that is a completely different ordeal."
    "Even with the boost to my confidence from Frederick, negotiating with the Emperor is still an intensive obstacle."
    "Failing at these negotiations could cost Prussia a significant opportunity."
    "Having these weights on my shoulders make failure at Vienna an even worse prospect."
    "Thinking about the matter only makes me more tired."
    play sound "audio/sfx_horse_gallop.mp3"
    "As I sit there in worry over my predicament, I did not notice the galloping of the horses ahead of me."
    "My carriage started to slow down and I soon realized something was occurring."
    "Once the galloping got closer, both the sound of my envoy and the galloping abruptly ended."
    stop sound fadeout 1.0
    "A few seconds passed and nothing happened."
    "In the complete silence, my mind began to wonder."
    Me "Why did the carriage stop?"
    Me "Is it a robbery? It can't be in this day and age?"
    Me "Did the carriage run someone over? I can't afford to start an incident!"
    Me "Should I step out of the carriage?"
default eugene1 = False
menu:
    "Step out of the carriage. If there's danger I must check it out.":
        $ initiative += 1
        $ eugene_meter += 1
        jump choices1_a
    "Stay in the carriage. It might be dangerous.":
        jump choices1_b
label choices1_a:
    "After a few seconds of indecision, I decided to step out and inspect the situation."
    $ eugene1 = True
    jump choices1_common

label choices1_b:
    "I waited for what seemed to be an eternity inside the carriage, hoping that the the situation had passed."
    "Instead, the silence was broken by a knock on the carriage door."
    "Carriage Driver" "Sir, there seems to be a man wanting to meet you."
    "Being forced to exit, I worked up the courage and walked towards the door."
    jump choices1_common
  
label choices1_common:
    "Stepping out the carriage door, the driver had a worried expression on his face."
    "Once I looked around, a hidden figure stood in front of the envoy column."
    "Looking behind him, it seemed there were several soldiers behind the figure with faces of concern."
    "Upon closer inspection of the figure, a bold, dominating aura was revealed."
    "With a bored look on their face, the figure hopped off their horse."
    "The figure then broke the delicate silence."
    play music "audio/bgm_village_dance.mp3" fadein 1.0 volume 0.4
    show eugene bored 
    Eugene "Greetings! I am Eugene of Savoy, but you may call me Eugene."
    Eugene "I'm afraid that I don't know your name. Who might you be?"
    Me "I'm the leader of the Prussian delegation to Austria."
    show eugene shocked
    Eugene  "Oh! You're from the Prussian diplomatic delegation!"
    show eugene laugh
    Eugene "Please excuse my brusqueness."
    "The faces of the soldiers behind the laughing figure quickly changed from nervousness to embarrassment."
    if eugene1:
        show eugene delighted
        Eugene "I appreciate your decisiveness! Such a trait is missing in some statesmen today."
        Eugene "Most diplomats need to be carried around by their men. Good to see a man who can take the initiative."
    else:
        show eugene angry2
        Eugene "I could've mistaken you for a French delegate with how long it took you to get out!"
        Eugene "A diplomat should take more initiative, not wait for his driver to knock for him."
        "I had no rebuttal to her statements. She was justifiably angry."
          
    show eugene smile 
    Eugene "Well, no matter. This is no way to treat such an important man."
    Eugene "I want the proud hospitality of the Habsburgs on display!"
    Eugene "Come now! Let's go to a more suitable venue for a delegation."
    stop music fadeout 1.0
    scene bg town
    with fade
     
    show eugene smile at left
    Eugene "It seems we've arrived earlier than expected!"  
label bgm:
    play music "audio/bgm_air.mp3" fadein 1.0 volume 0.2
    Eugene "Oh, the musicians are playing baroque?"
    Eugene "It's too ghastly for my tastes. I'm afraid I'll have to meet you somewhere else it seems."
    
    stop music fadeout 1.0
    scene bg castle hall
    with fade
    
label sfx:
    play music "audio/bgm_flute_concerto.mp3" fadein 1.0 volume 0.2
    Eugene "Oh, is it already time for our meeting?"
                                                               
    Eugene "Do you have any interest in aligning with us against the French?"
menu:
    "The French are clearly trying to stir up trouble. Austria has our support!":
        jump choices2_a
    "I have my doubts about an alliance for now. I need more time to think about it.":
        jump choices2_b
label choices2_a:
    show eugene delighted
    Eugene "Good man!"
    $ eugene_meter += 1
    Eugene "The French will realize their folly now!"
    jump choices2_common
                                                              
label choices2_b:
    show eugene annoyed
    Eugene "Very well. Austria will not force war upon you, but the French very much will."
    Eugene "You should realize the implications of a French-dominated Europe!"
    jump choices2_common

label choices2_common:
    Eugene "I think that is enough diplomacy for tonight."
    Eugene "You should get your rest."
    Eugene "Good night!"
    stop music fadeout 1.0
    return
