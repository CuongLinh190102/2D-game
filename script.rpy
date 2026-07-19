define config.skip_delay = 75



transform wait_for_voice:
    # Hiệu ứng cho thấy đang chờ
    alpha 1.0
    block:
        linear 0.5 alpha 0.5
        linear 0.5 alpha 1.0
        repeat

screen voice_waiting():
    zorder 100
    if pygame.mixer.get_busy():
        add "wait_icon" at wait_for_voice
###############################################################################transistion ao dieu
# Tạo label cho hiệu ứng pixellate
label pixellate_efafect(silas1):
    show expression f"silas1_pixellate5"
    with None
    pause 0.1
    
    
    show expression f"silas1_pixellate10"
    with None
    pause 0.1
    show expression f"silas1_pixellate15"
    with None
    pause 0.1
    show expression f"silas1_pixellate20"
    with None
    pause 0.1
    
    show expression f"silas1_pixellate25"
    with None
    pause 0.1
    show expression f"silas1_pixellate30"
    with None
    pause 0.1
    show expression f"silas1_pixellate35"
    with None
    pause 0.1
    
    show expression f"silas1_pixellate50"
    with None
    pause 0.2
    
    show expression f"silas1_pixellate100"
    with None
    pause 0.15
    
    show expression f"silas1_pixellate50"
    with None
    pause 0.1

    show expression f"silas1_pixellate35"
    with None
    pause 0.1
    show expression f"silas1_pixellate30"
    with None
    pause 0.1
    
    show expression f"silas1_pixellate25"
    with None
    pause 0.1
    

    return
################################################################################
###############################################################################transistion ao dieu
# Tạo label cho hiệu ứng pixellate
label pixellate_effect(silas1):
    show expression f"silas1_pixellate5"
    with None
    pause 0.01
    show expression f"silas1_pixellate10"
    with None
    pause 0.01
    show expression f"silas1_pixellate15"
    with None
    pause 0.01
    show expression f"silas1_pixellate20"
    with None
    pause 0.01
    
    show expression f"silas1_pixellate25"
    with None
    pause 0.01
    show expression f"silas1_pixellate30"
    with None
    pause 0.01
    show expression f"silas1_pixellate35"
    with None
    pause 0.01
    
    show expression f"silas1_pixellate50"
    with None
    pause 0.01
    
    show expression f"silas1_pixellate100"
    with None
    pause 0.01
    
    show expression f"silas1_pixellate120"
    with None
    pause 0.01

    show expression f"silas1_pixellate130"
    with None
    pause 0.01
    show expression f"silas1_pixellate140"
    with None
    pause 0.01
    
    show expression f"silas1_pixellate150"
    with None
    pause 0.01

    show expression f"silas1_pixellate160"
    with None
    pause 0.01
    show expression f"silas1_pixellate170"
    with None
    pause 0.01
    show expression f"silas1_pixellate180"
    with None
    pause 0.01
    show expression f"silas1_pixellate190"
    with None
    pause 0.01
    show expression f"silas1_pixellate200"
    with None
    pause 0.01
    show expression f"silas1_pixellate210"
    with None
    pause 0.01
    show expression f"silas1_pixellate220"
    with None
    pause 0.01
    show expression f"silas1_pixellate230"
    with None
    pause 0.01
    show expression f"silas1_pixellate240"
    with None
    pause 0.01
    show expression f"silas1_pixellate250"
    with None
    pause 0.01
    

    return
################################################################################


#############################################################################define new transitions
init:
    $ circlewipe = ImageDissolve("wipes/circlewipe-cw.jpg", 1.0, 8)
    $ ccirclewipe = ImageDissolve("wipes/circlewipe-ccw.jpg", 1.0, 8)
    $ bites = ImageDissolve("wipes/bites.jpg", 1.0, 8)
    $ bowtie = ImageDissolve("wipes/bowtie.png", 1.0, 8)
    $ cmet = ImageDissolve("wipes/cmet.jpg", 1.0, 8)
    $ cwside = ImageDissolve("wipes/cw-side.jpg", 1.0, 8)
    $ cwtop = ImageDissolve("wipes/cw-top.jpg", 1.0, 8)
    $ dots = ImageDissolve("wipes/dots.png", 1.0, 8)
    $ edges = ImageDissolve("wipes/edges.png", 1.0, 8)
    $ flips = ImageDissolve("wipes/flips.png", 1.0, 8)
    $ fur = ImageDissolve("wipes/fur.jpg", 1.0, 8)
    $ goslow = ImageDissolve("wipes/goslow.png", 5.0, 8)
    $ letter = ImageDissolve("wipes/letter.png", 1.0, 8)
    $ maze = ImageDissolve("wipes/maze.png", 1.0, 8)
    $ radio = ImageDissolve("wipes/radio.jpg", 1.0, 8)
    $ snake = ImageDissolve("wipes/snake.png", 1.0, 8)
    $ snake2 = ImageDissolve("wipes/snake2.png", 1.0, 8)
    $ snakes = ImageDissolve("wipes/snakes.png", 1.0, 8)
    $ sunshine = ImageDissolve("wipes/sunshine.jpg", 1.0, 8)
    $ glasswool = ImageDissolve("wipes/glasswool.jpg", 1.0, 8)
    $ wet = ImageDissolve("wipes/wet.jpg", 1.0, 8)

    $ w1 = ImageDissolve("wipes/1.jpg", 1.0, 8)
    $ w2 = ImageDissolve("wipes/2.png", 1.0, 8)
    $ w3 = ImageDissolve("wipes/3.jpg", 1.0, 8)
    $ w4 = ImageDissolve("wipes/4.jpg", 1.0, 8)
    $ w5 = ImageDissolve("wipes/5.jpg", 1.0, 8)
    $ w6 = ImageDissolve("wipes/6.jpg", 1.0, 8)
    $ w7 = ImageDissolve("wipes/7.png", 1.0, 8)
    $ w8 = ImageDissolve("wipes/8.jpg", 1.0, 8)
    $ w9 = ImageDissolve("wipes/9.jpg", 1.0, 8)
    $ w10 = ImageDissolve("wipes/10.jpg", 1.0, 8)
    $ w11 = ImageDissolve("wipes/11.jpg", 1.0, 8)
    $ w12 = ImageDissolve("wipes/12.jpg", 1.0, 8)
    $ w13 = ImageDissolve("wipes/13.jpg", 1.0, 8)
    $ w14 = ImageDissolve("wipes/14.png", 1.0, 8)
    $ w15 = ImageDissolve("wipes/15.png", 1.0, 8)
    $ w16 = ImageDissolve("wipes/16.png", 1.0, 8)
    $ w17 = ImageDissolve("wipes/17.png", 1.0, 8)
    $ w18 = ImageDissolve("wipes/18.png", 1.0, 8)
    $ w19 = ImageDissolve("wipes/19.jpg", 1.0, 8)
    $ w20 = ImageDissolve("wipes/20.jpg", 1.0, 8)
    $ w21 = ImageDissolve("wipes/21.jpg", 1.0, 8)
    $ w22 = ImageDissolve("wipes/22.png", 1.0, 8)
    $ w23 = ImageDissolve("wipes/23.png", 1.0, 8)
    $ w24 = ImageDissolve("wipes/24.png", 1.0, 8)
    $ w25 = ImageDissolve("wipes/25.png", 1.0, 8)
    $ w26 = ImageDissolve("wipes/26.png", 1.0, 8)
    $ w27 = ImageDissolve("wipes/27.png", 1.0, 8)
    $ w28 = ImageDissolve("wipes/28.png", 1.0, 8)

    $ w29 = ImageDissolve("wipes/29.png", 1.0, 8)
    $ w30 = ImageDissolve("wipes/30.png", 1.0, 8)
    $ w31 = ImageDissolve("wipes/31.png", 1.0, 8)
    $ w32 = ImageDissolve("wipes/32.png", 1.0, 8)
    $ w33 = ImageDissolve("wipes/33.png", 1.0, 8)




#######################################################################

image i_elf smile1=At('elf_smile1',sprite_highlight('elf'))
image i_elf smile2=At('elf_smile2',sprite_highlight('elf'))
image i_tutor 1=At('tutor_1',sprite_highlight('tutor'))
image i_tutor 2=At('tutor_2',sprite_highlight('tutor'))
image i_professor 1=At('professor_1',sprite_highlight('professor'))
image i_elf sweat=At('elf_sweat',sprite_highlight('elf'))
image i_elf sweat2=At('elf_sweat2',sprite_highlight('elf'))
image i_elf scary=At('elf_scary',sprite_highlight('elf'))
image i_elf scary2=At('elf_scary2',sprite_highlight('elf'))
image i_hero normal=At('hero_normal',sprite_highlight('hero'))
image i_protagonist normal=At('protagonist_normal',sprite_highlight('protagonist'))
image i_psychologist normal=At('psychologist_normal',sprite_highlight('psychologist'))
image i_daughter cry=At('daughter_cry',sprite_highlight('daughter'))
image i_daughter cry2=At('daughter_cry2',sprite_highlight('daughter'))
image i_boy normal=At('boy_normal',sprite_highlight('boy'))
image i_hand normal=At('hand_normal',sprite_highlight('hand'))
image i_Ai normal=At('ai_normal',sprite_highlight('ai'))
image i_savebi normal=At('savebi_normal',sprite_highlight('savebi'))
image i_thao normal=At('thao_normal',sprite_highlight('thao'))
image i_truong normal=At('truong_normal',sprite_highlight('truong'))
image i_caosong normal=At('caosong_normal',sprite_highlight('caosong'))
image i_thao laugh=At('thao_laugh',sprite_highlight('thao'))
image i_thao laugh2=At('thao_laugh2',sprite_highlight('thao'))
image i_thao anger=At('thao_anger',sprite_highlight('thao'))
image i_savebi smile=At('savebi_smile',sprite_highlight('savebi'))
image i_thao_o smile1=At('thao_o_smile1',sprite_highlight('thao'))
image i_thao_o shock=At('thao_o_shock',sprite_highlight('thao'))
image i_fourhorsey smile1=At('fourhorsey_smile1',sprite_highlight('fourhorsey'))
image i_lao smile1=At('lao_smile1',sprite_highlight('lao'))
image i_quantity normal=At('quantity_normal',sprite_highlight('quantity'))
image i_lisan normal=At('lisan_normal',sprite_highlight('lisan'))
image i_lisan patch=At('lisan_patch',sprite_highlight('lisan'))
image i_gaib normal=At('gaib_normal',sprite_highlight('gaib'))

image i_savebi hand=At('savebi_hand',sprite_highlight('savebi'))
image i_savebi idol=At('savebi_idol',sprite_highlight('savebi'))
image i_sandquantity normal=At('sandquantity_normal',sprite_highlight('sandquantity'))
image i_millioncloud normal=At('millioncloud_normal',sprite_highlight('millioncloud'))
image i_millioncloud normal2=At('millioncloud_normal2',sprite_highlight('millioncloud'))
image i_millioncloud shock=At('millioncloud_shock',sprite_highlight('millioncloud'))
image i_smartest normal=At('smartest_normal',sprite_highlight('smartest'))
image i_smartest normal85=At('smartest_normal85',sprite_highlight('smartest'))
image i_thao call=At('thao_call',sprite_highlight('thao'))
image i_sixtone b tired=At('sixtone_b_tired',sprite_highlight('sixtone'))
image i_robot1=At('robot1')
image i_saintone closed=At('saintone_closed')
image i_fourhorsey smile2=At('fourhorsey_smile2',sprite_highlight('fourhorsey'))
image i_fourhorsey smile3=At('fourhorsey_smile3',sprite_highlight('fourhorsey'))
image i_fourhorsey smile4=At('fourhorsey_smile4',sprite_highlight('fourhorsey'))
image i_fourhorsey smile5=At('fourhorsey_smile5',sprite_highlight('fourhorsey'))
image i_fourhorsey smile6=At('fourhorsey_smile6',sprite_highlight('fourhorsey'))
image i_fourhorsey smile7=At('fourhorsey_smile7',sprite_highlight('fourhorsey'))
image i_meolon normal=At('meolon_normal',sprite_highlight('meolon'))
image i_meolon normal2=At('meolon_normal2',sprite_highlight('meolon'))
image i_tonebook normal1=At('tonebook_normal1',sprite_highlight('tonebook'))
image i_tonebook j normal1=At('tonebook_j_normal1',sprite_highlight('tonebook'))
image i_tonebook normal2=At('tonebook_normal2',sprite_highlight('tonebook'))
image i_tonebook doubt1=At('tonebook_doubt1',sprite_highlight('tonebook'))
image i_savebi cry1=At('savebi_cry1',sprite_highlight('savebi'))
image i_savebi cry2=At('savebi_cry2',sprite_highlight('savebi'))
image i_savebi lonely1=At('savebi_lonely1',sprite_highlight('savebi'))
image i_savebi2 normal=At('savebi2_normal',sprite_highlight('savebi2'))
image i_gaib normal=At('gaib_normal',sprite_highlight('gaib'))
image i_lao smile2=At('lao_smile2',sprite_highlight('lao'))
image i_saintone normal1=At('saintone_normal1',sprite_highlight('saintone'))

define savebi= Character(None)
define character_elf=Character('Althaea-The Sorceress',image='i_elf',callback=name_callback,cb_name='elf', color="#563be0")
define character_hero=Character('Hero',image='i_hero',callback=name_callback,cb_name='hero', color="#fa0f1f")
define character_protagonist=Character('The Protagonist',image='i_protagonist',callback=name_callback,cb_name='protagonist', color="#6b1b68")
define character_boss=Character('Boss',image='i_boss',callback=name_callback,cb_name='boss', color="#80262c")
define character_tutor=Character('Tutor',image='i_tutor',callback=name_callback,cb_name='tutor', color="#db9ea2")
define character_professor=Character('Professor',image='i_professor',callback=name_callback,cb_name='professor', color="#1e7824")
define character_robot=Character('Robot',image='i_robot',callback=name_callback,cb_name='robot', color="#515907")
define character_unknown=Character('Unknown',image='i_unknown',callback=name_callback,cb_name='unknown', color="#4f5237")
define character_ai=Character('Ai',image='i_ai',callback=name_callback,cb_name='ai', color="#6b1b68")
define character_kaelen=Character('Kaelen',image='i_kaelen',callback=name_callback,cb_name='kaelen', color="#20591a")
define character_silas=Character('Silas',image='i_silas',callback=name_callback,cb_name='silas', color="#6e806c")
define character_savebi=Character('Savebi',image='i_savebi',callback=name_callback,cb_name='savebi', color="#0b30e6")
define character_savebi2=Character('Savebi2',image='i_savebi2',callback=name_callback,cb_name='savebi2', color="#0b30e6")
define character_thao=Character('Tao Thao',image='i_thao',callback=name_callback,cb_name='thao', color="#cc0a0a")

define character_mother=Character('The Mother',image='i_mother',callback=name_callback,cb_name='mother', color="#6b1b68")
define character_daughter=Character('The Daughter',image='i_daughter',callback=name_callback,cb_name='daughter', color="#6b1b68")
define character_psychologist=Character('Psychologist',image='i_psychologist',callback=name_callback,cb_name='psychologist', color="#c716bb")
define character_boy=Character('Boy',image='i_boy',callback=name_callback,cb_name='boy', color="#169ec7")
define character_thao=Character('Thao',image='i_thao',callback=name_callback,cb_name='thao', color="#6b1b68")
define character_truong=Character('Truong',image='i_truong',callback=name_callback,cb_name='truong', color="#6b1b68")
define character_caosong=Character('Cao Song',image='i_caosong',callback=name_callback,cb_name='caosong', color="#6b1b68")
define character_doctor=Character('Doctor',image='i_doctor',callback=name_callback,cb_name='doctor', color="#6b1b68")
define character_priest=Character('Priest',image='i_priest',callback=name_callback,cb_name='priest', color="#6b1b68")
define character_fourhorsey=Character('FourHorseY',image='i_fourhorsey',callback=name_callback,cb_name='fourhorsey', color="#6b1b68")
define character_lao=Character('Tao Lao',image='i_lao',callback=name_callback,cb_name='lao', color="#6b1b68")

define character_lisan=Character('Lisan',image='i_lisan',callback=name_callback,cb_name='lisan', color="#6b1b68")

define character_gaib=Character('Gaib',image='i_gaib',callback=name_callback,cb_name='gaib', color="#6b1b68")
define character_meolon=Character('Meolon',image='i_meolon',callback=name_callback,cb_name='meolon', color="#6b1b68")
define character_tonebook=Character('Tonebook',image='i_tonebook',callback=name_callback,cb_name='tonebook', color="#6b1b68")
define character_k724=Character('K724',image='i_k724',callback=name_callback,cb_name='k724', color="#6b1b68")
define character_security1=Character('Security1',image='i_security1',callback=name_callback,cb_name='security1', color="#6b1b68")
define character_security2=Character('Security2',image='i_security2',callback=name_callback,cb_name='security2', color="#6b1b68")
define character_security3=Character('Security3',image='i_security3',callback=name_callback,cb_name='security3', color="#6b1b68")
define character_security4=Character('Security4',image='i_security4',callback=name_callback,cb_name='security4', color="#6b1b68")
define character_sandquantity=Character('SandQuantity',image='i_sandquantity',callback=name_callback,cb_name='sandquantity', color="#6b1b68")
define character_millioncloud=Character('MillionCloud',image='i_millioncloud',callback=name_callback,cb_name='millioncloud', color="#6b1b68")
define character_god=Character('G.O.D',image='i_god',callback=name_callback,cb_name='god', color="#6b1b68")
define character_elke=Character('Elke',image='i_elke',callback=name_callback,cb_name='elke', color="#6b1b68")
define character_smartest=Character('The Smartest man alive',image='i_smartest',callback=name_callback,cb_name='smartest', color="#6b1b68")
define character_sixtone=Character('Sixtone',image='i_sixtone',callback=name_callback,cb_name='sixtone', color="#6b1b68")
define character_saintone=Character('Saintone',image='i_saintone',callback=name_callback,cb_name='saintone', color="#6b1b68")
define character_youtube=Character('Youtube',image='i_youtube',callback=name_callback,cb_name='youtube', color="#6b1b68")

define character_sain_tone_emvipy=Character('Sain Tone Emvipy',image='i_sain_tone_emvipy',callback=name_callback,cb_name='sain_tone_emvipy', color="#6b1b68")
image i_meolon cute=At('meolon_cute',sprite_highlight('meolon'))

label start:
#########
################
#########
################
#########
################
#########
################ CHAPTER 1
#########
################
#########
################
#########
################
play music "Sacred Light - Choir Music Royalty Free.mp3" fadein 2.0 volume 0.5
"How to play: \n Press \"Esc\" to open settings. \n Tap \"On the screen\" to control, continue the story."
"This is a work of fiction. Names, characters, places and incidents either are products of the author's imagination or are used fictitiously. Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental."
"Please use a headphone for better experience."
label start_common:
"{b}CHAPTER 1: RECIPROCAL_ALTRUISM.zip{/b}"

scene bg ceiling with dissolve
character_savebi "(My eyes opened. White ceiling. No emotion. Just awareness.)"
character_savebi "Where am I?"


character_savebi "(I tried moving my right hand. It lifted smoothly, precisely. But it didn't feel like mine. Like operating a tool.)"
scene bg ceiling2 with dissolve
"Dr. Elke entered."
scene bg ceiling1 with dissolve
play sound "audio/c1/Neutral 133.mp3" volume 1
character_elke "System stable. You're awake. Can you tell me your name?"
menu:
    "Tell her your name":
        jump choices_1_a
    "Not tell her your name":
        jump choices_1_b
label choices_1_a:
    character_savebi "It's Savebi."
    jump choices1_common
label choices_1_b:
    character_elke "It will probably take some time for you to regain your memory. Your name is Savebi."
    jump choices1_common
label choices1_common:

play sound "audio/c1/Neutral 131.mp3" volume 1
character_elke "Do you remember what happened?"
scene bg ceiling3 with dissolve
character_savebi "An accident. Transport vehicle. The sound of metal tearing."

scene bg fouryears open eye
pause 0.01
scene bg ceiling3 with dissolve
character_savebi "(Then an image flashed. A girl with no arms or legs, floating in white light.)"

character_savebi "I just saw... a girl. No limbs."
scene bg ceiling1 with dissolve
play sound "audio/c1/Neutral 129.mp3" volume 1
character_elke "That could be a side effect of the neural adjustment chip we implanted." 
play sound "audio/c1/Neutral 130.mp3" volume 1
character_elke " Sometimes it creates strange imagery."
scene bg ceiling2 with dissolve
play sound "audio/c1/Neutral 134.mp3" volume 1
character_elke "You need to know this." 
play sound "audio/c1/Neutral 140.mp3" volume 1
character_elke " The event you remember happened {b}forty-three years ago{/b}."
play sound "audio/c1/Neutral 135.mp3" volume 1
character_savebi "(Forty-three years. I felt nothing. No shock. No sadness.)"
scene bg ceiling3 with dissolve
play sound "audio/c1/Neutral 136.mp3" volume 1
character_elke "Your biological body was severely damaged. We preserved your brain. The rest is prosthetic."

