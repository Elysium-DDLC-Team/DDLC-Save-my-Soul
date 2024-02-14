## splash.rpy

# This is where the splashscreen, disclaimer and menu code reside in.

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.

init -100 python:
    if not renpy.android:
        # for archive in ['audio','images','fonts']:
        #     if archive not in config.archives:
        #         raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None:
                if onedrive_path in config.basedir:
                    raise IllegalModLocation

## These images are the background images shown in-game during the disclaimer.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## This sets the persistent to false in order to choose a language.
default persistent.has_chosen_language = False

## This sets the first run variable to False to show the disclaimer.
default persistent.first_run = False

## This sets the lockdown check variable to False to show the warning for developers.
default persistent.lockdown_warning = False

label splashscreen:
    #$ renpy.movie_cutscene('mod_assets/movies/splashes/presplash/DDLCSavemySoulPresplashEnglish.webm')
    #$ renpy.pause(21.0, hard=True)
    if persistent.is_prologue == False:
        $ movielength = 21.0     # The length of your movie.
        $ movieplaying = "mod_assets/movies/splashes/presplash/DDLCSavemySoulPresplashEnglish.webm"    # The name and file path of your movie.

        call screen custommoviescreen with dissolve   # calling the screen

        return

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

default persistent.is_theme_default = True
default persistent.theme_value = 0.0
