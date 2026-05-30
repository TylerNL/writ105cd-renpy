init python:
    renpy.music.register_channel("talk", mixer="sfx", loop=False)
    def talk_sound(event, **kwargs):
        if event == "begin":
            renpy.sound.play("audio/talk_blip.mp3", channel="talk", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="talk")
define v = Character("Voss", color="#88aacc", callback=talk_sound)
define e = Character("Eli", color="#cc9966", callback=talk_sound)
define narrator = Character(None, kind=nvl_narrator) if False else Character(None)
default trust_voss = 0
default trust_eli = 0
default knows_ability = False
default knows_incident = False
default helped_eli = False
default alarm_triggered = False
default found_wristband = False
default found_display = False
default found_sticky_note = False
default found_eli_window = False
default found_whiteboard = False
default found_readout = False
default found_case_file = False
default found_rotation_note = False
default found_voss_rec1 = False
default found_voss_rec2 = False
default found_memo = False
default caught_in = ""
image bg cell     = im.Scale("/images/bg Jail cell.jpg", 1920, 1080)
image bg hallway = im.Scale("/images/bg hallway.png", 1920, 1080)
image bg holding_cell = im.Scale("/images/bg holding cell.jpg", 1920, 1080)
image bg ending = im.Scale("/images/bg ending.jpg", 1920, 1080)
image bg lab = im.Scale("images/bg lab.png", 1920, 1080)
image bg junction = im.Scale("images/bg junction.png", 1920, 1080)
image bg morgue 1 = im.Scale("images/bg morgue 1.jpg", 1920, 1080)
image bg bando = im.Scale("images/bg bando 1.jpg", 1920, 1080)
image voss_neutral = "/images/voss_neutral.png"
image voss_talk = "/images/voss_talk.png"   
define audio.buzz    = "audio/freesound_community-room-with-buzz-incandescent-light-bulb-23892.mp3"
define audio.hum     = "audio/dragon-studio-creepy-industrial-hum-482882.mp3"
define audio.intercom = "audio/freesound_community-intercom-93581.mp3"
image eli = "/images/eli-bg.png"
transform right_up:
    xalign 1.0
    yalign 1.0
    yoffset -200


# SCENE 1 — HOLDING ROOM
label start:
    scene bg cell
    with fade
    play music audio.buzz fadein 2.0
    "Sterile white. Fluorescent panels humming overhead. The smell is clinical — disinfectant layered over something older."
    "A metal bed bolted to the wall. A one-way mirror on the far wall, its surface dark and flat."
    "A digital readout above the door pulses softly: {b}CONTAINMENT CELL 07{/b}."
    "Not 'room.' Not 'suite.' {i}Containment.{/i}"
    label cell_examine:
    menu:
        "Look around the cell."
        "Examine wristband" if not found_wristband:
            $ found_wristband = True
            "A plastic band cinched around your wrist. Stamped in blocky letters: {b}S-07{/b}."
            "A number. Not a name."
            jump cell_examine
        "Look at the mirror" if not found_display:
            $ found_display = True
            "You don't look at it directly. You never do."
            "From the corner of your eye, the glass reflects the room — distorted, slightly wrong. Someone could be standing right behind it."
            "The thought doesn't bother you as much as it should."
            jump cell_examine
        "Wait by the door":
            pass
    play sound audio.intercom
    "A buzz. The magnetic lock disengages."
    "A voice through the intercom — measured, professional."
    v "Subject zero-seven, you're being moved to a temporary holding area. Please step into the corridor and follow the guide line."
    "The door slides open."
    jump scene1b_interview

