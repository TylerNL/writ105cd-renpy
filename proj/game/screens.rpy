
init offset = -1


screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame(Solid("#0a0e12cc"), xalign=0.5, yalign=1.0)

style namebox:
    xpos 300
    xanchor 0.0
    ypos 0
    padding gui.namebox_borders.padding
    background Frame(Solid("#1a2530cc"), gui.namebox_borders, xalign=0.0)

style say_label:
    xalign 0.0
    yalign 0.5
    size gui.name_text_size
    bold True

style say_dialogue:
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos 50
    text_align gui.dialogue_text_xalign

style say_thought is say_dialogue


screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xanchor 0.5
            xpos 0.5
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input:
    xmaximum gui.dialogue_width


screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        for i in items:
            textbutton i.caption:
                action i.action

style choice_vbox is vbox

style choice_vbox:
    xalign 0.5
    ypos 300
    yanchor 0.5
    spacing 20

style choice_button:
    xsize gui.choice_button_width
    padding gui.choice_button_borders.padding
    background Frame(Solid("#111820"), gui.choice_button_borders)
    hover_background Frame(Solid("#1a2a38"), gui.choice_button_borders)

style choice_button_text:
    xalign 0.5
    idle_color "#8899aa"
    hover_color "#ffffff"
    size gui.text_size



screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -8

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button_text:
    size 18
    idle_color "#606060"
    hover_color gui.hover_color
    selected_color gui.accent_color


screen main_menu():
    tag menu
    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    vbox:
        style_prefix "navigation"
        xpos 0.06
        yalign 0.5
        spacing 8

        textbutton _("Start") action Start()
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm=False)

    text "SUBJECT ZERO-SEVEN":
        xalign 0.5
        ypos 80
        size gui.title_text_size
        color gui.accent_color
        text_align 0.5

    text "CONTAINMENT PROTOCOL ACTIVE":
        xalign 0.5
        ypos 160
        size 22
        color "#3a5060"
        text_align 0.5

style main_menu_frame is empty
style main_menu_frame:
    xsize 420
    yfill True
    background Solid("#0a0e12c0")

style navigation_button_text:
    idle_color "#888888"
    hover_color gui.hover_color
    selected_color gui.hover_color
    size 28


style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color