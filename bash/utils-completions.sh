#!/bin/bash

_complete_util_openscreen () {
  SCREENNAMES=$(screen -ls | sed "
    s/^.*\t\([0-9]\+\)\.\([^ \t\n]\+\)\t.*$/\1.\2/;
                                # match/extract (tab)pid.name(tab)
    t matched; d; :matched;     # if not matched then delete (skip pattern), else continue
    p;                          # print full pattern
    s/^[0-9]\+\.\(.*\)$/\1/;    # remove PID from the start (pid.name -> name)
    p; d;                       # print, then finish (don't print again)")
  COMPREPLY=($(compgen -W "$SCREENNAMES" $2))
}


_enable_util_completions () {
  complete -F _complete_util_openscreen openscreen
}


if [ "$1" = "i" ] || [ "$1" = "-i" ] || [ "$1" = "install" ] || [ "$1" = "--install" ]; then
  THISFILE=$(realpath ${0})
  if [ -z "$THISFILE" ]; then
    THISFILE=${0}; # if empty (command failed?), default to plain $0
  fi
  if [ ! -e "$THISFILE" ]; then
    # doesn't exist; bail
    echo "Cannot find this script reliably; failed."
  else
    echo "Found script at $THISFILE"

    WRITEFILE="/etc/bash_completion.d/hrm-utils"
    if [ -e "$WRITEFILE" ]; then
      echo "Moving existing file to .bak"
      mv "$WRITEFILE" "$WRITEFILE.bak"
    fi
    if printf '#!/bin/bash\n\n. '$THISFILE'\n_enable_util_completions\n' >$WRITEFILE; then
      echo "Done!"
    else
      echo "Failed write, should you be running as sudo?"
    fi
  fi
fi