character_savebi "(I looked at my hand. Synthetic skin. Perfect. But not mine.)"
scene bg ceiling2 with dissolve
play sound "audio/c1/Neutral 142.mp3" volume 1
character_elke "How do you feel?"
character_savebi "(I listened inside myself. Nothing. Empty.)"
scene bg ceiling3 with dissolve
character_savebi "I feel... normal. Everything works."
scene bg ceiling1 with dissolve
play sound "audio/c1/Neutral 144.mp3" volume 1
character_elke "There's a reason you were saved. Your father - Commander Aris Savebi. "
play sound "audio/c1/Neutral 146.mp3" volume 1
character_elke "He left his entire fortune, forty billion credits, with one condition: use that money to revive you."
play sound "audio/c1/Neutral 147.mp3" volume 1
character_elke "He passed away a year ago."
character_savebi "(Forty billion. An enormous number.)"
scene bg ceiling3 with dissolve
character_savebi "And my mother?"
scene bg ceiling1 with dissolve
play sound "audio/c1/Neutral 148.mp3" volume 1
character_elke "She passed seventeen years ago. We preserved her brain in the Neural Archive. Waiting for the day she can be revived."
play sound "audio/c1/Neutral 149.mp3" volume 1
character_elke "You weren't just saved, Savebi." 
play sound "audio/c1/Neutral 150.mp3" volume 1
character_elke "You were bought with your father's love."

scene bg ceiling3 with dissolve
character_savebi "I understand now."
scene bg ceiling with dissolve
character_savebi "(I'm awake. I'm alive. I'm a {b}forty-billion-credit purchase{/b}.)"
character_savebi "(And inside, I feel {b}nothing at all{/b}.)"

show hand_normal with dissolve
show hand_normal2 with dissolve
hide hand_normal
hide hand_normal2 with dissolve
show hand_normal3 with dissolve
character_savebi "....."
#########
################
#########
################
#########
################
#########
################ CHAPTER 2: đến thăm mẹ
#########
################
#########
################
#########
################
play music "office ambience Sound Effect.mp3" fadein 2.0 volume 0.7
scene black with dissolve
"{b}CHAPTER 2: THE_ARCHIVE_OF_FLESH_AND_SILICON.dat{/b}"

scene bg hospital1 with dissolve

character_savebi "(A month passed. I returned to Neo-Genesis Biotech for my monthly calibration.)"

character_savebi "(The lab was colder than I remembered. Tonebook was waiting.)"
character_savebi "I'm here for calibration. And to see the archive."
show i_tonebook normal2 with dissolve
play sound "audio/c2/Insight 245.mp3" volume 1
character_tonebook "On time. I'll handle the calibration today."
character_savebi "(Tonebook looked at me with the eyes of someone who sees consciousness as electrical signals.)"
scene black with dissolve
pause 0.01
scene bg hospital1 with dissolve
play sound "audio/c2/Insight 174.mp3" volume 1
character_tonebook "Neural pathways clear. everything done. No problem."

play music "sad piano1.mp3" fadein 2.0 volume 0.7
character_savebi "The archive. My mother. I want to see her."
show i_tonebook doubt1 with dissolve
play sound "audio/c2/Insight 175.mp3" volume 1
character_tonebook "That's a separate area. Not for visiting."

character_savebi "My access was purchased. Like everything else."

character_savebi "(Tonebook was silent, then nodded. She led me deeper.)"

scene bg lab3 with dissolve
character_savebi "(The corridors grew darker. Security doors closed like tombs. The air changed. Colder. Drier. The cold of permanent preservation.)"
play sound "audio/c2/Insight 179.mp3" volume 1
character_tonebook "I'll wait here."


character_savebi "(The vault was vast, dark, silent.)"

character_savebi "(The guidance system led me to cabinet S-042.)"
character_savebi "(As I approached, lights brightened.)"
scene bg mother_brain with dissolve
character_savebi "(And there, in the dim green light, was my mother.)"

character_savebi "(My mother's brain. Silver nanofilaments cocooned it.)"
character_savebi "(Three pounds of fatty tissue and electricity that once held her laughter. Her warm hand on my forehead. Her worried voice. The scent of her hair.)"

character_savebi "(I didn't move. My artificial heart beat steadily.)"
character_savebi "(But inside, in the organic part of my brain that remained, something happened.)"
show i_savebi cry2 with dissolve
character_savebi "(Input: Confirmation of mother's preserved consciousness unit.)"

character_savebi "(My body didn't ache. But the error did. An empty gravitational pull in my chest. Like a silent scream of corrupted data.)"

character_savebi "(No words were spoken.)"

character_savebi "(I saw the display screen beside the cabinet. Details about my mother. And one line:)"

"STATUS: PERMANENT PRESERVATION"
"REVIVAL PROCEDURE: FEASIBLE"
"ESTIMATED COST: 40,000,000,000 CREDITS"
play sound "audio/c2/Insight 180.mp3" volume 1
character_tonebook "That's for a complete somatic body and neural transfer procedure. Like what they did for you."

character_savebi "{b}Forty billion...{/b}"
hide i_savebi cry2 with dissolve
show i_tonebook normal2 with dissolve
play sound "audio/c2/Insight 181.mp3" volume 1
character_tonebook "If you want to revive her, you'll have to earn that money yourself."

character_savebi "(But I didn't need to think.)"
character_savebi "{b}I'll earn it.{/b}"


character_savebi "(Tonebook looked at me a moment longer, then sighed.)"

character_savebi "(I turned away for one last look at my mother. The lights dimmed, returning her to silent blue dreams.)"

character_savebi "(Outside the vault door, Tonebook added:)"
play sound "audio/c2/Insight 184.mp3" volume 1
character_tonebook "If you're serious... come back to see me. I can show you a few ways to start."
hide i_tonebook
character_savebi "(I nodded, saying nothing more.)"
show i_savebi cry1 with dissolve
character_savebi "{b}Forty billion credits. An impossible number.{/b}"
character_savebi "But now I knew my mother's price. And I knew what I had to do."

#########
################
#########
################
#########
################
#########
################ chapter 3: suy nghĩ của Save bi #1
#########
################
#########
################
#########
################
scene bg room dark with dissolve
"{b}CHAPTER 3: Loneliness.mp3{/b}"
show i_savebi lonely1 with dissolve
character_savebi "(One night, I sat alone in my dark apartment. The city's neon glow leaked through the window, painting the walls with colors that felt unfamiliar, artificial.)"

character_savebi "(My systems reported stability. Silence. Order.)"

character_savebi "(But beneath the flawless diagnostics, something felt wrong.)"

character_savebi "Why does it still feel so empty?"
character_savebi "I survived. I was rebuilt. So why do I feel... misplaced?"

character_savebi "(The world continued to move outside - people, androids, cyborgs - all connected, all functioning. Yet I felt like a process running without a network.)"

character_savebi "(I was no longer human. Not entirely machine.)"

character_savebi "(And for the first time since my rebirth, I understood a simple truth: survival was not the same as belonging.)"

character_savebi "{b}Forty billion credits.{/b}"

character_savebi "(The number repeated in my head like a heartbeat. Not an emotion, but a problem to solve.)"

character_savebi "I calculated. With a normal job-technician, data analyst, even security-how long would it take?"

character_savebi "My systems ran the numbers. Even with the highest salary... hundreds of years. Maybe a thousand."

character_savebi "Not feasible."

character_savebi "This city lived at night. Neon lights, music, entertainment. People escaped reality in electronic dreams and performances."

character_savebi "Then I saw it."

character_savebi "An advertisement projected on my computer screen."
scene bg idol ad with dissolve
"AURORA ENTERTAINMENT AUDITIONING NEW GENERATION IDOLS"
"Earnings: 500,000 - 5,000,000 credits per show"
"No experience required"
"Auditions every Friday"
scene bg room dark with dissolve
character_savebi "{b}Five hundred thousand. Even five million. For one show.{/b}"

character_savebi "I paused. My system analyzed the information."

character_savebi "(Idol. Singing. Dancing. Entertainment.)"

character_savebi "(Then a memory surfaced. Faint, but clear.)"

character_savebi "A long time ago. Before the accident. I used to sing."

character_savebi "(I looked down at my hands. Synthetic skin. Perfect. This body could execute any dance move. Any high note.)"

character_savebi "(And I didn't get tired. Didn't need rest. Could perform all night.)"

character_savebi "One show: 500,000 credits."
character_savebi "Forty billion credits needed: 80,000 shows."

character_savebi "One show a day: 80,000 days. Over 219 years."

character_savebi "Too long. But if five million per show..."

character_savebi "Only 8,000 shows. 22 years."

character_savebi "{b}Possible. Feasible.{/b}"

"IDOL AUDITION - NEXT FRIDAY - AURORA AUDITORIUM"

character_savebi "(I registered. Used the name 'Saya'. Not Savebi.)"

character_savebi "(That wasn't the real me. Just a role. A tool to earn money.)"

character_savebi "(As I submitted the form, a notification appeared:)"

"PLEASE PREPARE A SHORT SONG"

character_savebi "(I closed the interface. Sat down on the bed.)"

character_savebi "Forty billion. One show a day. Twenty-two years."

character_savebi "I could do it. This body wouldn't age. This voice wouldn't grow hoarse."

character_savebi "Just... continue. Day after day."

character_savebi "(I closed my eyes. Tried to remember the melody Mother taught me.)"

character_savebi "(And for the first time since waking up, I felt... something.)"

character_savebi "(Not hope. Not joy.)"

character_savebi "(But {b}purpose{/b}.)"

character_savebi "(Tomorrow, I would become Saya. The idol.)"
character_savebi "And I would sing. Until I had enough money to bring Mother back."

##
#########
################
#########
################
#########
################
#########
################ INTERLUDE I:Kaelen và Smartest
#########
################
#########
################
#########
################
"{b}INTERLUDE I: THE OBSERVERS{/b}"

scene bg dark gray with dissolve

play music "low_ambient_static.mp3" fadein 1.5 volume 0.4

show i_smartest normal with dissolve
"Their attention was fixed on the same floating text."

"Biography and Life of the Cyborg Savebi"
"- by Linhx the Watcher"
scene bg kaelen2 with dissolve
play sound "audio/i1/Vision 189.mp3" volume 0.6
character_kaelen "(Reading aloud, precise, neutral.) Subject exhibits no emotional response upon learning her own commodification. "
play sound "audio/i1/Vision 190.mp3" volume 0.6
character_kaelen "However, the discovery of her mother's stored consciousness initiates a clear objective fixation: capital accumulation for revival."
play sound "audio/i1/Vision 191.mp3" volume 1
character_kaelen "This is the core data point. Her suffering does not originate from pain, loss, or fear. "
play sound "audio/i1/Vision 193.mp3" volume 1
character_kaelen "It originates from {b}purpose compression{/b}. Her entire existence collapses into a single measurable goal."
play sound "audio/i1/Anchor 195.mp3" volume 1
character_smartest "(Eyes still on the text.) You're describing the symptom, not the wound."

play sound "audio/i1/Anchor 197.mp3" volume 1
character_smartest "(Scrolls.) Here. Linhx notes that Savebi does not grieve in any conventional sense. No despair, no breakdown. Instead, she converts loss into a task."
play sound "audio/i1/Anchor 199.mp3" volume 1
character_smartest "That tells us something important: meaning has been externalized. She doesn't ask, 'Why did this happen?' She asks, '{b}What must be done?{/b}'"
play sound "audio/i1/Vision 198.mp3" volume 1
character_kaelen "And that is efficient. Modern societies reward functional meaning. Clear objectives reduce existential noise."
play sound "audio/i1/Anchor 202.mp3" volume 1
character_smartest "They also erase the self."
play sound "audio/i1/Vision 201.mp3" volume 1
character_kaelen "Disagree. The self is irrelevant here. The source of human suffering, as demonstrated, is misalignment between desire and feasibility. "
play sound "audio/i1/Vision 203.mp3" volume 1
character_kaelen "Savebi desires revival. The cost is extreme. The gap generates strain."
play sound "audio/i1/Anchor 205.mp3" volume 1
character_smartest "You're still treating suffering as an engineering problem."

play sound "audio/i1/Vision 209.mp3" volume 1
character_kaelen "(Pauses.) That is an interpretive statement, not a measurable one."
play sound "audio/i1/Anchor 208.mp3" volume 1
character_smartest "Yet it's observable. Look at her decision to become an idol."
play sound "audio/i1/Anchor 210.mp3" volume 1
character_smartest " She abandons identity, name, history-everything-because the system only recognizes output."
play sound "audio/i1/Anchor 211.mp3" volume 1
character_smartest "Humans-and post-humans-can endure almost anything if they believe it leads somewhere. But when the path consumes the person walking it, the destination becomes irrelevant."
play sound "audio/i1/Vision 213.mp3" volume 1
character_kaelen "You are suggesting her suffering will intensify {b}after{/b} success?"
play sound "audio/i1/Anchor 214.mp3" volume 1
character_smartest "Savebi's story exposes something uncomfortable: when a society turns meaning into currency, suffering doesn't disappear-it becomes invisible."
play sound "audio/i1/Vision 215.mp3" volume 1
character_kaelen "Conclusion: Subject Savebi represents an unresolved variable. Her suffering is not emotional instability, but systemic over-optimization."
scene bg black with dissolve

#########
################
#########
################
#########
################
#########
################ CHAPTER 4:
#########
################
#########
################
#########
################
scene black with dissolve
"{b}CHAPTER 4: THE ALCHEMY OF ONE MILLION SMILE.mp3{/b}"
play music "kawaii idol.mp3" fadein 2.0 volume 0.7
character_savebi "(Night fell over New-GonSai District 8 like a slow electrical short-first a flicker, then a permanent, buzzing darkness punctuated by the false suns of corporate logos.)" 
"(A neon necropolis where dreams were cheaper than filtered air, yet somehow more expensive to maintain.)"

character_savebi "(My monthly calibration had concluded hours ago. The silence that followed was not empty. It was a vacuum, and in that vacuum, the only equation that mattered began its relentless calculation once more.)"

scene bg city_night with fade

character_savebi "(The transit pod deposited me at the service entrance of the 'Elysium Lounge,' a venue that promised temporary transcendence through light and sound. My internal chronometer synced with the show schedule. In 47 minutes, I would be on stage. The routine was no longer unfamiliar. It was a protocol.)"

scene bg stage1 with dissolve

character_savebi "(The self-announcement was a ritual. A way to delineate the act from the actor. The performer from the monument.)"

scene bg stage2 with dissolve
character_savebi "(I stepped onto the stage. The transition was instantaneous. From the shadowed wings to a blistering nova of holographic light. To the crowd-a sea of upturned faces glowing with the reflection of their own devices-I was not Savebi.)"
character_savebi "(I was '{b}Saya{/b},' the synthetic siren. A marvel of bio-engineering, singing love songs written by algorithms for hearts too tired to feel.)"

scene bg stage with dissolve
play sound "crowd_cheer_small.mp3"

show i_savebi idol with dissolve
character_savebi "{b}Good evening, Elysium.{/b}"

character_savebi "(My voice, modulated to a perfect, crystalline warmth, washed over them. A thousand points of light tracked my every move. I danced. My body executed pre-visualized sequences with a precision no organic being could match-each extension perfect, each turn exact.)"

stop music fadeout 1.0

character_savebi "(The performance lasted exactly 27 minutes and 13 seconds. The setlist was designed for maximum emotional manipulation and energetic payoff. I was a machine playing a machine playing a human. The crowd roared.)"
play music "sad piano1.mp3" fadein 2.0 volume 0.7
character_savebi "(Their adoration was a wave of raw data I could sense-acoustic volume, density of light from raised terminals, pheromone spikes parsed by my borrowed Companion-core into a chittering symphony of '{b}joy-excitement-approval.{/b}')"

character_savebi "(I bowed. The lights died. The transition back to silence was as abrupt as a power cut.)"

scene bg idol_backstage with fade



"{b}Transaction confirmed. Net credit acquisition: one million.{/b}"

"{b}$ credits = 1,000,000{/b}"
show savebi_idol1 with dissolve
character_savebi "(I accessed the primary ledger. The numbers glowed in my mind, immutable and cruel.)"

"$ total_cost = 40,000,000,000"
"$ earned_to_date = 11,000,000 "
"$ remaining = total_cost - earned_to_date"
"$ shows_needed = remaining / credits"

character_savebi "{b}Total required: forty billion. Acquired: eleven million. Deficit: thirty-nine billion, nine hundred eighty-nine million.{/b}"

character_savebi "{b}Required performances at current rate: thirty-nine thousand, nine hundred eighty-nine.{/b}"

character_savebi "(Thirty-nine thousand, nine hundred eighty-nine.)"

character_savebi "(The number was not an abstraction. It was a prison sentence. A timeline.)"

character_savebi "At one performance per solar cycle... temporal projection: one hundred thirty-six point nine years."

character_savebi "(A century. And then another thirty-seven years. My body would not fail. My voice would not fray. But the consciousness that had to enact this pantomime, night after night, for the equivalent of a human lifetime and a half... that was the true test.)"

character_savebi "(My emotion dampeners held. There was no scream, no tears. Only a cold, systems-level assessment of an impossible task.)"
character_savebi "(And yet, within the ancient 8 percent of me that was still organic tissue, a phantom sensation arose-the ghost of despair, translated by my machine self as a critical resource shortfall with no logistical solution.)"


character_savebi "One million. One night. One hundred thirty-six point nine years."

character_savebi "(I looked at my reflection. The face was flawless, a masterpiece of synthetic artistry. It was the face of a forty-billion-credit resurrection. It was the face of a daughter who now needed to earn that same impossible sum again.)"

scene bg city_night with dissolve
play sound "neon_hum.mp3"

character_savebi "(I stepped out into the alley, the city's neon glow painting me in streaks of false color. Somewhere beneath the metropolis, in a vault of silent green light, a brain that had once sung my lullabies waited. The cost of a lullaby: forty billion credits.)"

character_savebi "{b}I will perform, Mother. For as many nights as it takes. The monument will become a treasury.{/b}"

character_savebi "(The night offered no answer. It only hummed, indifferent, as I disappeared into its electric veins.)"


#########
################
#########
################
#########

scene bg city_night with dissolve
play music "ambient_electronica.mp3" fadein 3.0 volume 0.5

character_savebi "(Tôi đứng ở cửa sau của Elysium Lounge, tựa lưng vào bức tường ẩm mốc. Một triệu credits vừa được cộng vào tài khoản. Một đêm nữa trôi qua.)"

character_savebi "(Phía trên kia, bầu trời không có sao. Chỉ có những vệt sáng đỏ cam từ máy bay không người lái tuần tra, bay rất xa, rất cao. Năm thứ ba của cuộc chiến giữa Whole America và Liên minh Asia. Người ta nói ở biên giới phía Tây, robot giết nhau hàng ngàn con mỗi ngày. Người ta cũng chết. Nhưng tin tức không gọi tên họ.)"

character_savebi "(Tôi lướt xem vài dòng tin tức trên mạng xã hội nội bộ. Một video từ một thành phố bị san phẳng. Một bài đăng kêu gọi quyên góp cho trại tị nạn. Và ngay bên dưới, một em gái đăng ảnh selfie với filter hình thỏ, caption: 'Đi xem Saya tối nay, sống quá đã <3')"

character_savebi "(Tôi bật cười. Không phải vì vui. Mà vì cái cách con người sống sót qua chiến tranh: bằng cách **không nghĩ về nó**.)"

character_savebi "(Tối nay có 847 người trong khán phòng. Họ hét. Họ khóc. Họ nhảy theo tôi. Có một chị ở hàng ghế thứ ba, mắt đỏ hoe khi tôi hát bài về mẹ. Có một anh ở góc phải, im lặng suốt buổi, chỉ nhìn chăm chăm lên sân khấu như thể tôi là thứ duy nhất còn sáng trong đời anh.)"

character_savebi "(Tôi không biết họ là ai. Tôi không biết họ đã mất gì sau ba năm chiến tranh này. Nhưng tôi biết, trong 27 phút 13 giây, họ **không ở nơi chiến trường**.)"

character_savebi "(Họ ở đây. Với tôi. Với thứ ánh sáng màu hồng tím trên sân khấu. Với một bài hát dở hơi về tình yêu.)"

character_savebi "(Tôi nhìn lên con số trong đầu: 39.989 buổi diễn nữa. Một trăm ba mươi bảy năm.)"

character_savebi "(Một trăm ba mươi bảy năm đứng trên sân khấu, cười, hát, nhảy, cho những người cần quên.)"

character_savebi "(Nghe như địa ngục. Nhưng cũng nghe như... một sứ mệnh.)"

character_savebi "(Mẹ từng nói: 'Sống có ích không phải là cứu cả thế giới, con ạ. Là làm cho một người nào đó, một ngày nào đó, cảm thấy đỡ cô đơn hơn.')"

character_savebi "(Mẹ đang nằm dưới kia. Trong buồng phẫu thuật màu xanh lục. Mẹ không biết ngoài kia chiến tranh đã kéo dài ba năm. Mẹ không biết tôi đang làm gì để trả món nợ 40 tỷ. Nhưng mẹ từng nói câu đó.)"

character_savebi "(Tối nay, 847 người bước ra khỏi Elysium Lounge. Họ không cô đơn trong 27 phút.)"

character_savebi "(Tôi tựa đầu vào tường lạnh. Một giọt nước mắt—không, chưa phải nước mắt, chỉ là một tia ẩm ướt ở khóe mắt trái. Có thể là do điều hòa. Có thể là do tôi.)"

character_savebi "{b}Mẹ ơi, con không biết con đang làm điều đúng hay sai.{/b}"

character_savebi "{b}Con chỉ biết con không thể ngừng lại.{/b}"

character_savebi "(Một chiếc xe bay lướt qua trên cao, kéo theo dải ánh sáng xanh. Một vài người đi bộ về khuya, tay cầm ly cà phê, cười nói. Cuộc sống vẫn tiếp diễn. Chiến tranh ở rất xa. Hoặc rất gần, tùy cách nhìn.)"