# Multiple ways to gain the doctor's trust
label scene1b_interview:
    play music audio.hum fadein 2.0
    scene bg holding_cell
    with fade
    "Before they move you, they assess you."
    "The intercom panel buzzes beside the mirror."
    "The one-way glass brightens slightly from within. A silhouette resolves: a woman, seated, clipboard in her lap."

    show voss_neutral at right_up
    with dissolve
    show voss_talk at right_up
    v "Good morning, zero-seven. I'm Dr. Voss. I'll be conducting your routine cognitive assessment."
    v "This should take about fifteen minutes. Please answer as directly as you can."
    # Q1
    v "How have you been sleeping?"
    menu:
        "Fine.":
            "She makes a note. Clinical."
            v "Consistent sleep pattern. Good."

        "Not well. The lights don't turn off.": #Truthful - trust builds
            $ trust_voss += 1
            "A pause. Something crosses her expression."
            v "I'll look into the panel schedule."
            "Not 'flag it for review.' Not 'submit a request.' She said {i}I'll look into it.{/i}"

        "(Stay silent)":
            "She waits with her pen ready. Then lowers it."
            v "That's alright. We can move on."
    # Question 2
    v "Do you remember the twelve months before you came here?"
    menu:
        "Not much. Fragments.":
            v "That's consistent with intake profiles."
            "She writes."
        "Why does that matter to you?":
            "The pen lifts."
            v "It's a standard assessment question."
            "She says it the way someone says something they're reminding themselves is true."
        "I remember everything. I just don't know what it means yet.": #Truthful answer - trust increases
            $ trust_voss += 1
            "A pause. Longer. She looks up from the clipboard."
            v "Hmmm...okay then."
            "She's stopped writing. She's looking at you."
    # Question 3
    v "Do you feel different than you did when you first arrived?"
    menu:
        "I don't know what I felt when I first arrived.":
            v "Noted."
            "She writes, but the pace has slowed."
        "Do {i}you{/i} feel different?": # Trust incrfeases
            $ trust_voss += 1
            "The pen stops."
            "A long beat."
            v "...That's not part of the assessment."
            "She moves on. But she didn't say no."
        "Yes. Calmer.":
            "She writes the word. Then reads it back to herself, silently."
            v "Calmer. Interesting."
    # Question 4
    v "Is there anyone outside this facility you'd want us to contact?"
    menu:
        "No.":
            "She writes it down without looking up."
            v "Noted."
        "I don't know anymore.":
            $ trust_voss += 1
            "She looks up from the clipboard."
            "That's not the answer she was expecting."
            "She starts to say something. Then writes instead."
            v "...I'll note that."
        "Would it change anything?":
            $ trust_voss += 1
            "The pen stops."
            "A long silence. She doesn't answer the question."
            "She writes something down that takes longer than it should."
    # Closing
    v "That concludes today's session. Thank you for your cooperation."
    "She gathers her materials."
    "Then stops."
    "She's looking at the glass. She stares at your face blankly, not seeming to realize she's doing it."
    menu:
        "Watch her.":
            $ trust_voss += 1
            "Three seconds. Maybe four. Long, for someone this deliberate."
            "Then something shifts."
            v "Someone will be along to escort you to the corridor shortly."
            "She leaves. The glass dims."
            hide voss_neutral
            hide voss_talk
            with dissolve
            "She moved differently at the end. Like someone walking away from something they almost said."
        "Look toward the door instead.":
            v "Someone will be along shortly."
            "The glass dims. You don't see what she does before she goes."
    stop music fadeout 2.0
    jump scene2_hallway

