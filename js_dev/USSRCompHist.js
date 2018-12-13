/* This document runs an interactive infographic. It is associated with an html
document USSRCompHist.html and an image titled USSR_outline.jpg */
function move_forward() {
// this function will control the forward button to scroll through the main page as view events
// associated with different periods of time
}

function move_back() {
// this function will control the back button to scroll through the main page as view events
// associated with different periods of time
}

function display_page(){
// this function will display a new page with more information when the info buttons are clicked
}

function start() {
    $('#forward').on('click', move_forward);
    $('#cybernetics').on('click', display_page);
    $('#military tech').on('click', display_page);
    $('#secret computers').on('click', display_page);
}

$(document).ready(start);