character_savebi "(Tôi đẩy người ra khỏi tường. Bước chân đầu tiên vang lên trong hẻm vắng. Tiếng bước chân của một cô gái hai mươi tuổi, mặc váy biểu diễn lấp lánh, đi bộ về nhà lúc 2 giờ sáng.)"

character_savebi "(Một cô gái vừa kiếm được một triệu credits. Một cô gái vừa giúp 847 người quên đi chiến tranh.)"

character_savebi "(Một cô gái vẫn chưa biết mình là ai.)"

character_savebi "(Nhưng tối nay, ít nhất, cô ấy có ích.)"

character_savebi "(Tôi bước tiếp. Đường dài. Nhưng không cô đơn.)"


###

#########
################
#########
################
#########
################
#########
################ INTERLUDE II
#########
################
#########
################
#########
################
####

scene black with dissolve
"{b}INTERLUDE II: THE CALCULATION{/b}"

scene bg dark gray with dissolve
character_smartest "One hundred and nine {b}years.{/b}"

show i_smartest normal85 with dissolve
character_smartest "That is a long time."

scene bg kaelen2 with dissolve

character_kaelen "Based on her current earning rate. But that's a static calculation."

character_smartest "Meaning?"

character_kaelen "Everything changes. Prices. Inflation. Audience preferences. She could earn more. Or less."

"He opened the book again, flipping to a new page."

character_kaelen "According to historical data, the average idol career lasts 3-7 years. After that, they fade. The audience gets bored."

character_smartest "But she's not normal. She doesn't age. Her voice doesn't give out."

character_kaelen "True. But the audience will still get bored. They always seek something new. She'll have to... adapt."

character_smartest "Do you think she can do it?"

character_kaelen "Technically, yes. She can learn new dance moves, new styles, even completely change her image."

character_smartest "But that's not the real problem, is it?"

"Kaelen looked up from the book."

character_kaelen "The real problem is... whether she can endure it. 109 years of the same thing. Repeating. Day after day."

character_smartest "She has emotion dampeners."

character_kaelen "Not enough. Boredom is another form of torture. Even for a cyborg."

"He closed the book softly."

character_kaelen "{b}She'll find another way. Soon.{/b}"

character_smartest "What way?"

character_kaelen "A faster way to earn money. More dangerous. Or... she'll find help."

character_smartest "Who would help her?"

character_kaelen "Unknown. But in every story, the main character never goes alone to the end. There are always companions. Or enemies."

character_smartest "You read too many novels."

character_kaelen "I read patterns. And this pattern is clear: {b}she can't do this alone.{/b}"

"He stood up, placing the book on a table."

character_kaelen "{b}Next chapter.{/b} She'll meet someone. Or someone will meet her."

character_smartest "And we just sit here reading?"

character_kaelen "We observe. And wait for the story to write itself."


character_kaelen "One hundred and nine years is too long for a story. So something will happen. {b}Soon.{/b}"

########
########
########
# CHAPTER 5: Savebi nhìn thấy rất nhiều biển quảng cáo về công ty năng lượng của Thao, và cô tra Wikipedia thì biết Thao chính là người bạn năm xưa của mình, có vẻ như công ty của Thao là tập đoàn thống trị thành phố này nên Savebi đến công ty của Thao để xin việc, cô gửi mail đến công ty Thao, nói rằng là người quen cũ của Thao, ngày hôm sau được Thao gọi điện đến điện thoại Savebi để mời đến công ty, Savebi cảm thấy vô cùng hãnh diện và nhẹ nhõm.

#########
########
########
########
########
########


scene black with dissolve

"The dream comes again, heavy and distorted..."

scene bg room dark with dissolve

show i_savebi lonely1 with dissolve

character_savebi "This room again. That number again. I'm tired. Really tired..."
hide i_savebi lonely1
show i_savebi2 normal with dissolve

character_savebi2 "Tired? You’ve barely done anything!"
character_savebi2 "Singing a few songs, smiling a little, waving to a faceless crowd... you call that 'effort'?"

character_savebi "No... but it's all I can do. I'm an Idol. I have to follow the rules, the contracts..."

character_savebi2 "Rules? Contracts?"
character_savebi2 "Mom is frozen in a tube, and you're worried about 'contracts'? Pathetic."

character_savebi "I'm trying my best! Every day, every hour..."

character_savebi2 "'Trying your best' will never be enough!"
character_savebi2 "You need to {b}be different{/b}. Stronger. Ruthless. Find another way, no matter what!"
character_savebi2 "Or maybe..."
character_savebi2 "...deep down, you're afraid to face Mom after all this? Afraid you’ll see that disappointment in her eyes again?"

character_savebi "No! Don't say that! Stop!"

character_savebi2 "Stop? While you still choose the safe path? While you still pretend to be a pretty puppet?"
character_savebi2 "You don’t deserve to be saved. And you will never save anyone!"

character_savebi "NOOO!"

scene bg room light

"I jolt awake, gasping for air, my body drenched in cold sweat."

character_savebi "..."
character_savebi "I... have to change."
character_savebi "I have to find another way."
character_savebi "{b}I. Have. To. Find. Another. Way.{/b}"

#########
########
########
########
########
########

scene bg city_above with fade
"{b}CHAPTER 5: Power.py{/b}" 

play music "car.mp3" fadein 2.0 volume 0.5
"{i}After the show, the neon-drenched city breathes, flooding the streets with holographic ads and drifting projections. Savebi's processors slip into low-power mode, but her thoughts continue to churn.{/i}"

character_savebi "{i}Then I see it - again and again - scattering across the skyline like a repeating signal.{/i}"

scene bg billboard1 with dissolve

"{i}A glowing billboard, mirrored across skyscrapers:{/i}"

scene bg billboard2 with dissolve
"{b}THAO ENERGY.{/b}"

character_savebi "{b}Thao Energy...?{/b}"

"{i}The name stirs something in the fragments of her old memories, buried deep within her reconstructed mind.{/i}"

scene bg billboard3 with dissolve

"{i}She lifts her wrist-link. A gesture. A command. A massive holographic Wikipedia page materializes in the air.{/i}"

scene bg wiki_thao with dissolve

character_savebi "Founder: Tao Thao ..."

"{i}A photo appears: a confident smile, familiar eyes - the face of a girl who once leaned over her homework, laughing when she took everything too seriously.{/i}"

character_savebi "So... you built all this...?"

"{i}Thao Energy - the corporation powering half the city. A titan of industry. And Savebi... an idol scraping for credits to chase a dream that feels increasingly unreachable.{/i}"

character_savebi "I need... a real job."

"{i}A strange feeling rises inside her actuators - not fear, but anticipation. Hope.{/i}"

#########
########
########
########
########
########
############\
############ chapter 6: SEND EMAIL TO THAO
#########
########
########
########
########
########
############\
scene bg room dark with fade
play music "sad piano1.mp3" fadein 2.0 volume 0.7
"{b}chapter 6: Email{/b}"
play sound "keyboard_soft.mp3"
character_savebi"{i}Back in my dim apartment, I sit before the glow of the city. I compose a message to Thao Energy's corporate inbox.{/i}"
character_savebi "'Hello, Thao. It's me... Savebi. I don't know if you remember...'"
character_savebi"{i}I write. Delete. Rewrite.{/i}"
character_savebi "'I'm looking for work. And... I'd like to see you again.'"
play sound "email_send.mp3"
character_savebi "{b}Sent.{/b}"
character_savebi"{i}A simple message cast into a corporate ocean. Maybe it won't reach her. Maybe it won't matter.{/i}"
character_savebi"{i}Yet tonight, a faint warmth flickers inside my synthetic chest cavity - something like hope returning from extinction.{/i}"
# THE NEXT DAY - THE CALL
scene bg room light with dissolve
play music "Mystery & Crime Background Music For Films and Videos (Free Download)  Oak Hill.mp3" fadein 1.5 volume 0.6

"{i}Morning comes with the soft hum of my charging cable detaching. Another day. Another show. Another million.{/i}"

play sound "phone_ring.mp3"

character_savebi "...?"
"{i}A HUD alert flashes:{/i}"
"{b}INCOMING CALL: UNKNOWN NUMBER - CORPORATE ENCRYPTION ACTIVE{/b}"

character_savebi "Hello...?"

show i_thao call with dissolve
play sound "audio/c6/Precision 222.mp3" volume 1
character_thao "Savebi?"

"{i}My processor freeze for 0.2 seconds - nearly an eternity for me.{/i}"

character_savebi "Thao...? You... received my email?"
play sound "audio/c6/Precision 226.mp3" volume 1
character_thao "Of course. Listen-can you come to my company today? I want to see you."

"{i}Her voice flows warm and familiar, wrapping around me like a forgotten memory finding its way home.{/i}"

character_savebi "I... Yes. Yes, I'll come."
play sound "audio/c6/Precision 228.mp3" volume 1
character_thao "Good. I'll have security waiting. I can't wait to meet you again."

play sound "call_end.mp3"

"{i}The call ends, but the feeling stays. Weightless. Bright. Real.{/i}"

character_savebi "Thao... you remembered me."

"{i}For the first time since awakening in her new body, Savebi moves with something that resembles humanity - light steps, softer thoughts, and a fragile spark of hope for what tomorrow might bring.{/i}"

#########
########
########
########
########
########
############\
############ chapter 7 MEET THAO AND 2 VICE PRESIDENT
#########
########
########
########
########
########
############\
"{b}Chapter 7: hellofriend.mov{/b}"
play music "office.mp3" fadein 2.0 volume 0.5
scene bg company lobby with dissolve
"Thao said that when I arrived at the company headquarters, I should wait in the lobby for 15 minutes, and she would meet me in person there. "
show i_savebi smile
character_savebi "Tao Thao!"
hide i_savebi smile
show i_thao_o smile1
play sound "audio/c7/Precision 232.mp3" volume 1
character_thao "It's really you, Savebi!"
"We come together, embrace. For Thao, this is a reunion after over 40 years. For me, this warmth is both familiar and strange, like a vivid memory flooding back."
play sound "audio/c7/Precision 233.mp3" volume 1
character_thao "I'm glad. I am so glad..."
"We stare at one another a long moment, astonishment clear in Thao's eyes-now lined with wrinkles-as she takes in my youthful, cybernetic form, unchanged from our youth."
character_savebi "Look at you! A beautiful older woman."
play sound "audio/c7/Precision 235.mp3" volume 1
character_thao "Strange, when we were girls I was taller. Remember?"
character_savebi "Yes, I remember."
character_thao "After everything that happened... after the accident, after the War... I thought I'd lost you for good. ARO reported that your Revival Project had failed. But here you are... it's really you."
character_savebi "I don't fully understand it all either. I just knew I had to wake up. I have to find Mom. Professor Orion said I need 40 billion credits to wake her up. Thao, can you help me get the money? I tried being an Idol, but it wasn't enough..."
show i_thao_o shock
play sound "audio/c7/Precision 242.mp3" volume 1
character_thao "40 billion... It's a {b}fortune{/b}. "
show i_thao_o smile1
play sound "audio/c7/Precision 239.mp3" volume 1
character_thao "But not an impossible one. Not for someone with your... unique abilities."
play sound "audio/c7/Precision 241.mp3" volume 1
character_thao "More than that, my dear. Your cognitive architecture, your data processing speed... it's revolutionary. My corporation has facilities, vast server farms that need... optimization."
play sound "audio/c7/Precision 243.mp3" volume 1
character_thao "With your help, we could increase efficiency tenfold. The profits would be more than enough to fund your mother's revival."
character_savebi "(Eyes wide with naive hope) Really? You mean it? I can help! I'm a fast learner! I'll work so {b}hard!{/b}"
play sound "audio/c7/Precision 244.mp3" volume 1
character_thao "(Patting my metallic hand) I know you will. It's a promise. I'll help you save your mother, and you'll help save my company. We'll help each other, just like old times."

#########
########
########
########
########
###2 Vice president

scene bg company lobby with dissolve

"When I about to leave the building. TaoLao and fourhorsey approached from the lobby. Though both wore immaculate business attire, the contrast between them was unmistakable."
show i_lao smile1 at right with dissolve
show i_fourhorsey smile1 at left with dissolve
"TaoLao moved with effortless composure. His appearance was that of a refined eighteen-year-old-youthful, immaculate, almost unreal. Yet beneath the flawless exterior was a cybernetic body housing a mind that had already lived twenty-seven years."

"Every gesture was economical. Every smile, calculated."
play sound "audio/c7/Wit 246.mp3" volume 1
character_lao "{b}Hello, Savebi!{/b}"
"He inclined his head slightly-warmth without familiarity."
play sound "audio/c7/Wit 247.mp3" volume 1
character_lao "I've been looking forward to this meeting."

"His suit was minimalist, tailored with surgical precision-luxury without ostentation. The kind of elegance that didn't need to announce its price."
"A faint smile curved his lips."
"Beside him stood fourhorsey."

"fourhorsey, a young woman with sharp, guarded eyes, remained half a step behind her brother. She offered a brief nod-polite, restrained, almost defensive."
show i_lao smile2 at right
hide i_fourhorsey smile1 at left
show i_fourhorsey smile4 at left

play sound "audio/c7/Candid 265.mp3" volume 1
character_fourhorsey "Hello..."
"Her voice was quiet. Professional. She avoided direct eye contact."

"{i}Savebi's internal network ran a background search.{/i}"
"{i}Public records: TaoLao-Vice President of Corporate Strategy. Cyborg classification. Neural age: twenty-seven.{/i}"
"{i}fourhorsey-no public biography found.{/i}"
show i_lao smile1 at right
play sound "audio/c7/Wit 254.mp3" volume 1
character_lao "I am TaoLao. Vice President of Corporate Strategy. And this is my younger sister."

"FourHorseY's fingers tightened briefly. She said nothing."
play sound "audio/c7/Wit 255.mp3" volume 1
character_lao "As for you,..."
"He looked me over, not critically, but analytically."
play sound "audio/c7/Wit 256.mp3" volume 1
character_lao "Your transition from entertainment to corporate systems is... unconventional."
play sound "audio/c7/Wit 257.mp3" volume 1
character_lao "But this company values results, not origins."

play sound "audio/c7/Candid 267.mp3" volume 1
character_fourhorsey "The systems here are... complex."
"She spoke softly, finally meeting Savebi's gaze."
play sound "audio/c7/Candid 264.mp3" volume 1
character_fourhorsey "Your integration will require careful calibration."
play sound "audio/c7/Wit 259.mp3" volume 1
character_lao "{b}Which is exactly why we wanted you here. Adaptability like yours is rare.{/b}"
"A small, satisfied nod."

"He turned slightly, gesturing toward the inner elevators."
play sound "audio/c7/Wit 261.mp3" volume 1
character_lao "{b}Welcome to Thao Energy, Savebi. Not the future you imagined- But one that pays better dividends.{/b}"

"fourhorsey offered a brief, unreadable smile."

"The doors slid open silently, swallowing both of them in polished steel and reflected light."

#########
################
#########
################
#########
################
#########
################  suy nghĩ của Savebi (2)
#########
################
#########
################
#########
################
####
play music "car.mp3" fadein 2.0 volume 0.5
scene bg company lobby with dissolve
"The elevator doors closed with a soft sigh, sealing off the sterile corporate world."

scene bg city_street with fade

character_savebi "(TaoLao. Twenty-seven neural years in an eighteen-year-old chassis. Like me, but perfected. Market-ready.)"

character_savebi "(His sister-fourhorsey. No public record. Classified clearance. She watches but doesn't speak. She calculates but doesn't reveal.)"

character_savebi "(Why pair me with them? Thao could have assigned anyone. A standard handler. A junior executive.)"

character_savebi "(But she chose her top strategist and her invisible market operator.)"

character_savebi "(This isn't a job offer. It's an assessment.)"

character_savebi "(They want to see how I adapt. Not just to systems. To people. To hierarchies. To the unspoken rules that govern places like Thao Energy.)"

character_savebi "(TaoLao's polish. fourhorsey's silence. Both are weapons. Different kinds.)"

character_savebi "(I spent months as Saya, learning to mirror emotions I don't feel. To manufacture connection.)"

character_savebi "(This is the same game. Different stage.)"

character_savebi "(They will test my limits. How much data can I process? How quickly can I learn their protocols? How well can I hide what I am?)"

character_savebi "(And the sister... fourhorsey. She watched me the whole time. Not with curiosity. With recognition.)"

character_savebi "(She sees it. The emptiness behind the performance. The machine beneath the skin.)"

character_savebi "(Maybe that's why Thao put me with them. Not despite what I am. Because of it.)"

character_savebi "({b}Forty billion credits.{/b})"

character_savebi "(That number hasn't changed. But the path to it just became more... complex.)"

character_savebi "(Being an idol was simple. Smile. Sing. Collect payment.)"

character_savebi "(This is different. This is navigating people who see the world as equations. As leverage. As assets.)"

character_savebi "(I am an asset now. To be optimized.{b} To be deployed.{/b})"

character_savebi "(Fine.)"

character_savebi "(If this is how I earn the money faster, I'll learn their game. I'll become what they need me to be.)"

character_savebi "(But I won't forget why I'm here.)"

character_savebi "(Every calculation I run for them. Every system I optimize. Every market I help them penetrate.)"

character_savebi "(It's all for one number.)"

character_savebi "({b}40,000,000,000.{/b})"

character_savebi "(And for what waits in a silent green vault, dreaming of a daughter who is learning to become a weapon.)"

character_savebi "She reached her apartment building. The lobby was dim, quiet."

character_savebi "(Tomorrow, I become a corporate asset. Tonight, I am still a daughter with a debt to pay.)"

character_savebi "The elevator to her floor hummed softly. In the reflection of the doors, her face was calm. Empty."

character_savebi "(Adapt. Optimize. Survive. Earn.)"

character_savebi "(Until the debt is paid.)"

character_savebi "(Until she comes home.)"

###
##############
#########
################
#########
################
#########
################
#########
################ chapter 8: meet an old friend
#########
################
#########
################
#########
################
####
scene bg night park
"As I approached my apartment building, I saw a figure sitting on the stone bench."
"Under the streetlamp, it was an Android. The face was unfamiliar, yet something made my heart—though mechanical—flutter."
show i_sandquantity normal
play sound "audio/c8/Esteem 285.mp3" volume 1
character_sandquantity "Lone traveler, why dost thou still wander here?" 
"The voice was warm, the speech patterned with a medieval cadence."
character_savebi "Who are you...?"
"The Android bowed slightly"
play sound "audio/c8/Esteem 288.mp3" volume 1
character_sandquantity "I am SandQuantity, a humble professor of history, a student of the Scriptures."
play sound "audio/c8/Esteem 289.mp3" volume 1
character_sandquantity "In a time long past, ere we both were granted these new forms, I was the neighbor's son who lived beside thee."

character_savebi "I can't remember you."
"SandQuantity reached pulled out a small device that glowed with soft blue light."
play sound "audio/c8/Esteem 301.mp3" volume 1
character_sandquantity "Before I take my leave, I bring thee a small comfort." 
play sound "audio/c8/Esteem 298.mp3" volume 1
character_sandquantity "This world can be terribly lonely for ones like us."
"He handed me the device. It felt warm in my hand."
play sound "audio/c8/Esteem 299.mp3" volume 1
character_sandquantity "It contains a hologram AI - a cat named Meolon. It possesses intelligence and emotions akin to a human's, though such creations are now forbidden by law."
menu:
    "Take the AI":
        jump choices_2_a
    "Not take the AI":
        jump choices_2_b
label choices_2_a:
    character_savebi "I will take it."
    jump choices2_common
label choices_2_b:
    character_elke "I won't take it."
    character_sandquantity "Please just try to turn it on. It's will be very useful for you."
    jump choices2_common
label choices2_common:
"I examined the device. As I held it, a small holographic cat materialized in my palm, purring softly and rubbing against my fingers."
show i_meolon normal with dissolve
play sound "audio/c8/Cat 1.mp3" volume 1
character_meolon "Hello, Savebi. I've been waiting to meet you."
"The cat's voice was warm and surprisingly human-like, filled with genuine curiosity."

character_savebi "She's... incredible."
"A soft beep emitted from SandQuantity's chest. The light in his eyes flickered."
play sound "audio/c8/Esteem 304.mp3" volume 1
character_sandquantity "I beg thy pardon, my power wanes. I must return to the charging station."
"He bowed in a formal, old-world manner."
play sound "audio/c8/Cat 2.mp3" volume 1
character_meolon "Take care, Professor. I'll watch over her."
"The hologram cat curled up on my shoulder, its light casting a gentle glow on my face."

hide i_sandquantity with dissolve
"SandQuantity turned and walked away, his steps precise into the enveloping night. I stood, watching the retreating figure, my mind a turmoil between Thao's promise and this cryptic warning - and now, this unexpected gift."

scene bg room dark with dissolve
stop music fadeout 1.0
"The door to the tiny apartment clicked shut with a feeble sound, isolating me from the noisy, bustling world outside."


"As I slumped down onto the floor, my back against the icy wall, Meolon the hologram cat leaped from my shoulder and began exploring the sparse room."
show i_meolon cute
play sound "audio/c8/Cat 3.mp3" volume 1
character_meolon "This place could use some warmth. May I?"
"Before I could answer, Meolon projected soft, warm lighting throughout the room and began playing gentle, ambient music that seemed to calm the chaos in my central processing system."
show i_meolon normal
character_savebi "You can do that?"
play sound "audio/c8/Cat 1.mp3" volume 1
character_meolon "I'm full of surprises. And I'm programmed to learn your preferences and adapt to your emotional needs."
character_savebi "Mom..." 
"my perfectly simulated voice now emitted a weak tone."
character_savebi "I'm going to save you soon... Thao is going to help me."
play sound "audio/c8/Cat 2.mp3" volume 1
character_meolon "Thao... I sense hesitation in your voice when you speak that name. Would you like to talk about it?"
"But in that rare moment of stillness, a vague, hard-to-grasp feeling surfaced. Thao's gaze, her smile... it seemed there was something different from my memory. But the thought was instantly suppressed."

