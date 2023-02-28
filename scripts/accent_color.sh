#!/bin/bash
# Change the accent color of blog.

input_file="../my_blog/blogcore/static/css/blogcore.css"
colors=("darkseagreen" "darksalmon" "darkviolet" "darkkhaki" \
"darkturquoise" "darkgoldenrod" "crimson" "lime" "slateblue" "fuchsia")
current_color=$(cat $input_file | head -n1 | cut -d " " -f 3)

usage=\
"\nList of accent colors: \n\
\n\t0 - darkseagreen \
\n\t1 - darksalmon \
\n\t2 - darkviolet \
\n\t3 - darkkhaki \
\n\t4 - darkturquoise \
\n\t5 - darkgoldenrod \
\n\t6 - crimson \
\n\t7 - lime \
\n\t8 - slateblue \
\n\t9 - fuchsia\n"

echo -e $usage
read -p "Pick accent color (0-9): " user_input

if [[ "$user_input" == [0-9] ]]; then
    picked_color=${colors[$user_input]}
fi


if [ -z "$picked_color" ]; then
    echo "wrong input, try again."
    exit 1
elif [ ! -w $input_file ]; then
    echo "file doesn't have write permission."
    exit 1
elif [[ "$picked_color" == "$current_color" ]]; then
    echo "$picked_color is already accent color."
    exit 0
else
    sed -i "s/$current_color/$picked_color/" $input_file
    echo "Successfully replaced."
    exit 0
fi

