layeredimage yuri turned:
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="yuri", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    always paths.yuri("bases", "turned", "face")
  
    group autofocus_coloring:
        attribute day default null
        attribute dawn null
        attribute sunset null
        attribute night null
        attribute evening null
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
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
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        #attribute bful null #full face blush.  Currently unused for her turned pose.
    
    
    
    group left:
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        #uniform
        attribute ldown default if_any(["uniform"]):
            paths.yuri("bases", "turned", "uniform_left_down")
        attribute lup if_any(["rup","rcut"]) if_all(["uniform"]):
            paths.yuri("bases", "turned", "uniform_left_up")
        
        #casual
        attribute ldown default if_any(["casual"]):
            paths.yuri("bases", "turned", "casual_left_down")
        attribute lup if_any(["rup","rcut"]) if_all(["casual"]):
            paths.yuri("bases", "turned", "casual_left_up")
    
    
    
    group right:
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            paths.yuri("bases", "turned", "uniform_right_down")
        attribute rup if_any(["uniform"]):
            paths.yuri("bases", "turned", "uniform_right_up")
        attribute rcut if_any(["uniform"]):
            paths.yuri("bases", "turned", "uniform_right_cut")
        
        
        attribute rdown default if_any(["casual"]):
            paths.yuri("bases", "turned", "casual_right_down")
        attribute rup if_any(["casual"]):
            paths.yuri("bases", "turned", "casual_right_up")
    
    
    
    group left:#This is here a second time to deal with if the right half of Yuri is shown only down; the left half of her with her arm up has to render over the right half.
        #anchor (0,0)
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        #uniform
        attribute lup if_not(["rup","rcut"]) if_all(["uniform"]):
            paths.yuri("bases", "turned", "uniform_left_up")
        
        #casual
        attribute lup if_not(["rup","rcut"]) if_all(["casual"]):
            paths.yuri("bases", "turned", "casual_left_up")
    
    
    
    group nose:
        
        anchor (0,0) subpixel (True)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.yuri("nose", "turned", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.yuri("nose", "turned", "n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.yuri("nose", "turned", "n3")
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            paths.yuri("nose", "turned", "n4")
        
        
        ###All noses - truncated tags:
        attribute n1:
            paths.yuri("nose", "turned", "n1")
        attribute n2:
            paths.yuri("nose", "turned", "n2")
        attribute n3:
            paths.yuri("nose", "turned", "n3")
        attribute n4:
            paths.yuri("nose", "turned", "n4")
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","laug"]):
            paths.yuri("mouth", "turned", "ma")
        attribute cm default if_any(["neut","lsur","worr"]):
            paths.yuri("mouth", "turned", "md")#
        attribute cm default if_any(["sedu"]):
            paths.yuri("mouth", "turned", "me")
        attribute cm default if_any(["pout","curi"]):
            paths.yuri("mouth", "turned", "mf")
        attribute cm default if_any(["shoc"]):
            paths.yuri("mouth", "turned", "mg")
        attribute cm default if_any(["dist","anno","vsur","sad","angr","cry","doub"]):
            paths.yuri("mouth", "turned", "mj")
        attribute cm default if_any(["nerv","flus"]):
            paths.yuri("mouth", "turned", "mk")
        attribute cm default if_any(["vang","pani"]):
            paths.yuri("mouth", "turned", "mm")
        attribute cm default if_any(["yand"]):
            paths.yuri("mouth", "turned", "mo")
        
        #Open Mouths:
        attribute om if_any(["happ"]):
            paths.yuri("mouth", "turned", "mb")
        attribute om if_any(["laug","nerv","yand"]):
            paths.yuri("mouth", "turned", "mc")
        attribute om if_any(["worr","pout"]):
            paths.yuri("mouth", "turned", "me")
        attribute om if_any(["sedu"]):
            paths.yuri("mouth", "turned", "mf")
        attribute om if_any(["dist","lsur","angr","cry"]):
            paths.yuri("mouth", "turned", "mg")
        attribute om if_any(["neut","anno","vsur","curi"]):
            paths.yuri("mouth", "turned", "mh")
        attribute om if_any(["flus","doub"]):
            paths.yuri("mouth", "turned", "mi")
        attribute om if_any(["sad"]):
            paths.yuri("mouth", "turned", "mk")
        attribute om if_any(["vang","shoc","pani"]):
            paths.yuri("mouth", "turned", "ml")
        
        
        ###All mouths - truncated tags:
        attribute ma:
            paths.yuri("mouth", "turned", "ma")
        attribute mb:
            paths.yuri("mouth", "turned", "mb")
        attribute mc:
            paths.yuri("mouth", "turned", "mc")
        attribute md:
            paths.yuri("mouth", "turned", "md")
        attribute me:
            paths.yuri("mouth", "turned", "me")
        attribute mf:
            paths.yuri("mouth", "turned", "mf")
        attribute mg:
            paths.yuri("mouth", "turned", "mg")
        attribute mh:
            paths.yuri("mouth", "turned", "mh")
        attribute mi:
            paths.yuri("mouth", "turned", "mi")
        attribute mj:
            paths.yuri("mouth", "turned", "mj")
        attribute mk:
            paths.yuri("mouth", "turned", "mk")
        attribute ml:
            paths.yuri("mouth", "turned", "ml")
        attribute mm:
            paths.yuri("mouth", "turned", "mm")
        attribute mn:
            paths.yuri("mouth", "turned", "mn")
        attribute mo:
            paths.yuri("mouth", "turned", "mo")
        attribute mp:
            paths.yuri("mouth", "turned", "mp")
        attribute mq:
            paths.yuri("mouth", "turned", "mq")
        attribute mr:
            paths.yuri("mouth", "turned", "mr")
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","sedu"]):
            paths.yuri("eyes", "turned", "e1a")
        attribute oe default if_any(["dist","worr"]):
            paths.yuri("eyes", "turned", "e1b")
        attribute oe default if_any(["happ","angr","pout","curi"]):
            paths.yuri("eyes", "turned", "e1d")
        attribute oe default if_any(["cry"]):
            paths.yuri("eyes", "turned", "e1h")
        attribute oe default if_any(["lsur","vang"]):
            paths.yuri("eyes", "turned", "e2a")
        attribute oe default if_any(["anno","flus","laug","sad"]):
            paths.yuri("eyes", "turned", "e2b")
        attribute oe default if_any(["nerv","doub"]):
            paths.yuri("eyes", "turned", "e2c")
        attribute oe default if_any(["shoc","pani","vsur"]):
            paths.yuri("eyes", "turned", "e2d")
        attribute oe default if_any(["yand"]):
            paths.yuri("eyes", "turned", "e3a")
        
        #Default Closed eyes:
        attribute ce if_any(["dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            paths.yuri("eyes", "turned", "e4a")
        attribute ce if_any(["neut","happ","yand","pani","laug","sedu","pout"]):
            paths.yuri("eyes", "turned", "e4b")
        attribute ce if_any(["cry"]):
            paths.yuri("eyes", "turned", "e4e")
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            paths.yuri("eyes", "turned", "e1a")
        attribute e1b:
            paths.yuri("eyes", "turned", "e1b")
        attribute e1c:
            paths.yuri("eyes", "turned", "e1c")
        attribute e1d:
            paths.yuri("eyes", "turned", "e1d")
        attribute e1e:
            paths.yuri("eyes", "turned", "e1e")
        attribute e1f:
            paths.yuri("eyes", "turned", "e1f")
        attribute e1g:
            paths.yuri("eyes", "turned", "e1g")
        attribute e1h:
            paths.yuri("eyes", "turned", "e1h")
        attribute e2a:
            paths.yuri("eyes", "turned", "e2a")
        attribute e2b:
            paths.yuri("eyes", "turned", "e2b")
        attribute e2c:
            paths.yuri("eyes", "turned", "e2c")
        attribute e2d:
            paths.yuri("eyes", "turned", "e2d")
        attribute e3a:
            paths.yuri("eyes", "turned", "e3a")
        attribute e3b:
            paths.yuri("eyes", "turned", "e3b")
        attribute e4a:
            paths.yuri("eyes", "turned", "e4a")
        attribute e4b:
            paths.yuri("eyes", "turned", "e4b")
        attribute e4c:
            paths.yuri("eyes", "turned", "e4c")
        attribute e4d:
            paths.yuri("eyes", "turned", "e4d")
        attribute e4e:
            paths.yuri("eyes", "turned", "e4e")
        attribute e0a:
            paths.yuri("eyes", "turned", "e0a")
        attribute e0b:
            paths.yuri("eyes", "turned", "e0b")
        attribute ela:
            paths.yuri("eyes", "turned", "ela")
        attribute elb:
            paths.yuri("eyes", "turned", "elb")
    
    
    
    group brows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut"]):
            paths.yuri("brows", "turned", "b1a")
        attribute brow default if_any(["flus","lsur","laug"]):
            paths.yuri("brows", "turned", "b1b")
        attribute brow default if_any(["dist","sedu"]):
            paths.yuri("brows", "turned", "b1c")
        attribute brow default if_any(["anno"]):
            paths.yuri("brows", "turned", "b1d")
        attribute brow default if_any(["vang","angr"]):
            paths.yuri("brows", "turned", "b1e")
        attribute brow default if_any(["curi","doub"]):
            paths.yuri("brows", "turned", "b1f")
        attribute brow default if_any(["happ"]):
            paths.yuri("brows", "turned", "b2a")
        attribute brow default if_any(["worr","sad","nerv","cry"]):
            paths.yuri("brows", "turned", "b2b")
        attribute brow default if_any(["yand","shoc","vsur","pani"]):
            paths.yuri("brows", "turned", "b2c")
        attribute brow default if_any(["pout"]):
            paths.yuri("brows", "turned", "b3b")
        
        
        ###All eyebrows - truncated tags:
        #This first set of definitions has only the logic to exclude certain eyebrows for particular large eye Yuri expressions.
        attribute b1a:
            paths.yuri("brows", "turned", "b1a")
        attribute b1b:
            paths.yuri("brows", "turned", "b1b")
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b1c")
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b1d")
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b1e")
        attribute b1f:
            paths.yuri("brows", "turned", "b1f")
        attribute b2a:
            paths.yuri("brows", "turned", "b2a")
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b2b")
        attribute b2c:
            paths.yuri("brows", "turned", "b2c")
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b3a")
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            paths.yuri("brows", "turned", "b3b")
        attribute b3c:
            paths.yuri("brows", "turned", "b3c")
        
        
        #This second set allows those above eyebrows to render on problematic moods...so long as their eyes are closed.
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b1c")
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b1d")
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b1e")
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b2b")
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b3a")
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            paths.yuri("brows", "turned", "b3b")
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        anchor (0,0) subpixel (True)
        
        attribute s_scream:
            paths.yuri("bases", "turned", "special_scream")



layeredimage yuri shy:
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="yuri", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    always paths.yuri("bases", "shy", "face")
    

    group outfit:
        
        anchor (0,0) subpixel (True)
        attribute uniform default:
            paths.yuri("bases", "shy", "uniform_body")
        attribute casual:
            paths.yuri("bases", "shy", "casual_body")
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute happ null #happy
        attribute sad null  #sad
    
    
    
    group blush:
        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    group nose:
        
        anchor (0,0) subpixel (True)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.yuri("nose", "shy", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.yuri("nose", "shy", "n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.yuri("nose", "shy", "n3")
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            paths.yuri("nose", "shy", "n4")
        attribute nose default if_any(["bful"]):#Full face blush
            paths.yuri("nose", "shy", "n5")
        
        
        ###All noses - truncated tags:
        attribute n1:
            paths.yuri("nose", "shy", "n1")
        attribute n2:
            paths.yuri("nose", "shy", "n2")
        attribute n3:
            paths.yuri("nose", "shy", "n3")
        attribute n4:
            paths.yuri("nose", "shy", "n4")
        attribute n5:
            paths.yuri("nose", "shy", "n5")
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        #default closed mouths
        attribute cm default if_any(["neut"]):
            paths.yuri("mouth", "shy", "m1")
        attribute cm default if_any(["angr","sad"]):
            paths.yuri("mouth", "shy", "m2")
        attribute cm default if_any(["happ"]):
            paths.yuri("mouth", "shy", "m3")
        
        #default open mouth.  As of this writing...she only has one open mouth.
        attribute om:
            paths.yuri("mouth", "shy", "m4")
        
        
        #All mouths - truncated tags:
        attribute m1:
            paths.yuri("mouth", "shy", "m1")
        attribute m2:
            paths.yuri("mouth", "shy", "m2")
        attribute m3:
            paths.yuri("mouth", "shy", "m3")
        attribute m4:
            paths.yuri("mouth", "shy", "m4")
    
    
    
    group eyes if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        
        #Open eyes
        attribute oe default if_any(["happ"]):
            paths.yuri("eyes", "shy", "e1")
        attribute oe default if_any(["neut"]):
            paths.yuri("eyes", "shy", "e2")
        attribute oe default if_any(["angr"]):
            paths.yuri("eyes", "shy", "e3")
        attribute oe default if_any(["sad"]):
            paths.yuri("eyes", "shy", "e4")
        
        #Closed eyes
        attribute ce if_any(["angr","neut","happ"]):
            paths.yuri("eyes", "shy", "e5")
        attribute ce if_any(["sad"]):
            paths.yuri("eyes", "shy", "e6")
        
        
        #All eyes - truncated tags:
        attribute e1:
            paths.yuri("eyes", "shy", "e1")
        attribute e2:
            paths.yuri("eyes", "shy", "e2")
        attribute e3:
            paths.yuri("eyes", "shy", "e3")
        attribute e4:
            paths.yuri("eyes", "shy", "e4")
        attribute e5:
            paths.yuri("eyes", "shy", "e5")
        attribute e6:
            paths.yuri("eyes", "shy", "e6")
    
    
    
    group brows if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["happ"]):
            paths.yuri("brows", "shy", "b1")
        attribute brow default if_any(["neut","sad"]):
            paths.yuri("brows", "shy", "b2")
        attribute brow default if_any(["angr"]):
            paths.yuri("brows", "shy", "b3")
        
        
        #all brows - truncated:
        attribute b1:
            paths.yuri("brows", "shy", "b1")
        attribute b2:
            paths.yuri("brows", "shy", "b2")
        attribute b3:
            paths.yuri("brows", "shy", "b3")