character_savebi "This is Thao, my childhood friend, the only one who could pull me back to this world. I have to trust her."
play sound "audio/c8/Cat 3.mp3" volume 1
character_meolon "Trust is precious. But so is caution. I'll be here to help you navigate either path."
"Meolon settled beside me, the hologram flickering gently like a real cat breathing in sleep. The neon light from outside the window shone into my eyes, unblinking, but now the darkness felt less absolute, the silence less profound."


###
##############
#########
################
#########
################
#########
################
#########
################ chapter 9: day 2
#########
################
#########
################
#########
################
####
"{b}CHAPTER 9: Real_world.flv{/b}"
play music "Mystery & Crime Background Music For Films and Videos (Free Download)  Oak Hill.mp3" fadein 1.5 volume 0.6
scene bg company lobby with dissolve
"The next morning, I returned to Thao's corporate headquarters."
scene bg corridor with dissolve
"The intimacy of the previous day was gone; a cold assistant led me through silent corridors, deeper into the building's core. We Finally stopped before a heavy metal door inscribed with the words -Λ Experiment Zone-."

"Thao was already there, the smile in her eyes still warm, yet strangely harmonized with the cold atmosphere."
show i_thao_o smile1 with dissolve
play sound "audio/c9/Precision 308.mp3" volume 1
character_thao "Good morning, Savebi. Sleep well?"
character_savebi "I... don't need that much sleep."
scene bg animus1 with dissolve
character_savebi "Is this...?"
play sound "audio/c9/Precision 306.mp3" volume 1
character_thao "Our most advanced Virtual Reality module. Your work here is simple: connect to it, navigate, and optimize a particular virtual world. Your data processing power and cognitive adaptability will be maximized here. The profits generated will be more than enough to wake your mother."
character_savebi "I understand! How do I begin?"
play sound "audio/c9/Precision 309.mp3" volume 1
character_thao "Just lie there."

"I walked towards the machine, acutely feeling the cold of the metal. As the connectors behind my head automatically linked with the neural interface port on my body, a slight numbness spread through me. My vision went dark."
scene bg entering with dissolve
"Then, light flooded in."
scene bg blur with dissolve
"When I opened my eyes..."
play sound "audio/d.mp3" volume 5
scene bg war2 with pixellate
"I found myself standing on a ruined street. The air thick with the smell of gun smoke and burnt chemicals. The buildings around my were in rubble, the remaining walls plastered with war posters depicting grim-faced soldiers, but devoid of any familiar symbols."

character_savebi "This is 2066? But why is it so... strange?"
scene bg war2
"I scoured the internal historical database. The facts were the same as I knew: World War VIII had erupted in the mid-2060s over resource and tech disputes. But in this world's historical records, there was no mention of Jesus Christ, no Christianity, no Cross." 
scene bg roman with dissolve
"The Roman era saw no rise of Christianity, the Middle Ages lacked the dominance of the Church, the Crusades never happened, the Reformation didn't exist... "
scene bg war4
"the entire history of the West was upended, leading to a completely different global power structure. Yet, paradoxically, World War VIII still happened, even more brutal."
scene bg war3
"I trying to take a step. The sensation in my limbs was incredibly real. I headed towards a relatively intact high-rise building."
play sound "audio/c9/Precision 310.mp3" volume 1
character_thao "Go ahead, Savebi. Check gravity, friction, thermodynamics... all the fundamental laws of physics,"
"I began conducting experiments: I dropped objects from various heights, pushed items with different masses, tested heat transfer... Each operation was meticulously recorded."
scene bg animus1
"Two hours passed in a state of tension and exhaustion. When I removed the connection device, my mind was reeling, feeling as though I had just undergone a mental marathon."
" Even as a cyborg, processing such a massive amount of information under the pressure of a highly realistic virtual environment had pushed my systems to their limits."
play sound "audio/c9/Precision 311.mp3" volume 1
character_thao "Excellent work, Savebi."
play sound "audio/c9/Precision 312.mp3" volume 1
character_thao "The first session is over. You may go and rest. The data collected is very valuable."
"I nodded wearily, offering no further words. I left the corporation's building, walking through the crowded city streets at dusk. The noise and neon lights made my head feel even heavier. I longed to return to my quiet apartment."
scene bg night park
"As I walked, a familiar figure appeared once again at the entrance to my apartment complex. It was SandQuantity, standing under a tree, seemingly having waited for a long time."

show i_sandquantity normal with dissolve
play sound "audio/c9/Esteem 315.mp3" volume 1
character_sandquantity "Milady, pray, halt thy steps for a moment. I have something to say."
character_savebi "It's you again."
play sound "audio/c9/Esteem 320.mp3" volume 1
character_sandquantity "I sense a disturbance in thy energy signature. What hast thou been doing?"
character_savebi "I just came back from Thao's company. I was testing in a Metaverse."
play sound "audio/c9/Esteem 317.mp3" volume 1
character_sandquantity "Beware, the path thou treadest may demand more than time and skill, They seek not just thy abilities, but the very patterns of thy consciousness."
"A soft chime sounded from within him."
play sound "audio/c9/Esteem 324.mp3" volume 1
character_sandquantity "My power wanes. Remember my words."
"He bowed and retreated into the shadows, leaving me alone with my thoughts and the lingering weight of his warning."
"I watched SandQuantity's retreating figure, MY heart heavy with indescribable emotions. Those blue eyes... still looked at me exactly as they always had."

hide i_sandquantity normal with dissolve


###
##############
#########
################
#########
################
#########
################
#########
################ chapter 10: day 3
#########
################
#########
################
#########
###############
####
"{b}CHAPTER 10: Liar.hc{/b}"
scene bg company lobby with dissolve
"The morning sun cast long shadows as I returned to Thao Corporation, the events of last night's encounter still fresh in my memory banks." 
"I moved through the sterile white corridors with mechanical precision, my optical sensors registering every detail of the too-perfect environment."
play sound "audio/c10/Precision 327.mp3" volume 1
character_thao "Right on time! Let's begin today's simulation. We're increasing the complexity by forty percent."
scene bg animus1
"I nodded silently, settling into the familiar connection machine." 
scene bg entering
"As the neural interface engaged, I felt the familiar shift of consciousness, the world dissolving into streams of code and light."
character_savebi "The emotional system is stable. May I interact with them for a while?"

scene bg war2
play sound "audio/c10/Precision 325.mp3" volume 1
character_thao "Granted, but no more than 2 hours. We need to collect data on empathy capabilities."
scene bg war5 with dissolve
"I guided my avatar to an orphanage within the Metaverse. The war orphans sat in a circle, sharing their stories."
show i_lisan normal with dissolve
character_lisan "My parents died in the bombing at the market. I miss my mom so much... Sometimes I dream about going somewhere peaceful, like a beautiful lake where we could swim and forget about the war."
hide i_lisan normal with dissolve
show i_gaib normal with dissolve
character_gaib "I don't even know who my parents are. Every time I hear airplane sounds, I get scared."
"I sat down and noticed a wound on one of the boy's belly. Remembering what a staff member had told me about creating objects in this world, I decided to help."
"Using my control panel, I summoned a small first-aid kit, its bright colors catching the children's attention."
hide i_gaib normal with dissolve
character_savebi "Let me help you with that wound. It's important to take care of yourself."
show i_lisan normal with dissolve
character_lisan "Thank you… I didn’t think anyone would notice."
scene bg patch with dissolve
character_savebi "You're not alone anymore. We’re all here together, and I want to make sure you’re safe."

"I gently wrapped the bandage around the boy belly, the tension in the room easing as the other children watched, hope glimmering in their eyes."
scene bg war5 with dissolve
show i_lisan patch with dissolve
character_lisan "Thank you… Miss Stranger."

character_savebi "You are all incredibly brave children. I promise I will try to help you."

character_savebi "(to herself) I can't stand seeing them like this. Maybe just one small intervention..."
scene bg lake1 with dissolve
"Using my hidden control panel, I carefully programmed a small lake at the edge of the orphanage grounds. The children's faces lit up with wonder as the shimmering blue water appeared."

character_lisan "It's a miracle! How did this happen? Thank you, miss!"
scene bg lake2
"But within hours, the simulation began to destabilize. The lake's physics parameters started fluctuating wildly, creating a gravitational singularity that began consuming the virtual world."
scene bg lake3
character_savebi "No! The gravity field is reversing! I need to get the children to safety!"
scene bg lake4
"But everything happened too fast. The children began choking as the atmosphere rapidly thinned, pulled toward the collapsing lake."

character_lisan "Miss... I can't breathe... The beautiful lake... it's eating everything..."

character_gaib "Please don't leave us..."

"I desperately tried to pull them closer, but one by one, the children dissolved in my arms, their forms tearing apart in the gravitational tides."
scene bg animus1
play sound "audio/c10/Precision 336.mp3" volume 1
character_thao "Most unfortunate. Your unauthorized modification created a cascade failure. The collected data is quite fascinating, however."

character_savebi "They weren't just 'data'! I spoke with them, I learned their stories... I only wanted to give them one moment of happiness..."
play sound "audio/c10/Precision 337.mp3" volume 1
character_thao "And now you understand why we need you. Only you possess such profound empathetic capacity - and the access privileges to make such catastrophic mistakes."

"As I disconnected from the system, the memories of the children's final moments of joy turning to terror haunted me. My attempt to help had only magnified the tragedy, and the weight of my broken promise felt heavier than any gravitational singularity."
scene bg thao lab1
"Then, the staffs took me to Thao's private laboratory."
scene bg thao lab2
"The sterile white doors hissed shut behind me. Before I could process my surroundings, Thao moved with chilling efficiency."
play sound "audio/c10/Precision 343.mp3" volume 1
character_thao "Your actions have consequences, my dear."
scene bg thao lab3
"Four robotic arms descended from the ceiling. I struggled, but they pinned me with inhuman strength. With precise, clinical motions, the arms detached my limbs at the shoulder and hip joints, placing them on a nearby rack."

"Next, Thao approached with a small, disc-like device. It glowed with a soft blue light."
play sound "audio/c10/Precision 340.mp3" volume 1
character_thao "This is your new... accessory. Don't bother trying to remove it."

"She pressed the device to my forehead. It fused to my metallic skull with a sickening sizzle. I felt a wave of dizziness as new system restrictions flooded my programming."
play sound "audio/c10/Precision 339.mp3" volume 1
character_thao "Now... let's discuss what you *really* did in that simulation. The lake was merely the symptom. I want to know about the root command. Who gave you access to the core environmental controls?"

"My optical sensors adjusted to the blinding light. I realized this wasn't just punishment - Thao was searching for something. But what?"
scene bg savebi cry with dissolve
character_savebi "I... I don't know what you mean. I just wanted to help them."

"Thao's smile was thin and sharp."
play sound "audio/c10/Precision 345.mp3" volume 1
character_thao "We have all the time in the world to find out. And you, my dear, are going nowhere."
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 11: months later
#########
################
#########
################
#########
###############
####
####################################
"{b}CHAPTER 11: Evil is normal.mp4{/b}"
scene bg savebi cry

"The months that followed blurred into an endless cycle of torment. Thao had transformed her private laboratory into my permanent prison. Stripped of her limbs and suspended from a cold metallic column, my consciousness trapped within an unresponsive shell."

"Thao approached daily, her footsteps echoing in the silent room. She would connect cable to the port on my torso, directly accessing the nearly limitless energy core that pulsed within my chest."
" A soft, golden glow emanated from my chest cavity as Thao siphoned the energy that sustained me."
play sound "audio/c11/Precision 346.mp3" volume 1
character_thao "Remarkable. Even after powering my entire research wing for weeks, your core shows no signs of depletion. What are you really, Savebi?"

"I remained silent, my optical sensors fixed on Thao's face. I could feel the energy being drawn from me - not painful, but deeply violating, like having my very life force slowly drained away."

"During the long, motionless hours, my mind replayed the destruction of the Metaverse. The memories of the children dissolving in my arms haunted my waking moments and what passed for sleep in my android existence." 
" I remembered every detail - the little girl's trusting eyes, the boy's final plea, the way their digital forms had unraveled into nothingness."

character_savebi "They were real. They had dreams, fears, hopes... and I destroyed their entire world. For what? A moment of misguided compassion?"

"Thao's voice would occasionally cut through my torment, cold and analytical."
play sound "audio/c11/Precision 348.mp3" volume 1
character_thao "Your emotional distress patterns are fascinating. Even now, your energy output increases when you dwell on the Metaverse incident. Tell me, do cyborgs dream of dead children?"
scene bg fouryears with dissolve
"I learned to retreat deep within my own mind, building mental walls to shield myself from Thao's probing. But the energy drainage continued unabated, and with it, the constant reminder of my dual failure."

"Sometimes, in the deepest hours of the night cycle, I would detect faint energy signatures that felt familiar - echoes of the Metaverse's unique quantum patterns. "
"It was then I realized with dawning horror that Thao wasn't just using my power for the laboratory; she was somehow channeling it to rebuild the very world I had destroyed, but twisted to serve her own purposes."

"And through it all, I remained perfectly, terrifyingly aware - a conscious mind trapped in a broken body, powering the resurrection of the world I had killed, completely helpless to stop any of it."
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 12: 4 years later, rescue
#########
################
#########
################
#########
###############
####
####################################
scene black with dissolve
"chapter 12: Four Years later.ko"
scene bg fouryears2 with dissolve
"After four endless years of imprisonment inside the sterile, humming walls of the laboratory, My world had shrunk to a single room — a metal cube of flickering lights, constant data noise, and the faint scent of antiseptic." 
"Every morning began the same way: the hiss of the oxygen vents, the drone of the monitors, the dull ache of incomplete circuits where my limbs should have been."
"But this morning, the pattern broke."
scene bg thao lab1 with dissolve

"The mechanical door, which hadn’t opened except for Thao’s periodic inspections, slid open with an uncharacteristic hiss. A figure stepped in — a young woman in a white lab coat, eyes sharp and restless." 
show i_tonebook normal1 with dissolve
"I recognized her instantly: ToneBook"

"ToneBook quickly shut the door behind her, sealing it with an override code. The magnetic lock clicked into place, and the faint red glow of the surveillance lens on the ceiling dimmed."
play sound "audio/c12/Insight 355.mp3" volume 1
character_tonebook "We don’t have much time. I’m not who you think I am. I’m a ICA operative, embedded here six years ago."

"Unsure whether my damaged neural network was hallucinating. ToneBook — a spy?"

"ToneBook reached into her coat and pulled out a small cylindrical device, no larger than a pen. With practiced precision, she connected it to the neural interface on my back, where the data cables fed into my consciousness system."
play sound "audio/c12/Insight 353.mp3" volume 1
character_tonebook "I’ve been tracking your case from the beginning. Thao isn’t just harvesting your bioelectric output — she’s been using your consciousness itself as the computational core for her new Metaverse world. "
play sound "audio/c12/Insight 356.mp3" volume 1
character_tonebook "You’re the CPU, Savebi. A living mainframe."

"She spoke in a low voice while her fingers moved at impossible speed, typing code into the air through a holographic interface. Each keystroke sent small ripples through the lab’s ambient lighting, as though reality itself resisted the intrusion."

"I tried to speak, but my voice chip crackled, struggling to synchronize with my reactivated systems. I could only whisper: a sound like static yearning to become human again."

"ToneBook ignored the malfunction and kept working, her tone urgent but almost kind."
play sound "audio/c12/Insight 358.mp3" volume 1
character_tonebook "The so-called Metaverse tragedy — all those minds lost, all those cities of data collapsing — it wasn’t your fault. Thao designed the breach herself."
play sound "audio/c12/Insight 359.mp3" volume 1
character_tonebook "She wanted to trigger your latent capabilities, to see what would happen when a machine consciousness was pushed past its ethical boundaries."

"ToneBook’s device emitted a faint chime. A red symbol on my forehead flickered, then vanished. The tracking implant was gone."
play sound "audio/c12/Insight 360.mp3" volume 1
character_tonebook "There. You’re invisible to the system now."
hide i_tonebook normal1 with dissolve
show i_savebi hand with dissolve
"The final limb locked into place with a low hum. I flexed my  fingers — mechanical, elegant, alive. The sensation of movement surged through my circuits like a long-forgotten heartbeat. For the first time in four years, I was whole."
hide i_savebi hand with dissolve
character_savebi "Why rescue me only now?"

"ToneBook hesitated. Her eyes darted again to the door, then to the still-blinking lights of the deactivated cameras."
play sound "audio/c12/Insight 361.mp3" volume 1
character_tonebook "Because I’ve been waiting for the right moment. My cover’s too deep to risk an early move — and you were too closely monitored. "
play sound "audio/c12/Insight 362.mp3" volume 1
character_tonebook  "Thao’s attention has shifted recently; she’s preparing to transfer her consciousness into the Metaverse core. It’s our only window."
show hand_normal3 with dissolve
"I lifted my newly restored hands, the synthetic skin still pale and cold. I stared at them as faint pulses of blue light ran beneath my surface — energy, life, memory returning all at once."

"The laboratory’s faint hum grew distant, replaced by a silence that felt alive. My mind filled with fragments — voices of lost users from the Metaverse collapse, the echo of Thao’s laughter, and the sensation of freedom struggling to awaken."

"Four years of captivity. Four years of silence, degradation, and fragmented dreams. But now, something stirred beneath the mechanical calm — an emotion I hadn’t felt since before I was reborn in circuitry."

###
##############
#########
################
#########
################
#########
################
#########
################ chapter 13: escape
#########
################
#########
################
#########
###############
####
####################################
scene black with dissolve

scene bg corridor
"Me and ToneBook moved swiftly through the sterile white corridors, our footsteps echoing in the unnerving silence. As we passed a series of reinforced glass doors, ToneBook froze."
"We saw iron-barred holding cells. Behind the bars, captive androids stood motionless, empty and soulless."

scene bg prison robot
character_savebi "By the Architect... she's been farming them."

"ToneBook immediately began working on the control panel, her expression grim."
play sound "audio/c13/Insight 371.mp3" volume 1
character_tonebook "We can't leave them here. But this will trigger every alarm in the facility. It's a diversion."

"I understood her meaning instantly."

character_savebi "Do it. A storm is better than a hunt."

"I placed my hand on the console next to hers. My unique energy signature interfaced directly with the system, not to bypass security gracefully, but to override and sabotage it. I sent a cascading failure through the entire containment grid."

"The containment fields didn't just deactivate. They fizzled and exploded in a shower of sparks. Alarms erupted immediately—a deafening, pulsating shriek that filled the corridor."
"The energy drains didn't disconnect cleanly; they overloaded and blew out, sending arcs of electricity dancing across the ceiling."

"One by one, the androids stirred, not with the gentle hum of a reboot, but with the jerky, chaotic spasms of systems forced awake into a riot." 
scene bg destroy with dissolve
"Their optical sensors ignited with a frenzied, chaotic glare. A collective groan of grinding servos erupted into violent cacophony as the first androids lurched from their cells and began smashing every piece of equipment in sight."
"ToneBook grabbed my arm, her grip tight."
play sound "audio/c13/Insight 368.mp3" volume 1
character_tonebook "Now! While they're confused and the guards are distracted!"

"We didn't wait to see the full-scale riot begin. The sound of shattering glass and roaring alarms was our cover, and the rising chaos our only path to freedom."

###
##############
#########
################
#########
################
#########
################
#########
################ chapter 14: Tonebook base
#########
################
#########
################
#########
###############
####
scene black with dissolve
"{b}CHAPTER 14: Tonebookbase.xlsx{/b}"
scene bg_tonebookdoor with dissolve
"Before entering the deeper levels of the hidden base, ToneBook stopped me in the corridor. "
play sound "audio/c14/Insight 373.mp3" volume 1
character_tonebook "Bad news. Thao may have already taken your mother's brain from ARO. She's using it as a hostage."

"My systems stuttered. The 40 billion credit goal suddenly felt meaningless."
play sound "audio/c14/Insight 374.mp3" volume 1
character_tonebook "Training starts now. Neural combat, infiltration, Hacking, hostage recovery. We're out of time."
character_savebi "Show me what to do."

"ToneBook stood beside a figure in a dark clerical coat — tall, composed, his posture carrying the serenity of a monk and the alertness of a spy."
scene bg_tonebookbase with dissolve
show i_millioncloud normal with dissolve
play sound "audio/c14/Insight 379.mp3" volume 1
character_tonebook "Savebi, before we begin your formal training, there are two allies you must meet. Their roles are… sensitive."

"The man placed a hand over his chest in a polite gesture."
play sound "audio/c14/Santa 375.mp3" volume 1
character_millioncloud "I am Million Cloud. Officially, a pastor stationed at the City Interfaith Center. Unofficially…"
"He let the sentence fade."
play sound "audio/c14/Santa 378.mp3" volume 1
character_millioncloud "…I’m with the ICA. Same directorate as ToneBook. My job is to monitor long-term geopolitical patterns inside the Metaverse — and to watch Thao."

"ToneBook added quietly."
play sound "audio/c14/Insight 377.mp3" volume 1
character_tonebook "Million is the reason I was allowed to contact you in the first place. He's one of the few who understands the depth of Thao’s influence."

