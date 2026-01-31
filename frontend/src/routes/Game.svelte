<script>
    import { onMount } from "svelte";
    import { setPage, envServerAddress } from "../store";

    let token = "asd";
    let data = {}

    onMount(() => {
        document.title = "Color Mask | Game";
    });


    async function handleSubmit(event) {
        event.preventDefault();
        data = {};

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
            //alert(localStorage.getItem("Token"));
            console.log("Signed in", data);
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
