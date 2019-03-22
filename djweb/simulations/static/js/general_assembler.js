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
        this.style.height = this.scrollHeight + 'px';
    }, false);
}


function display_operations() {
    let operations = new Set();

    for (let operation in operation_b_to_no) {
        operations.add(operation);
    }

    for (let operation in operation_a_to_no) {
        operations.add(operation);
    }
    let string = Array.from(operations).join(", ");
    let place = document.getElementById("available_operations");
    place.innerText = string;
}

function assemble_from_code_box() {
    try {
        const code = document.getElementById("code_box").value;
        const code_lines = code.split(newline_regex);
        computer.assemble(0, code_lines);
    } catch (err) {
        computer.clear();
    }
}

/**
 * Runs scripts to initialize page.
 */
function start() {
    common_start();
    $('#assemble_button').on('click', () => {
        assemble_from_code_box();
        update();
    });
    $('#reset_button').on('click', ()=>{
        alert("cannot reset");
    });
    expand_text_area("code_box");
    display_operations();
    update();
}