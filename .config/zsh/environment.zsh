# Just an enviroment setup.

# I use **Vim** as my primary editor, `less` as a pager, **Chromium** with
# **Vimium** extension for browser experience.
export EDITOR="/usr/bin/vim"
export PAGER="/usr/bin/less"
export MANPAGER="/usr/bin/less"
export BROWSER="/usr/bin/firefox"
export LESS="-r -S"

# I like playing around with **NodeJS** sometimes.
export NODE_PATH="/usr/lib/node_modules"

# PATH extension.
export PATH="$HOME/.cargo/bin:/usr/lib/ruby/gems/1.9.1/bin:$HOME/.gem/ruby/2.3.0/bin:$PATH:$HOME/bin:/opt/android-sdk/platform-tools"

# This is for Android development.
export CLASSPATH=/opt/android-sdk/platforms/android-19/android.jar

# Locale. I prefer English messages in programs, but time format is best
# percieved in d/m/Y, not m/d/Y.
export LC_ALL=fr_FR.UTF-8
export LC_TIME=fr_FR.UTF-8

# Chrome & chromium options: move cache to tmpfs.
export CHROMIUM_USER_FLAGS="--disk-cache-dir=/tmp --disk-cache-size=50000000"
export CHROME_USER_FLAGS="$CHROMIUM_USER_FLAGS"

# This is the placement of todo.sh config file
export TODOTXT_CFG_FILE="$HOME/.config/todo/config"