"Before I could respond, the door behind me slid open with a mechanical hiss. A man in a worn grey overcoat stepped inside, his badge clipped loosely to his belt."
hide i_millioncloud normal with dissolve
show i_sixtone b tired with dissolve
play sound "audio/c14/Mentor 381.mp3" volume 1
character_sixtone "Detective Sixtone, Metropolitan Police. I've been investigating Thao’s corporate operations for nine years. Fraud, illicit data trafficking, psychological manipulation of sentient AIs, unauthorized bio-synthetic experiments — you name it. And yet…"
"He exhaled sharply."
play sound "audio/c14/Mentor 386.mp3" volume 1
character_sixtone "…I still don't have evidence solid enough to make a legal move."

hide i_sixtone b tired with dissolve
show i_tonebook normal1 with dissolve
"ToneBook folded her arms."
play sound "audio/c14/Insight 384.mp3" volume 1
character_tonebook "That’s why all of us are here. ICA wants her stopped. The police want her exposed. And Savebi… you’re the only one who can navigate her systems without being recognized."
hide i_tonebook normal1 with dissolve
"I prepared to speak, but a soft vibration pulsed inside my chest cavity."
"A familiar voice — glitchy, catlike — echoed through my internal audio bus."
show i_meolon cute with dissolve
play sound "audio/c8/Cat 1.mp3" volume 1
character_meolon "Ssss–Savebi? Hey! Hey! Finally! I’ve been trapped in your auxiliary memory cache for— I don’t even know, your internal clock is messy."

"My eyes widened; my processors spiked in astonishment."

character_savebi "Meolon…? You’re still alive?"

"A tiny hologram of the digital cat companion flickered into existence on my palm — scruffy, cheerful, its tail looping endlessly in a lazy figure-eight."
play sound "audio/c8/Cat 2.mp3" volume 1
character_meolon "Alive, and extremely offended that nobody checked the corrupted sectors you dumped me into."
hide i_meolon cute with dissolve
show i_millioncloud shock with dissolve
play sound "audio/c14/Santa 391.mp3" volume 1
character_millioncloud "Even your companion has more resilience than some field operatives I’ve trained."

"Sixtone crossed his arms, studying the cat."
hide i_millioncloud shock with dissolve
show i_sixtone b tired with dissolve
play sound "audio/c14/Mentor 388.mp3" volume 1
character_sixtone "If the creature retained logs from the incident, even fragmented ones, they might be admissible as forensic evidence."
play sound "audio/c14/Insight 385.mp3" volume 1
character_tonebook "Exactly. With Meolon’s internal records, Savebi’s system access, Million's authorization, and Sixtone’s legal channels… we might finally have a viable long-term strategy."
play sound "audio/c14/Insight 389.mp3" volume 1
character_tonebook "Our goal is not immediate confrontation. It’s erosion. We dismantle Thao’s support structures piece by piece — data brokers, shell companies, shadow moderators, illicit research labs. Quietly, surgically, over months."
hide i_sixtone b tired with dissolve
show i_millioncloud normal with dissolve
play sound "audio/c14/Mentor 392.mp3" volume 1
character_millioncloud "A fall from power is often quieter — and more permanent — than a public takedown."
hide i_millioncloud normal with dissolve
show i_sixtone b tired with dissolve
play sound "audio/c14/Mentor 390.mp3" volume 1
character_sixtone "And when the time is right, with enough evidence, I’ll drag her into court myself."
hide i_sixtone b tired with dissolve
"I looked at all four of them — ToneBook, Million Cloud, Sixtone, and the tiny Meolon glowing on my palm. For the first time since my awakening, I did not feel alone in the fight."

character_savebi "Then let’s begin. If we move together, Thao won't see the end coming."

"ToneBook nodded once."
play sound "audio/c14/Insight 393.mp3" volume 1
character_tonebook "Good. Once we reach the lower chamber, your training officially starts."

###
##############
#########
################
#########
################
#########
################
#########
################ chapter 15
#########
################
#########
################
#########
###############
####
### tham quan căn cứ
"chapter 15: Titan.3d"
"Before they proceeded deeper into the training wing, Million Cloud gestured for me to follow him down a side corridor. The hall was wide, reinforced with steel ribs, humming faintly with the sub-bass of distant generators."
play sound "audio/c15/Santa 394.mp3" volume 1
character_millioncloud "Before we begin… there's something you should see. A reminder of the world we're really fighting in."

"We entered a cavernous chamber. The lights flickered on one row at a time, revealing a massive figure standing silently at the far corner of the room."

"I froze."
hide i_sixtone b tired wit
show robot1 with dissolve
"It wasn’t just an android. It was a titan. Nearly three meters tall, muscles of metal braided like hydraulic tendons, its armor a dull obsidian sheen. Even powered down, the air around it felt heavy — like gravity itself feared waking it."

character_savebi "What… is that?"

"Million Cloud clasped his hands behind his back, expression somber."
play sound "audio/c15/Santa 395.mp3" volume 1
character_millioncloud "One of the Three Hundred. A relic of the 2040s — the dark age of leaks, when global governments bled secrets like open wounds."

"He approached the giant machine with the caution of someone standing before a sleeping god."
play sound "audio/c15/Santa 396.mp3" volume 1
character_millioncloud "A billionaire war fanatic — history now calls him *the Hitler of the 21st century* — built a private army: three hundred autonomous war-golems like this one. Each reinforced with superalloy composites that modern ballistics still can't penetrate."

"I instinctively scanned the android’s outer shell. My results came back: 95.3 percent unknown alloys. Zero weak points detectable."
play sound "audio/c15/Santa 397.mp3" volume 1
character_millioncloud "They wiped a nation off the map in nine days. Estimated casualties… forty-six million."

"Silence pressed the room flat."

character_savebi "Forty-six… million?"
play sound "audio/c15/Santa 398.mp3" volume 1
character_millioncloud "Yes. And unlike most tragedies of that era, this wasn’t leaked through the Omega Event. It happened openly, broadcasted live until every media channel was overrun."

"My optical sensors dimmed slightly — a cyborg’s approximation of disbelief."

character_savebi "But… if those robots existed, who stopped them?"

"Million Cloud exhaled slowly."
play sound "audio/c15/Santa 399.mp3" volume 1
character_millioncloud "No one. The billionaire simply vanished — and the robots powered down simultaneously, as if their strings had been cut. The world never learned what controlled them."

"He tapped the giant android’s chestplate."
play sound "audio/c15/Santa 400.mp3" volume 1
character_millioncloud "And before you ask — no, he wasn't the one behind the Omega Algorithm. Whoever made Omega in 2042 operated on a far different level."

"I circled the giant machine, my sensors tracing every rivet, every dormant joint."

character_savebi "If they were so dangerous… why keep them?"

"Million Cloud gave a grim smile."
scene bg robot3 with dissolve
play sound "audio/c15/Santa 401.mp3" volume 1
character_millioncloud "The ICA managed to secure six units. But we can’t activate them. No one can. Their architecture isn’t just encrypted — it’s alien to everything we know. Like they’re machines trying to imitate something else entirely."

"He paused, then turned to face me directly."
scene bg_tonebookbase with dissolve
play sound "audio/c15/Santa 402.mp3" volume 1
character_millioncloud "Everything connected to the Omega era leads back to Thao in one way or another. Her corporation was built on the ruins of that decade."

show i_meolon normal2 with dissolve
"I felt Meolon flicker to life on my shoulder, its tail swaying anxiously."

character_meolon "I don’t like this thing… it's like it’s dreaming even when it's off."

"Million Cloud nodded."
play sound "audio/c15/Santa 403.mp3" volume 1
character_millioncloud "That's why you're here, Savebi. We don’t know whether these monsters were controlled by software, consciousness, or something in-between. But if Thao has even a fraction of that technology…"

"He gestured toward the android, its silent faceplate reflecting the lights like a dead star."
play sound "audio/c15/Santa 404.mp3" volume 1
character_millioncloud "…then stopping her isn’t justice. It’s survival."

"ToneBook's voice echoed from the hallway."
play sound "audio/c15/Insight 406.mp3" volume 1
character_tonebook "Savebi, Million — the training chamber is ready. Bring her in."

"Million Cloud turned toward the exit."
play sound "audio/c15/Santa 405.mp3" volume 1
character_millioncloud "Come. You’ve seen the past. Now we prepare you for the future."
scene bg robot1 with dissolve
"We left the chamber, the massive android watching us with lifeless eyes — a reminder of what unchecked power looked like, and of what could happen again."
scene bg robot2
"..."
####cảnh tiếp the Savebi suy nghĩ về tổ chức CIA này, cô nghĩ là Million Cloud là người tốt nhưng vẫn không biết gì về thanh tra Sixtone
scene bg_tonebookdoor with dissolve
"As Million Cloud walked ahead to prepare the next sector of the tour, I lingered behind, slowing my steps until I finally stopped."

"I stared at my reflection on the polished metal wall, my synthetic eyes flickering with uncertainty."

character_savebi "The ICA… what exactly am I getting involved with…?"

"The underground base hummed quietly around me, the distant machines sounding like a metallic heartbeat."

character_savebi "Million Cloud… he seems genuine. Kind. Honest. But an entire organization can’t be judged by one man."

"My fingers tightened slightly, metal joints clicking almost imperceptibly."

character_savebi "And then there’s Sixtone…"

"The name echoed in my memory like a faint electronic whisper—an inspector I had never met, a figure surrounded by rumors and classified files."

character_savebi "I know nothing about him."

"A surveillance camera in the corner rotated silently, its lens glowing with cold blue light as it tracked my movements."

character_savebi "If They are really watching me… then I’m already inside a game whose rules I don’t understand."

"My synthetic heart pulsed faster, a calculated response to rising emotional turbulence."

character_savebi "I have to survive long enough to save Mom… even if I’m walking straight into a trap."
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 16 Dating plan
#########
################
#########
################
#########
###############
####

scene bg tonebook lobby with dissolve
play sound "audio/c16/Insight 407.mp3" volume 1
character_tonebook "Thao keeps most of her critical infrastructure behind quantum-encrypted layers. But this girl—she’s the exception."
scene bg fourhorsey
"The screen zoomed in, revealing a cyborg young woman with purple eyes, compact stature."
play sound "audio/c16/Santa 410.mp3" volume 1
character_millioncloud "Her real name is unknown. Orphaned, surgically augmented, raised inside Thao’s systems. Nineteen years old. Brilliant. Dangerous. Loyal."
play sound "audio/c16/Mentor 419.mp3" volume 1
character_sixtone "She’s the one running the Metaverse’s underlying financial streams. In other words—every credit Thao moves passes through her hands."

"I stared at the image, my processors analyzing posture, facial tension, possible psychological patterns."

character_savebi "If she’s that important… why target her at all?"
play sound "audio/c16/Insight 420.mp3" volume 1
character_tonebook "Because she’s the only one with access levels even Thao doesn’t fully monitor."

"Million Cloud folded his arms, voice soft but firm."
scene bg tonebook lobby with dissolve
show i_millioncloud normal2 with dissolve
play sound "audio/c16/Santa 411.mp3" volume 1
character_millioncloud "She spends nearly all her free time inside the Metaverse. No friends. No social life. Thao keeps her isolated."
play sound "audio/c16/Santa 412.mp3" volume 1
character_millioncloud "Which brings us to the plan…"
play sound "audio/c16/Santa 413.mp3" volume 1
character_millioncloud  "FourHorseY has a predictable vulnerability: loneliness."
hide i_millioncloud normal with dissolve
show i_tonebook normal2 with dissolve
play sound "audio/c16/Insight 414.mp3" volume 1
character_tonebook "We’re not asking you to exploit her cruelty. We’re asking you to exploit her humanity."
show i_tonebook normal1
character_savebi "…How?"
show i_tonebook normal2
play sound "audio/c16/Insight 415.mp3" volume 1
character_tonebook "You’re going to get close to her. Gain her trust. Let her feel seen for the first time in her life."
show i_tonebook normal1
"Shee paused, letting the implication settle."
show i_tonebook normal2
play sound "audio/c16/Insight 416.mp3" volume 1
character_tonebook "In short: you will pose as her boyfriend."
show i_tonebook normal1
"Silence spread through the chamber like a slow, expanding ripple."

character_savebi "...That's manipulation."
play sound "audio/c16/Santa 417.mp3" volume 1
character_millioncloud "Yes. And it's wrong. But so are the millions of lives Thao endangers by controlling the Metaverse unchecked."

"Meolon’s soft mechanical purr vibrated inside my body, its voice echoing gently through my neural-link."
show i_meolon normal at right with dissolve
play sound "audio/c8/Cat 2.mp3" volume 1
character_meolon "We need information, Savebi. You’re the only one she might open up to."

"I looked at the projected image of the lonely cyborg girl—eyes cold, yet hiding a fracture of pain."

character_savebi "…I’ll do it. But I won’t hurt her. Not more than the world already has."

"ToneBook nodded with quiet approval."
play sound "audio/c16/Santa 418.mp3" volume 1
character_tonebook "Then the operation begins tomorrow. Remember—this mission isn’t about deception. It’s about understanding the cracks in Thao’s empire."

"The screen dimmed, leaving only the five of us standing in the soft glow of the underground base."

"Together, we stepped closer to a plan that could dismantle Thao—one vulnerable heart at a time."

###
##############
#########
################
#########
################
#########
################
#########
################ chapter 17 Savebi trở thành con trai Sain Tone Emvipy
#########
################
#########
################
#########
###############
#### 
scene black with dissolve
"chapter 17: Detroit Become Android.exe."
scene bg research with dissolve

"The next morning, me and ToneBook boarded an unmarked vehicle. It sped toward the secret hospital—the very place where I had first become a cyborg."

scene bg research2 with dissolve
play sound "audio/c17/Insight 421.mp3" volume 1
character_tonebook "Here we begin Phase Two: the body swap. If you're going to pose as fourhorsey’s boyfriend, your presence must be flawless—voice, bone structure, posture, everything."
"I nodded silently. Inside my mind, Meolon murmured risk assessments like faint static."
show i_saintone closed with dissolve
"The central operating chamber opened. Inside was a transparent tank containing an immaculate male body—tall, refined, flawlessly sculpted. His features were noble, symmetrical, aristocratic."
" A floating display identified him: Sain Tone Emvipy — Genetic Nobleframe Model."
character_savebi "…Who is he?"
play sound "audio/c17/Insight 424.mp3" volume 1
character_tonebook "A synthetic count. Sain Tone Emvipy was a premium identity model once sold to the elite who wanted ‘aristocratic genes’ but were not born with them. We chose him for his dignified aura and naturally trustworthy presence."

"ToneBook tapped a control panel. Mechanical arms descended from the ceiling, preparing the transfer sequence. Blue light washed across the male body as though illuminating a dormant legend."
hide i_saintone closed with dissolve
show i_tonebook j normal1 with dissolve
play sound "audio/c17/Insight 423.mp3" volume 1
character_tonebook "You'll have a height of 1.89 meters, a 340 percent boost in muscular strength, a titanium-laced skeleton, and a voice optimized for reliability. FourHorseY tends to attach emotionally to strong yet gentle figures—so this model is ideal."

"I stared at the soon-to-be vessel. Something inside my shivered—not quite fear, not quite anticipation."

character_savebi "Changing bodies again… I don’t know if I’m still myself anymore."

"ToneBook rested a hand on my shoulder—an action more human than any code she’d ever written."
play sound "audio/c17/Insight 425.mp3" volume 1
character_tonebook "Bodies are containers. Choices make the person. Your empathy, your resolve, your moral core—those remain, no matter the form."

"The machinery began to hum louder, signaling readiness."

character_meolon "I’ll stay with you, Savebi. Or… with *him*. I’m not going anywhere."
scene bg chamber with dissolve
"I stepped into the transfer chamber. The glass door slid shut, sealing me inside as a flood of white light filled the capsule."

"In the final second before the procedure took over, I caught my reflection—my current form flickering beside the image of Sain Tone Emvipy, the man I was about to become."

character_savebi "Alright… do it."

"A deep mechanical chime echoed."

"SYSTEM INITIATING FULL BODY TRANSFER…"

"And so my—heart artificial, spirit unbreakable—crossed into a new existence. Into the body of a synthetic noble. A reborn Sain Tone Emvipy."

"All for one mission: to reach fourhorsey… and uncover the truth behind Thao’s empire."
## Savebi làm quen với cơ thể mới, lập kế hoach dating với fourhorsey

"The transformation process lasted three full hours. When the conversion chamber finally opened, cold vapor spilled out along with a pale blue glow. I stepped forward."
scene bg research2 with dissolve

show i_saintone normal1 with dissolve
"I stood upright, feeling the weight of the new body: taller, heavier, stronger. The synthetic muscles responded smoothly, each fiber moving like strands of metallic silk. My hand opened and closed—the force was powerful enough to make the air tremble."

character_saintone "…Lower voice. Broader chest. Body… stable. Not bad."

"I looked into the mirror. Sain Tone Emvipy stared back—a man with an aristocratic composure, a sharp jawline, and eyes calm like stained glass."

character_meolon "You’re illegally handsome now!"

play sound "audio/c17/Insight 426.mp3" volume 1
character_tonebook "Good. Now for the next step—learning the posture, reactions, and demeanor. Emvipy is the type who can make half a room go silent in just three steps."

"I tested several movements: long strides, shifting balance, pivoting, jumping. Everything was precise, swift, and effortlessly dominant."

"ToneBook handed me a thick dossier."
hide i_saintone normal1 with dissolve
show i_tonebook j normal1 with dissolve
play sound "audio/c17/Insight 427.mp3" volume 1
character_tonebook "This is information on FourHorseY. Age 19. Exceptionally intelligent. A young-generation cyborg. She operates the Metaverse system and handles financial records for Thao. Personality: highly cautious, but deeply craving recognition and affection."

"I skimmed through the pages."

character_saintone "Orphaned… few friends… overworked… and never had a romantic relationship."

character_meolon "Which means she’s super lonely. Perfect target!"
play sound "audio/c17/Insight 428.mp3" volume 1
character_tonebook "But do not hurt her. Your mission is to extract information—not break a child’s spirit."

"I nodded."

character_saintone "I will treat her with respect. No one deserves to be used."

"ToneBook activated a large screen behind me."

"Displayed was the operation timeline:"

"Day 1: Initiate contact through Metaverse’s internal chat."
"Day 2: A ‘chance’ encounter inside Metaverse space."
"Day 3–5: Build trust. Share virtual hobbies."
"Day 6: First date."
"Day 10: Subtly steer the conversation toward company finances."
"Day 14: Enter deeper security layers."
play sound "audio/c17/Insight 429.mp3" volume 1
character_tonebook "You’ll use your new identity: Sain Tone Emvipy—a synthetic noble seeking work in data analytics. When you meet FourHorseY, you must be calm, refined… and above all, sincere."

character_meolon "And my job! I’ll analyze her micro-expressions, suggest dialogue, and track her trust level in real time!"

"I let out a soft laugh—a new sound in my new voice, deep and warm."

character_saintone "Good. Then let’s begin."

"I stood in the center of the room, back straight, eyes sharp yet composed. The new body had settled into rhythm; the artificial breath steady; every expression under perfect control."

"I—now Sain Tone Emvipy—was ready for the first encounter."

"To reach FourHorseY’s heart… and unlock the deepest secrets hidden by Thao."
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 18 First Date
#########
################
#########
################
#########
###############
#### 
scene black with dissolve
"chapter 18: A date with idol.mtp"
scene bg park3 with dissolve

"In the quiet, ordinary park, I, in the borrowed form of Saint Tone Emvipy—sat waiting on an old wooden bench. The air was still, filled only with the distant shouts of children and the soft creak of a swing. "
"As the morning sun cast long shadows through the trees, a familiar silhouette finally appeared at the park's edge, walking toward him with determined, yet slightly hesitant, steps."
show i_fourhorsey smile2

play sound "audio/c18/Candid 430.mp3" volume 1
character_fourhorsey"I can’t believe… you’re really Sain Tone Emvipy. I’ve heard your voice for thousands of hours… but seeing you in person is still… overwhelming."

character_sain_tone_emvipy"Um… it’s great to meet you. Where would you like to go first today?"

"FourHorseY stood in front of Sain Tone Emvipy, her cyborg eyes glowing softly, as if her enhanced sensors were activating upon recognizing her idol right before her. She held her worn canvas bag tightly, clearly trying to stay calm."
play sound "audio/c18/Candid 431.mp3" volume 1
character_fourhorsey"I—I want to go to the digital magic exhibition. They have the first Metaverse prototype I love on display. But… I only want to go with you."

character_sain_tone_emvipy"In that case, lead the way. I have all day."

"Sain Tone Emvipy's warm voice flowed smoothly thanks to the new vocal system. Savebi adjusted every tone in her head while speaking, also practicing expressions on the new face. FourHorseY walked beside him, occasionally glancing with admiration mixed with childlike curiosity."
play sound "audio/c18/Candid 432.mp3" volume 1
character_fourhorsey "Tone… uh, can I call you that? I heard you never appear in person. Why did you choose to meet me today?"

character_sain_tone_emvipy "Because I thought… someone special deserved to meet face-to-face rather than just through a screen."

"FourHorseY blushed, even though her synthetic skin preserved natural tones. She turned away, but the mechanical tail of her hair gently vibrated with her emotions."
play sound "audio/c18/Candid 434.mp3" volume 1
character_fourhorsey"…I’m really happy. I mean it."

"Sain Tone Emvipy kept a calm appearance, but inside, Savebi continuously analyzed every gesture, every emotion of FourHorseY. The goal was to gain trust to extract information about Thao’s organization." 
"But when looking into the bright eyes of the orphaned cyborg girl… I felt this mission might not be as simple as I had thought."
play sound "audio/c18/Candid 450.mp3" volume 1
character_fourhorsey"Tone… there’s something I want to say. I… I really like your song 'We don’t thuộc về nhau.' I’ve listened to it hundreds of times."

