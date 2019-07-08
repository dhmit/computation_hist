'use strict';

import { timer } from "./simulator.js";

export class Renderer {
    constructor(computer) {
        this.computer = computer; // an IBM_704 instance
        this.highlighting = true;
    }
    
    /**
     * Produces HTML for all the general memory registers of the computer.
     */
    create_memory_display() {
        const general_memory_display = document.getElementById("general_memory_div");
        for (let i = 0; i < this.computer.size; i++) {
            let element = $(`
                <div class="row general_memory_row">
                      <div class="col-2">
                             <p class="line_no_text">${i.toString()}: </p>
                      </div>
                      <div class="col-10">
                             <span class="general_memory number" id="general_memory_${i.toString()}" 
                             data-toggle="tooltip"></span>
                      </div>
               </div>
            `)[0];
            general_memory_display.appendChild(element);
        }
    }

    /**
     * Update the display of the computer's memory.
     */
    async update_computer_display(highlighted_registers = []) { // jshint ignore:line
        const general_memory_html = $(".general_memory");
        for (let i = 0; i < this.computer.size; i++) {
            const new_value = this.computer.general_memory[i].toString();
            if (new_value !== general_memory_html[i].innerHTML) {
                if (this.highlighting && general_memory_html[i].innerHTML !== "") {
                    general_memory_html[i].classList.add("changed");
                }
                general_memory_html[i].innerHTML = new_value;
                let title_text = "Instruction: " + this.computer.general_memory[i].instruction.toString();
                title_text += "\r\nFixed Point: " + this.computer.general_memory[i].fixed_point;
                title_text += "\r\nFloating Point: " + this.computer.general_memory[i].floating_point;
                general_memory_html[i].setAttribute("data-original-title", title_text);
            }
        }

        const instruction_location_counter_element = $("#instruction_location_counter")[0];
        if (parseInt(instruction_location_counter_element.innerHTML, 2) !== this.computer.ilc.valueOf() - 1 && instruction_location_counter_element.innerHTML !== "" && this.highlighting) {
            instruction_location_counter_element.classList.add("changed");
        } else {
            instruction_location_counter_element.classList.remove("changed");
        }
        instruction_location_counter_element.innerHTML = this.computer.ilc.toString();
        const ilc_text = "Location: " + this.computer.ilc.valueOf();
        instruction_location_counter_element.title = ilc_text;
        instruction_location_counter_element.setAttribute("data-original-title", ilc_text);
        
        const instruction_register_element = $("#instruction_register")[0];
        if (instruction_register_element.innerHTML !== this.computer.instruction_register.toString()) {
            instruction_register_element.innerHTML = this.computer.instruction_register.toString();
            instruction_register_element.title = "Operation: " + this.computer.instruction_register.get_instruction_str();
            instruction_register_element.setAttribute("data-original-title", instruction_register_element.title);
        }

        const storage_register_element = $("#storage_register")[0];
        if (storage_register_element.innerHTML !== this.computer.storage_register.toString()) {
            storage_register_element.innerHTML = this.computer.storage_register.toString();
            storage_register_element.title = "Instruction: " + this.computer.storage_register.instruction.toString();
            storage_register_element.title += "\r\nFixed Point: " + this.computer.storage_register.fixed_point;
            storage_register_element.title += "\r\nFloating Point: " + this.computer.storage_register.floating_point;
            storage_register_element.setAttribute("data-original-title", storage_register_element.title);
        }

        const accumulator_element = $("#accumulator")[0];
        if (accumulator_element.innerHTML !== this.computer.accumulator.toString()) {
            if (this.highlighting && accumulator_element.innerHTML !== "") {
                accumulator_element.classList.add("changed");
            } else {
                accumulator_element.classList.remove("changed");
            }
            accumulator_element.innerHTML = this.computer.accumulator.toString();
            accumulator_element.title = "Fixed Point: " + this.computer.accumulator.fixed_point;
            accumulator_element.title += "\r\nFloating Point: " + this.computer.accumulator.floating_point;
            accumulator_element.setAttribute("data-original-title", accumulator_element.title);
        } else {
            accumulator_element.classList.remove("changed");
        }

        const mq_register_element = $("#mq_register")[0];
        if (mq_register_element.innerHTML !== this.computer.mq_register.toString()) {
            if (this.highlighting && mq_register_element.innerHTML !== "") {
                mq_register_element.classList.add("changed");
            } else {
                mq_register_element.classList.remove("changed");
            }
            mq_register_element.innerHTML = this.computer.mq_register.toString();
            mq_register_element.title = "Fixed Point: " + this.computer.mq_register.fixed_point;
            mq_register_element.title += "\r\nFloating Point: " + this.computer.mq_register.floating_point;
            mq_register_element.setAttribute("data-original-title", mq_register_element.title);
        } else {
            mq_register_element.classList.remove("changed");
        }

        const index_a_element = $("#index_a")[0];
        if (index_a_element.innerHTML !== this.computer.index_a.toString()) {
            if (this.highlighting && index_a_element.innerHTML !== "") {
                index_a_element.classList.add("changed");
            } else {
                index_a_element.classList.remove("changed");
            }
            index_a_element.innerHTML = this.computer.index_a.toString();
            index_a_element.title = "Value: " + this.computer.index_a.valueOf();
            index_a_element.setAttribute("data-original-title", index_a_element.title);
        } else {
            index_a_element.classList.remove("changed");
        }

        const index_b_element = $("#index_b")[0];
        if (index_b_element.innerHTML !== this.computer.index_b.toString()) {
            if (this.highlighting && index_b_element.innerHTML !== "") {
                index_b_element.classList.add("changed");
            } else {
                index_b_element.classList.remove("changed");
            }
            index_b_element.innerHTML = this.computer.index_b.toString();
            index_b_element.title = "Value: " + this.computer.index_b.valueOf();
            index_b_element.setAttribute("data-original-title", index_b_element.title);
        } else {
            index_b_element.classList.remove("changed");
        }

        const index_c_element = $("#index_c")[0];
        if (index_c_element.innerHTML !== this.computer.index_c.toString()) {
            if (this.highlighting && index_c_element.innerHTML !== "") {
                index_c_element.classList.add("changed");
            } else {
                index_c_element.classList.remove("changed");
            }
            index_c_element.innerHTML = this.computer.index_c.toString();
            index_c_element.title = "Value: " + this.computer.index_c.valueOf();
            index_c_element.setAttribute("data-original-title", index_c_element.title);
        } else {
            index_c_element.classList.remove("changed");
        }

        const changed_registers = $(".changed");
        changed_registers.addClass("blink");
        await timer(500); // jshint ignore:line
        changed_registers.removeClass("blink");

        general_memory_html.removeClass("next_instruction target_register special_highlight changed");
        const next_instruction_target = this.computer.general_memory[this.computer.ilc.valueOf()].instruction.address;
        if (this.highlighting) {
            for (let i = 0; i < this.computer.size; i++) {
                if (i === this.computer.ilc.valueOf()) {
                    general_memory_html[i].classList.add("next_instruction");
                } else if (i === next_instruction_target) {
                    general_memory_html[i].classList.add("target_register");
                } else if (highlighted_registers.includes(i)) {
                    general_memory_html[i].classList.add("special_highlight");
                }
            }
        }
    }


