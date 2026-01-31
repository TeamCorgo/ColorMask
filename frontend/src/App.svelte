<script>
    import { currentPage, envServerAddress } from "./store";

    import Attract from "./routes/Attract.svelte";
    import Register from "./routes/Register.svelte";
</script>

{#if $currentPage === "attract"}<Attract />{/if}
{#if $currentPage === "register"}<Register />{/if}