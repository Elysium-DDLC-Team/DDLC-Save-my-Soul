## screens.rpy

# This file declares all the screens and styles in DDLC.

## Initialization
################################################################################

init offset = -1

# Thanks RenpyTom! Borrowed from the Ren'Py Launcher
init python:
    def scan_translations():

        languages = renpy.known_languages()

        if not languages:
            return None

        rv = [(i, renpy.translate_string("{#language name and font}", i)) for i in languages ]
        rv.sort(key=lambda a : renpy.filter_text_tags(a[1], allow=[]).lower())

        rv.insert(0, (None, "English"))

        bound = math.ceil(len(rv)/2.)

        return (rv[:bound], rv[bound:2*bound])

default translations = scan_translations()

# Enables the ability to add more settings in the game such as uncensored mode.
default extra_settings = True
default enable_extras_menu = True
default enable_languages = True

## Color Styles
################################################################################

# This controls the color of outlines in the game like
# text, say, navigation, labels and such.
define -2 text_outline_color = "#b59"

## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    #outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## New as of 3.0.0
##    - You may now pass through argurments to the menu options to colorize
##      your menu as you like. Add (kwargs=[color hex or style name]) to your
##      menu option name and you get different buttons! 
##
##      Examples: "Option 1 (kwargs=#00fbff)" | "Option 2 (kwargs=#00fbff, #6cffff)"
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []


################################################################################
# Main and Game Menu Screens
################################################################################

screen viewframe_options(title):

    style_prefix "viewframe"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 2

            label title

            null height 10

            transclude

style viewframe_frame is confirm_frame
style viewframe_label is confirm_prompt:
    xalign 0.5
style viewframe_label_text is confirm_prompt_text
style viewframe_button is confirm_button
style viewframe_button_text is confirm_button_text
style viewframe_text is confirm_prompt_text:
    size 20
    yalign 0.7

## Windowed Resolutions
## Windowed Resolutions allow players to scale the game to different resolutions.
## Uncomment the below #'s to enable this.
# screen confirm_res(old_res):
    
#     ## Ensure other screens do not get input while this screen is displayed.
#     modal True

#     zorder 200

#     style_prefix "confirm"

#     add "gui/overlay/confirm.png"

#     frame:

#         vbox:
#             xalign .5
#             yalign .5
#             spacing 30

#             ## This if-else statement either shows a normal textbox or
#             ## glitched textbox if you are in Sayori's Death Scene and are
#             ## quitting the game.
#             # if in_sayori_kill and message == layout.QUIT:
#             #     add "confirm_glitch" xalign 0.5
#             # else:
#             label _("Would you like to keep these changes?"):
#                 style "confirm_prompt"
#                 xalign 0.5

#             add DynamicDisplayable(res_text_timer) xalign 0.5

#             hbox:
#                 xalign 0.5
#                 spacing 100

#                 ## This if-else statement disables quitting from the quit box
#                 ## if you are in Sayori's Death Scene, else normal box.
#                 # if in_sayori_kill and message == layout.QUIT:
#                 #     textbutton _("Yes") action NullAction()
#                 #     textbutton _("No") action Hide("confirm")
#                 # else:
#                 textbutton _("Yes") action Hide()
#                 textbutton _("No") action [Function(renpy.set_physical_size, old_res), Hide()]
    
#     timer 5.0 action [Function(renpy.set_physical_size, old_res), Hide()]

# init python:
#     def res_text_timer(st, at):
#         if st <= 5.0:
#             time_left = str(round(5.0 - st))
#             return Text(time_left, style="confirm_prompt"), 0.1
#         else: return Text("0", style="confirm_prompt"), 0.0

#     def set_physical_resolution(res):
#         old_res = renpy.get_physical_size()
#         renpy.set_physical_size(res)
#         renpy.show_screen("confirm_res", old_res=old_res)

screen display_options():

    style_prefix "viewframe"

    modal True

    zorder 150

    use viewframe_options(_("Display Resolutions")):

        default scale = renpy.get_physical_size()

        vbox:
            xmaximum 500
            ysize 120
            viewport:
                style_prefix "radio"
                scrollbars "vertical"
                mousewheel True
                draggable True
                has vbox

                textbutton "1280x720" action SetScreenVariable("scale", (1280, 720))
                textbutton "1600x900" action SetScreenVariable("scale", (1600, 900))

        null height 10

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Reset") action [Hide(), Function(renpy.reset_physical_size)]
            textbutton _("Set") action [Hide(), Function(set_physical_resolution, scale)]

screen text_options():
    modal True

    zorder 150

    use viewframe_options(_("Text Settings")):
        style_prefix "radio"
        label _("Rollback Side")
        hbox:
            textbutton _("Disable") action Preference("rollback side", "disable")
            textbutton _("Left") action Preference("rollback side", "left")
            textbutton _("Right") action Preference("rollback side", "right")

        label _("Skip")
        hbox:
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

        hbox:
            spacing 10
            label _("Text Speed")
            text str(preferences.text_cps) style "viewframe_text"

        bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20) xsize 500

        hbox:
            spacing 10
            label _("Auto-Forward Time")
            text str(round(preferences.afm_time)) style "viewframe_text"

        bar value Preference("auto-forward time") xsize 500

        null height 10

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Hide() style "confirm_button"

