// this is a sample javascript file for JS development




function go() {

    console.log(current_highlight)
    $('.highlighted').addClass("highlighted_2")
    $('.highlighted').removeClass("highlighted")


    $(current_highlight).addClass("highlighted")

}
function remove(){
    $('.highlighted').removeClass("highlighted")
    $('.highlighted_2').removeClass("highlighted_2")
}


function nonexec(){
    current_highlight='.non_executable_statements';
    console.log(current_highlight);
}

function termination(){
    current_highlight='.termination';
}
function execution(){
    current_highlight='.execution';
}
function intrinsic(){
    current_highlight='.intrinsic';
}
function local_var(){
    current_highlight='.local_var';
}
function start() {
    console.log(current_highlight)
    $('#go_btn').on('click', go);
    $('#remove_btn').on('click', remove);
    $('#nonexec_btn').on('click', nonexec);
    $('#termination_btn').on('click', termination);
    $('#execution_btn').on('click', execution);
    $('#intrinsic_btn').on('click', intrinsic);
    $('#local_var_btn').on('click', local_var);


}

$(document).ready(start);
var current_highlight="global";
console.log(current_highlight)