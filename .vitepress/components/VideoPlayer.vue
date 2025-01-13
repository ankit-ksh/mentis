<template>
  <div class="video-player-container">
    <!-- Video player section -->
    <div class="video-frame-container">
      <iframe
        ref="videoPlayer"
        v-if="currentVideo"
        :src="`https://www.youtube.com/embed/${currentVideo.id}?enablejsapi=1`"
        frameborder="0"
        allow="autoplay"
        allowfullscreen
        class="video-frame"
      ></iframe>
    </div>

    <!-- Video Info and Navigation (Controls) -->
    <div class="video-info">
      <div class="navigation-buttons">
        <span 
          class="icon" 
          @click="prevVideo" 
          :class="{ disabled: currentVideoIndex === 0 }"
        >
        <svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="36px" fill="#999999"><path d="M220-240v-480h80v480h-80Zm520 0L380-480l360-240v480Zm-80-240Zm0 90v-180l-136 90 136 90Z"/></svg>
        </span>
        <span class="icon" @click="togglePlayPause">
        <!-- Conditionally render Play or Pause SVG -->
        <svg v-if="isPlaying" xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#999999">
          <path d="M520-200v-560h240v560H520Zm-320 0v-560h240v560H200Zm400-80h80v-400h-80v400Zm-320 0h80v-400h-80v400Zm0-400v400-400Zm320 0v400-400Z"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#999999">
          <path d="m380-300 280-180-280-180v360ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/>
        </svg>
      </span>
        <span 
          class="icon"
          @click="nextVideo" 
          :class="{ disabled: currentVideoIndex === videoData.length - 1 }"
        >
        <svg xmlns="http://www.w3.org/2000/svg" height="36px" viewBox="0 -960 960 960" width="36px" fill="#999999"><path d="M660-240v-480h80v480h-80Zm-440 0v-480l360 240-360 240Zm80-240Zm0 90 136-90-136-90v180Z"/></svg>
      </span>
      </div>
    </div>
  </div>

  <!-- Video List (Scrollable) -->
  <div class="video-list-container">
    <ul class="video-list">
      <li
        v-for="(video, index) in videoData"
        :key="index"
        @click="selectVideo(index)"
        :class="{ active: index === currentVideoIndex }"
      >
        {{ index + 1 }}. {{ video.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    videoData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      currentVideoIndex: 0,
      isSmallScreen: window.innerWidth <= 768,
      isPlaying: false,
    };
  },
  computed: {
    currentVideo() {
      return this.videoData[this.currentVideoIndex];
    },
  },
  methods: {
    nextVideo() {
      if (this.currentVideoIndex < this.videoData.length - 1) {
        this.currentVideoIndex++;
        this.playVideo();
      }
    },
    prevVideo() {
      if (this.currentVideoIndex > 0) {
        this.currentVideoIndex--;
        this.playVideo();
      }
    },
    selectVideo(index) {
      this.currentVideoIndex = index;
      this.playVideo();
    },
    playVideo() {
      const iframe = this.$refs.videoPlayer?.contentWindow;
      if (iframe) {
        setTimeout(() => {
          iframe.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
          this.isPlaying = true;
        }, 500); // Adding a small delay to ensure the iframe is ready
      }
    },
    togglePlayPause() {
      const iframe = this.$refs.videoPlayer?.contentWindow;
      if (iframe) {
        if (this.isPlaying) {
          iframe.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
        } else {
          iframe.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
        }
        this.isPlaying = !this.isPlaying;
      }
    },
    handleResize() {
      this.isSmallScreen = window.innerWidth <= 768;
    },
  },
  mounted() {
    window.addEventListener("resize", this.handleResize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.handleResize);
  },
};
</script>

<style scoped>
.video-player-container {
  width: 100%; /* Full width */
  max-width: 800px; /* You can adjust this if necessary */
  margin: 0 auto; /* Center the container */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  font-family: Arial, sans-serif;
  color: #333;
  /* border: 1px solid #ddd; */
  /* border-radius: 8px; */
  overflow: hidden;
  position: sticky;
}

.video-frame-container {
  width: 100%;
  height: 100%;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  position: relative;
  background-color: black;
  z-index: 21;
}

.video-frame {
  position: absolute;
  width: 100%;
  height: 100%;
  border: none;
}

.video-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  z-index: 22;
}

.navigation-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  padding: 10px;
}

.navigation-buttons .icon {
  font-size: 1.5em;
  cursor: pointer;
  color: #555;
  transition: color 0.3s ease;
}

.navigation-button .icon.hover:hover {
  background-color:rgb(234, 64, 64);
  color: red;
}

.navigation-buttons .icon.disabled {
  color: #ccc;
  cursor: not-allowed;
}

.video-list-container {
  z-index: 20;
  width: 100%;
  max-height: 200px;
  overflow-y: auto;
  scrollbar-width: thin;
  margin-top: 20px; /* Small gap between the video player and the list */
  z-index: 21;
}
.video-list-container::-webkit-scrollbar-button {
  display: none; /* Hides the up and down arrow buttons */
}

.video-list {
  padding: 0;
  list-style: none;
  margin: 0;
}

.video-list li {
  padding: 8px 12px;
  cursor: pointer;
  border-bottom: 1px solid #ddd;
  transition: background-color 0.3s ease;
}

.video-list li:hover {
  background-color: #f0f0f0;
}

.video-list li.active {
  background-color: #e1e1e1;
  font-weight: bold;
}

/* Mobile View */
@media (max-width: 768px) {
  .video-player-container {
    margin: 0; /* Ensure no extra margins */
  }

  .video-frame-container {
    height: auto;
  }

  .navigation-buttons {
    flex-direction: row;
    justify-content: space-between;
    padding: 5px 10px;
  }

  .video-list-container {
    padding: 0 10px;
  }
}
</style>
