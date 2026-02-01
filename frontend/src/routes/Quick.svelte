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


  onMount(() => {
      document.title = "Color Mask | Create Account";
      localStorage.removeItem("Token");

      if (localStorage.getItem("Dev")) {
          envServerAddress = "http://10.101.0.6:9000/";
      }

      const interval = setInterval(() => {
        colorIndex = (colorIndex + 1) % colors.length;
        bgColor = colors[colorIndex];
      }, 1000);

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
  class="bg-transition flex items-center justify-center h-screen"
  style="background-color: {bgColor};"
>
  <div class="flex flex-col items-center">

  <h1 class="text-white text-[6rem] font-bold drop-shadow-lg mb-16 z-10 stroke-black select-none">
    Color Mask
  </h1>

    <div class="bg-white p-8 rounded-lg shadow-md w-[36rem]">
        <h1 class="text-2xl font-semibold mb-6">Quick Play</h1>
        <p class="text-gray-600 mb-4 text-center max-w-md">
          Jump straight into the game without a username. You will be unable to resume this character in the future.
        </p>

        <form on:submit={handleSubmit}>
            <div class="mb-4 flex justify-end">
              <button type="submit"
                class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Play
              </button>
            </div>
        </form>
    </div>
  </div>
</div>