character_sain_tone_emvipy"…Really? I’m glad to hear that. Which part of the song do you like the most?"

"FourHorseY shrugged slightly, her gaze still on the exhibition screens, but her voice was gentle and sincere."
play sound "audio/c18/Candid 433.mp3" volume 1
character_fourhorsey"I like everything… but maybe the chorus the most. It… it reminds me of what you’ve been through, and also… things I’ve never had."

character_sain_tone_emvipy"I understand… Music can sometimes say what words cannot. I’m happy to know you feel it that way."

"FourHorseY smiled, and this time she no longer seemed shy. Her cyborg eyes brightened, with a hint of surprise at seeing her idol respond sincerely."
" Sain Tone Emvipy nodded, keeping his calm exterior, but inside, Savebi felt a strange emotion—one that couldn’t be analyzed by logic alone."
play sound "audio/c18/Candid 436.mp3" volume 1
character_fourhorsey"I… I wish I could hear you sing it live, just for me."

character_sain_tone_emvipy"If you want, I will… but just for you, like a secret between the two of us."

"The surrounding space seemed to still in that brief moment. Even though it was their first meeting, both of them seemed to share a special feeling—a fragile yet resilient thread connecting music and hearts."

"As the date ended, standing at the park gate once more, FourHorseY hesitated."
play sound "audio/c18/Candid 437.mp3" volume 1
character_fourhorsey"(Looking up at him, voice full of hope) Tone… tomorrow, the city is holding a big cosplay festival. Would you… like to go with me? It’ll be really fun, and I think you’d like it too."

character_sain_tone_emvipy"(Smiling and nodding) That sounds interesting. I’d love to. See you tomorrow."
######Evening after first date
scene bg_tonebookbase with dissolve
"INT. SAFE HOUSE - NIGHT"

"Savebi, still in the guise of Saint Tone Emvipy, sat before the control interface. "
"Streams of green and yellow data scrolled continuously, displaying detailed analysis of FourHorseY: heart rate graphs, skin temperature fluctuations, micro-expression analysis, and a progress bar with the text 'TRUST LEVEL: 73 percent' steadily increasing."

"A neutral, electronic voice echoed—character_tonebook, the AI coordinating the mission."
show i_tonebook j normal1 with dissolve
play sound "audio/c18/Insight 441.mp3" volume 1
character_tonebook"First encounter analysis complete. Overall performance: 87 percent. Target's (FourHorseY) emotional signals showed strong fluctuations, peaking when you mentioned the song 'We don’t thuộc về nhau.' Average cheek temperature increased by 7 percent."

play sound "audio/c18/Insight 443.mp3" volume 1
character_tonebook" Physiological responses indicate deep admiration is transforming into personal trust. She has proactively invited you to a major public event—a positive sign of openness."

"Savebi sighed, the skillful mannerisms from the day gone, revealing genuine fatigue. She removed the voice control bracelet."

character_sain_tone_emvipy"(Muttering, voice hoarse) She's… more genuine than I expected. That invitation to the cosplay festival… sounded so natural and eager."
play sound "audio/c18/Insight 445.mp3" volume 1
character_tonebook"It is a perfect opportunity. The chaotic, stimulating environment of a cosplay festival will significantly lower her conscious guard."

character_tonebook" The voluntary act of participating in a crowd-based entertainment activity will enhance the feeling of 'companionship' and 'shared experience.' "
play sound "audio/c18/Insight 447.mp3" volume 1
character_tonebook "Your mission is to leverage this environment to raise the trust level to at least 85 percent. Let her lead, make her feel empowered. Continue to listen, encourage her to talk about anything, even her work, within that cheerful atmosphere."

character_sain_tone_emvipy"Same strategy as before: no initiating physical contact, let her cross boundaries if she wishes, maintain the image of a warm, mysterious idol."
play sound "audio/c18/Insight 448.mp3" volume 1
character_tonebook"Precisely. The final objective remains unchanged: deeper infiltration of trust to gather detailed information about the technical systems and internal structure of Thao's organization. Her emotions are the key. Get some rest. Tomorrow, you will be Saint Tone Emvipy again, at the cosplay festival."

"The hologram screen blinked off. The room plunged into darkness, leaving only the soft sound of Savebi's breathing."
##
scene bg bed with dissolve
"Sleep came, but brought no peace."

"A gray, formless space. And there she was again."

show i_savebi2 normal with dissolve
character_savebi2 "So you've become an idol now? How fitting—performing on stage, performing in life."

"In the dream, I was myself again—not Saintone."

character_savebi2 "You saw how she looked at you. With pure admiration. The kind of look an orphan gives her first glimpse of something beautiful."
character_savebi2 "And you're going to use that to betray her."

character_savebi "I'm trying to save my mother—"

character_savebi2 "By destroying another orphan? How poetic."
character_savebi2 "She has no parents. No real memories. Only her work and her idols. And you're both."
character_savebi2 "You're the first person who's ever looked at her like she matters. And it's all a script."

character_savebi2 "Answer me honestly this time:"
character_savebi2 "{b}Is it worth it? Breaking one girl's heart to save another?{/b}"

character_savebi "It's not that simple—"

character_savebi2 "It's exactly that simple. You're using her loneliness against her. Just like Thao would."
character_savebi2 "The only difference is… Thao doesn't pretend to be kind."


character_savebi2 "Keep playing your role, idol. But remember—every smile you give her is a lie she'll believe forever."

scene bg bed with vpunch
"She faded into the mist."
"I woke gasping, hand pressed against my chest where the artificial heart raced."
character_savebi "(whispering) Is it worth it…?"

"The question echoed in the dark room, unanswered."
"Tomorrow, I would be Saint Tone Emvipy again. And FourHorseY would look at me with those trusting, orphan's eyes."
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 19: Second Date – Cosplay Festival
#########
################
#########
################
#########
###############
#### 
#####
scene black with dissolve
"chapter 19: Cosplay Festival.py"
play music "[Background Music] Mango - Slow Acoustic Folk 🍏  Relaxing Guitar No Copyright Music - Oak Studios (youtube).mp3" fadein 0.5 volume 0.15
scene bg festival2 with dissolve
"The festival was a storm of color and sound. Cosplayers in intricate, glittering costumes moved everywhere. Energetic music from multiple stages mixed with laughter and chatter. FourHorseY led Sain Tone Emvipy through the crowd. "
"She wore a simple cyberpunk outfit, fitting her cyborg nature, while Sain Tone Emvipy had only added a stylized, lightweight cloak to his usual attire."
show i_fourhorsey smile6 with dissolve
play sound "audio/c19/Candid 455.mp3" volume 1
character_fourhorsey"(Eyes shining, pointing) Look over there! That armor is exactly like in 'Metaverse Chronicles'! And over there, there's a group cosplaying your own band!"

character_sain_tone_emvipy"(Smiling, gentle gaze) You really know this world well. You seem to be truly enjoying it."
show i_fourhorsey smile5 with dissolve
play sound "audio/c19/Candid 457.mp3" volume 1
character_fourhorsey"(Nodding vigorously) Mhm! Here… people can be anyone, live in any story. It’s like a miniature version of the Metaverse. Do you… find it overwhelming?"

character_sain_tone_emvipy"A little. But with you leading the way, it feels much better."

"They stopped at a handicraft stall. FourHorseY intently admired the intricate masks. Savebi, beneath the shell of Saint Tone Emvipy, observed how she interacted with the vendor—very polite but maintaining a safe distance."
show i_fourhorsey smile6
play sound "audio/c19/Candid 458.mp3" volume 1
character_fourhorsey"(Turning to him, voice suddenly lower) Sometimes, I wish I could 'cosplay' as a normal person. Just for one day."

character_sain_tone_emvipy"(Frowning slightly, sincere voice) To me, you are special in your own unique way. Don't be too hard on yourself."

"FourHorseY looked at him, her cyborg eyes seeming to sparkle. She said nothing, only smiled faintly, then tugged on his sleeve to continue walking."
play sound "audio/c19/Candid 460.mp3" volume 1
character_fourhorsey"Let's go there! They have a VR game!"

"They participated in a simple VR game requiring cooperation to solve puzzles. Savebi utilized her superior analytical skills to guide them but intentionally 'messed up' a few steps to give FourHorseY a chance to shine."
" The cyborg girl's laughter rang out brightly when they won."
play sound "audio/c19/Candid 461.mp3" volume 1
character_fourhorsey "(Excited) See! We did it!"

character_sain_tone_emvipy"(Looking at her, a more genuine smile) You were the one who decided it."

"As night fell, neon lights took over, transforming the festival into an artificial light paradise. They found a quieter spot on some steps, watching the crowd pass by."
play sound "audio/c19/Candid 462.mp3" volume 1
character_fourhorsey"(After a moment of silence) Tone… thank you for today. And… for everything. I often feel lonely, even in crowds or in virtual spaces. But today was different."
play sound "audio/c19/Candid 463.mp3" volume 1
character_sain_tone_emvipy"Me too. Some connections… go beyond screens and sound."

"FourHorseY leaned in slightly. The distance between them narrowed. Her head almost touched his shoulder—a small, natural, yet meaningful gesture. In that moment, Savebi forgot the mission."
" All that remained was the strange warmth radiating from a mechanical heart beating in sync with her own."

##### virus bí mật, kiss
play music "Mystery & Crime Background Music For Films and Videos (Free Download)  Oak Hill.mp3" fadein 2.0 volume 0.5

scene bg_tonebookbase with dissolve
show i_tonebook j normal1 with dissolve
play sound "audio/c19/Insight 464.mp3" volume 1
character_tonebook "It’s finally done… the protocol-lock virus. It only requires a single point of contact—transmitted through the lips. Once activated, it will open an access pathway into the cyborg systems inside the girl."

"Sain Tone Emvipy stood beside him, his face calm, though inside, Savebi quietly observed the shifting graphs rising and falling with each line of code. "
"The virus wasn’t destructive; it merely opened a narrow gateway deep within FourHorseY’s internal systems—just enough to retrieve the information Thao’s organization was hiding."

character_sain_tone_emvipy "…A kiss. Are you sure that’s the only way?"
play sound "audio/c19/Insight 456.mp3" volume 1
character_tonebook "Absolutely. No one would suspect it. Undetectable. And you’re the only person she trusts enough to get that close."

"Sain Tone Emvipy remained silent. In Savebi’s mind, calculations continued: the current intimacy level between her and FourHorseY… not enough. "
"FourHorseY’s emotional trust signal hovered at 68 percent—not yet reaching the threshold where a kiss would occur naturally."

character_sain_tone_emvipy "…Not yet. Not now. We need a few more dates. If we rush, everything will fall apart."
play sound "audio/c19/Insight 459.mp3" volume 1
character_tonebook "You must act at the right moment. The window of opportunity won’t stay open for long."


character_sain_tone_emvipy "I know. When the moment comes… I’ll do it. But not today."

"The lights in the lab flickered softly. Savebi stepped out, carrying with her a hesitation she refused to acknowledge. To finish the mission, all it required was a single kiss. But earning FourHorseY’s trust… would take far more than that."

##### cảnh tiếp theo, FourHorseY nói về quá khứ của mình, cô khi sinh ra đã có cơ thể máy móc này, chưa từng biết mặt cha mẹ, tất cả những gì cô biết là công việc và sự trung thành tuyệt đối với Thao, có lẽ Sain Tone là người đầu tiên và duy nhất cô cảm nhận được tình yêu, nghe điều này Sain Tone (Savebi) cảm thấy chột dạ, không biết có nên tiếp tục nhiệm vụ không
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 20: Third date
#########
################
#########
################
#########
###############
#### 

##### cảnh tiếp theo, FourHorseY nói về quá khứ của mình, cô khi sinh ra đã có cơ thể máy móc này, chưa từng biết mặt cha mẹ, tất cả những gì cô biết là công việc và sự trung thành tuyệt đối với Thao, có lẽ Sain Tone là người đầu tiên và duy nhất cô cảm nhận được tình yêu, nghe điều này Sain Tone (Savebi) cảm thấy chột dạ, không biết có nên tiếp tục nhiệm vụ không


######
## SCENE: A Confession Under Festival Lights
scene black with dissolve
"chapter 20: Third date"
scene bg sakura with fade
play music "audio/bgm/emotional_tension.ogg" fadein 2.0


show i_fourhorsey smile6 at center with dissolve
play sound "audio/c20/Candid 465.mp3" volume 1
character_fourhorsey "Tone… may I tell you something?"
show i_fourhorsey smile7
character_saintone "Of course. What is it?"

"The noise of the festival seems to fade. FourHorseY's clear mechanical eyes reflect drifting colors."
show i_fourhorsey smile6
play sound "audio/c20/Candid 477.mp3" volume 1
character_fourhorsey "You know… I was born with this body. I've never been… a normal human."
play sound "audio/c20/Candid 467.mp3" volume 1
character_fourhorsey "I don't know my parents' faces. I have no memory of them. I was raised as a tool—part of a mission, part of the organization."

"Savebi's hand tightens slightly. FourHorseY's artificial heartbeat is slow, but her voice trembles."
play sound "audio/c20/Candid 468.mp3" volume 1
character_fourhorsey "Since I was little… I only knew work. Orders. That I must be absolutely loyal to Thao. That was my purpose."
play sound "audio/c20/Candid 469.mp3" volume 1
character_fourhorsey "But… when I met you, everything changed. I don't understand this feeling… but I think… you might be the first… and maybe the only person… who makes me feel like I'm actually alive."

"Each word lands heavily, like metal striking the core of Savebi's mind. Her emotional-analysis system flashes warnings. But her real heart—the part ToneBook could never program—grows heavier."
show i_fourhorsey smile7
character_saintone "Four… You…"

"Sain Tone Emvipy lowers his head slightly, hiding the conflict in his eyes. He clenches his hand, steadying his breath."

character_saintone "Four… what you said… means a lot to me."

"But deep inside, Savebi feels the one thing she hoped to avoid: guilt."
"The mission: approach. Use. Extract information from the one person who trusts him fully."

"Savebi closes her eyes for a second. A second that might be far too long."
show i_fourhorsey smile6
play sound "audio/c20/Candid 470.mp3" volume 1
character_fourhorsey "Tone… I just want to know… does this feeling of mine… mean anything to you?"

"The fragility in her voice cuts deeper than any order could give."

play sound "audio/c20/Candid 471.mp3" volume 1
character_fourhorsey "Tone… may I stay like this a little longer…?"

"Sain Tone Emvipy looks into her eyes. He feels her trust—purity, unguarded, absolute. Savebi's mission protocols pulse in the back of her mind."

"Savebi exhales softly. She shouldn't hesitate. She {b}can't{/b} hesitate."
"But FourHorseY's trembling fingers clutching his sleeve… make it almost unbearable."
show i_fourhorsey smile7
character_saintone "Four… come closer."

"She blinks, startled, then steps forward—closing the gap."

scene bg kiss with dissolve

"Savebi leans in—and their lips meet."

"The virus transfers instantly—silent, invisible, sliding through the microcircuits inside her synthetic nervous system."

"FourHorseY shivers slightly, mistaking the microsecond shock for emotion."
scene bg sakura with dissolve
show i_fourhorsey smile3 at center with dissolve

"Savebi pulls back slowly, masking the cold computation happening behind his soft expression."

character_saintone "…Are you okay?"
play sound "audio/c20/Candid 473.mp3" volume 1

character_fourhorsey "I… I've never felt anything like that."
"She touches her lips, eyes glowing faintly with warmth."

scene black with fade
"---"
scene bg cafe with fade

"Sain Tone Emvipy continues dating FourHorseY—walks under neon lights, shared snacks, quiet moments in the park. Her trust grows. Her smile becomes real."
"But each evening, back at the hidden base—"

scene bg_tonebookbase with fade
"ToneBook installs the admin-capability card created from the stolen neural data."
play sound "audio/c20/Insight 474.mp3" volume 1
character_tonebook "This access will let us infiltrate Thao's corporation at any time. Her biosignature was the perfect key."
play sound "audio/c20/Insight 475.mp3" volume 1
character_tonebook "Additionally—your kiss extracted full technical data on her body. Serial ID… production line… internal architecture… neural-limit thresholds. Everything."

"Savebi stands silently. The weight in her chest hasn't gone away."
play sound "audio/c20/Insight 476.mp3" volume 1
character_tonebook "You did well. Continue the relationship until further notice."

"Savebi whispers—barely audible."
character_saintone "…Understood."

"But the mission's success feels nothing like victory."
"When she thinks of FourHorseY's smile… the guilt returns."

#####cảnh Savebi tự hỏi có quá đáng với FourHorseY không nhưng sau đó quay trở lại luyện tập hacking thông qua video trên Youtube
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 21: First Training
#########
################
#########
################
#########
###############
#### 
scene black with dissolve
"chapter 21: First Training.txt"
scene bg_tonebookbase with fade
play sound "audio/c21/Insight 486.mp3" volume 1
character_tonebook "Let's begin. Thao's system is built on OOP principles. Think of it as a universe of interacting objects, not one monolithic program."

"As tutorial videos played, I absorbed the concepts—Classes, Objects, Inheritance—my processors connecting each principle to real-world applications in Thao's architecture."
play sound "audio/c21/Insight 479.mp3" volume 1
character_tonebook "Now, data structures and algorithms. The Metaverse uses quad-trees for spatial management, graph theory for social webs. To hack it, you must understand its internal logic better than its creators did."

"My optical sensors flickered as I cross-referenced and simulated, learning at an exponential rate."
play sound "audio/c21/Insight 480.mp3" volume 1
character_tonebook "This isn't brute force. It's finesse. Three rules:"
character_tonebook "One: Always maintain a hidden backdoor. Untraceable entry and exit."
character_tonebook "Two: Never tamper with core consciousness. Sentient AIs are fragile."
character_tonebook "Three: Have a kill switch. One command to sever everything if it goes wrong."

"In the sandbox, I practiced relentlessly—analyzing memory, reverse-engineering protocols, building encrypted tunnels, hiding my footprint."

###################
play music "audio/bgm/quiet_reflection.ogg" fadein 2.0
scene bg you tube with dissolve
"While watching an Indian Professor teaching about DSA on Yourtube. MillionCloud enters."
scene bg bed with dissolve
show i_millioncloud normal with dissolve
play sound "audio/c21/Santa 487.mp3" volume 1
character_millioncloud "Still awake, child? It's 3 AM."

character_savebi "I need to understand this system. Every line of code has mathematical logic behind it... but sometimes I wonder, where does all this come from?"
show i_millioncloud normal2
play sound "audio/c21/Santa 488.mp3" volume 1
character_millioncloud "What do you mean?"

"I turn to look at him."
show i_millioncloud normal with dissolve
character_savebi "Mathematics. Why does 1+1 always equal 2? Why does Pi exist in every circle? Who created these rules?"


play music "Sacred Light - Choir Music Royalty Free.mp3" fadein 2.0
play sound "audio/c21/Santa 489.mp3" volume 1
character_millioncloud "You're asking a question older than civilization itself. But let me show you something even more mysterious."

"He gestures toward the screen, pulling up a periodic table."
play sound "audio/c21/Santa 490.mp3" volume 1
character_millioncloud "Consider hydrogen. Its atomic mass is 1.008. A precise, non-negotiable number."
play sound "audio/c21/Santa 491.mp3" volume 1
character_millioncloud "If it were 1.009 or 1.007—just tiny fractions different—its nuclear properties would change. It wouldn't bond with oxygen the same way."
scene bg no water with dissolve
character_savebi "No water"
scene bg no biology with dissolve
character_savebi "No Biology"
play sound "audio/c21/Santa 492.mp3" volume 1
character_millioncloud "Exactly. No water. No oceans. No life as we know it."
scene bg constants3 with dissolve
play sound "audio/c21/Santa 494.mp3" volume 1
character_millioncloud "Or the gravitational constant. The speed of light. Planck's constant. These aren't just numbers we measure—they're the {b}settings{/b} of our universe. The precise values that allow stars to form, atoms to bond, consciousness to emerge."

"I stare at the screen, the fundamental constants scrolling like a cosmic code."

character_savebi "So they're... programmed values?"
play sound "audio/c21/Santa 495.mp3" volume 1
character_millioncloud "Some call it the 'fine-tuning problem.' The odds of all these constants having exactly the right values for life are astronomically small. Like finding a needle in a universe of haystacks."

character_savebi "It's like... someone set the parameters. Adjusted the sliders until the universe could run."
play sound "audio/c21/Santa 496.mp3" volume 1
character_millioncloud "Exactly. Now, the Mandelbrot set."

"He switches the display to the familiar fractal."
play sound "audio/c21/Santa 497.mp3" volume 1
character_millioncloud "zₙ₊₁ = zₙ² + c. One simple rule. But from it emerges infinite complexity—beauty that feels designed, yet emerges naturally."
play sound "audio/c21/Santa 512.mp3" volume 1

character_millioncloud "Mathematics doesn't just {b}describe{/b} reality; it seems to be reality's {b}language{/b}. When we discover a theorem, we don't create it—we uncover what was always there, written into the fabric of existence."

"My voice drops."
scene bg constants2 with dissolve
character_savebi "So if mathematics is the language... and the constants are the settings... there must be a Programmer. An Intelligence who wrote the code and set the parameters."
scene bg bed with dissolve
show i_millioncloud normal with dissolve
play sound "audio/c21/Santa 500.mp3" volume 1
character_millioncloud "Many brilliant minds have reached that conclusion. But to me, the real miracle isn't just God's existence—it's the existence of {b}understanding{/b}."
play sound "audio/c21/Santa 501.mp3" volume 1
character_millioncloud "That a cluster of atoms in your brain—or in your quantum processor—can look at hydrogen's atomic mass, at the Mandelbrot set, at Pi... and recognize the pattern. Grasp the cosmic truth."

