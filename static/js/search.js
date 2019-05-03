'use strict';

export function setup_refine_search() {

    const refine_author = $("a[id^='refine_author:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_author) {
        console.log(el.id);
    }

    const refine_recipient = $("a[id^='refine_recipient:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_recipient) {
        console.log(el.id);
    }

    const refine_cced = $("a[id^='refine_cced:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_cced) {
        console.log(el.id);
    }

    const refine_year = $("a[id^='refine_year:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_year) {
        console.log(el.id);
    }

}
