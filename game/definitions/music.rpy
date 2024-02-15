## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

## Non-Cyberpunk 2077 OST

## Cyberpunk 2077 Base OST
define audio.adsm = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/AdamSmasher.mp3"
define audio.atl = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/Atlantis.mp3"
define audio.bgtky = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/BeenGoodtoKnowYa.mp3"
define audio.bolb = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/BellsofLagunaBend.mp3"
define audio.cp = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/CloseProbing.mp3"
define audio.cd = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/CloudyDay.mp3"
define audio.cdi = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/CodeRedInitiated.mp3"
define audio.cc = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/ConsumerCathedral.mp3"
define audio.cdddtm = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/CrackDeDamDownTheMiddle.mp3"
define audio.cn = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/Cyberninja.mp3"
define audio.cwlp = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/CyberwildlifePark.mp3"
define audio.dl = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/DreamsLost.mp3"
define audio.ea = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/ExtractionAction.mp3"
define audio.gk9 = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/GateK9.mp3"
define audio.hny = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/HanakoAndYorinobu.mp3"
define audio.ju = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/JuicedUp.mp3"
define audio.ktd = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/KangTaoDown.mp3"
define audio.mm = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/MiningMinds.mp3"
define audio.ma = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/ModernAnthill.mp3"
define audio.mus = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/Musorshchiki.mp3"
define audio.nfa = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/NeverFadeAwaySAMURAICover.mp3"
define audio.onm = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/OutsiderNoMore.mp3"
define audio.prdis = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/Patri_di_ots.mp3"
define audio.rop = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/RiteOfPassage.mp3"
define audio.sh = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/ScavengerHunt.mp3"
define audio.sf = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/Streetfighters.mp3"
define audio.th = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheHeist.mp3"
define audio.tmic = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheManInCharge.mp3"
define audio.trp = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheRebelPath.mp3"
define audio.tgbp = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheresGonnaBeaParade.mp3"
define audio.tsatp = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheSacredAndTheProfane.mp3"
define audio.tsalag = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheStreetsAreLong-AssGutters.mp3"
define audio.tsac = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheSuitsAreScared.mp3"
define audio.tvimh = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TheVoiceInMyHead.mp3"
define audio.thab = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/ToHellAndBack.mp3"
define audio.tl = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TowerLockdown.mp3"
define audio.tft = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/TroubleFindsTrouble.mp3"
define audio.ub = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/UrbanDownunder.mp3"
define audio.v = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/V.mp3"
define audio.wd = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/WushuDolls.mp3"
define audio.ysnhtfma = "mod_assets/audio/music/mainstory/cp2077_ost/base_ost/YouShallNeverHaveToForgiveMeAgain.mp3"
