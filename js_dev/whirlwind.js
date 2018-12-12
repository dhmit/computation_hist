let number = [];
document.getElementById('cur_num').innerHTML = 0;
function add_num(p1) {
    number.push(p1);
    if (document.getElementById('cur_num').innerHTML == 0) {
        document.getElementById('cur_num').innerHTML = p1
    }
    else {
        document.getElementById('cur_num').innerHTML += p1
    }
}
function tabulate() {
    let number_rev = number.reverse();
    let true_number = 0;
    let i;
    for (i = 0; i < number_rev.length; i++) {
        true_number += number_rev[i] * (10**i);
    }
    document.getElementById("bin_num").innerHTML = (true_number >>> 0).toString(2);
    document.getElementById('cur_num').innerHTML = 0;
    number = [];
}
function reset() {
    document.getElementById('cur_num').innerHTML = 0;
    number = [];
}
document.getElementById("butt_0").onclick = function() {add_num(0)};
document.getElementById("butt_1").onclick = function() {add_num(1)};
document.getElementById("butt_2").onclick = function() {add_num(2)};
document.getElementById("butt_3").onclick = function() {add_num(3)};
document.getElementById("butt_4").onclick = function() {add_num(4)};
document.getElementById("butt_5").onclick = function() {add_num(5)};
document.getElementById("butt_6").onclick = function() {add_num(6)};
document.getElementById("butt_7").onclick = function() {add_num(7)};
document.getElementById("butt_8").onclick = function() {add_num(8)};
document.getElementById("butt_9").onclick = function() {add_num(9)};
document.getElementById("store").onclick = function() {tabulate()};
document.getElementById("reset").onclick = function() {reset()};