<script>
    import { onMount } from "svelte";
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




<h2>Grid 5×5 — Use arrow keys or buttons</h2>


<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(5, 50px);
    grid-template-rows: repeat(5, 50px);
    gap: 5px;
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
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.7), 0 0 16px rgba(255, 255, 0, 0.6);
  }
  50% {
    box-shadow: 0 0 16px rgba(0, 0, 0, 0.8), 0 0 32px rgba(255, 255, 0, 1);
  }
  100% {
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.7), 0 0 16px rgba(255, 255, 0, 0.6);
  }
}

</style>





<!-- Player Info -->
<div class="bg-gray-800 text-white rounded-2xl shadow-lg p-4 space-y-1">
  <p><span class="font-bold">Username:</span> {user.username}</p>
  <p><span class="font-bold">X:</span> {user.posx}</p>
  <p><span class="font-bold">Y:</span> {user.posy}</p>
  <p><span class="font-bold">Universe:</span> {user.universe}</p>
  <p class="flex items-center gap-2">
    <span class="font-bold">Mask Color:</span>
    <span class="w-4 h-4 rounded-full border"
          style="background:{user.color}"></span>
    {user.color}
  </p>
</div>

<div class="grid">
  {#each grid as row}
    {#each row as color}
      <div class="cell" style="background-color: {color}"></div>
    {/each}
  {/each}
</div>



<div class="grid gap-[5px] mb-4
            [grid-template-columns:repeat(3,50px)]
            [grid-template-rows:repeat(3,50px)]">

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-2 row-start-1
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("north")}>
    ⬆️
  </button>

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-1 row-start-2
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("west")}>
    ⬅️
  </button>

  <button
    class="flex items-center justify-center text-2xl border rounded
           col-start-2 row-start-2
           transition hover:shadow-lg hover:-translate-y-0.5"
    style="background-color: {user.color}"
    on:click={() => paint()}
  >
    🎨
  </button>
    
  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-3 row-start-2
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("east")}>
    ➡️
  </button>

  <button class="flex items-center justify-center text-2xl border rounded
                 col-start-2 row-start-3
                 transition hover:shadow-lg hover:-translate-y-0.5"
          on:click={() => move("south")}>
    ⬇️
  </button>

</div>
