image _mon_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.065
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.095
        paths.monika("blink", "blink_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.monika("blink", "blink_am")
        0.015
        paths.monika("eyes", "forward","e4a")
        0.035
        paths.monika("blink", "blink_am")
        0.015
    repeat

image _mon_blink_l_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.065
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.095
        paths.monika("blink", "blink_l_am")
        0.015
    choice:
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        paths.monika("blink", "blink_l_am")
        0.015
        paths.monika("blink", "blink_l_af")
        0.035
        paths.monika("blink", "blink_l_am")
        0.015
    repeat

layeredimage monika forward: #All definitions are for her facing forward.
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="monika", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    always paths.monika("bases", "forward", "face")  #We always use the basic face.
  
    group autofocus_coloring:
        attribute day default null
        attribute dawn null
        attribute sunset null
        attribute night null
        attribute evening null
    
    group outfit:
        
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    
    
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            paths.monika("bases", "forward", "uniform_left_down")
        attribute ldown default if_any(["casual"]):
            paths.monika("bases", "forward", "casual_left_down")
        attribute lpoint if_any(["uniform"]):
            paths.monika("bases", "forward", "uniform_left_point")
        attribute lpoint if_any(["casual"]):
            paths.monika("bases", "forward","casual_left_point")
    
    
    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            paths.monika("bases", "forward","uniform_right_down")
        attribute rdown default if_any(["casual"]):
            paths.monika("bases", "forward","casual_right_down")
        attribute rhip if_any(["uniform"]):
            paths.monika("bases", "forward","uniform_right_hip")
        attribute rhip if_any(["casual"]):
            paths.monika("bases", "forward","casual_right_hip")
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.monika("nose", "forward", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.monika("nose", "forward", "n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.monika("nose", "forward", "n3")
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            paths.monika("nose", "forward", "n4")
        
        
        #All noses - truncated tags:
        attribute n1:
            paths.monika("nose", "forward", "n1")
        attribute n2:
            paths.monika("nose", "forward", "n2")
        attribute n3:
            paths.monika("nose", "forward", "n3")
        attribute n4:
            paths.monika("nose", "forward", "n4")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv"]):
            paths.monika("mouth", "forward","ma")
        attribute cm default if_any(["neut","worr","anno","dist","doub"]):
            paths.monika("mouth", "forward","md")
        attribute cm default if_any(["lsur","curi"]):
            paths.monika("mouth", "forward","me")
        attribute cm default if_any(["vsur","pout"]):
            paths.monika("mouth", "forward","mf")
        attribute cm default if_any(["shoc"]):
            paths.monika("mouth", "forward","mi")
        attribute cm default if_any(["cry","sad","angr","flus"]):
            paths.monika("mouth", "forward","mj")
        attribute cm default if_any(["vang","pani"]):
            paths.monika("mouth", "forward","mm")
        attribute cm default if_any(["laug","sedu"]):
            paths.monika("mouth", "forward","mn")
        attribute cm default if_any(["yand"]):
            paths.monika("mouth", "forward","mo")
        
        #Open Mouths:
        attribute om if_any(["happ","sedu"]):
            paths.monika("mouth", "forward","mb")
        attribute om if_any(["nerv","yand","laug"]):
            paths.monika("mouth", "forward","mc")
        attribute om if_any(["neut","dist"]):
            paths.monika("mouth", "forward","me")
        attribute om if_any(["worr","vsur","pout"]):
            paths.monika("mouth", "forward","mg")
        attribute om if_any(["anno","flus"]):
            paths.monika("mouth", "forward","mh")
        attribute om if_any(["lsur","curi"]):
            paths.monika("mouth", "forward","mi")
        attribute om if_any(["sad"]):
            paths.monika("mouth", "forward","mk")
        attribute om if_any(["cry","shoc"]):
            paths.monika("mouth", "forward","ml")
        attribute om if_any(["vang","angr","doub","pani"]):
            paths.monika("mouth", "forward","mq")
        
        
        ###All mouths - truncated tags:
        attribute ma:
            paths.monika("mouth", "forward","ma")
        attribute mb:
            paths.monika("mouth", "forward","mb")
        attribute mc:
            paths.monika("mouth", "forward","mc")
        attribute md:
            paths.monika("mouth", "forward","md")
        attribute me:
            paths.monika("mouth", "forward","me")
        attribute mf:
            paths.monika("mouth", "forward","mf")
        attribute mg:
            paths.monika("mouth", "forward","mg")
        attribute mh:
            paths.monika("mouth", "forward","mh")
        attribute mi:
            paths.monika("mouth", "forward","mi")
        attribute mj:
            paths.monika("mouth", "forward","mj")
        attribute mk:
            paths.monika("mouth", "forward","mk")
        attribute ml:
            paths.monika("mouth", "forward","ml")
        attribute mm:
            paths.monika("mouth", "forward","mm")
        attribute mn:
            paths.monika("mouth", "forward","mn")
        attribute mo:
            paths.monika("mouth", "forward","mo")
        attribute mp:
            paths.monika("mouth", "forward","mp")
        attribute mq:
            paths.monika("mouth", "forward","mq")
        attribute mr:
            paths.monika("mouth", "forward","mr")
    
    
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]):
            paths.monika("eyes", "forward","e1a")
        attribute oe default if_any(["worr","flus","dist"]):
            paths.monika("eyes", "forward","e1b")
        attribute oe default if_any(["anno","angr","sedu","doub"]):
            paths.monika("eyes", "forward","e1d")
        attribute oe default if_any(["cry"]):
            paths.monika("eyes", "forward","e1g")
        attribute oe default if_any(["vang","vsur","lsur"]):
            paths.monika("eyes", "forward","e2a")
        attribute oe default if_any(["nerv"]):
            paths.monika("eyes", "forward","e2b")
        attribute oe default if_any(["pani","shoc"]):
            paths.monika("eyes", "forward","e2d")
        attribute oe default if_any(["yand"]):
            paths.monika("eyes", "forward","e3a")
        
        #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr"]):
            paths.monika("eyes", "forward","e4a")#
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub"]):
            paths.monika("eyes", "forward","e4b")#
        attribute ce if_any(["cry"]):
            paths.monika("eyes", "forward","e4e")
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            paths.monika("eyes", "forward","e1a")
        attribute e1b:
            paths.monika("eyes", "forward","e1b")
        attribute e1c:
            paths.monika("eyes", "forward","e1c")
        attribute e1d:
            paths.monika("eyes", "forward","e1d")
        attribute e1e:
            paths.monika("eyes", "forward","e1e")
        attribute e1f:
            paths.monika("eyes", "forward","e1f")
        attribute e1g:
            paths.monika("eyes", "forward","e1g")
        attribute e1h:
            paths.monika("eyes", "forward","e1h")
        attribute e2a:
            paths.monika("eyes", "forward","e2a")
        attribute e2b:
            paths.monika("eyes", "forward","e2b")
        attribute e2c:
            paths.monika("eyes", "forward","e2c")
        attribute e2d:
            paths.monika("eyes", "forward","e2d")
        attribute e3a:
            paths.monika("eyes", "forward","e3a")
        attribute e3b:
            paths.monika("eyes", "forward","e3b")
        attribute e4a:
            paths.monika("eyes", "forward","e4a")
        attribute e4b:
            paths.monika("eyes", "forward","e4b")
        attribute e4c:
            paths.monika("eyes", "forward","e4c")
        attribute e4d:
            paths.monika("eyes", "forward","e4d")
        attribute e4e:
            paths.monika("eyes", "forward","e4e")
        attribute e0a:
            paths.monika("eyes", "forward","e0a")
        attribute e0b:
            paths.monika("eyes", "forward","e0b")


    group blink:
        
        attribute blink default null
        attribute no_blink null

    if persistent.blinking:
        "_mon_blink_a" if_all "blink" if_not(["ce","e4a","e4b","e4c","e4d","e4f","e4e","e1e","e1f"])
    else:
        Null()
    
    
    group brows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand"]):
            paths.monika("brows", "forward","b1a")#
        attribute brow default if_any(["cry","worr","shoc","laug","sad","flus","pani","worr","nerv"]):
            paths.monika("brows", "forward","b1b")#
        attribute brow default if_any(["anno","sedu"]):
            paths.monika("brows", "forward","b1c")#
        attribute brow default if_any(["vang","angr"]):
            paths.monika("brows", "forward","b1e")#
        attribute brow default if_any(["lsur"]):
            paths.monika("brows", "forward","b2b")#
        attribute brow default if_any(["vsur"]):
            paths.monika("brows", "forward","b2a")#
        attribute brow default if_any(["dist","pout"]):
            paths.monika("brows", "forward","b1d")#
        attribute brow default if_any(["curi"]):
            paths.monika("brows", "forward","b1f")#
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["doub"]) if_all(["oe"]) if_not(["ce"]):
            paths.monika("brows", "forward","b1f")#
        attribute brow default if_any(["doub"]) if_all(["ce"]) if_not(["oe"]):
            paths.monika("brows", "forward","b3b")#
        
        
        #All eyebrows - truncated tags:
        attribute b1a:
            paths.monika("brows", "forward","b1a")
        attribute b1b:
            paths.monika("brows", "forward","b1b")
        attribute b1c:
            paths.monika("brows", "forward","b1c")
        attribute b1d:
            paths.monika("brows", "forward","b1d")
        attribute b1e:
            paths.monika("brows", "forward","b1e")
        attribute b1f:
            paths.monika("brows", "forward","b1f")
        attribute b2a:
            paths.monika("brows", "forward","b2a")
        attribute b2b:
            paths.monika("brows", "forward","b2b")
        attribute b2c:
            paths.monika("brows", "forward","b2c")
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.monika("brows", "forward","b3a")
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.monika("brows", "forward","b3b")
        attribute b3c if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.monika("brows", "forward","b3c")
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
    
        attribute s_scream:
            paths.monika("bases", "forward","special_scream")



