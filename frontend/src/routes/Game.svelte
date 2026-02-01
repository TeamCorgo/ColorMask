<script>
    import { onMount } from "svelte";
    import { setPage } from "../store";

    let token = "";
    let data = {};
    let grid = [];
    let envServerAddress = "http://104.251.216.28:9000/";

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
</style>

<div class="grid">
  {#each grid as row}
    {#each row as color}
      <div class="cell" style="background-color: {color}"></div>
    {/each}
  {/each}
</div>

<div>
  <button on:click={() => move("north")}>⬆️</button><br/>
  <button on:click={() => move("west")}>⬅️</button>
  <button on:click={() => paint()}>🎨</button>
  <button on:click={() => move("east")}>➡️</button><br/>
  <button on:click={() => move("south")}>⬇️</button>
</div>