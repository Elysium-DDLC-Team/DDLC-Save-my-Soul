# Custom Movie Screen
# Source: https://www.reddit.com/r/RenPy/comments/oqwubr/how_do_you_make_it_so_that_the_user_cannot/

## Without skipping
screen custommoviescreen():
    add Movie(size=(1920,1080))
    on "show" action Play("movie", movieplaying, loop=False)
    on "hide" action Stop("movie")

    timer 0.1 repeat True action If(movielength > 0.0, true=(SetVariable('movielength', movielength - 0.1)), false=(Return(0)))


## With skipping
screen custommoviescreen_skipping():
    add Movie(size=(1920,1080))
    on "show" action Play("movie", movieplaying, loop=False)
    on "hide" action Stop("movie")

    timer 0.1 repeat True action If(movielength > 0.0, true=(SetVariable('movielength', movielength - 0.1)), false=(Return(0)))

    textbutton "Skip":
        action Return(0)
        sensitive (not renpy.get_screen("say"))
        align (.95,.95)