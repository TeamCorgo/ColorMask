<script>
  import { onMount } from "svelte";
  import { setPage } from "../store";

  function randomString(length) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
  }

  let username = "";
  let data = {}; // keep as object
  let envServerAddress = "http://104.251.216.28:9000/";

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

  let colorIndex = 0;
  let bgColor = colors[colorIndex];

  const text = "Color Mask";
  let charColors = Array(text.length).fill(colors[0]); // initial colors

  // Function to randomize color for a character
  function randomColor() {
    return colors[Math.floor(Math.random() * colors.length)];
  }


  onMount(() => {
      document.title = "Color Mask | Home";
      localStorage.removeItem("Token");

      if (localStorage.getItem("Dev")) {
          envServerAddress = "http://10.101.0.6:9000/";
      }

      const interval = setInterval(() => {
        colorIndex = (colorIndex + 1) % colors.length;
        bgColor = colors[colorIndex];
      }, 2500);


  // Set up independent timers for each character
  text.split("").forEach((_, i) => {
    setInterval(() => {
      charColors[i] = randomColor();
    }, 500 + Math.random() * 1500); // random interval per character
  });

      return () => clearInterval(interval);
  });

  async function handleSubmit(event) {
    event.preventDefault();
    username = randomString(8);
    data = {};

    try {
      const response = await fetch(`${envServerAddress}account/create`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username }),
      });
      
      data = await response.json();
      localStorage.setItem("Token", data.token);
      setPage("game");
    } catch (err) {
      data = { detail: "Error: " + err.message };
    }
  }
</script>

<div
  class="bg-transition flex items-center justify-center min-h-[100dvh]"
  style="background-color: {bgColor};"
>
  <div class="flex flex-col items-center">

    <h1 class="text-[9rem] font-bold drop-shadow-lg mb-16 z-10 stroke-black select-none">
      {#each text.split("") as char, i}
        <span class="char" style="color: {charColors[i]}">{char}</span>
      {/each}
    </h1>

    <div class="bg-white p-8 rounded-lg shadow-md w-[36rem]">
      <h1 class="text-2xl font-semibold mb-6">
        <a href="https://globalgamejam.org/" target="_blank" class="text-blue-500 hover:underline">
          GGJ
        </a> 2026 Topic: Mask
      </h1>
      <p class="mb-4 max-w-md">
        A color mask refers to a way of filtering, isolating, or modifying colors in an image or graphic.
      </p>

      <hr class="my-6 border-gray-300">

      <h1 class="text-2xl font-semibold mb-6">How to play:</h1>
      <p class="mb-4 max-w-md">
        Move around the grid painting squares with the color of your mask. The map origin 
        <span class="font-bold text-pink-500">Pink</span> of X:0, Y:0 allows players to change their color mask. 
        The map origin cannot be painted. Players are unable to step into squares of opposing colors. 
        Example: a <span class="font-bold text-red-500">Red</span> masked player is unable to enter a 
        <span class="font-bold text-green-500">Green</span> colored square, or 
        <span class="font-bold text-yellow-400">Yellow</span> onto 
        <span class="font-bold text-purple-500">Purple</span>.
      </p>


      <form on:submit={handleSubmit}>
          <div class="mb-4 flex justify-end">
            <button type="submit"
              class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
            Quick Play
            </button>
          </div>
      </form>

      <div
        on:click={() => setPage("login")}
        class="text-blue-500 hover:underline cursor-pointer"
        >Log into an existing account</div
      >
      <div
        on:click={() => setPage("create")}
        class="text-blue-500 hover:underline cursor-pointer"
        >Create an account</div
      >
    </div>
  </div>
</div>
