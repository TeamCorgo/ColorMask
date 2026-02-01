<script>
    import { onMount } from "svelte";
    import { setPage } from "../store";

    let isLoading = false;
    let token = "";
    let data = {}
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
        document.title = "Color Mask | Login";

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
        if (isLoading) return;
        isLoading = true;

        try {
            const response = await fetch(envServerAddress + "account/protected", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
            });

            data = await response.json();
            if (response.status !== 200) {
                //console.log(response.statusText + ": " + data.detail);
                isLoading = false;
                return;
            }

            localStorage.setItem("Token", token);
            setPage("game");
            isLoading = false;
            // setPage("game");
        } catch (error) {
            console.error("Error:", error);
            // addToast({ type: "error", message: error.message }); // if you have a toast system
            setPage("login");
            isLoading = false;
        }
    }
</script>


<style>
.gridc {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
}
</style>


<div
  class="bg-transition flex items-center justify-center min-h-[100dvh]"
  style="background-color: {bgColor};"
>

    <div class="flex flex-col items-center">
        <h1 class="text-white text-[6rem] font-bold drop-shadow-lg mb-16 z-10 stroke-black select-none">
            Color Mask
        </h1>

        <div class="bg-white p-8 rounded-lg shadow-md w-96">
            <h1 class="text-2xl font-semibold mb-6">Login into your account</h1>

            {#if token}
                <div class="avatar flex items-center justify-center mb-4">
                    <div class="w-24 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
                        <img src="https://api.dicebear.com/9.x/avataaars/svg?seed=corgo_{token}" alt="Avatar" />
                    </div>
                </div>
            {/if}

            <form on:submit={handleSubmit}>
                <div class="mb-4">
                    <label for="token" class="block text-gray-700 font-medium mb-2">Token:</label>
                    <input
                        type="text"
                        id="token"
                        bind:value={token}
                        required
                        class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-400"
                        placeholder="Enter login token"
                    />
                </div>

                {#if data.detail} 
                  <div class="mb-4 flex justify-end">
                    <div class="flex items-center bg-yellow-100 text-yellow-800 text-sm font-medium px-4 py-2 rounded-lg shadow-sm border border-yellow-200">
                      <span>{data.detail}</span>
                    </div>
                  </div>
                {/if}


                <div class="mb-4 flex justify-end">
                    <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                        Log In
                    </button>
                </div>

                <div
                    on:click={() => setPage("home")}
                    class="text-blue-500 hover:underline cursor-pointer"
                    >Home Screen</div
                >
            </form>
        </div>
    </div>
</div>
