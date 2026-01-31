import { writable } from 'svelte/store';

export let currentPage = writable('login');

export function setPage(page) {
    currentPage.set(page);
}
