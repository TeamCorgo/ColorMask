<script>
  import {currentPage} from "../store";
  import {setPage} from "../store";
</script>

<nav class="bg-gray-800 text-white">
  <div class="max-w-7xl mx-auto px-4">
    <div class="flex items-center justify-between h-16">
      
      <!-- Logo or Brand -->
      <div class="flex-shrink-0 text-xl font-bold">
        Color Mask
      </div>
      
      <!-- Menu items -->
      <div class="hidden md:flex space-x-6">
          <a href="#" class="hover:text-gray-300" on:click={() => setPage('create')}>Create</a>
      </div>
      <div class="hidden md:flex space-x-6">
          <a href="#" class="hover:text-gray-300" on:click={() => setPage('login')}>Login</a>
      </div>
      <div class="hidden md:flex space-x-6"
        on:click={() => {
          localStorage.removeItem("Token");
          setPage('login');
        }}
      >
        Logout
      </div>
    </div>
  </div>
</nav>
