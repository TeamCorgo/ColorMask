<script>
    import { currentPage, envServerAddress } from "./store";

    import Create from "./routes/Create.svelte";
    import Login from "./routes/Login.svelte";
    import Game from "./routes/Game.svelte";
    import Map from "./routes/Map.svelte";
    import Home from "./routes/Home.svelte";
    import Menu from "./parts/Menu.svelte";

    
</script>
{#if $currentPage === "create"}<Create />{/if}
{#if $currentPage === "login"}<Login />{/if}
{#if $currentPage === "game"}<Game />{/if}
{#if $currentPage === "home"}<Home />{/if}
{#if $currentPage === "map"}<Map />{/if}
