import { writable } from 'svelte/store';

export let currentPage = writable('home');

export function setPage(page) {
    currentPage.set(page);
}
