import { writable } from 'svelte/store';

export let envServerAddress = "http://10.101.0.6:9000/";
export let currentPage = writable('login');

export function setPage(page) {
    currentPage.set(page);
}
