# Keyboard bindings.

# First we load keymap for current terminal type.
autoload -Uz zkbd
#source $HOME/.zkbd/$TERM-$VENDOR-$OSTYPE || DISPLAY= zkbd

# `Home` and `End` keys are used from time to time.
#bindkey ${key[Home]} vi-beginning-of-line
#bindkey ${key[End]} vi-end-of-line

# I like fast search feature. This way I need to type a few first letters of a
# command and just press `Up` or `Down` to look through history filtered
# by the prefix.
#bindkey ${key[Up]} up-line-or-search
#bindkey ${key[Down]} down-line-or-search