layeredimage monika lean:
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="monika", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute happ default null #happy
        attribute angr null #angry
        attribute anno null #annoyed
        attribute neut null #neutral
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute bful null #attribute bful null #full face blush.
    
    
    
    group body:
        attribute body default if_any(["uniform"]):
            paths.monika("bases", "lean","uniform_body")
        attribute body default if_any(["casual"]):
            paths.monika("bases", "lean","casual_body")
    
    
    
    group head:
        attribute head default if_any(["uniform"]):
            paths.monika("bases", "lean","uniform_face")
        attribute head default if_any(["casual"]):
            paths.monika("bases", "lean","casual_face")
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.monika("nose", "lean","n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.monika("nose", "lean","n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.monika("nose", "lean","n3")
        attribute nose default if_any(["blaw"]):#default nose when both "blushing" and "awkward"
            paths.monika("nose", "lean","n4")
        attribute nose default if_any(["bful"]):#full face blush, obscures eyes/eyebrows.
            paths.monika("nose", "lean","n5")
        
        
        #All noses - truncated tags:
        attribute n1:
            paths.monika("nose", "lean","n1")
        attribute n2:
            paths.monika("nose", "lean","n2")
        attribute n3:
            paths.monika("nose", "lean","n3")
        attribute n4:
            paths.monika("nose", "lean","n4")
        attribute n5:
            paths.monika("nose", "lean","n5")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ"]):
            paths.monika("mouth", "lean","m1")
        attribute cm default if_any(["neut","angr","anno"]):
            paths.monika("mouth", "lean","m4")
        
        #Open Mouths:
        attribute om if_any(["neut","angr","anno"]):
            paths.monika("mouth", "lean","m2")
        attribute om if_any(["happ"]):
            paths.monika("mouth", "lean","m3")
        
        
        #All mouths - truncated tags:
        attribute m1:
            paths.monika("mouth", "lean","m1")
        attribute m2:
            paths.monika("mouth", "lean","m2")
        attribute m3:
            paths.monika("mouth", "lean","m3")
        attribute m4:
            paths.monika("mouth", "lean","m4")
    
    
    
    group eyes if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        ##Default Opened eyes:
        attribute oe default if_any(["happ","neut"]):
            paths.monika("eyes", "lean","e1")
        attribute oe default if_any(["anno"]):
            paths.monika("eyes", "lean","e2")
        attribute oe default if_any(["angr"]):
            paths.monika("eyes", "lean","e3")
        
        #Default Closed eyes:
        attribute ce if_any(["happ"]):
            paths.monika("eyes", "lean","e4")
        attribute ce if_any(["neut","angr","anno"]):
            paths.monika("eyes", "lean","e5")
        
        
        #All eyes - truncated tags:
        attribute e1:
            paths.monika("eyes", "lean","e1")
        attribute e2:
            paths.monika("eyes", "lean","e2")
        attribute e3:
            paths.monika("eyes", "lean","e3")
        attribute e4:
            paths.monika("eyes", "lean","e4")
        attribute e5:
            paths.monika("eyes", "lean","e5")
        attribute e6:
            paths.monika("eyes", "lean","e6")
    
    
    
    group brows if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        #Default Eyebrows:
        attribute brow default if_any(["happ","neut"]):
            paths.monika("brows", "lean","b1")
        attribute brow default if_any(["angr","anno"]):
            paths.monika("brows", "lean","b2")
        
        
        #All eyebrows - truncated tags:
        attribute b1:
            paths.monika("brows", "lean","b1")
        attribute b2:
            paths.monika("brows", "lean","b2")
        attribute b3:
            paths.monika("brows", "lean","b3")