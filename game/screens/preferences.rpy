
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
   
    tag menu
    add "menu_bg"
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 150

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Windowed") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    xsize 400
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    label _("Theme")
                    textbutton _("Default") action Function(ColorTheme().default)
                    textbutton _("Orange") action Function(ColorTheme().orange)
                    textbutton _("Yellow") action Function(ColorTheme().yellow)
                    textbutton _("Blue") action Function(ColorTheme().blue)


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                if extra_settings:
                    xoffset 15
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    #bar value Preference("text speed")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    if extra_settings:
                        xoffset 15

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):

                            action Preference("all mute", "toggle")


            hbox:
                style_prefix "radio"
                if extra_settings:
                    xoffset 15

                if translations:
                    vbox:
                        label _("Language")

                        hbox:
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                ysize 110
                                has vbox

                                for tran in translations:
                                    vbox:
                                        for tlid, tlname in tran:
                                            textbutton tlname:
                                                action Language(tlid)

                vbox:
                    label _("Discord RPC")

                    python:
                        rpc_text = _("Disabled")
                        connect_status = _("Disconnected")
                        if persistent.enable_discord:
                            rpc_text = _("Enabled")
                        if RPC.rpc_connected:
                            connect_status = _("Connected")

                    textbutton rpc_text action [ToggleField(persistent, "enable_discord"),
                        If(persistent.enable_discord, Function(RPC.close), Function(RPC.connect, reset=True))]

                    text "Status: [connect_status]" style "main_menu_version" xalign 0.0

                    if persistent.enable_discord and not RPC.rpc_connected:
                        textbutton _("Reconnect") action Function(RPC.connect, reset=True)
                vbox:
                    vbox:
                        xoffset 50
                        xsize 400
                        style_prefix "check"
                    
                        label _("Blinking")
                        textbutton _("On") action SetField(persistent, "blinking", True)
                        textbutton _("Off") action SetField(persistent, "blinking", False)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font"gui/font/RifficFree-Bold.ttf"
    size 36
    color "#fff"
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    #outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Aller_Rg.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Aller_Rg.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450
