<script>
    import { currentPage, envServerAddress } from "./store";

    import Attract from "./routes/Attract.svelte";
</script>

{#if $currentPage === "attract"}<Attract />{/if}