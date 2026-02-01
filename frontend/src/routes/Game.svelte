<script>
    import { onMount, onDestroy } from "svelte";
    import { setPage } from "../store";

    let token = "";
    let data = {};
    let grid = [];
    let envServerAddress = "http://104.251.216.28:9000/";
    let user = "";

    onMount(() => {
        document.title = "Color Mask | Game";

        if (localStorage.getItem("Dev")) {
            envServerAddress = "http://10.101.0.6:9000/";
        }

        // If token is not set, redirect to login
        if (!localStorage.getItem("Token")) {
            setPage("login");
        }

        window.addEventListener("keydown", preventScroll);

        // Convert session to token
        token = localStorage.getItem("Token");

        const interval = setInterval(() => {
            updateData();
        }, 1000);

        const handleKey = (e) => {
        if (e.key === "ArrowUp") move("north");
        if (e.key === "ArrowDown") move("south");
        if (e.key === "ArrowLeft") move("west");
        if (e.key === "ArrowRight") move("east");
        if (e.key === " ") paint();
        };
        window.addEventListener("keydown", handleKey);



        // Fire on first load (skip the interval)
        updateData();

        return () => {
            clearInterval(interval);
            window.removeEventListener("keydown", handleKey);
        };
    });




    function preventScroll(event) {
        // List of keys that scroll the page
        const keys = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", " "];
        if (keys.includes(event.key)) {
        event.preventDefault();
        }
    }

    onDestroy(() => {
        window.removeEventListener("keydown", preventScroll);
    });

    async function swap(color) {
        data = {};
        try {
            const response = await fetch(envServerAddress + "game/swap_" + color, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
            });
            data = await response.json();
        } catch (error) {
            console.error("Error:", error);
        }
    }





    async function paint() {
        data = {};
        try {
            const response = await fetch(envServerAddress + "game/paint", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
            });
            data = await response.json();
                        //alert(localStorage.getItem("Token"));
            console.log(data);
            console.log(data.view);
            // data.view is a 25 length array of hex colors

            // Convert 1D array into 2D 5x5 grid
            grid = [];
            for (let i = 0; i < 5; i++) {
                grid.push(data.view.slice(i * 5, i * 5 + 5));
            }
        } catch (error) {
            console.error("Error:", error);
        }
    }





    async function move(direction) {
        data = {};

        try {
            const response = await fetch(envServerAddress + "game/move_" + direction, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
            });
            data = await response.json();
                        //alert(localStorage.getItem("Token"));
            console.log(data);
            console.log(data.view);
            // data.view is a 25 length array of hex colors

            // Convert 1D array into 2D 5x5 grid
            grid = [];
            for (let i = 0; i < 5; i++) {
                grid.push(data.view.slice(i * 5, i * 5 + 5));
            }
        } catch (error) {
            console.error("Error:", error);
        }
    }

    async function updateData() {
        data = {};

        try {
            const response = await fetch(envServerAddress + "game/view", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
            });

            data = await response.json();
            if (response.status !== 200) {
                //console.log(response.statusText + ": " + data.detail);
                return;
            }

            //alert(localStorage.getItem("Token"));
            console.log(data);
            console.log(data.view);
            // data.view is a 25 length array of hex colors

            // Convert 1D array into 2D 5x5 grid
            grid = [];
            for (let i = 0; i < 5; i++) {
                grid.push(data.view.slice(i * 5, i * 5 + 5));
            }
            user = data.userdata;


            // setPage("game");
        } catch (error) {
            console.error("Error:", error);
            // addToast({ type: "error", message: error.message }); // if you have a toast system
            //setPage("login");
        }
    }
</script>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(5, 50px);
    grid-template-rows: repeat(5, 50px);
    gap: 9px;
    margin-bottom: 1rem;
  }
  .cell {
    width: 50px;
    height: 50px;
    border: 1px solid #333;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s;
  }
  .control-btn {
    width: 55px;
    height: 55px;
    font-size: 1.6rem;
    border-radius: 14px;
    border: 1px solid rgb(229,231,235);
    display: flex;
    align-items: center;
    justify-content: center;

    transition: all .12s ease;
    user-select: none;
  }

  .control-btn:hover {
    background: rgb(243,244,246);
    transform: translateY(-2px);
  }

  .control-btn:active {
    transform: scale(.90);
  }