screen audio_options():
    style_prefix "viewframe"

    modal True

    zorder 150

    use viewframe_options(_("Audio Settings")):
        style_prefix "slider"
        if config.has_music:
            hbox:
                spacing 10
                label _("Music Volume")
                text str(round(preferences.music_volume * 100)) style "viewframe_text"

            hbox:
                bar value Preference("music volume") xsize 500

        if config.has_sound:

            hbox:
                spacing 10
                label _("Sound Volume")
                text str(round(preferences.sfx_volume * 100)) style "viewframe_text"

            hbox:
                bar value Preference("sound volume") xsize 500

                if config.sample_sound:
                    textbutton _("Test") action Play("sound", config.sample_sound)

        if config.has_voice:
            hbox:
                spacing 10
                label _("Voice Volume")
                text str(round(preferences.get_volume("voice") * 100)) style "viewframe_text"

            hbox:
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton _("Test") action Play("voice", config.sample_voice) 

        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing

            textbutton _("Mute All"):
                action Preference("all mute", "toggle")
                style "mute_all_button"

        null height 10

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Hide() style "confirm_button"

screen extra_options():
    style_prefix "viewframe"

    modal True

    zorder 150

    use viewframe_options(_("Extra Settings")):
        style_prefix "radio"

        label _("Game Modes")
        hbox:
            textbutton _("Uncensored Mode") action If(persistent.uncensored_mode, 
                ToggleField(persistent, "uncensored_mode"), 
                Show("confirm", message="Are you sure you want to turn on Uncensored Mode?\nDoing so will enable more adult/sensitive\ncontent in your playthrough.\n\nThis setting will be dependent on the modder if\nthey programmed these checks in their story.", 
                    yes_action=[Hide("confirm"), ToggleField(persistent, "uncensored_mode")],
                    no_action=Hide("confirm")
                ))
            textbutton _("Let's Play Mode") action If(persistent.lets_play, 
                ToggleField(persistent, "lets_play"),
                [ToggleField(persistent, "lets_play"), Show("dialog", 
                    message="You have enabled Let's Play Mode.\nThis mode allows you to skip content that\ncontains sensitive information or apply alternative\nstory options.\n\nThis setting will be dependent on the modder\nif they programmed these checks in their story.", 
                    ok_action=Hide("dialog")
                )])

        if not renpy.android:
            label _("Discord RPC")

            python:
                connect_status = "Disconnected"
                if RPC.rpc_connected:
                    connect_status = "Connected"

            textbutton "Enable" action [ToggleField(persistent, "enable_discord"), 
                If(persistent.enable_discord, Function(RPC.close), Function(RPC.connect, reset=True))]
            
            text "Status: [connect_status]" style "main_menu_version" xalign 0.0

            if persistent.enable_discord and not RPC.rpc_connected:
                textbutton "Reconnect" action Function(RPC.connect, reset=True) style "viewframe_button"

        label _("Player Name")
        vbox:
            style_prefix "confirm"
            if player == "":
                text "Current Name: No Name Set" style "viewframe_text"
            else:
                text "Current Name: [player]" style "viewframe_text"
            textbutton "Change Name" action Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName, launchGame=False)) xoffset 10

        null height 10

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Hide() style "confirm_button"



################################################################################
## Additional screens
################################################################################

screen name_input(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            #additionally added Cyrillic characters to support Russian names for MC

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen dialog(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm
screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            ## This if-else statement either shows a normal textbox or
            ## glitched textbox if you are in Sayori's Death Scene and are
            ## quitting the game.
            # if in_sayori_kill and message == layout.QUIT:
            #     add "confirm_glitch" xalign 0.5
            # else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                ## This if-else statement disables quitting from the quit box
                ## if you are in Sayori's Death Scene, else normal box.
                # if in_sayori_kill and message == layout.QUIT:
                #     textbutton _("Yes") action NullAction()
                #     textbutton _("No") action Hide("confirm")
                # else:
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label renpy.translate_string(_("{#in language font}Please select a language"), local_lang):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign .5
                for tran in translations:
                    vbox:
                        for tlid, tlname in tran:
                            textbutton tlname:
                                xalign .5
                                action SetScreenVariable("chosen_lang", tlid)
                                hovered SetScreenVariable("local_lang", tlid)
                                unhovered SetScreenVariable("local_lang", chosen_lang)

            $ lang_name = renpy.translate_string("{#language name and font}", local_lang)
            
            hbox:
                xalign 0.5
                spacing 100

                textbutton renpy.translate_string(_("{#in language font}Select"), local_lang):
                    style "confirm_button"
                    action [Language(chosen_lang), Return()]

translate None strings:
    old "{#language name and font}"
    new "English"

label choose_language:
    call screen choose_language
    return