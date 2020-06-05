# This is the base of my Zshell configuration.
# To install this configuration, symlink this file to ~/.zshrc:
#
#     ln -s ~/.config/zsh/zshrc ~/.zshrc
#
# This file just loads all `*.zsh` files from `~/.zsh` directory.
# Please don't modify it directly, put your custom config files into `~/.zsh`
# with appropriate name and `zsh` extension.
#

POWERLEVEL9K_MODE=nerdfont-complete
POWERLEVEL9K_USER_DEFAULT_BACKGROUND='005'
POWERLEVEL9K_USER_DEFAULT_FOREGROUND='000'
POWERLEVEL9K_OS_ICON_BACKGROUND='000'
POWERLEVEL9K_OS_ICON_FOREGROUND='004'
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon user dir)

POWERLEVEL9K_BATTERY_HIDE_ABOVE_THRESHOLD=100
POWERLEVEL9K_DISABLE_RPROMPT=false
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(battery)



for conf in ~/.config/zsh/*.zsh; do
    source $conf
done

source /usr/share/zsh-theme-powerlevel9k/powerlevel9k.zsh-theme
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

