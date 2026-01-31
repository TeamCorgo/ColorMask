<script>
    import { currentPage, envServerAddress } from "./store";

    import Attract from "./routes/Attract.svelte";
    import Create from "./routes/Create.svelte";
    import Login from "./routes/Login.svelte";
    import Menu from "./parts/Menu.svelte";
    
</script>
<Menu />
{#if $currentPage === "attract"}<Attract />{/if}
{#if $currentPage === "create"}<Create />{/if}
{#if $currentPage === "login"}<Login />{/if}
