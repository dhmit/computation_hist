'use strict';

const CHAR_BINARY_PAIRS = {a: '101'};
CHAR_BINARY_PAIRS.a = '100';

export function character_to_binary_string(character) {
    // TODO: actually implement me!
    if (character === "numbers") {
        return "123";
    }
    else if (character === "letters") {
        return "abc";
    }
    return 'I do nothing yet';
}