    reset(instructions, memory_value_pairs){
        this.computer.clear();
        const instruction_text = [];
        for (let i = 0; i < instructions.length; i++) {
            instruction_text.push(instructions[i].instruction);
        }
        this.computer.assemble(instruction_text);

        if (memory_value_pairs !== undefined) {
            for (const [memory_index, value] of memory_value_pairs) {
                this.computer.general_memory[memory_index].fixed_point = value;
            }
        }
    }
}


export class DemoRenderer extends Renderer {
    async update(instructions, num_code_lines, highlighted_registers = []) {

        await this.update_computer_display(highlighted_registers);

        const code_html = $(".code_line");
        code_html.removeClass("next_instruction");
        const code_line = this.computer.ilc.valueOf();
        if (code_line < num_code_lines && code_html.length !== 0) {
            if (this.highlighting) {
                code_html[code_line].classList.add("next_instruction");
            }
        }

        // update line descriptions
        let line_desc = "";
        if (typeof instructions[code_line] !== "undefined") {
            line_desc = instructions[code_line].description;
        }
        $('#line_desc')[0].innerHTML = line_desc;
    }
}


export class GeneralAssemblerRenderer extends Renderer {
    constructor(computer) {
        super(computer);
        this.num_lines = 0;
    }

    update() {
        const computer = this.computer;
        let line_desc = "Next Instruction to be Executed: ";
        line_desc += computer.general_memory[computer.ilc.valueOf()].instruction.toString();
        $('#line_desc')[0].innerHTML = line_desc;
        this.update_computer_display();
    }

    add_code_line() {
        const code = document.getElementById("code");

        const line = $(`
            <div class="row code_line" id="code_line_${this.num_lines}">
                  <div class="col-sm-1 pl-3 pr-2 line_no_text">
                         <p>${this.num_lines + 1}.</p>
                  </div>
                  <div class="col-sm-3 px-2" id="code_label_${this.num_lines}">
                         <textarea class="form-control code_box code_label" rows="1"></textarea>
                  </div>
                  <div class="col-sm-3 px-2" id="code_operation_${this.num_lines}">
                         <textarea class="form-control code_box code_operation" rows="1"></textarea>
                  </div>
                  <div class="col-sm-4 px-2" id="code_numbers_${this.num_lines}">
                         <textarea class="form-control code_box code_numbers" rows="1"></textarea>
                  </div>
           </div>
        `)[0];

        code.appendChild(line);
        this.num_lines++;
    }

    remove_code_line() {
        if (this.num_lines > 0) {
            const last_line_no = this.num_lines - 1;
            const last_line = document.getElementById("code_line_" + last_line_no.toString());
            last_line.remove();
            this.num_lines--;
        }
    }
}
