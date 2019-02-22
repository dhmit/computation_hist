const computer = new IBM_704(7); // this is the IBM 704
const num_code_lines = 3;
const general_memory_display = 7;
code_line = 0;

/**
 * Updates page to highlight correct line of code and display correct memory values.
 */
function update() {
    const code_html = $(".symbolic_code");
    code_html.removeClass("highlighted");
    code_html[code_line].className += " highlighted";

    const general_memory_html = $(".general_memory");
    for (let i = 0; i < general_memory_display; i++) {
        general_memory_html[i].innerHTML = computer.general_memory[i].toString();
    }

    general_memory_0 = $('#general_memory0')[0];
    general_memory_0.title = computer.general_memory[0].instruction_b.toString();
    general_memory_1 = $('#general_memory1')[0];
    general_memory_1.title = computer.general_memory[1].instruction_b.toString();
    general_memory_2 = $('#general_memory2')[0];
    general_memory_2.title = computer.general_memory[2].instruction_b.toString();
    general_memory_3 = $('#general_memory3')[0];
    general_memory_3.title = computer.general_memory[3].fixed_point;
    general_memory_4 = $('#general_memory4')[0];
    general_memory_4.title = computer.general_memory[4].fixed_point;
    general_memory_5 = $('#general_memory5')[0];
    general_memory_5.title = computer.general_memory[5].fixed_point;
    general_memory_6 = $('#general_memory6')[0];
    general_memory_6.title = computer.general_memory[6].fixed_point;


    instruction_location_counter_element = $("#instruction_location_counter")[0];
    instruction_location_counter_element.innerHTML = computer.ilc.toString();
    instruction_location_counter_element.title = computer.ilc.valueOf();

    $("#instruction_register").html(computer.instruction_register.toString());

    storage_register_element = $("#storage_register")[0];
    storage_register_element.innerHTML = computer.storage_register.toString();
    storage_register_element.title = (new General_Word(computer.storage_register)).fixed_point;

    accumulator_element = $("#accumulator")[0];
    accumulator_element.innerHTML = computer.accumulator.toString();
    accumulator_element.title = computer.accumulator.fixed_point;
}

/**
 * Steps through a single line of code indicated by the instruction location counter.
 */
function step() {
    if (code_line < num_code_lines && !computer.halt) {
        computer.step();
        code_line++;
        update();
    }
}

/**
 * Initializes ibm704_assembly_addition.html, including initializing register 3 of general memory to
 * 12 and register 4 of general memory to 30, and storing the set program into memory.
 */
function start() {
    $('#step_button').on('click', step);

    computer.general_memory[4].fixed_point = 12;
    computer.general_memory[5].fixed_point = 30;

    const code = $(".symbolic_code");
    const code_innerHTML = Array(code.length);
    for (let i = 0; i < num_code_lines; i++) {
        code_innerHTML[i] = code[i].innerHTML;
    }
    computer.assemble(0, code_innerHTML);
    update();
}

$(document).ready(start);