#Scene 2 - Hallway (Items to collect: Sticky note and window -- both build trust with Dr.)
label scene2_hallway:
    play music audio.hum fadein 2.0
    scene bg hallway
    with fade

    "A long institutional corridor. A yellow hazard stripe runs down the center of the floor."

    "Security cameras at regular intervals. Staff rooms behind frosted glass. Emergency strip lighting at the baseboards"
    label hallway_examine:
    menu:
        "Try the staff room door" if not alarm_triggered:
            "The handle is locked. But the electronic panel beside it flickers when you get close."
            "A camera above you adjusts its angle."
            menu:
                "Keep trying.":
                    $ caught_in = "hallway"
                    $ alarm_triggered = True
                    "The panel emits a sharp, flat tone. A red indicator pulses twice."
                    "Down the corridor, a door opens."
                    jump caught_snooping_hallway
                "Step back.":
                    "You step back. The camera holds on you for a moment, then resumes its sweep."
                    jump hallway_examine
        "The corridor stretches ahead."
        "Read sticky note on the wall" if not found_sticky_note:
            $ found_sticky_note = True
            "A small yellow note, curling at the edges, stuck to the wall beside a staff door."
            "{i}\"DO NOT engage verbally unless behind glass. — Dr. Voss\"{/i}"
            "Someone underlined 'verbally' twice."
            $ trust_voss += 1 # Builds trust with voss
            jump hallway_examine
        "Look through the reinforced glass" if not found_eli_window:
            $ found_eli_window = True
            "Movement in the adjacent cell. A figure — young, close to your age — presses his hand flat against the window."
            "His cell looks identical to yours. Same bed. Same mirror. Same readout."
            "He mouths something. You can't hear it."
            "Staff in the background move faster near both doors."
            $ trust_eli += 1 # Builds trust with eli
            jump hallway_examine
        "Keep walking":
            pass
    v "Continue along the guide line. You'll be directed to the observation wing shortly."

    "The guide line leads past a row of reinforced windows."

    "You slow without meaning to."

    "A figure is already at the glass. He was waiting."

    "There's a strip of tape on the window frame, handwritten in marker: {b}ELI{/b}"

    "Not a subject number. A name."

    "He presses a folded piece of paper against the window. Blocky letters: {b}HOW LONG{/b}"

    menu:
        "Hold up three fingers.":
            $ trust_eli += 1
            "He looks at your hand. Then holds up three of his own."
            "Same."
        "Shrug — you're not sure.":
            "He nods slowly. Like that's an answer too."
        "(Say nothing)":
            "He waits a moment. Then nods."

    "He uncaps a pen and writes again. Presses it to the glass."
    "{b}DO YOU TRUST HER{/b}"
    "An arrow pointing up. Toward the speaker on the wall."

    menu:
        "Nod.":
            $ trust_eli += 1
            "He tilts his hand back and forth. {i}Maybe.{/i}"
        "Shake your head.":
            "He writes {b}NOT YET{/b} and holds it up."
            "You're not sure if that's agreement or a warning."
        "Shrug.":
            $ trust_eli += 1
            "He tilts his hand back and forth. {i}Maybe.{/i}"

    "At the end of the corridor, a staff member stops walking."
    "They find something on their clipboard. Study it very carefully."
    "They don't look up."

    "Eli writes one more thing and presses it to the glass."
    "{b}I'LL FIND YOU{/b}"

    "You're not sure if that's a threat or a plan."

    "The staff member starts moving again."
    "You keep walking."

    menu:
        "The corridor branches ahead."
        "Head to the observation wing":
            jump scene3_observation
        "Turn toward the archive corridor" if found_sticky_note:
            jump scene4_archive
        "Follow the guide line":
            jump scene_eli_split
    stop music fadeout 2.0

#Scene 3
label scene3_observation:
    play music audio.buzz fadein 1.0
    scene bg morgue 1 
    with fade
    "A converted lab. Monitoring equipment lines one wall — screens dark, cables coiled."
    "A whiteboard. Cabinet drawers left slightly open. The room smells like stale coffee and dry-erase markers."
    label lab_examine:
    menu:
        "The lab is quiet. Undisturbed for a while."
        "Read the whiteboard" if not found_whiteboard:
            $ found_whiteboard = True
            "Most of it has been erased. Smudged blue ink. One fragment remains, barely legible:"
            "{i}\"It doesn't know\"{/i}"
            jump lab_examine
        "Check the monitoring readout" if not found_readout:
            $ found_readout = True
            "A screen flickers to life at your touch. Behavioral metrics for {b}Subject 07{/b}."
            "Attachment rate. Proximity response. Emotional compliance index."
            "The numbers are climbing."
            jump lab_examine
        "Open the case file" if not found_case_file:
            $ found_case_file = True
            "A manila folder, half-tucked into a drawer. The relevant line jumps out:"
            "{i}\"...accelerated attachment formation in exposed personnel...\"{/i}"
            "The rest is redacted."
            jump lab_examine
        "Read the pinned note" if not found_rotation_note:
            $ found_rotation_note = True
            "Pinned to the corkboard, typed on official letterhead:"
            "{i}\"Staff rotation mandatory...no single researcher shall exceed 4hrs contact.\"{/i}"
            "Four hours. You've been here much longer than that."
            jump lab_examine
        "Leave the lab":
            pass
    if found_whiteboard and found_readout and found_case_file and found_rotation_note:
        $ knows_ability = True
        "Something settles in your chest. Not a revelation — a confirmation. Like a word you've been trying to remember finally surfacing."
        "You affect people. Just by being near them."
    elif found_readout or found_case_file:
        "Fragments. Not enough to see the full picture, but enough to feel its weight."
    menu:
        "Where to now?"
        "Head toward the archive" if not knows_incident:
            jump scene4_archive
        "Continue to the exit wing":
            jump scene_eli_split
    stop music fadeout 2.0

