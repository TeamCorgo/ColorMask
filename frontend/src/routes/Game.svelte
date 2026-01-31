<script>
    import { onMount } from "svelte";
    import { setPage, envServerAddress } from "../store";

    let token = "asd";
    let data = {};
    let grid = [];

    onMount(() => {
        document.title = "Color Mask | Game";



        const interval = setInterval(() => {
            updateData();
        }, 1000);

        return () => clearInterval(interval);

    });


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


    // Fire on first load (skip the interval)
    updateData();
</script>




<h2>Grid 5×5 — Use arrow keys or buttons</h2>


<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(5, 3rem);
    grid-template-rows: repeat(5, 3rem);
    gap: 4px;
  }

  .cell {
    width: 3rem;
    height: 3rem;
    border: 1px solid #333;
    border-radius: 4px;
  }
</style>

<div class="grid">
  {#each grid as row}
    {#each row as color}
      <div class="cell" style="background-color: {color}"></div>
    {/each}
  {/each}
</div>