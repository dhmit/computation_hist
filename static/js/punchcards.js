'use strict';

const BINARY_DICT = {a:'1010', b:'1001', c:'0001'};

export function character_to_binary_string(character) {
    let new_string = "";
    let i = 0;
    for (i; i < character.length; i++) {
        if (character[i] in BINARY_DICT){
            new_string += BINARY_DICT[character[i]]
        }
    }
    return new_string;

}