# SCENE 4 — ARCHIVE
label scene4_archive:
    scene bg lab 
    with fade
    "A narrow room lined with metal shelving. Filing cabinets. A playback terminal bolted to a desk, its screen casting pale blue light."
    "This isn't where they keep the subjects. This is where they keep the records."
    label archive_examine:
    menu:

        "Play recording #1" if not found_voss_rec1:
            $ found_voss_rec1 = True
            "The timestamp reads three weeks ago."
            v "Subject zero-seven presents standard containment metrics. I've reviewed the protocols. I know what to look for."
            "A pause."
            v "I'll be fine."
            "Her voice is clipped. Professional. Controlled."
            $ trust_voss += 1
            jump archive_examine

        "Play recording #2" if not found_voss_rec2:
            $ found_voss_rec2 = True
            "The timestamp reads twenty days later."
            v "I've been thinking about them. Not in a clinical way. Just... thinking."
            "Her voice is different. Softer. Almost dreamy."
            v "They're not dangerous. I really believe that."
            "The recording ends with a long silence."
            $ trust_voss += 1
            jump archive_examine

        "Read the memo" if not found_memo:
            $ found_memo = True
            "A typed memo, stamped INTERNAL ONLY."
            "{i}\"Cognitive Bleed — passive radius expanding. Estimated range: 40ft.\"{/i}"
            "Forty feet. That's not a room. That's a corridor. A wing."
            jump archive_examine

        "Search for restricted files" if not alarm_triggered:
            "At the bottom of the filing cabinet: a locked drawer. The label reads {b}LEVEL 4 — BIOHAZARD ADVISORY{/b}."
            menu:
                "Force it open.":
                    $ caught_in = "archive"
                    $ alarm_triggered = True
                    "The lock is cheap. It breaks under little pressure."
                    "Inside: a single file folder. A photograph clipped to the front."
                    "Your face. From before. A name written underneath it — your real name."
                    "You hadn't heard it in so long you'd almost stopped expecting to."
                    "A tone sounds through the building. Then again."
                    jump caught_snooping_archive
                "Leave it.":
                    "You close the drawer and step back."
                    jump archive_examine

        "Leave the archive":
            pass
    if found_voss_rec1 and found_voss_rec2 and found_memo:
        $ knows_ability = True
        $ knows_incident = True
        "You understand now. What you do to people. What you did to Voss without trying."
        "The warmth that makes people trust you isn't kindness. It's a field. And it's getting stronger."
    elif found_voss_rec2 and found_memo:
        $ knows_ability = True
        "Pieces click together. Not everything — but enough."

    "You step out of the archive. The blue light of the terminal fades behind you."
    scene bg hallway
    with fade
    "The corridor is empty in both directions."
    

    if knows_incident:
        "Your real name keeps surfacing. The one under the photograph."
        "You'd almost stopped expecting to hear it. Now you can't put it back down."
    elif knows_ability:
        "You keep a careful distance from the walls, the cameras, as if proximity were the problem."

    "You follow the corridor toward the perimeter. The signage thins out. Fewer cameras."
    "Somewhere behind a wall, a ventilation fan winds down and doesn't start again."

    "Up ahead the corridor funnels to a single controlled point. The only way out runs through it."

    jump scene_checkpoint

# SCENE 4B
label scene_eli_split:
    scene bg hallway
    with fade

    "The corridor shifts."

    "Someone coming from the other direction."

    "It's Eli. Moving fast. A researcher two steps behind him, tablet out."

    "He sees you."
    show eli at right_up
    menu:
        "Slow down.":
            $ trust_eli += 1
            "Eli slows down. So does the research."
            "The researcher behind him glances up from their tablet."
            "Then back down."
            "Three seconds. Maybe more."
            e "They're moving us today. Separately."
            menu:
                "\"Where are they taking you?\"":
                    e "Different wing. I don't know whi—"
                    "A second staff member appears at the far end of the corridor."
                    "The researcher behind Eli blinks. Seems to remember something."
                "\"I know.\"":
                    "He looks at you."
                    e "Then you know more than I do."
                    "A second staff member appears at the far end of the corridor."
        "Keep walking.":
            "Eye contact. That's all."
            "He nods once. You nod back."
            "The researcher behind him doesn't slow down."
            "A second staff member appears at the far end of the corridor."

    "The second staff member reaches Eli. A hand on his shoulder."
    "Firm. Practiced."

    e "Exi-"

    "He's turned around before he can finish the word."

    if knows_incident:
        "You know what he's talking about."
        "The junction between wings. The exit gate."
    else:
        "You don't know what he was trying to say."
        "But you remember the strip of tape on the window frame. His handwriting."
        "{b}I'LL FIND YOU{/b}"

    "You keep walking."

    jump scene_checkpoint


