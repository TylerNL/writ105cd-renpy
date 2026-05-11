define v = Character("Voss", color="#88aacc")
define e = Character("Eli", color="#cc9966")
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


# SCENE 1 — HOLDING ROOM
label start:
    scene bg cell
    with fade
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
    "A buzz. The magnetic lock disengages."
    "A voice through the intercom — measured, professional."
    v "Subject zero-seven, you're being moved to a temporary holding area. Please step into the corridor and follow the guide line."
    "The door slides open."
    jump scene2_hallway

#Scene 2 - Hallway (Items to collect: Sticky note and window)
label scene2_hallway:
    scene bg hallway
    with fade

    "A long institutional corridor. A yellow hazard stripe runs down the center of the floor."

    "Security cameras at regular intervals. Staff rooms behind frosted glass. Emergency strip lighting at the baseboards — faint orange, like a second heartbeat."
    label hallway_examine:
    menu:
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
    menu:
        "The corridor branches ahead."
        "Follow the guide line to the observation wing":
            jump scene3_observation
        "Turn toward the archive corridor" if found_sticky_note:
            jump scene4_archive
        "Follow the guide line":
            jump scene5_convergence

#Scene 3

label scene3_observation:
    scene bg lab
    with fade
    "A converted lab. Monitoring equipment lines one wall — screens dark, cables coiled. Observation chairs face a one-way window looking into an empty room."
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
            "{i}\"Staff rotation mandatory — no single researcher exceeds 4hrs contact.\"{/i}"
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
            jump scene5_convergence

# SCENE 4 — ARCHIVE
label scene4_archive:
    scene bg archive
    with fade
    "A narrow room lined with metal shelving. Filing cabinets. A playback terminal bolted to a desk, its screen casting pale blue light."
    "This isn't where they keep the subjects. This is where they keep the records."
    label archive_examine:
    menu:
        "The terminal hums. Files are scattered across the desk."
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
    jump scene5_convergence

# SCENE 5 — CONVERGENCE / EXIT GATE
label scene5_convergence:
    scene bg junction
    with fade
    "The junction between the research wing and the security-locked exit. Emergency lighting flickers — amber, then white, then amber again."
    "Blast doors ahead. Heavy. Industrial. A keycard reader blinks red."
    "The intercom crackles."
    v "You're almost at the perimeter lock. I can open it from here."
    if trust_voss >= 3:
        "Her voice is different from the start. Warmer. The professional distance is gone."
        v "I want you to get out. I need you to get out."
    else:
        "Her voice is strained. Urgent."
        v "Move quickly. I don't know how long I can keep this corridor clear."
    "A sound behind you. Footsteps — fast, uneven."
    e "Wait — {i}wait{/i}!"
    "Eli rounds the corner. Breathing hard. His containment band is cracked, hanging loose."
    if trust_eli >= 1:
        "He looks at you like you're the only real thing in the building."
    else:
        "He looks desperate. Afraid."
    e "They're locking everything down. If we don't go now, we don't go."
    v "Zero-seven. Listen to me carefully."
    if knows_incident:
        v "I know you've read the files. I know what you're thinking."
        v "But right now, the door is open. {i}Please.{/i}"
    else:
        v "The door is open. Don't hesitate."
    if alarm_triggered:
        jump ending_captured
    menu:
        "The blast doors hum. Eli stands beside you. Voss's voice hangs in the air."
        "\"Let's go — both of us.\"":
            $ helped_eli = True
            jump ending_shared_escape
        "\"I need to go alone. I'm sorry.\"":
            jump ending_alone
        "\"Is what I read in the archive true? Am I actually—\"" if knows_incident:
            jump ending_stay

# ENDINGS
label ending_shared_escape:
    e "You mean it?"
    "You take his arm. He doesn't resist. He doesn't question it."
    "Neither of you notice that he should have."
    v "Go. Both of you. Now."
    "The blast doors grind open. Cold air rushes in — real air, not recycled."
    "You step through together. The corridor behind you goes dark."
    "Somewhere in the facility, Dr. Voss leans back in her chair and closes her eyes."
    "She doesn't file the breach report."
    if knows_ability:
        "You wonder, as the night air hits your face, whether Eli chose to come with you."
        "Or whether he ever had a choice at all."
    else:
        "The night is cold and clear. For the first time in as long as you can remember, no one is watching."
    "END — Shared Escape"
    return
label ending_alone:
    e "What? No — you can't just—"
    "His hand reaches for you. You step back."
    "The look on his face isn't anger. It's something worse."
    "The blast doors open. You walk through alone."
    v "..."
    "Voss doesn't say anything. The intercom stays open. You can hear her breathing."
    "Behind you, the doors close. Eli's hand drops."
    if knows_ability:
        "You tell yourself it's the right thing. That staying would only make it worse."
        "You tell yourself his grief is real, and that's exactly why you have to go."
    else:
        "You don't look back."
    "END — Alone"
    return
label ending_stay:
    "The blast doors are open. The exit is right there."
    "You don't move."
    v "What are you doing?"
    "\"Is it true? The cognitive bleed. The attachment formation. All of it.\""
    "Silence."
    v "...Yes."
    "\"Then none of this is real. Not Eli. Not you. None of it.\""
    e "What are you talking about?"
    "Eli's voice is hurt. Confused. Genuine — as far as he can tell."
    "You sit down on the floor of the corridor."
    "\"Close the doors.\""
    v "You don't have to do this."
    "\"Close them.\""
    "The blast doors grind shut. The cold air disappears."
    "Eli stares at you. Then, slowly, sits down beside you."
    "You don't tell him to leave. You're not sure it would work."
    "The fluorescent lights hum. The cameras watch. And for the first time, you choose to stay where you can't hurt anyone else."
    "END — Stay"
    return
label ending_captured:
    "The alarm screams through the corridor. Red light washes everything in pulses."
    "The blast doors slam shut before you reach them. The lock cycles — once, twice — then goes dead."
    v "No — no, I almost had it—"
    "Her voice breaks. Not with professionalism. With something personal."
    e "We're trapped."
    "Eli backs against the wall. His breathing goes ragged."
    "Boots on tile. Getting closer."
    "You stand in the center of the corridor, under the emergency lights, and wait."
    "They don't use force. They don't need to."
    "Everyone who gets close to you becomes gentle."
    "END — Captured"
    return