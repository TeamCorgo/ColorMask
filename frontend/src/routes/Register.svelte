<script>
  import { envServerAddress } from "../store";
  import {setPage} from "../store";

  let username = "";
  let response = {}; // keep as object

  async function register() {
    response = {};

    if (!username) {
      response.detail = "Please enter a username.";
      return;
    }

    try {
      const res = await fetch(
        `${envServerAddress}account/register?username=${encodeURIComponent(username)}`,
        {
          method: "POST",
          headers: { "Accept": "application/json" },
          body: "" // empty body like your curl
        }
      );

      const data = await res.json();
      response = data;

      //response = data; // keep as object
    } catch (err) {
      response = { shield: "Error: " + err.message };
    }
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
  {#if !response.token}
    <h1 class="text-3xl font-bold mb-4">Register</h1>

    <input
      type="text"
      placeholder="Enter username"
      bind:value={username}
      class="border p-2 mb-2 rounded"
    />

    <button
      on:click={register}
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
    >
      Register
    </button>
  {/if}



  <!-- Display Responses -->
  {#if response.detail}
    <p class="mt-4 p-2 border rounded bg-red-200">{response.detail}</p>
  {/if}

  {#if response.token}
    <h1 class="text-3xl font-bold mb-4">
      This is your username/password, keep it in a safe place!
    </h1>
    <div class="mt-4 flex mb-4 items-center gap-2 p-2 border rounded bg-green-200">
      <span class="flex-1 break-all">{response.token}</span>
    </div>
    <button
      on:click={() => setPage('login')}
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
    >
      Login
    </button>
  {/if}
</main>