label scene_checkpoint:
    scene bg hallway
    with fade

    "You reach the end of the hallway where two guards are positioned."
    "A wristband scanner mounted to the wall."

    "The first guard looks up when you approach."
    "He reaches for your wrist. Scans the band."
    "He looks at his screen."

    menu:
        "Wait.":
            "He's still looking at the screen."
            "Not reading it. Just looking at it."
            "Eleven seconds. You count."
        "Say your number. \"Zero-seven.\"":
            "He looks up."
            "\"Right.\" He says it like he already knew."
            "He doesn't look back at the readout."

    "The second guard is supposed to sign you out."
    "His pen is uncapped. He's looking at the middle distance."

    "A radio is clipped to the first guard's shoulder. It crackles"
    "He doesn't reach for it."
    "The request repeats. Louder. A name you don't catch, then a number you do. {b}Zero-seven.{/b}"
    "His thumb drifts toward the transmit button. Hovers there."
    if knows_ability:
        "You understand what's happening to him. You're standing too close. They both are."
    else:
        "You don't know why he doesn't answer it. Only that he doesn't."

    "Neither of them is going to stop you. You could wait for the door to release on its own."
    "Or you could take what you need and be gone before they surface."

    menu:
        "Wait for the door.":
            "The lock disengages with a soft mechanical sigh. The door clicks open."
            "You walk through."
            "Behind you, neither guard moves."
            jump scene_voss_window
        "Take the keycard from his belt and go.":
            "You lift it off the clip. He lets you. His eyes follow your hand like it belongs to someone else."
            $ alarm_triggered = True
            play sound audio.intercom
            "A tone. Then another. The light above the door snaps from green to red."
            "Both guards blink, like sleepers waking."
            "You run."
            jump scene5_convergence


# SCENE 4C — THE WINDOW
label scene_voss_window:
    scene bg hallway
    with fade

    "Past the checkpoint, the corridor keeps going. Longer than it should."
    "The overhead lights are spaced further apart here. Pools of dark between them."

    "On your right, a window set into the wall. Reinforced glass. An office on the other side."

    "Someone's in there."
    "A woman, bent over a console, the blue glow of it on her cheek. She hasn't looked up yet."
    "But you know the voice that goes with that face. The one from the recordings. The one that's been getting warmer for weeks."
    "Voss."

    "You drop below the sill before she can turn."
    "Back against the wall."

    play sound audio.intercom
    "A speaker clicks on above the door."
    v "I saw you."
    "Not loud. Not an alarm. Just a fact, set down between you."
    v "Stand up. Let me look at you."

    menu:
        "Stay down.":
            "You don't move. Your heartbeat does."
            v "I'm not going to call anyone. I just want to see you."
            "A long pause."
            v "Please."
        "Stand.":
            pass

    "You rise into the frame."
    show voss_talk at right_up
    "For the first time it's just glass between you and Voss. Nothing else."

    "Her hand comes up to the surface. Fingers spread flat against it."
    if knows_ability or knows_incident:
        "And you feel it leave you. The warmth. The field. Reaching across the gap whether you want it to or not."
        "You're doing this to her. Right now. And you don't know how to stop."
    else:
        "Something crosses the space between you. You don't have a word for it."
        "The tension drains out of her face like water finding a drain."

    if trust_voss >= 3:
        v "I knew it would be you. I think I've known for weeks."
        v "Go. The perimeter lock is the last door. I'll have it open before you reach it."
    else:
        v "I'm supposed to stop you. That's the job."
        "Her hand stays on the glass."
        v "Go. Before I remember how."

    "The office light clicks off."

    "You keep walking, toward the last door."

    jump scene5_convergence


