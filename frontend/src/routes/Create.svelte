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
  class="bg-transition flex items-center justify-center h-screen"
  style="background-color: {bgColor};"
>
  <div class="flex flex-col items-center">

    <h1 class="text-white text-[6rem] font-bold drop-shadow-lg mb-16 z-10 stroke-black">
      Color Mask
    </h1>



    <div class="bg-white p-8 rounded-lg shadow-md w-[36rem]">
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
              <div class="mb-4 flex justify-end">
                <div class="flex items-center bg-yellow-100 text-yellow-800 text-sm font-medium px-4 py-2 rounded-lg shadow-sm border border-yellow-200">
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
            <span
              on:click={() => setPage("login")}
              class="text-blue-500 hover:underline cursor-pointer"
              >Log into an existing account</span
            >
        </form>
        {/if}


        {#if data.token} 
        <h1 class="text-2xl font-semibold mb-6 text-center">Authentication Token</h1>

        <p class="font-mono text-xl text-center text-white bg-red-600 px-4 py-2 rounded-lg shadow-lg animate-pulse">
          {data.token}
        </p>

        <p class="text-gray-600 mb-6 text-center max-w-md mx-auto">
          This token allows you to sign back into your account without needing private information (email, password, name).
        </p>

        <div class="flex flex-col items-center gap-4">
          <div class="w-24 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
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
