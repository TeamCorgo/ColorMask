<script>
    import { currentPage, envServerAddress } from "./store";

    import Create from "./routes/Create.svelte";
    import Login from "./routes/Login.svelte";
    import Game from "./routes/Game.svelte";
    import Menu from "./parts/Menu.svelte";

    
</script>
<Menu />
{#if $currentPage === "create"}<Create />{/if}
{#if $currentPage === "login"}<Login />{/if}
{#if $currentPage === "game"}<Game />{/if}
