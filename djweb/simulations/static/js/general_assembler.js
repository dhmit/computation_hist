const newline_regex = /\r\n|[\n\v\f\r\x85\u2028\u2029]/;
const GENERAL_ASSEMBLER = 1;
const computer_size = 8192;

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

function start() {
    general_start();
    computer.general_memory[101].fixed_point = 1;
    expand_text_area("code_box");
    update();
}