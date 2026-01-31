import { writable } from 'svelte/store';

export let currentPage = writable('login');

// Set the IP based on localStorage "Prod"
export let envServerAddress = localStorage.getItem("Dev")
    ? "http://10.101.0.6:9000/"
    : "http://104.251.216.28:9000/";


export function setPage(page) {
    currentPage.set(page);
}
