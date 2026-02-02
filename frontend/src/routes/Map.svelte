<script>
  import { onMount } from "svelte";
  import { setPage } from "../store";

  let canvas;
  let ctx;
  let img = new Image();
  let scale = 1;
  let offsetX = 0;
  let offsetY = 0;
  let isDragging = false;
  let startX, startY;

  let envServerAddress = "http://104.251.216.28:9000/";
  let token = localStorage.getItem("token") || "";

  // Load image from server
  async function loadImage() {
    try {
      const res = await fetch(`${envServerAddress}game/overview`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) throw new Error("Failed to fetch image");
      const blob = await res.blob();
      img.src = URL.createObjectURL(blob);
    } catch (e) {
      console.error("Error loading image:", e);
    }
  }

  function draw() {
    if (!ctx || !img.complete) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Disable smoothing for pixel art
    ctx.imageSmoothingEnabled = false;

    ctx.save();
    ctx.translate(offsetX, offsetY);
    ctx.scale(scale, scale);
    ctx.drawImage(img, 0, 0);
    ctx.restore();
  }

  function handleWheel(event) {
    event.preventDefault();
    const zoomFactor = 0.1;
    const mouseX = (event.offsetX - offsetX) / scale;
    const mouseY = (event.offsetY - offsetY) / scale;

    if (event.deltaY < 0) {
      scale *= 1 + zoomFactor;
    } else {
      scale /= 1 + zoomFactor;
    }

    // Keep zoom centered on mouse
    offsetX = event.offsetX - mouseX * scale;
    offsetY = event.offsetY - mouseY * scale;
    draw();
  }

  function handleMouseDown(event) {
    isDragging = true;
    startX = event.clientX - offsetX;
    startY = event.clientY - offsetY;
  }

  function handleMouseMove(event) {
    if (!isDragging) return;
    offsetX = event.clientX - startX;
    offsetY = event.clientY - startY;
    draw();
  }

  function handleMouseUp() {
    isDragging = false;
  }

  // Touch handlers for mobile
  let lastTouchDistance = null;
  let lastTouchMid = null;

  function getTouchDistance(touches) {
    const dx = touches[0].clientX - touches[1].clientX;
    const dy = touches[0].clientY - touches[1].clientY;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function getTouchMidpoint(touches) {
    return {
      x: (touches[0].clientX + touches[1].clientX) / 2,
      y: (touches[0].clientY + touches[1].clientY) / 2
    };
  }

  function handleTouchStart(event) {
    if (event.touches.length === 1) {
      isDragging = true;
      startX = event.touches[0].clientX - offsetX;
      startY = event.touches[0].clientY - offsetY;
    } else if (event.touches.length === 2) {
      lastTouchDistance = getTouchDistance(event.touches);
      lastTouchMid = getTouchMidpoint(event.touches);
    }
  }

  function handleTouchMove(event) {
    event.preventDefault();
    if (event.touches.length === 1 && isDragging) {
      offsetX = event.touches[0].clientX - startX;
      offsetY = event.touches[0].clientY - startY;
      draw();
    } else if (event.touches.length === 2) {
      const newDistance = getTouchDistance(event.touches);
      const mid = getTouchMidpoint(event.touches);

      const zoomFactor = newDistance / lastTouchDistance;
      scale *= zoomFactor;

      // Keep zoom centered on midpoint
      offsetX = mid.x - (mid.x - offsetX) * zoomFactor;
      offsetY = mid.y - (mid.y - offsetY) * zoomFactor;

      lastTouchDistance = newDistance;
      lastTouchMid = mid;
      draw();
    }
  }

  function handleTouchEnd(event) {
    if (event.touches.length < 2) lastTouchDistance = null;
    if (event.touches.length === 0) isDragging = false;
  }

  function resizeCanvas() {
    if (!canvas) return;
    canvas.width = window.innerWidth - 20;
    canvas.height = window.innerHeight - 20;
    draw();
  }

  onMount(() => {
    document.title = "Color Mask | Map";
    ctx = canvas.getContext("2d");

    if (localStorage.getItem("Dev")) {
      envServerAddress = "http://10.101.0.6:9000/";
    }

    loadImage();
    const interval = setInterval(loadImage, 60000);
    img.onload = draw;

    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    return () => {
      clearInterval(interval);
      window.removeEventListener("resize", resizeCanvas);
    };
  });
</script>

<style>
  canvas {
    border: 1px solid #ccc;
    cursor: grab;
    touch-action: none; /* required for mobile touch gestures */
  }
  canvas:active {
    cursor: grabbing;
  }

  h1, p {
    margin-left: 10px;
  }
</style>

<h1>Image Viewer (Refresh every 60 seconds)</h1>
<p>Use mouse wheel or pinch to zoom, drag to pan.</p>
<p><span class="text-blue-500 hover:underline cursor-pointer" on:click={() => setPage("game")}>Return to game</span></p>
<canvas
  bind:this={canvas}
  on:wheel={handleWheel}
  on:mousedown={handleMouseDown}
  on:mousemove={handleMouseMove}
  on:mouseup={handleMouseUp}
  on:mouseleave={handleMouseUp}
  on:touchstart={handleTouchStart}
  on:touchmove={handleTouchMove}
  on:touchend={handleTouchEnd}
/>
