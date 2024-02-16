layeredimage sayori turned: #turned definitions.
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="sayori", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    always paths.sayori("bases", "turned", "face") #Always need this face.
   
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
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    
    
    
    #Left arm variants
    group left if_any(["uniform"]):
        attribute ldown default:
            paths.sayori("bases", "turned", "uniform_left_down")
        attribute lup:
            paths.sayori("bases", "turned", "uniform_left_up")
    
    group left if_any(["casual"]):
        attribute ldown default:
            paths.sayori("bases", "turned", "casual_left_down")
        attribute lup:
            paths.sayori("bases", "turned", "casual_left_up")
    
    
    
    #Right arm variants
    group right if_any(["uniform"]):
        attribute rdown default:
            paths.sayori("bases", "turned", "uniform_right_down")
        attribute rup:
            paths.sayori("bases", "turned", "uniform_right_up")
    
    group right if_any(["casual"]):
        attribute rdown default:
            paths.sayori("bases", "turned", "casual_right_down")
        attribute rup:
            paths.sayori("bases", "turned", "casual_right_up")
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.sayori("nose", "turned", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.sayori("nose", "turned", "n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.sayori("nose", "turned", "n3")
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            paths.sayori("nose", "turned", "n4")
        
        
        #All noses - truncated tags:
        attribute n1:
            paths.sayori("nose", "turned", "n1")
        attribute n2:
            paths.sayori("nose", "turned", "n2")
        attribute n3:
            paths.sayori("nose", "turned", "n3")
        attribute n4:
            paths.sayori("nose", "turned", "n4")
        attribute nl:
            paths.sayori("nose", "turned", "nl")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            paths.sayori("", "turned", "ma")
        attribute cm default if_any(["neut","anno","worr","curi"]):
            paths.sayori("mouth", "turned", "md")
        attribute cm default if_any(["dist","flus"]):
            paths.sayori("mouth", "turned", "me")
        attribute cm default if_any(["lsur","shoc"]):
            paths.sayori("mouth", "turned", "mf")
        attribute cm default if_any(["sad","angr","pout","doub"]):
            paths.sayori("mouth", "turned", "mj")
        attribute cm default if_any(["cry","pani","vsur"]):
            paths.sayori("mouth", "turned", "mk")
        attribute cm default if_any(["vang"]):
            paths.sayori("mouth", "turned", "mm")
        attribute cm default if_any(["laug"]):
            paths.sayori("mouth", "turned", "mn")
        attribute cm default if_any(["yand"]):
            paths.sayori("mouth", "turned", "mo")
        
        #Open Mouths:
        attribute om if_any(["happ","laug"]):
            paths.sayori("mouth", "turned", "mb")
        attribute om if_any(["yand","nerv"]):
            paths.sayori("mouth", "turned", "mc")
        attribute om if_any(["pout","sedu"]):
            paths.sayori("mouth", "turned", "mf")
        attribute om if_any(["sad","lsur","dist"]):
            paths.sayori("mouth", "turned", "mg")
        attribute om if_any(["neut","anno","shoc","worr"]):
            paths.sayori("mouth", "turned", "mh")
        attribute om if_any(["curi","doub"]):
            paths.sayori("mouth", "turned", "mi")
        attribute om if_any(["flus"]):
            paths.sayori("mouth", "turned", "mk")
        attribute om if_any(["cry","vsur"]):
            paths.sayori("mouth", "turned", "ml")
        attribute om if_any(["angr","pani","vang"]):
            paths.sayori("mouth", "turned", "mq")
        
        
        ###All mouths - truncated tags:
        attribute ma:
            paths.sayori("mouth", "turned", "ma")
        attribute mb:
            paths.sayori("mouth", "turned", "mb")
        attribute mc:
            paths.sayori("mouth", "turned", "mc")
        attribute md:
            paths.sayori("mouth", "turned", "md")
        attribute me:
            paths.sayori("mouth", "turned", "me")
        attribute mf:
            paths.sayori("mouth", "turned", "mf")
        attribute mg:
            paths.sayori("mouth", "turned", "mg")
        attribute mh:
            paths.sayori("mouth", "turned", "mh")
        attribute mi:
            paths.sayori("mouth", "turned", "mi")
        attribute mj:
            paths.sayori("mouth", "turned", "mj")
        attribute mk:
            paths.sayori("mouth", "turned", "mk")
        attribute ml:
            paths.sayori("mouth", "turned", "ml")
        attribute mm:
            paths.sayori("mouth", "turned", "mm")
        attribute mn:
            paths.sayori("mouth", "turned", "mn")
        attribute mo:
            paths.sayori("mouth", "turned", "mo")
        attribute mp:
            paths.sayori("mouth", "turned", "mp")
        attribute mq:
            paths.sayori("mouth", "turned", "mq")
        attribute mr:
            paths.sayori("mouth", "turned", "mr")
    
    
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad"]):
            paths.sayori("eyes", "turned", "e1a")
        attribute oe default if_any(["dist","worr","pout"]):
            paths.sayori("eyes", "turned", "e1b")
        attribute oe default if_any(["anno","sedu","doub"]):
            paths.sayori("eyes", "turned", "e1d")
        attribute oe default if_any(["cry"]):
            paths.sayori("eyes", "turned", "e1g")
        attribute oe default if_any(["lsur","flus","vsur","curi"]):
            paths.sayori("eyes", "turned", "e2a")
        attribute oe default if_any(["nerv"]):
            paths.sayori("eyes", "turned", "e2b")
        attribute oe default if_any(["pani","vang","shoc"]):
            paths.sayori("eyes", "turned", "e2d")
        attribute oe default if_any(["yand"]):
            paths.sayori("eyes", "turned", "e3a")
        
        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            paths.sayori("eyes", "turned", "e4a")
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            paths.sayori("eyes", "turned", "e4b")
        attribute ce if_any(["vang","flus","pani"]):
            paths.sayori("eyes", "turned", "e4c")
        attribute ce if_any(["cry"]):
            paths.sayori("eyes", "turned", "e4d")
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            paths.sayori("eyes", "turned", "e1a")
        attribute e1b:
            paths.sayori("eyes", "turned", "e1b")
        attribute e1c:
            paths.sayori("eyes", "turned", "e1c")
        attribute e1d:
            paths.sayori("eyes", "turned", "e1d")
        attribute e1e:
            paths.sayori("eyes", "turned", "e1e")
        attribute e1f:
            paths.sayori("eyes", "turned", "e1f")
        attribute e1g:
            paths.sayori("eyes", "turned", "e1g")
        attribute e1h:
            paths.sayori("eyes", "turned", "e1h")
        attribute e2a:
            paths.sayori("eyes", "turned", "e2a")
        attribute e2b:
            paths.sayori("eyes", "turned", "e2b")
        attribute e2c:
            paths.sayori("eyes", "turned", "e2c")
        attribute e2d:
            paths.sayori("eyes", "turned", "e2d")
        attribute e3a:
            paths.sayori("eyes", "turned", "e3a")
        attribute e3b:
            paths.sayori("eyes", "turned", "e3b")
        attribute e4a:
            paths.sayori("eyes", "turned", "e4a")
        attribute e4b:
            paths.sayori("eyes", "turned", "e4b")
        attribute e4c:
            paths.sayori("eyes", "turned", "e4c")
        attribute e4d:
            paths.sayori("eyes", "turned", "e4d")
        attribute e4e:
            paths.sayori("eyes", "turned", "e4e")
        attribute e0a:
            paths.sayori("eyes", "turned", "e0a")
        attribute e0b:
            paths.sayori("eyes", "turned", "e0b")
    
    
    
    group brows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc"]):
            paths.sayori("brows", "turned", "b1a")
        attribute brow default if_any(["sad","cry","pani","yand","nerv"]):
            paths.sayori("brows", "turned", "b1b")
        attribute brow default if_any(["laug","vsur","worr","sedu"]):
            paths.sayori("brows", "turned", "b1c")
        attribute brow default if_any(["anno","pout"]):
            paths.sayori("brows", "turned", "b1d")
        attribute brow default if_any(["angr","vang"]):
            paths.sayori("brows", "turned", "b1e")
        attribute brow default if_any(["curi","doub"]):
            paths.sayori("brows", "turned", "b1f")
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            paths.sayori("brows", "turned", "b2a")
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            paths.sayori("brows", "turned", "b3c")
        
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            paths.sayori("brows", "turned", "b1a")
        attribute b1b:
            paths.sayori("brows", "turned", "b1b")
        attribute b1c:
            paths.sayori("brows", "turned", "b1c")
        attribute b1d:
            paths.sayori("brows", "turned", "b1d")
        attribute b1e:
            paths.sayori("brows", "turned", "b1e")
        attribute b1f:
            paths.sayori("brows", "turned", "b1f")
        attribute b2a:
            paths.sayori("brows", "turned", "b2a")
        attribute b2b:
            paths.sayori("brows", "turned", "b2b")
        attribute b2c:
            paths.sayori("brows", "turned", "b2c")
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.sayori("brows", "turned", "b3a")
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.sayori("brows", "turned", "b3b")
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            paths.sayori("brows", "turned", "b3c")
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        attribute s_scream:
            paths.sayori("bases", "turned", "special_scream")



layeredimage sayori tap: #tapping definitions.
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at AutofocusDisplayable(name="sayori", AutofocusDropShadow_blur=20, AutofocusColoring=True)
    
    group outfit:
        attribute uniform default:
            paths.sayori("bases", "tapping", "uniform_body")
        attribute casual:
            paths.sayori("bases", "tapping", "casual_body")
    
    always paths.sayori("bases", "tapping", "face")
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute nerv default null #nervous
        attribute angr null #angry
        attribute dist null #distant
        attribute neut null #neutral
        attribute pout null #pouting
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #no blush applied.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            paths.sayori("nose", "tapping", "n1")
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            paths.sayori("nose", "tapping", "n2")
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            paths.sayori("nose", "tapping", "n3")
        attribute nose default if_any(["blaw"]):#default nose when "blushing" and "awkward"
            paths.sayori("nose", "tapping", "n4")
        attribute nose default if_any(["bful"]):#default nose when "blushing" and "awkward"
            paths.sayori("nose", "tapping", "n5")
        
        #All noses - truncated tags:
        attribute n1:
            paths.sayori("nose", "tapping", "n1")
        attribute n2:
            paths.sayori("nose", "tapping", "n2")
        attribute n3:
            paths.sayori("nose", "tapping", "n3")
        attribute n4:
            paths.sayori("nose", "tapping", "n4")
        attribute n5:
            paths.sayori("nose", "tapping", "n5")
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["pout"]):
            paths.sayori("mouth", "tapping", "m2")
        attribute cm default if_any(["neut","nerv","angr","dist"]):
            paths.sayori("mouth", "tapping", "m3")
        
        #Open Mouths:
        attribute om if_any(["nerv"]):
            paths.sayori("mouth", "tapping", "m1")
        attribute om if_any(["neut","pout","angr","dist"]):
            paths.sayori("mouth", "tapping", "m4")
        
        
        #All mouths - truncated tags:
        attribute m1:
            paths.sayori("mouth", "tapping", "m1")
        attribute m2:
            paths.sayori("mouth", "tapping", "m2")
        attribute m3:
            paths.sayori("mouth", "tapping", "m3")
        attribute m4:
            paths.sayori("mouth", "tapping", "m4")
    
    
    
    group eyes if_not(["n5","bful"]):
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","nerv"]):
            paths.sayori("eyes", "tapping", "e1")
        attribute oe default if_any(["pout","dist"]):
            paths.sayori("eyes", "tapping", "e2")
        attribute oe default if_any(["angr"]):
            paths.sayori("eyes", "tapping", "e5")
        
        #Default Closed eyes:
        attribute ce if_any(["neut","nerv","pout","angr","dist"]):
            paths.sayori("eyes", "tapping", "e6")
        
        
        #All eyes - truncated tags:
        attribute e1:
            paths.sayori("eyes", "tapping", "e1")
        attribute e2:
            paths.sayori("eyes", "tapping", "e2")
        attribute e3:
            paths.sayori("eyes", "tapping", "e3")
        attribute e4:
            paths.sayori("eyes", "tapping", "e4")
        attribute e5:
            paths.sayori("eyes", "tapping", "e5")
        attribute e6:
            paths.sayori("eyes", "tapping", "e6")
    
    
    
    group brows if_not(["n5","bful"]):
        
        #Default Eyebrows:
        attribute brow default if_any(["neut"]):
            paths.sayori("brows", "tapping", "b3")
        attribute brow default if_any(["nerv","dist"]):
            paths.sayori("brows", "tapping", "b1")
        attribute brow default if_any(["pout","angr"]):
            paths.sayori("brows", "tapping", "b2")
        
        
        #All eyebrows - truncated tags:
        attribute b1:
            paths.sayori("brows", "tapping", "b1")
        attribute b2:
            paths.sayori("brows", "tapping", "b2")
        attribute b3:
            paths.sayori("brows", "tapping", "b3")