.grid .cell:nth-child(13) {
  animation: pulseGlow 1.5s infinite;
}

/* Keyframes for pulsing glow */
@keyframes pulseGlow {
  0% {
    box-shadow:
      0 0 12px rgba(255, 255, 0, 0.9),
      0 0 24px rgba(255, 255, 0, 0.8),
      0 0 48px rgba(255, 255, 0, 0.6);
  }
  50% {
    box-shadow:
      0 0 20px rgba(255, 255, 0, 1),
      0 0 40px rgba(255, 255, 0, 0.95),
      0 0 80px rgba(255, 255, 0, 0.75);
  }
  100% {
    box-shadow:
      0 0 12px rgba(255, 255, 0, 0.9),
      0 0 24px rgba(255, 255, 0, 0.8),
      0 0 48px rgba(255, 255, 0, 0.6);
  }
}

</style>





<!-- Player Info -->
<div class="bg-gray-800 text-white rounded-2xl shadow-lg p-4 space-y-1 max-w-sm ml-4">
  
  <div class="avatar flex items-center justify-center mb-4">
    <div class="w-24 rounded-full">
      <img src="https://api.dicebear.com/9.x/avataaars/svg?seed=corgo_{token}" alt="Avatar" />
    </div>
    <div>{user.username}</div>
  </div>
  <p><span class="font-bold">X:</span> {user.posx}</p>
  <p><span class="font-bold">Y:</span> {user.posy}</p>
  <p><span class="font-bold">Universe:</span> {user.universe}</p>
  <p class="flex items-center gap-2">
    <span class="font-bold">Mask Color:</span>
    <span class="w-4 h-4 rounded-full border"
          style="background:{user.color}"></span>
    {user.color}
  </p>
  <p><span class="text-blue-500 hover:underline cursor-pointer" on:click={() => setPage("home")}>Logout</span></p>

  <div class="grid">
    {#each grid as row}
      {#each row as color}
        <div class="cell" style="background-color: {color}"></div>
      {/each}
    {/each}
  </div>

</div>



<div class="grid gap-[5px] mb-4 w-full"
     style="grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);">

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-2 row-start-1 bg-gray-100
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("north")}>
    ⬆️
  </button>

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-1 row-start-2 bg-gray-100
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("west")}>
    ⬅️
  </button>

  <button
    class="flex items-center justify-center text-2xl border rounded
           col-start-2 row-start-2 disabled:opacity-50 disabled:cursor-not-allowed
           transition hover:shadow-lg hover:-translate-y-0.5"
    style="background-color: {user.color}"
    on:click={() => paint()}
    disabled={user.posx == 0 && user.posy == 0}
  >
    🎨
  </button>
    
  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-3 row-start-2 bg-gray-100
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("east")}>
    ➡️
  </button>

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-2 row-start-3 bg-gray-100
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("south")}>
    ⬇️
  </button>
</div>

<div class="flex flex-col gap-3">
  <!-- White Button -->
  <button
    class="flex items-center justify-center text-black text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #FFFFFF"
    on:click={() => swap("white")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to White
  </button>

  <!-- Black Button -->
  <button
    class="flex items-center justify-center text-white text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #000000"
    on:click={() => swap("black")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Black
  </button>

  <!-- Green Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #00FF00"
    on:click={() => swap("green")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Green
  </button>

  <!-- Red Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #FF0000"
    on:click={() => swap("red")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Red
  </button>

  <!-- Blue Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #0000FF"
    on:click={() => swap("blue")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Blue
  </button>

  <!-- Orange Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #FFA500"
    on:click={() => swap("orange")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Orange
  </button>

  <!-- Yellow Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #FFFF00"
    on:click={() => swap("yellow")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Yellow
  </button>

  <!-- Purple Button -->
  <button
    class="flex items-center justify-center text-2xl font-semibold border rounded-lg 
           px-6 py-3 transition transform hover:shadow-lg hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
    style="background-color: #800080"
    on:click={() => swap("purple")}
    disabled={user.posx !== 0 || user.posy !== 0}
  >
    Change 🎭 to Purple
  </button>
</div>
