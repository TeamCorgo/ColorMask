import { writable } from 'svelte/store';

export let envServerAddress = "http://10.101.0.6:9000/";
export let currentPage = writable('attract');


// Create a writable store to hold the intervals
export const intervals = writable([]);

// Function to add a new interval to the store
export function addInterval(interval) {
    // Update the intervals store by pushing the new intervalId to the existing array
    intervals.update(currentIntervals => [...currentIntervals, interval]);
}

// Function to delete all intervals from the store
export function deleteIntervals() {
    // Clear all intervals in the store by clearing each interval and updating the store with an empty array
    intervals.update(currentIntervals => {
        currentIntervals.forEach(intervalId => clearInterval(intervalId));
        return [];
    });
}

export function setPage(page) {
    currentPage.set(page);
}
