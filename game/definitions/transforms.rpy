## transforms.rpy

# This file defines the placements and animations in DDLC.

# This transform sizes the character properly at the given X position.
transform tcommon(x=960, z=0.50):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=960, z=0.60):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# This transform makes the character zoom in when they talk.
transform focus(x=960, z=0.60):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

# This transform causes the character to sink down on the screen.
transform sink(x=960, z=0.60):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# This transform makes the character jump for a bit
transform hop(x=960, z=0.60):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# This transform makes the character jump and be in focus at the same time.
transform hopfocus(x=960, z=0.60):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# This causes the character to sink down from the screen then come back up.
transform dip(x=960, z=0.60):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# This transform causes the character to wobble on-screen.
# This might be a left-over transform from DDLC's development for Natsuki's Closet CG.
transform panic(x=960, z=0.60):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# This transform causes the character to "fly in" (enter the scene) from the left.
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# This transform causes the character to "fly in" (enter the scene) from the right.
transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# This transform hides the character from the screen.
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20

# This transform hides the character by moving them to the left.
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

# This transform hides the character by moving them to the left.
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

# These transforms have the characters stand still at a given position given
# how many characters are on screen and which character number they are.
#     Example for Monika with 2 other girls; being in between them: t32
transform t41:
    tcommon(300)
transform t42:
    tcommon(740)
transform t43:
    tcommon(1179)
transform t44:
    tcommon(1620)
transform t31:
    tcommon(360)
transform t32:
    tcommon(960)
transform t33:
    tcommon(1560)
transform t21:
    tcommon(600)
transform t22:
    tcommon(1320)
transform t11:
    tcommon(960)

# These transforms makes the character pop in.
transform i41:
    tinstant(300)
transform i42:
    tinstant(740)
transform i43:
    tinstant(1179)
transform i44:
    tinstant(1620)
transform i31:
    tinstant(360)
transform i32:
    tinstant(960)
transform i33:
    tinstant(1560)
transform i21:
    tinstant(600)
transform i22:
    tinstant(1320)
transform i11:
    tinstant(960)

# These transforms makes the character be the main focus on-screen.
transform f41:
    focus(300)
transform f42:
    focus(740)
transform f43:
    focus(1179)
transform f44:
    focus(1620)
transform f31:
    focus(360)
transform f32:
    focus(960)
transform f33:
    focus(1560)
transform f21:
    focus(600)
transform f22:
    focus(1320)
transform f11:
    focus(960)

# These transforms makes the character sink downwards.
transform s41:
    sink(300)
transform s42:
    sink(740)
transform s43:
    sink(1179)
transform s44:
    sink(1620)
transform s31:
    sink(360)
transform s32:
    sink(960)
transform s33:
    sink(1560)
transform s21:
    sink(600)
transform s22:
    sink(1320)
transform s11:
    sink(960)

# These transforms makes the character hop.
transform h41:
    hop(300)
transform h42:
    hop(740)
transform h43:
    hop(1179)
transform h44:
    hop(1620)
transform h31:
    hop(360)
transform h32:
    hop(960)
transform h33:
    hop(1560)
transform h21:
    hop(600)
transform h22:
    hop(1320)
transform h11:
    hop(960)

# These transforms makes the character hop and be in focus at the same time.
transform hf41:
    hopfocus(300)
transform hf42:
    hopfocus(740)
transform hf43:
    hopfocus(1179)
transform hf44:
    hopfocus(1620)
transform hf31:
    hopfocus(360)
transform hf32:
    hopfocus(960)
transform hf33:
    hopfocus(1560)
transform hf21:
    hopfocus(600)
transform hf22:
    hopfocus(1320)
transform hf11:
    hopfocus(960)

# These transforms makes the character dip down the screen, then come back up.
transform d41:
    dip(300)
transform d42:
    dip(740)
transform d43:
    dip(1179)
transform d44:
    dip(1620)
transform d31:
    dip(360)
transform d32:
    dip(960)
transform d33:
    dip(1560)
transform d21:
    dip(600)
transform d22:
    dip(1320)
transform d11:
    dip(960)

# These transforms makes the character fly in from the left.
transform l41:
    leftin(300)
transform l42:
    leftin(740)
transform l43:
    leftin(1179)
transform l44:
    leftin(1620)
transform l31:
    leftin(360)
transform l32:
    leftin(960)
transform l33:
    leftin(1560)
transform l21:
    leftin(600)
transform l22:
    leftin(1320)
transform l11:
    leftin(960)

# These transforms makes the character fly in from the right.
transform r41:
    rightin(300)
transform r42:
    rightin(740)
transform r43:
    rightin(1179)
transform r44:
    rightin(1620)
transform r31:
    rightin(360)
transform r32:
    rightin(960)
transform r33:
    rightin(1560)
transform r21:
    rightin(600)
transform r22:
    rightin(1320)
transform r11:
    rightin(960)

# This transform acts as in your eyes are opening up to see where you are at.
transform face(z=0.60, y=850):
    subpixel True
    xcenter 960
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

# This transform fades the screen for CGs to be shown/hidden.
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

# This transform causes Natsuki to wiggle on screen when she panics in her closet CG.
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

# This transform loop repeats the wiggle effect each second.
transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

# This transform causes Natsuki's face to be very close to your face during her 
# closet CG route.
transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200

# This variable defines the effect used by 'dissolve' by characters.
define dissolve = Dissolve(0.25)

# These variables define Dissolve(X) for CGs and scenes.
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# This variable makes the screen dissolve itself to black to show another scene later.
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# This variable dissolves the screen for a bit then shows the next scene afterwards.
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# This variable makes the screen shut to black; like your eyes closing themselves.
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# This variable makes the screen show the scene in return; like your eyes opening themselves.
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# This variable makes the screen instantly hide to black.
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

# This variable makes the current character hide by wiping their sprite off-screen to the left.
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

# This variable makes the current scene wipe to black from the left, then shows another scene.
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

# This variable makes the current character hide by wiping their sprite off-screen to the right.
define wiperight = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True)

# This variable makes the current scene wipe to black from the right, then shows another scene.
define wiperight_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    True])

# This variable is possibly a left-over from DDLC's development.
# This variable pauses the game for .25 seconds.
define tpause = Pause(0.25)

# This image transform causes a noise animation to play out.
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

# This transform causes the noise effect to appear 25% transparent.
transform noise_alpha:
    alpha 0.25

# This transform causes the noise effect to appear for a bit then disappear.
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

# This image adds a vignette image for a vignette effect.
image vignette:
    truecenter
    "images/bg/vignette.png"

# This transform has the vignette effect fade in.
transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

# This transform has the vignette effect flicker on-screen.
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

# This transform causes the screen layer to flicker.
transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

# This transform applies the rewind effect seen in Act 2.
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

# These transforms applies a heartbeat effect on-the screen in some random
# playthroughs of DDLC.
transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

# This transform and function controls the animation of Yuri's eyes
# moving during Act 2.
transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

# This transform makes the character appear on top with a transparency 
# for a bit during Act 2.
transform malpha(a=1.00):
    i11
    alpha a
