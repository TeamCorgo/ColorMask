<script>
  import { onMount } from 'svelte';
  import {setPage} from "../store";

  // Predefined Tailwind colors (or hex codes)
  const colors = [
    '#f87171', // red-400
    '#34d399', // green-400
    '#60a5fa', // blue-400
    '#facc15', // yellow-400
    '#a78bfa', // purple-400
    '#2dd4bf', // teal-400
    '#f472b6'  // pink-400
  ];

  let index = 0;
  let bgColor = colors[index];

  onMount(() => {
    const interval = setInterval(() => {
      index = (index + 1) % colors.length;
      bgColor = colors[index];
    }, 1000);

    return () => clearInterval(interval);
  });
</script>

<style>
  /* Smooth background transition */
  body, html {
    margin: 0;
    padding: 0;
    height: 100%;
  }

  .bg-transition {
    transition: background-color .1s ease;
  }

  .stroke-black {
    -webkit-text-stroke: 2px black; /* for Chrome/Safari */
    text-stroke: 2px black; /* for other browsers that support it */
  }
</style>

<div class="w-screen h-screen flex flex-col items-center justify-center transition-colors duration-500" style="background-color: {bgColor};">
  <h1 class="text-white text-[12rem] font-bold drop-shadow-lg text-center mb-4 stroke-black">
    Color Mask
  </h1>
<p 
  class="text-white text-sm underline cursor-pointer" 
  on:click={() => setPage('create')}
>
  Link to create
</p>
</div>