# SCENE 5 — CONVERGENCE / EXIT GATE
label scene5_convergence:
    if alarm_triggered:
        jump ending_captured
    scene bg junction
    with fade
    "Blast doors ahead. A keycard reader blinks red."
    play sound audio.intercom
    "The intercom crackles."
    v "You're almost at the perimeter lock. I can open it from here."
    if trust_voss >= 3:
        "Her voice is different from the start. Warmer. The professional distance is gone."
        v "I want you to get out. I need you to get out."
    else:
        "Her voice is strained. Urgent."
        v "Move quickly. I don't know how long I can keep this corridor clear."
    "A sound behind you. Footsteps"
    show eli at right_up
    e "Wait! {i}wait{/i}!"
    "Eli rounds the corner. Breathing hard. His containment band is cracked, hanging loose."
    if trust_eli >= 1:
        "He looks at you like you're the only real thing in the building."
    else:
        "He looks desperate. Afraid."
    e "They're locking everything down. If we don't go now, we don't go."
    if trust_eli >= 1:
        e "I'm not asking you to save me. I'm asking you not to leave."
        "He says it simply. Like it's the easiest thing in the world to want."
    else:
        e "I don't even know your real name. I don't care. We just have to move."
    "His hand is already half-extended toward you."
    v "Zero-seven. Listen to me carefully."
    if knows_incident:
        v "I know you've read the files. I know what you're thinking."
        v "But right now, the door is open. {i}Please.{/i}"
    else:
        v "The door is open. Don't hesitate."
    "The keycard reader flicks from red to green. The blast doors release a long breath and begin to part."
    "Cold air threads through the gap - real air, from outside. The first you've felt in longer than you can remember."
    if knows_ability:
        "You think about what you are. What standing near these two has already done to them."
        "Whatever you choose now, you won't be able to tell if they chose it back."
    "Two people want different things from you. The door wants only one."
    menu:
        "Eli's hand hangs half-raised. Voss's voice still in the air. The cold pulling at you from beyond the doors."
        "\"Let's go.\"":
            $ helped_eli = True
            jump ending_shared_escape
        "\"I need to go alone. I'm sorry.\"":
            jump ending_alone
        "\"Is what I read in the archive true? Am I actually—\"" if knows_incident:
            jump ending_stay

#Getting caught scenes:
label caught_snooping_hallway:
    scene bg hallway
    "Footsteps. Fast. Two pairs."
    "The staff door swings open ahead of you. Two technicians enter."
    "One of them says, carefully: \"We need you to come with us.\""
    "You notice they don't grab you. They stand close, but they don't grab you."
    "You wonder, as they lead you back, if that's protocol."
    "Or if it's something else."
    jump ending_caught_snooping
label caught_snooping_lab:
    scene bg lab
    "The red light pulses."
    "Through the porthole, the figure in cell four is still watching."
    "You don't know how long you stand there before you hear the door behind you open."
    "A hand on your shoulder. Carefully placed."
    "\"Subject zero-seven. Please come with us.\""
    "You let them lead you away from the glass."
    "You keep thinking about that other cell. About the figure who looked up at exactly the right moment."
    "Like they already knew you were there."
    jump ending_caught_snooping
label caught_snooping_archive:
    scene bg lab
    "You're still holding the photograph when the door opens."
    "A researcher you've never seen stops just inside the doorway."
    "They look at the photograph. Then at you. Then back at the photograph."
    "They're fumbling. Flushed. They can't quite meet your eyes."
    "You've been in this room less than three minutes."
    "You fold the photograph once and set it on the desk before you go."
    "They don't stop you from folding it. They don't take it back."
    jump ending_caught_snooping
label ending_caught_snooping:
    scene bg cell
    with fade
    "Same cell. Same fluorescent panels. Same digital readout above the door: {b}CONTAINMENT CELL 07{/b}."
    "The intercom crackles."
    if trust_voss >= 3:
        v "I'm sorry. I tried to get ahead of it."
        "A pause."
        v "I should have moved faster."
        "Her voice is different from the assessment session."
    else:
        v "This is why we have protocols."
        "A pause. Shorter than it should be."
        v "...Someone will bring you something to eat."
    "The glass on the far wall is dark."
    "It's never just a mirror."
    if caught_in == "archive":
        "Somewhere in this facility, there's a photograph with your real name on it."
        "You left it on the desk. They didn't take it back."
        "You don't know what to do with that yet."
    elif caught_in == "lab":
        "You keep thinking about the figure in cell four."
        "How they looked up at exactly the right moment."
        "You wonder if they're thinking about you."
    elif caught_in == "hallway":
        "You think about the way those technicians looked when they came for you."
        "Not afraid. Not angry."
        "{i}Apologetic.{/i}"
    "You sit on the metal bed and wait."
    "There's more to find in here."
    "There always is."
    "END - Caught"
    return

