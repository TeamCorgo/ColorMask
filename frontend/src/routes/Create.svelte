<script>
  import { onMount } from "svelte";
  import { setPage } from "../store";

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
  let bgColor = randomColor();

  const text = "Color Mask";
  let charColors = Array(text.length).fill(colors[0]); // initial colors

  // Function to randomize color for a character
  function randomColor() {
    return colors[Math.floor(Math.random() * colors.length)];
  }

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

      // random starting colors
      charColors = Array.from(
        { length: text.length },
        () => randomColor()
      );

      const id = setInterval(() => {
        const i = Math.floor(Math.random() * text.length);
        charColors[i] = randomColor();
        charColors = [...charColors];
      }, 250); // smoother look

      return () => clearInterval(id);
  });

  async function handleSubmit(event) {
    event.preventDefault();
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

    <h1 class="text-4xl sm:text-6xl md:text-8xl lg:text-[9rem] font-bold drop-shadow-lg mb-4 sm:mb-8 md:mb-16 z-10 stroke-black select-none">
      {#each text.split("") as char, i}
        <span class="char" style="color: {charColors[i]}">{char}</span>
      {/each}
    </h1>

    <div class="bg-white p-4 sm:p-6 md:p-8 rounded-lg shadow-md w-full max-w-sm sm:max-w-md md:max-w-2xl mx-4">
        {#if !data.token} 
        
        <h1 class="text-2xl font-semibold mb-6">Create your account</h1>
        <p class="text-gray-600 mb-4 text-center max-w-md">
          Registration is intentionally simple — no email, password, or personal
          information is required. Your secure token will act as your login, so be
          sure to store it somewhere safe.
        </p>
        <form on:submit={handleSubmit}>
            <div class="mb-4">
                <label
                    for="username"
                    class="block text-gray-700 font-medium mb-2">Username:</label
                >
                <input
                    type="text"
                    id="username"
                    bind:value={username}
                    required
                    class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-400"
                    placeholder="Enter desired username"
                />
            </div>

            <!-- Display errors & shields -->
            {#if data.detail} 
              <div class="mb-4 flex justify-center sm:justify-end">
                <div class="flex items-center bg-yellow-100 text-yellow-800 text-xs sm:text-sm font-medium px-3 sm:px-4 py-2 rounded-lg shadow-sm border border-yellow-200">
                  <span>{data.detail}</span>
                </div>
              </div>
            {/if}

            <div class="mb-4 flex justify-end">
              <button type="submit"
                class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Create Account
              </button>
            </div>
            <div
                on:click={() => setPage("home")}
                class="text-blue-500 hover:underline cursor-pointer"
                >Home Screen</div
            >
        </form>
        {/if}


        {#if data.token} 
        <h1 class="text-2xl font-semibold mb-6 text-center">Authentication Token</h1>

        <p class="font-mono text-sm sm:text-base md:text-xl text-center text-white bg-red-600 px-4 py-2 rounded-lg shadow-lg animate-pulse break-all">
          {data.token}
        </p>

        <p class="text-gray-600 mb-6 text-center max-w-md mx-auto">
          This token allows you to sign back into your account without needing private information (email, password, name).
        </p>

        <div class="flex flex-col items-center gap-4">
          <div class="w-16 sm:w-24 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
            <img
              src="https://api.dicebear.com/9.x/avataaars/svg?seed=corgo_{data.token}"
              alt="Avatar"
            />
          </div>
        </div>

        <div class="mb-4 flex justify-end">
          <button type="submit"
            on:click={() => setPage("login")}
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Login Screen
          </button>
        </div>
        {/if}
        

    </div>

  </div>
</div>
