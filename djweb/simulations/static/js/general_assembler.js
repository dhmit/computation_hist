const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;

/**
 * Attaches an event listener to a textarea that allows it to dynamically resize as you type in it.
 * From https://stackoverflow.com/questions/37629860/automatically-resizing-textarea-in-bootstrap.
 *
 * @param {string} id   Id of textarea to attach event listener to.
 */
function expand_text_area(id) {
    document.getElementById(id).addEventListener('keyup', function() {
        this.style.overflow = 'hidden';
        this.style.height = 0;
        this.style.height = this.scrollHeight + 'px';
    }, false);
}

/**
 * Assembles code from code box into program which is placed in computer.
 */
function assemble() {
    code = document.getElementById("code_box").value;
    code_lines = code.split(newline_regex);
    computer.assemble(0, code_lines);
    update();
}

function start() {
    general_start();
    computer.general_memory[4].fixed_point = 12;
    computer.general_memory[5].fixed_point = 30;

    create_memory_display();
    expand_text_area("code_box");
    update();
}

$(document).ready(start);