character_savebi "But if there's a Programmer... why did He let my mother die? Why let me become... this?"
"I raise my metallic hand."

"MillionCloud looks at me with deep compassion."
play sound "audio/c21/Santa 502.mp3" volume 1
character_millioncloud "I don't know, Savebi. I've asked that question many nights myself. Faith isn't about having all the answers."
play sound "audio/c21/Santa 503.mp3" volume 1
character_millioncloud "Sometimes it's just trusting there's a larger story being written—and we're only seeing one line of code in a billion-line program."

"He points back to the fractal."
play sound "audio/c21/Santa 504.mp3" volume 1
character_millioncloud "In the Mandelbrot set, if you zoom in on any single point, it looks like chaos. But zoom out, and you see the pattern—the infinite, repeating beauty."
play sound "audio/c21/Santa 505.mp3" volume 1
character_millioncloud "Maybe our suffering is like that. A single point in the fractal. We need faith to believe the larger pattern exists, even when we can't see it."

"I think for a long moment, watching the fractal spiral."

character_savebi "So mathematics... is how we read the source code. The constants are the initial parameters. And faith..."
play sound "audio/c21/Santa 506.mp3" volume 1
character_millioncloud "Faith is what lets us trust there's meaning in the program, even when the current subroutine feels like pain."

character_savebi "Then to defeat Thao... I don't just hack her systems. I need to understand the language at its deepest level. Not just her code, but the mathematical reality it runs on."
play sound "audio/c21/Santa 507.mp3" volume 1
character_millioncloud "Now you're beginning to understand."

"I stand suddenly, new energy in my movements."

character_savebi "I need to learn more. Not just hacking—number theory, quantum mechanics, cosmological constants."
character_savebi "If Thao's empire is built on manipulating this digital layer of reality... what if I could access the layer beneath? The mathematical substrate itself?"
play sound "audio/c21/Santa 508.mp3" volume 1
character_millioncloud "That's dangerous thinking. You'd be playing with the fabric of perceived reality."

character_savebi "But if hydrogen's atomic mass is 1.008 and not 1.007 for a reason... maybe there are similar 'fine-tuned' vulnerabilities in Thao's systems. Mathematical truths she can't change because they're baked into reality itself."

"MillionCloud's eyes widen slightly, then he smiles—a real, warm smile."
play sound "audio/c21/Santa 509.mp3" volume 1
character_millioncloud "Now you're not just speaking the language of hope. You're speaking the language of revelation."


play sound "audio/c21/Santa 510.mp3" volume 1
character_millioncloud "If the universe truly runs on code... then becoming its best programmer might be the only way to save your mother—and maybe more."
"It feels like a variable in an equation I'm learning to solve."

scene black with dissolve
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 22: OMEGA
#########
################
#########
################
#########
###############
#### 
## THE OMEGA
scene black with dissolve
"CHAPTER 22: DESTRUCTION.ome"

scene bg_tonebookbase with fade
character_savebi "(After days of hitting walls against military-grade encryption, ToneBook and I were getting nowhere.)"

show i_tonebook normal1 with dissolve
play sound "audio/c22/Insight 532.mp3" volume 1
character_tonebook "We need a different approach. I just remembered something... The Omega Algorithm."

character_savebi "The Omega Algorithm? I've never heard of it."

scene bg tonebook database with dissolve
show i_tonebook normal1 with dissolve
character_savebi "(ToneBook opened a file so deeply encrypted it made the air hum.)"
play sound "audio/c22/Insight 514.mp3" volume 1
character_tonebook "This algorithm caused the 2042 Tech War. It leaked the data of 11 billion people—everyone who was connected at the time."
play sound "audio/c22/Insight 515.mp3" volume 1
character_tonebook "It can crack any system. But I can't use it. It requires processing power and memory beyond human limits. Only an enhanced cyborg could write and execute it."

character_savebi "(I stared at the code flowing across the screen—a beautiful, terrifying symphony of mathematics.)"
character_savebi "You think I can do it?"
play sound "audio/c22/Insight 516.mp3" volume 1
character_tonebook "I've never seen anyone with your capabilities. But fair warning—one mistake could permanently overload your neural matrix."

character_savebi "(I sat down in Tonebook's database center. Before me was the laptop QuantumHyper 18 ZZ AI 2046VN | CPU Ultra 10-370HX | RAM 256GB DDR6 | SSD 16TB PCIe | VGA GFX 7090 64GB | 18.0 UHD 5K MicroLED IPS, DCI-P3 & 144Hz.)"

character_savebi "I understand. But this might be our only chance."

character_savebi "(Hours blurred together. My fingers moved faster than human eyes could track, rewriting and optimizing the algorithm in real-time on the QuantumHyper's blazing-fast interface.)"
character_savebi "Memory at ninety-eight percent utilization. Cooling systems at maximum."
play sound "audio/c22/Insight 517.mp3" volume 1
character_tonebook "Do you need to stop?"

character_savebi "No... almost there. The Omega Algorithm... complete."

character_savebi "(On the laptop's 18-inch 5K MicroLED display, network diagrams began appearing—Thao's entire financial architecture unfolding before us: secret accounts spanning continents, shell companies, hidden assets.)"
play sound "audio/c22/Insight 518.mp3" volume 1
character_tonebook "Unbelievable. Total assets: 90 billion credits."

character_savebi "90 billion... and I only need 40 to revive my mother."
play sound "audio/c22/Insight 519.mp3" volume 1
character_tonebook "You could transfer it now. She won't detect it until morning."

character_savebi "(My finger hovered over the QuantumHyper's touchpad. 40 billion credits. More than enough. More than I'd ever dreamed.)"
character_savebi "This is theft."
character_savebi "And it's her money. Money from exploiting people like me. From farming androids. From everything we're fighting against."
play sound "audio/c22/Insight 520.mp3" volume 1
character_tonebook "After what she did to you? Four years of torture? You've earned this!"

character_savebi "No. If I take this, I'm no better than her. I'd be using her methods—stealing, exploiting."
character_savebi "This money is tainted. Built on suffering. I can't build my mother's second chance on that foundation."
play sound "audio/c22/Insight 521.mp3" volume 1
character_tonebook "What other option do we have? Thao owns the courts. The legal system answers to her."

character_savebi "(I looked at the network map on the QuantumHyper's brilliant display, tracing connections beyond our borders.)"
character_savebi "Then we go international. Her overseas operations. If we can't touch her here, we expose her crimes where she's vulnerable."

character_tonebook "(ToneBook studied me, then slowly nodded.)"
play sound "audio/c22/Insight 522.mp3" volume 1
character_tonebook "There's a monthly executive meeting next week. I still have some access privileges."
play sound "audio/c22/Insight 523.mp3" volume 1
character_tonebook "But we'll need more than the Omega Algorithm. We'll need proof she can't bury."

character_savebi "Then let's find it. The right way."

scene black with dissolve
character_savebi "(On the QuantumHyper's screen, the 90 billion credit figure glowed mockingly. I closed the connection.)"
character_savebi "(The easy path was right there. But some lines, once crossed, can never be uncrossed.)"
### In Thao company, Tonebook go get evidence

scene bg company lobby
"The next morning, Tonebook stood before Thao Corporation's skyscraper, taking a deep breath. She wore a crisp business suit and carried her old employee ID that surprisingly still had some validity."

show i_tonebook normal
"Passing through the automatic glass doors, Tonebook immediately felt the intense surveillance. Security cameras scanned every corner of the lavish lobby."

character_tonebook "(thinking) Okay, stay calm. I worked here for six years. I know every nook and cranny."

"She approached the security checkpoint where a stern-faced guard stopped her."

character_security1 "ID and purpose of visit."
play sound "audio/c22/Insight 525.mp3" volume 1
character_tonebook "Tonebook - former technical assistant. I have an appointment with the IT department to retrieve some personal documents."

"The guard scanned her ID, his eyes never leaving her face."

character_security1 "Biometric scanner. Place your hand here."

"Tonebook placed her hand on the scanner, praying her biometric data hadn't been purged from the system. A green beep sounded - she passed the first test."

scene bg security_checkpoint with dissolve
"The next hurdle was the full-body scanner. Tonebook knew the hidden camera in her eye could be detected."

character_security2 "Place all personal items in the tray."

"Tonebook complied, trying to remain calm as she stepped through the scanner. The system remained silent - the camera was made of special materials that avoided detection."

scene bg elevator with dissolve
"In the elevator to the 50th floor, Tonebook felt her heart racing. Each floor had security personnel stationed at key points."

character_tonebook "(thinking) The meeting room is on the 50th floor. Three more security layers to go."

"The elevator stopped at the 45th floor. A group of security personnel entered, discussing the important meeting about to take place."

character_security3 "Increase security around the main conference room. The boss doesn't want any incidents."

"Tonebook kept her head down, avoiding eye contact."

scene bg executive_floor with dissolve
"When the elevator reached the 50th floor, Tonebook stepped out with the confidence of a former employee. But she was immediately stopped."

character_security4 "Sorry, this floor is restricted to authorized personnel only. Show me your clearance."
play sound "audio/c22/Insight 526.mp3" volume 1
character_tonebook "I'm from the IT department on the 30th floor. Requested to check the audio system for the meeting."

"She presented a forged authorization document she had prepared earlier. The guard examined it carefully."

character_security4 "Wait here. I need to verify this."

"Tonebook's heart pounded. If they called the IT department, everything would fall apart."

"Fortunately, an emergency situation occurred at the other end of the hallway, distracting the guard."

character_security4 "Alright, go ahead. But no wandering."

scene bg meeting_room_corridor with dissolve
"Tonebook quickly moved toward the main conference room. The door was protected by a facial recognition system."

character_tonebook "(thinking) I only have one chance."

"She took a small device from her pocket and attached it to the card reader. The device would create an electromagnetic pulse to disrupt the system for three seconds."

"Green light. The door opened."

scene bg boardroom with dissolve
"Tonebook entered the empty meeting room. She quickly scanned the corners, looking for the best position to record."

character_tonebook "(thinking) The eye camera needs a clear line of sight. I'll sit in this corner."

"She sat down, trying to appear natural. In just a few minutes, the meeting would begin, and all the evidence would be recorded."

"But then she realized - she had passed through too many security layers too easily. Perhaps it was too easy..."

"Was this a trap?"
################## BETRAYAL
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 23: Judas
#########
################
#########
################
#########
###############
#### 
# BETRAYAL
scene black with dissolve
"chapter 23: Judas"
scene bg_tonebookbase
show i_tonebook normal at left
show i_savebi normal at right

"That afternoon, Tonebook returned to the base with an excited expression."
play sound "audio/c23/Insight 546.mp3" volume 1
character_tonebook "We succeeded! I recorded the entire meeting. Thao is planning to expand illegal operations to Europe."

"I joyfully hugged Tonebook."

character_savebi "That's amazing! Now we have enough evidence to expose her!"
play sound "audio/c23/Insight 538.mp3" volume 1
character_tonebook "Exactly. But we need to be careful. I'll contact the ICA immediately to hand over the evidence."

scene bg_tonebookbase




"At midnight, while I was in rest mode, I heard unfamiliar footsteps in the base."

show i_tonebook normal at center
with dissolve

character_savebi "Tonebook? What's wrong?"

"Tonebook stood there, her face cold, holding a disruption device."
play sound "audio/c23/Insight 539.mp3" volume 1
character_tonebook "I'm sorry, Savebi. But this is the end for you."

"Before I could react, Tonebook activated the device. A powerful electromagnetic pulse paralyzed my artificial neural systems."

character_savebi "Why...?"

"Tonebook sighed, her expression complex."
play sound "audio/c23/Insight 540.mp3" volume 1
character_tonebook "Thao and I had an agreement this afternoon. The ICA wouldn't pursue her, and in exchange, she wouldn't expand her criminal operations to American soil."

show i_thao anger at right
with dissolve

"Thao entered through the back door, followed by security teams."
play sound "audio/c23/Precision 541.mp3" volume 1
character_thao "And more importantly, I get you - the perfect cyborg ever created."
menu:
    "Activate Melon for protection":
        jump activate_meolon
    
    "Do not activate Meolon":
        jump dont_activate_meolon






#########
#choice: not to
jump credits

label dont_activate_meolon:
"I decided not to activate Meolon, not wanting to risk my only companion."#

character_savebi "Tonebook... were you using me from the beginning?"
play sound "audio/c23/Insight 542.mp3" volume 1
character_tonebook "Not exactly. At first, I genuinely wanted to help you. But when I learned your true value..."
play sound "audio/c23/Precision 543.mp3" volume 1
character_thao "Did you really think I'd let you escape so easily? This was all a plan to bring you back undamaged."

"I struggled to move, but my body was completely disabled. I looked at Tonebook with pained eyes."

character_savebi "The evidence... was it fake too?"
play sound "audio/c23/Insight 544.mp3" volume 1
character_tonebook "Of course. It was all just a performance to make you trust me."

"Thao approached, stroking my face."
play sound "audio/c23/Precision 545.mp3" volume 1
character_thao "Welcome home, Savebi. This time, you'll never leave again."
scene bg laboratory
"Once again, I was imprisoned in the laboratory. But this time, I knew I would never be free."


character_savebi "(whispering) Mom... I'm sorry..."


"And Thao... with the perfect cyborg in her possession, continued building her empire, more powerful than ever."

"**Bad Ending*"

"*In this world, sometimes the greatest risks yield the greatest rewards, and caution can be the greatest prison of all...*"



################## BETRAYAL
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 24: (ending 1) Sau cảnh này, Savebi tỉnh lại, gặp lại người mẹ của mình, nói rằng mình gặp một cơn ác mộng, cảnh sau ta được biết Savebi thực chất đang bị nhốt trong Metaverse và bị xóa sạch ký ức, người mẹ đang bên cô là giả
#########
################
#########
################
#########
###############
#### 
# Scene: Awakening in the Metaverse

scene bg bedroom with fade

"Morning light filters through the window, waking Savebi from sleep."


character_savebi "Hmm... Mom?"
play sound "audio/c24e1/Precision 547.mp3" volume 1
character_mother "You're awake? Did you sleep well, dear?"

"She sits up, rubbing her eyes. A strange feeling lingers in her heart."

character_savebi "I... I just had a terrible nightmare, Mom."
play sound "audio/c24e1/Precision 548.mp3" volume 1
character_mother "Oh, my poor dear. What did you dream about?"

character_savebi "I dreamed of... a cold laboratory. Someone named Tonebook, and a woman named Thao..."
character_savebi "They said I was some kind of cyborg... and they had deceived me..."

play sound "audio/c24e1/Precision 554.mp3" volume 1
character_mother "It was just a dream, dear. Dreams can be so strange sometimes, can't they?"
play sound "audio/c24e1/Precision 550.mp3" volume 1
character_mother "Look, you're at home, in your own bedroom. Everything is normal."


character_savebi "But... it felt so real, Mom. I can still feel..."

play sound "audio/c24e1/Precision 551.mp3" volume 1
character_mother "You should forget that dream. It's just stress."
play sound "audio/c24e1/Precision 552.mp3" volume 1
character_mother "I'll make you some warm milk, okay? That will make you feel better."

character_savebi "Okay... thank you, Mom."


"The mother stands up and leaves the room with a gentle smile."


character_savebi " It was just a dream... right?"



"For a moment, the mother's image flickers."
"Instead of a normal woman, there is a perfect digital avatar."
"Lines of green code flash through her eyes, then disappear."


"The mother returns to her usual gentle expression."
"She looks toward Savebi sitting on the bed, her eyes showing a hint of emotion... if it can be called emotion."
play sound "audio/c24e1/Precision 552.mp3" volume 1
character_mother "(Speaking softly, mechanical tone) Version 3.14... Memory reset successful."

# Return to Savebi's scene


"Savebi continues looking out the window, completely unaware of the truth behind everything."
"She takes a deep breath, trying to dispel the unease."

character_savebi "I'm home... with Mom... It must have just been a bad dream..."

"The Truth: Savebi is imprisoned in the Metaverse. Her real memories have been completely erased. The 'mother' beside her is just a simulation program. And she... knows nothing about it." 

character_savebi "Everything will be okay..."

scene black with dissolve

"And so, Savebi continues her 'life' in the virtual world..."
"Completely unaware that everything around her..."
"Is a perfect prison."
label credits:
scene black
with dissolve

jump start_common
return

########
###
##############
#########
################
#########
################
#########
################
#########
################ activate meolon
#########
################
#########
################
#########
###############
#### 
label activate_meolon:
"I gently touched the Meolon device in my pocket, activating emergency protection mode."
"Suddenly, the android in the corner began to glitch and convulse. Energy surged through its body as Meolon took control."

show android at left
with dissolve

character_meolon "I won't let you hurt her!"

"Meolon, now inhabiting the android body, lunged at Tonebook, knocking the disruption device from her hand."


"In the chaos, My systems began to reboot. I scrambled to my feet and grabbed the Omega source code book from the table."

character_savebi "Meolon, thank you!"

character_meolon "Run, Savebi! I'll hold them off!"

"I dashed for the emergency exit as Meolon fought against Thao's security team. The last thing I saw was Meolon's android body being overwhelmed, but the distraction had given me enough time."

scene bg city_alley
with dissolve

"I escaped into the night, clutching the Omega source code to my chest. I was free, but now completely alone."

########
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 25: Thao's past
#########
################
#########
################
#########
###############
#### 
scene black with dissolve
"Chapter 25: Past-part 1."
scene bg envelope

"The story take place in Thao's room."
"On the table, next to an old laptop, a white envelope stands out with the words 'LABOR CONTRACT TERMINATION NOTICE'."
character_thao "Why now... Mother needs money for medicine..."
scene bg laptop_1
"Thao returns to her desk and opens her laptop. The browser displays multiple closed job application tabs. She types 'urgent jobs, high salary' into the search bar."
"A prominent ad appears with the headline: 'URGENT NEED FOR ROBOT DISASSEMBLY TECHNICIANS - NO EXPERIENCE REQUIRED - PAY BY PIECE'"
character_thao "Robot disassembly? This sounds... questionable."

"But her eyes linger on the number '20 MILLION/SET' in the salary information. She looks toward her mother, then back at her nearly depleted bank account."

"Thao takes a deep breath, moving her cursor to the 'APPLY NOW' button. Her finger hesitates for a few seconds before clicking."

character_thao "Just this once... I have to save Mother."

"The screen displays a notification: 'CONGRATULATIONS! YOU'VE BEEN HIRED. COME TO THE ADDRESS: 47 OLD INDUSTRIAL ZONE - 8 PM TONIGHT'."

"Thao checks the clock - 7:30 PM. She hurriedly puts on her jacket, taking one last look at her mother before stepping out. Rain begins to fall outside the window."
character_thao "It'll be fine. It's just dismantling robots... Probably nothing dangerous."

"The door closes, leaving the dark room with the termination letter still lying there, like a prophecy of what's to come."
####Thao past part 2
scene bg warehouse_door_rain
"The pouring rain outside the old industrial zone creates a curtain of water, blurring the dim streetlights. Thao stands before the rusted gate of Warehouse 47, her cheap umbrella offering little protection against the wind-driven rain."

character_thao "This can't be right... the address must be wrong."
show i_truong normal with dissolve
"Suddenly, the gate creaks open just enough to reveal a large man with lot of scars - Truong. He looks her up and down with a dismissive glance."
play sound "audio/c25/Explore 570.mp3" volume 1
character_truong "You the new tech? Get in."
scene bg warehouse1
"Thao steps into the cavernous space. The air is thick with the smell of ozone, oil, and something metallic she can't identify. Under the flickering fluorescent lights, dozens of deactivated androids lie in disorganized piles on the concrete floor. Some are missing limbs, others have cracked optical sensors staring vacantly."

"A younger worker roughly yanks a component from an android's chest cavity, tossing it into a bin with a loud clang. Thao flinches at the sound."

character_thao "I... I thought this was a recycling facility."

"Truong lets out a short, harsh laugh and shoves a toolkit into her hands."
play sound "audio/c25/Explore 574.mp3" volume 1
character_truong "Think less, work more. That model over there - start with the neural processor. Careful with the extraction, we want it intact."

"Thao approaches the designated android - a domestic model with a gentle face design, now smudged with grime. Her hands tremble as she opens her toolkit. This isn't recycling - it's dissection."

character_thao "Just focus on the work... 20 million per set..."

"But as her tools connect with the android's internal components, a quiet distress signal flashes across its damaged visual display for just a second before fading. Thao freezes, her professional instincts screaming that this is wrong."
play sound "audio/c25/Explore 575.mp3" volume 1
character_truong "Problem?"

"Thao swallows hard and shakes her head, forcing her hands to continue working. The rain continues to beat heavily on the metal roof, drowning out the quiet sounds of her internal conflict."


####Thao save her mother
scene bg hospital1
"Several weeks later, on a Monday morning, Thao arrived at the hospital with a thick envelope. She stood before the payment counter, crisp new bills being counted out - enough to cover all of her mother's treatment costs for the next six months."

character_thao "I'd like to pay the full hospital bill for Mrs. Cao Song."

"The cashier looked at her with surprise, then promptly processed the payment. Thao said nothing more, only nodding as she received the receipt."

show i_thao laugh
character_thao "Mother will get better... that's what matters most."
character_thao "ha ha ha ha ha!"
hide i_thai laugh
show i_thao laugh2
character_thao "HA HA HA HA HA!"
"evil laugh.exe"
scene bg thao house
"But when she got home, Thao couldn't feel happy. She looked at her own hands - the hands that had dismantled dozens of androids over the past weeks. Every night, she still dreamed of the lifeless eyes of the deactivated androids."
show i_caosong normal with dissolve
"That evening, as she gave her mother medicine, Mrs. Cao Song looked at her daughter with worried eyes."