# ENDINGS
label ending_shared_escape:
    scene bg ending
    show eli at right_up
    e "You mean it?"
    "You take his arm. He doesn't resist. He doesn't question it."
    "Neither of you notice that he should have."
    v "Go. Both of you. Now."
    "The blast doors grind open."
    "You step through together. The corridor behind you goes dark."
    "Somewhere in the facility, Dr. Voss leans back in her chair and closes her eyes."
    "She doesn't file the breach report."
    if knows_ability:
        "You wonder, as the night air hits your face, whether Eli chose to come with you."
        "Or whether he ever had a choice at all."
    else:
        "The night is cold and clear. For the first time in as long as you can remember, no one is watching."
    "You walk until the facility is a low grey shape behind the treeline. Eli keeps pace beside you."
    "He's smiling. He hasn't stopped since the doors opened."
    if knows_ability:
        "You keep half a step of distance. He keeps closing it."
        "You'll have to tell him eventually. What you are."
        "Not tonight. Tonight you let him walk beside you and try not to count the inches."
    else:
        e "Where do we go?"
        "You don't have an answer. It doesn't seem to bother either of you."
    "END - Shared Escape"
    return
label ending_alone:
    scene bg ending
    e "What? No-"
    "His hand reaches for you. You step back."
    "The look on his face isn't anger. It's something worse."
    "The blast doors open. You walk through alone and push Eli to stay."
    v "..."
    "Voss doesn't say anything. The intercom stays open. You can hear her breathing."
    "Behind you, the doors close. Eli's hand drops."
    if knows_ability:
        "You tell yourself it's the right thing. That staying would only make it worse."
    else:
        "You don't look back."
    scene bg bando
    with fade
    "Outside, the air is colder than you expected. The facility's lights throw long rectangles across the gravel behind you."
    "You walk until you can't hear the alarm. Then further."
    if knows_ability:
        "It's the cleanest thing you've done since you understood what you are."
        "Out here there's no one close enough to bend toward you. No one to lie to without meaning to."
        "You think it's supposed to feel like freedom."
    else:
        "You don't know where you're going. Only that it's away."
        "Somewhere behind a steel door, a man who reached for you is learning you're not coming back."
        "You keep your eyes on the dark ahead and let him learn it."
    "END - Alone"
    return
label ending_stay:
    scene bg ending
    "The blast doors are open. The exit is right there."
    "You don't move."
    v "What are you doing?"
    "\"Is it true? My ability? The attachment formation? All of it?\""
    "Silence."
    v "...Yes."
    "\"Then none of this is real. Not Eli. Not you. None of it.\""
    show eli at right_up
    e "What are you talking about?"
    "Eli's voice is hurt. Confused."
    "You sit down on the floor of the corridor."
    "\"Close the doors.\""
    v "You don't have to do this."
    "\"Close them.\""
    "The blast doors grind shut. The cold air disappears."
    "Eli stares at you. Then, slowly, sits down beside you."
    "You don't tell him to leave. You're not sure it would work."
    v "...I'll log it as a containment success."
    "Her voice is careful. The professional distance back in place."
    v "It's the only way I can keep them from sending someone for you."
    "A pause."
    v "Thank you. For not making me watch you leave and wonder if I meant it."
    "The intercom clicks off."
    "Beside you, Eli's shoulder is warm against yours."
    "You choose to stay where you can't hurt anyone else."
    "END - Stay"
    return
label ending_captured:
    scene bg ending
    "The alarm screams through the corridor. Red light washes everything in pulses."
    "The blast doors slam shut before you reach them."
    v "No, I almost had it—"
    "Her voice breaks."
    show eli at right_up
    e "We're trapped."
    "Eli backs against the wall. His breathing goes ragged."
    "Getting closer."
    "You stand in the center of the corridor, under the emergency lights, and wait."
    "They don't use force. They don't need to."
    "Everyone who gets close to you becomes gentle."
    "Hands settle on your arms. Soft. Almost apologetic — the same hands that an hour ago were locking the doors."
    "They walk you back the way you came. Behind you, Eli is calling your number. Then your number again. Until a door closes between you and the sound stops."
    if trust_voss >= 3:
        "The intercom trails you down the corridor. Voss, quiet, not quite to herself."
        v "I'll try again. I'm not going to stop trying."
        "You don't know if she means it. You're not sure she can tell the difference anymore either."
    else:
        "No one says anything. There's nothing to say to a problem that solves itself just by standing near you."
    "END - Captured"
    return