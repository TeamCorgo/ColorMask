import { writable } from 'svelte/store';

export let envServerAddress = "http://10.101.0.6:9000/";
export let currentPage = writable('register');

export function setPage(page) {
    currentPage.set(page);
}
