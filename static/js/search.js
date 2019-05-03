'use strict';

export function start() {
    const advanced_search = $('#advanced_search');
    const adv_search_link = $('#show_advanced_search');
    advanced_search.hide();
    adv_search_link.click(() => {
        advanced_search.show();
        adv_search_link.remove();
    });
    setup_refine_search();
}

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
