import { writable } from 'svelte/store';

export let currentPage = writable('login');

// Default IP
export let envServerAddress = "http://104.251.216.28:9000/";

// Override if "Dev" exists in localStorage
if (localStorage.getItem("Dev")) {
    envServerAddress = "http://10.101.0.6:9000/";
}
export function setPage(page) {
    currentPage.set(page);
}