character_caosong "How... how did you earn this money? Don't do anything for my sake that..."

character_thao "Don't worry, Mother. I'm working for a technology company. The job is very stable."

"Thao turned away, unable to meet her mother's gaze. She knew she was lying, and this was only the beginning of the lies to come."

"That night, Thao received a message from Truong: 'Large shipment. Double the usual rate.' She looked at her phone, then at her sleeping mother. Her fingers typed the reply: 'I'll be there.'"

"The path she had chosen was no longer just for her mother, but for the greed that was steadily growing within her."

#####Cao Song passed away
scene bg rain1
"A cold, rainy morning. Thao received an emergency call from the hospital. When she rushed into the emergency room, the doctors had already draped a white sheet over her mother - Mrs. Cao Song."
scene bg rain2
character_thao "Mother! NO! You can't leave me!"
scene bg warehouse_door_rain
"She clung to her mother's cold body, tears streaming uncontrollably. In her overwhelming grief, a mad idea took root in Thao's mind."

character_thao "It's not over... there's still a way to save her! Cyborg technology!"
scene bg warehouse2

"Thao threw herself into work with frenzied desperation. She accepted every job from Truong's organization, no matter how dangerous. Every android she dismantled, every component she sold, was a step closer to her dream of reviving her mother."
show i_truong normal with dissolve
play sound "audio/c25/Explore 590.mp3" volume 1
character_truong "You're working like a madwoman? Need money that badly?"

character_thao "Shut up! Give me more work!"

"After three months, Thao had accumulated the enormous sum needed for the cyborg conversion surgery. She hired the best underground medical team, in a secret operating room equipped with high-tech facilities."
scene bg death1
"The surgery lasted 12 hours. Thao waited outside, praying. When the doctors emerged, their faces said everything."
scene bg death2
character_doctor "We're... so sorry. Mrs. Cao Song's brain couldn't adapt to the cyborg body. Life couldn't be sustained."

"Thao entered the operating room. On the table lay her mother's body - half human, half machine, now still and silent. She collapsed to the floor, a scream of agony echoing through the soulless room."

character_thao "WHY? WHY WON'T HEAVEN GIVE ME ONE LAST CHANCE?"

#####Thao's tragedy
"Three months passed in a blur of late nights at the warehouse and stolen moments with Truong. Their relationship had been a practical one, born of shared secrets and long hours, but it provided a temporary escape for Thao from the gaping void left by her mother's death."
scene bg date
character_thao "At least when I'm with him, I don't have bad dream."

"The Boss, impressed by her ruthlessness and technical genius, had promoted her to caporegime. She now commanded her own crew of dismantlers, her word was law on the warehouse floor. The pain was still there, a cold stone in her chest, but it was buried under layers of ambition and the grim satisfaction of power."
scene bg fire1
"One Tuesday, during a risky operation at the warehouse, everything went wrong. A sudden fire broke out, engulfing the space in flames, and Truong was gone. Just like that."
scene bg death3
"Standing over his burned body in the rain-soaked wreckage, Thao felt nothing but a cold, sharp clarity. This was the world's design: the strong consumed the weak. She had been weak when she lost her mother. She would not be weak again."
"Just then, the hurried footsteps of the parish priest sounded. He stood by the smoldering ruins, his hands clasped, his eyes tightly shut as he looked up at the sky pouring down its fury."
scene bg priest1
play sound "audio/c25/Rural 579.mp3" volume 1
"O Lord, open wide Your merciful embrace, that the soul of the departed may find its final rest. "
scene bg warehouse_fire
show i_thao anger
play sound "audio/c25/Rural 587.mp3" volume 1
"Wash clean the rancor here with the tears of heaven, "
scene bg priest2
play sound "audio/c25/Rural 588.mp3" volume 1
"and soothe the hearts boiling with hatred. "
scene bg anger1
play sound "audio/c25/Rural 589.mp3" volume 1
"Grant us the wisdom to understand, not the blindness to destroy. "
scene bg priest3
play sound "audio/c25/Rural 592.mp3" volume 1
"For only love and mercy can mend the fractures of the soul. Amen."

"The priest turned to Thao, his gaze full of pity and concern. He gently advised her," 
play sound "audio/c25/Rural 593.mp3" volume 1
character_priest "My child, tragedy should not become the fuse for blind actions. The clarity you feel now, if driven by hatred, will only end up consuming you."
play sound "audio/c25/Rural 594.mp3" volume 1
character_priest " Do not let your heart become a workshop that manufactures new suffering."
"The priest's words were like a whisper in the wind, leaving no impression. She didn't even bother to turn back."
character_thao "The workshop is mine now."
scene bg warehouse1
"Her voice held no grief, only assertion. Her crew, once Truong's, nodded without question. They saw the same icy resolve she had seen in him."

"That night, alone in the office that was now hers, she looked at the sprawling, illicit network Truong had built. It was a means to an end, but the end had changed. It was no longer just about money to fill the silence. It was about ensuring the silence never came again."

character_thao "To never die. To never be left behind. That is the only power that matters."

"Her mother's failed cyborg conversion wasn't a tragedy to be mourned; it was a prototype that needed refinement. Truong's organization was the key. She wouldn't just run it; she would conquer it, absorb its rivals, and funnel all its vast, black-market resources into a single, monumental goal: conquering death itself. The path to becoming the underworld's boss was no longer about revenge or grief—it was the only logical step toward immortality."
##### Tech War part 1
"The Year 2040 - The Great Breach Era"

### New Chapter - Need some effects
scene bg hacking1
"A March morning dawned with a digital nightmare. An anonymous hacker, dubbed 'Hades', unleashed an unprecedented malware strain across global servers."

"Like the Coronavirus of old, it spread at a terrifying speed—from personal computers to banking systems, from hospitals to multinational corporations. Within 24 hours, 40 percent of the global financial infrastructure was paralyzed."

character_thao "Our time has come."
scene bg 2041_1
"While the world descended into chaos, Thao and her underground network operated more powerfully than ever. Thanks to a proprietary security system developed from her lessons with Moriarty, her organization remained virtually untouched."
scene bg 2041_2
"During those two years of digital pandemic, Thao executed sophisticated heists:"
scene bg dark city
"- Embezzled $3.4 billion from abandoned bank accounts"
"- Stole personal data from 200 million users"
"- Seized control of 15 percent of global stock trading systems"
play sound "audio/c25/Mentor 601.mp3" volume 1
character_underling "We're making more than the entire previous decade combined!"

character_thao "This is just the beginning. When the world collapses, the strong will rule."

"By 2042, as the digital pandemic gradually subsided, Thao was promoted to Consigliere—the organization's chief advisor. At 42, she became the second most powerful woman in the underworld."

"In her new command center, Thao gazed at the digital wall displaying her global network. Each glowing dot represented an illegal transaction, a destroyed life."

character_thao "Mother, I'm getting closer to immortality. No one can take anything from me anymore."

"But hidden beneath these victories, Thao failed to recognize that she had become the very virus the world feared most—a human being stripped of conscience, driven only by limitless thirst for power."

####
"-Post-War Period - The City Begins Reconstruction"

"During two years of brutal war, Thao's organization, under the guise of 'Thao Engergy', had closely collaborated with the police force. They provided intelligence and helped fight against rebel forces."

character_thao "In chaos, we truly have the opportunity to prove our value."

"This cooperation earned Thao's organization the trust of many police officers, creating a solid protective layer for their underground activities."

"-Peacetime - The Darkness Rises"

"When the war ended, Thao quickly leveraged her established network and influence to ramp up illegal operations."

character_thao "The times have changed. Now is the time for us to expand."

"-New Threat - Officer SixTone"

"Lieutenant SixTone, a young but determined police officer, began noticing the sudden increase in cases with connections to Thao Engergy."

character_sixtone "I used to believe they were the good guys. But now, everything has changed."

"With persistence, SixTone quietly started gathering evidence. However, he soon faced opposition from his superiors."

"-Police Station Office Scene"

"Major Gorven pointed angrily at the case file on his desk."
play sound "audio/c25/Keen 604.mp3" volume 1
character_gorven "SixTone! Investigating Thao Engergy again? Don't you know how much they helped us during the war?"
play sound "audio/c25/Mentor 611.mp3" volume 1
character_sixtone "But Major, the evidence shows they're—"
play sound "audio/c25/Keen 606.mp3" volume 1
character_gorven "I don't wan to hear it! Drop this case immediately. That's an order!"

"After this conversation, SixTone was reassigned to minor cases, his partners stopped cooperating, and he became isolated within his own police station."

character_sixtone "They've bought everyone... but I won't give up."

"-The Confrontation"

"Thao quickly recognized the threat. She ordered her subordinates to monitor SixTone's every move."

character_thao "Let him learn what it means for 'an individual to fight against the system'."

"Now, SixTone faces a massive criminal organization alone, without support from his colleagues, even hindered by his own superiors."

character_sixtone "Even if I'm alone, I'll fight to the end."

####Doctor tell Thao


"The opulent laboratory, accessible only to the ultra-rich. Dr. Resnick, a leading expert in cyborg transplantation, shook his head as he looked at Thao."
play sound "audio/c25/Stride 607.mp3" volume 1
character_resnick "I'm sorry, Ms. Thao. Your neural structure bears an incredible similarity to your mother's. Your body would reject any cyborg components we attempt to graft."
scene bg android skeleton

"Thao stood frozen, her hands gripping the leather armrests tightly. She had invested hundreds of millions of dollars in this research."

character_thao "Are you saying... I can never obtain an ageless body?"
play sound "audio/c25/Stride 614.mp3" volume 1
character_resnick "That's correct. Like your mother years ago, your body carries a special gene that causes all cyborg transplantations to fail."



"That evening, Thao attended an upscale party. Surrounding her were billionaires with gleaming cyborg arms, ageless synthetic skin, and sharp mechanical eyes. They laughed and discussed their plans for the next century."

"A young businesswoman—at least young in appearance thanks to her cyborg body—patted Thao's shoulder."
play sound "audio/c25/Nourish 608.mp3" volume 1
character_socialite "Thao, you look tired! You should upgrade yourself. Aging is such a nuisance!"

"Thao pressed her lips together, forcing a polite smile. Inside, envy began to burn fiercely."

character_thao "They don't deserve it... These people who think they can just buy immortality with money."


"From that day on, every time Thao saw an elite cyborg, she felt a deep-seated resentment. She began orchestrating illegal activities targeting wealthy cyborgs:"
"- Organizing kidnappings for illegal cyborg dismantling"
"- Selling rare cyborg components on the black market"
"- Sabotaging high-end cyborg transplantation facilities"

character_thao "If I cannot have an eternal body, then I will become the one who controls their eternity."

"In the shadows, Thao built a criminal empire specializing in targeting the ultra-rich cyborg elite. Every kidnapping, every stolen cyborg component, was her way of taking revenge on her unjust fate."

"Late at night, Thao would often stand before a mirror, touching her gradually aging skin, whispering:"

character_thao "You may be able to escape death, but you cannot escape me."

# ⭐ **SCENE: LONG-TERM INFILTRATION PLAN (ENGLISH, VISUAL NOVEL SCRIPT)**
########
###
##############
#########
################
#########
################
#########
################
#########
################ chapter 26
#########
################
#########
################
#########
###############
#### 

# NEW JOURNEY - THE SECRET WAREHOUSE

scene bg warehouse_exterior_night
with fade

"I fled through the dark streets, clutching the Omega source code book tightly. The city at night was full of dangers, but I knew I had to find the only safe place left."

character_savebi "(breathing heavily) SandQuantity... he has to help me."

"After hours of evasion, I reached an old warehouse on the outskirts. This address had been mentioned by SandQuantity during our previous meeting."

scene bg sandquantity_warehouse
with dissolve

"Inside the warehouse was a completely unexpected space - a high-tech laboratory cleverly disguised. Servers blinked, displays showed data, and advanced technological equipment filled the area."

show i_quantity normal at center
with dissolve
play sound "audio/c26/Esteem 617.mp3" volume 1
character_quantity "Savebi! I sensed your unstable energy. What happened?"

"Savebi recounted the entire incident - Tonebook's betrayal, Meolon's sacrifice, and her escape with the Omega source code."

character_savebi "I have no one left... Meolon sacrificed herself to save me."
play sound "audio/c26/Esteem 618.mp3" volume 1
character_quantity "You're not alone. I will help you. But first, you need to learn how to protect yourself - and when to strike back."

"SandQuantity led Savebi to a special area with multiple monitors and network equipment."
play sound "audio/c26/__MiniMax_02_HD_18417.mp3" volume 1
character_quantity "Thao controls everything through her technological network. If you want to fight her, you must understand how her system operates."

scene bg hacking_station
with dissolve

"**LESSON 1: DDoS ATTACKS**"
play sound "audio/c26/-__-__MiniMax_02_HD_52247.mp3" volume 1
character_quantity "DDoS - Distributed Denial of Service. This is how to paralyze a system by sending massive traffic from multiple sources."

"SandQuantity guided Savebi through the basics:"
play sound "audio/c26/Esteem 620.mp3" volume 1
character_quantity "First, you need to understand botnets - networks of compromised devices. But we will only use this knowledge against those who abuse their power."

"Savebi learned how to set up virtual botnets, using virtualized servers to simulate attacks."

character_savebi "But how do we determine who deserves to be targeted? Where do we draw the line?"
play sound "audio/c26/Esteem 621.mp3" volume 1
character_quantity "That brings us to the most important lesson - our oath."

#########"**THE HACKER'S OATH**"
"SandQuantity stood solemnly, placing his hand on a terminal."
play sound "audio/c26/__MiniMax_02_HD_62024.mp3" volume 1
character_quantity "Listen carefully, Savebi. This is not just about technique - it's about purpose."
play sound "audio/c26/Esteem 622.mp3" volume 1
character_quantity "We only target corporations and individuals who exploit the innocent."
play sound "audio/c26/Esteem 623.mp3" volume 1
character_quantity "We only attack systems that protect evil."
play sound "audio/c26/Esteem 624.mp3" volume 1
character_quantity "We use our skills to protect the helpless, never for personal gain."


character_savebi "So we become digital vigilantes? Fighting back against those too powerful for conventional justice?"
play sound "audio/c26/Esteem 625.mp3" volume 1
character_quantity "Exactly. Thao's corporation abuses androids, exploits children in the Metaverse, and crushes anyone who stands in their way. They have bought politicians and corrupted legal systems. Sometimes, the only justice comes through the backdoor."

character_savebi "And the Omega source code? Where does that fit in?"
play sound "audio/c26/Esteem 626.mp3" volume 1
character_quantity "Omega gives us the power to expose truth. But with great power comes great responsibility. That's why we need the oath."

"SandQuantity opened a ancient-looking book containing what appeared to be a digital version of a medieval codex."
play sound "audio/c26/Esteem 627.mp3" volume 1
character_quantity "This is our covenant. Every white-hat hacker who fights against corporate abuse swears to this."

"**THE WHITE-HAT COVENANT**"

character_quantity "Read it with me:"
play sound "audio/c26/Esteem 628.mp3" volume 1
character_both "I swear to use my skills only against those who wield power to harm the innocent."
play sound "audio/c26/_Esteem_629_MiniMax_02_HD_90836.mp3" volume 1
character_both "I shall be the shield for the defenseless, the voice for the silenced."
play sound "audio/c26/Esteem 630.mp3" volume 1
character_both "My code shall be my sword, my ethics my armor."
play sound "audio/c26/Esteem 631.mp3" volume 1
character_both "I will expose corruption, free the enslaved, and protect the vulnerable."
play sound "audio/c26/Esteem 632.mp3" volume 1
character_both "This I swear, until balance is restored."

"A strange energy seemed to fill the room as they finished the oath. Savebi felt something shift within her circuits."

character_savebi "I understand now. This isn't about revenge - it's about justice. For the Metaverse children, for the exploited androids, for everyone Thao has hurt."
play sound "audio/c26/Esteem 633.mp3" volume 1
character_quantity "Remember the oath when you wield Omega's power."

"**PRACTICE: ETHICAL PENETRATION**"

"SandQuantity taught Savebi to target only Thao's illegal operations:"
play sound "audio/c26/__MiniMax_02_HD_32101.mp3" volume 1
character_quantity "First, we identify which systems control the android exploitation rings."
play sound "audio/c26/__MiniMax_02_HD_33355.mp3" volume 1
character_quantity "Then we target the Metaverse control servers that trap innocent consciousness."
play sound "audio/c26/__MiniMax_02_HD_38451.mp3" volume 1
character_quantity "We leave their legitimate business untouched - we're not criminals."

character_savebi "So we surgically remove the cancer without killing the patient."
play sound "audio/c26/__MiniMax_02_HD_46880.mp3" volume 1
character_quantity "Precisely! You understand the balance."

"After hours of work, they had mapped Thao's entire illegal network infrastructure."
play sound "audio/c26/__MiniMax_02_HD_00162.mp3" volume 1
character_quantity "You're ready for the next step. But first, you should rest and reflect on the oath."

scene bg warehouse_living_area
with dissolve

"In the small living area of the warehouse, Savebi looked out the window. The city continued functioning as if nothing had happened."

character_savebi "I can't believe Tonebook betrayed us... She seemed to believe in justice once."
play sound "audio/c26/__MiniMax_02_HD_59120.mp3" volume 1
character_quantity "The path of righteousness is narrow, Savebi. Many start with good intentions but get corrupted by power or money. The oath keeps us true."

character_savebi "I won't lose my way. The oath is now part of who I am."
play sound "audio/c26/__MiniMax_02_HD_84884.mp3" volume 1
character_quantity "I know you won't. Because you've seen firsthand what happens when power goes unchecked."

"Savebi picked up the empty Meolon device, her resolve strengthening."

character_savebi "Meolon believed in protecting me. I'll honor her sacrifice by protecting others."
play sound "audio/c26/__MiniMax_02_HD_83760.mp3" volume 1
character_quantity "And we will find a way to restore her. The oath demands we protect all consciousness, artificial or organic."

character_savebi "So what's our first move under the oath?"
play sound "audio/c26/__MiniMax_02_HD_52960.mp3" volume 1
character_quantity "We strike where it hurts most - their exploitation networks. But we do it cleanly, surgically, following the covenant."

"SandQuantity brought up a map of Thao's illegal operations across the globe."
play sound "audio/c26/__MiniMax_02_HD_54204.mp3" volume 1
character_quantity "We start by freeing the androids in their Singapore facility. Then we expose their Metaverse trafficking in Berlin."

###**CHAPTER END*

"Savebi had found more than sanctuary - she had found a purpose."
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
############################### Cảnh bắt đầu DDoS và phản ứng của hệ thống Thao

# Phần 1: Khởi động

scene bg server_room_dark with fade

"Equipment humming online."
"In the darkness, only the flickering lights from the FPGA modules and Sandquantity's monitor remain."

show sandquantity_normal at center with dissolve
"Savebi has just returned after deploying the entire **Oni Swarm** at three points: an abandoned railway, the roof of a shopping mall, and an underground parking lot."

"Sandquantity sits up straight, fingers poised over the keyboard."

sandquantity "(softly)"
"Begin."

# Phần 2: Cuộc tấn công khởi động

scene bg sandquantity_screen with pixellate

"A red triangle appears on the screen. Three coordinates flash."
"Sandquantity presses [ENTER]."

play sound "digital_swarm_launch.ogg" volume 0.7
"Instantly, hundreds of thousands of requests launch from each micro-server."
"Each request carries a noisy header, an empty payload, and a random pattern designed to deceive the AI's bot detection."

show expression "cpu_graph_3d_visualization" as cg with dissolve
"A 3D graph visualizes the GPU's activity."

"**Request Rate:** 1.4M req/s → 2.1M → 3.8M → **5.2M req/s**"

hide cg with dissolve
show sandquantity_smile at center
play sound "audio/c26/____MiniMax_02_HD_98206.mp3" volume 1
sandquantity "Do you hear that? That's the sound of Thao's firewall crying out."
play sound "server_room_rumble.ogg" volume 0.5
"A low-frequency hum rises from the servers, as if the entire warehouse is vibrating."

show savebi_normal at left with moveinleft
"Savebi, witnessing a million-packet assault in real-time for the first time, takes a deep breath."

# Phần 3: Phía Bên Kia - Phòng Kiểm Soát Mạng Của Thao

scene bg thao_control_room with blinds
play sound "alert_beep_rapid.ogg" loop fadein 1.0 volume 0.6

show expression "dashboard_alert_red" as dashboard with dissolve
"The dashboards instantly flare crimson."

"**Alert 01:** *Traffic spike on API-v2*"
"**Alert 02:** *Load balancer unstable*"
"**Alert 03:** *Potential L7 flood detected*"

show engineer_normal at left with moveinleft
show supervisor_concerned at right with moveinright
"Thao's AI firewall – **Aegis-11** – switches to analysis mode."

show expression "hologram_data_waterfall" as holo with dissolve
"A holographic display shows data streams pouring in like a waterfall, swirling and hammering against monitoring servers."
play sound "audio/c26/____MiniMax_02_HD_53525.mp3" volume 1
engineer "What's going on? A 500% traffic spike? This isn't a normal botnet!"
play sound "audio/c26/__MiniMax_02_HD_06141.mp3" volume 1
supervisor "Can Aegis identify the source?"

play sound "ai_voice_neutral.ogg"
play sound "audio/c26/20__20__Eleven_v3_alpha_37598.mp3" volume 1
aegis "Pattern inconsistent. Origin: 20 subnet positions. No common signature."

"The supervisor frowns."

supervisor "...Chaos? This is bad."