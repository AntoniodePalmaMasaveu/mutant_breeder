#!/bin/bash
# print directory s
print_tree() {
    local max_depth="$1"
    local dir="$2"
    local prefix="$3"
    local depth="$4"

    [ "$depth" -gt "$max_depth" ] && return

    local files=()
    local dirs=()
    while IFS= read -r item; do
        if [ -d "$dir/$item" ]; then
            dirs+=("$item")
        else
            files+=("$item")
        fi
    done < <(ls "$dir")

    # Files first, then folders
    local all=("${files[@]}" "${dirs[@]}")
    local total=${#all[@]}

    for i in "${!all[@]}"; do
        local item="${all[$i]}"

        if [ "$i" -eq "$((total - 1))" ]; then
            echo "${prefix}└ ${item}"
            local new_prefix="${prefix} ${PREPREFIX}"
        else
            echo "${prefix}├ ${item}"
            local new_prefix="${prefix}│${PREPREFIX}"
        fi

        if [ -d "$dir/$item" ] && [ "$depth" -lt "$max_depth" ]; then
            print_tree "$max_depth" "$dir/$item" "$new_prefix" "$((depth + 1))"
        fi
    done
}

TARGET="${2:-$PWD}" 
SPACER="   "
PREPREFIX="${3:-"$SPACER"}"  

echo "> $(basename "$TARGET")"
print_tree "${1:-3}" "$TARGET" "$PREPREFIX" 1
