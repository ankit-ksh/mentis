<script setup>
import { ref, onMounted, onUnmounted, defineAsyncComponent } from 'vue';
import RenderMarkdown from './RenderMarkdown.vue';

// Props for contents and topic
const props = defineProps({
  chapterData: {
    type: Object,
    required: true
}});

// Extract the topic-specific data from contents
const chapterContents = props.chapterData.contents || {};
// Get data
const videoData = chapterContents.videos || [];
const bookData = chapterContents.books || [];

const showNotes = chapterContents.notes || false;
const showReference = chapterContents.reference || false;
const showQuestions = chapterContents.questions || false;

const notes = props.chapterData.notes;

// Sidebar visibility state
const isFocusModeEnabled = ref(false);
const isNavVisible = ref(true); // Add this to manage navigation visibility
const isAtTop = ref(true); // Add this for detecting top of the page
const activeSection = ref('notes'); // Add this to manage active section


// Function to toggle focus mode
const toggleFocusMode = () => {
  const contentAreaWithSideBar = document.querySelector("#VPContent"); 
  const navbar = document.querySelector("#app > div > header.VPNav");
  const sidebar = document.querySelector("#app > div > aside.VPSidebar");
  const aside = document.querySelector("#VPContent > div > div > div.aside");
  const localnav = document.querySelector("#app > div > div.VPLocalNav.has-sidebar.empty");
  
  navbar.style.display = isFocusModeEnabled.value ? "block" : "none";
  sidebar.style.display = isFocusModeEnabled.value ? "block" : "none";
  aside.style.display = isFocusModeEnabled.value ? "block" : "none";
  localnav.style.display = isFocusModeEnabled.value ? "block" : "none";
  contentAreaWithSideBar.style.paddingLeft = isFocusModeEnabled.value ? "" : "0px";
  contentAreaWithSideBar.style.paddingRight = isFocusModeEnabled.value ? "" : "0px";
  contentAreaWithSideBar.style.paddingTop = isFocusModeEnabled.value ? "" : "0px";
  contentAreaWithSideBar.style.paddingBottom = isFocusModeEnabled.value ? "" : "0px";
  contentAreaWithSideBar.classList.toggle("focus-mode", isFocusModeEnabled.value);
  
  isFocusModeEnabled.value = !isFocusModeEnabled.value;
};
// Always disable previous next buttons when this component is being rendered
const pager = document.querySelector("#VPContent > div > div > div.content > div > footer > nav.prev-next");
if (pager) {
    pager.style.visibility = "hidden";
  }

// Handle keydown event to trigger focus mode with Ctrl+Shift+F
const handleKeydown = (event) => {
  if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.key === 'F') {
    toggleFocusMode();  // Toggle focus mode
  }
};

// Add keydown event listener
onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
});

// Remove event listener on unmount
onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown);
});

// Scroll listener
const handleScroll = () => {
  const currentScrollPos = window.scrollY;
  isNavVisible.value = prevScrollPos > currentScrollPos || currentScrollPos <= 0; // Show nav when scrolling up or at the top
  isAtTop.value = currentScrollPos <= 0; // Update isAtTop when scroll position is at the top or not
  prevScrollPos = currentScrollPos;
};

// Add/remove scroll event listeners
onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});





let prevScrollPos = window.scrollY;

// Section toggle handler
const setActiveSection = (section) => {
  activeSection.value = section;
};
console.log(props.chapterData.helloo)
</script>

<template>
<div>
  <!-- Page switch navigation -->
  <div :class="['page-switch-nav', { hidden: !isNavVisible, 'at-top': isAtTop, 'focus-mode-enabled': isFocusModeEnabled }]">
    <button 
      v-if="videoData.length > 0"
      class="nav-button" 
      :class="{ active: activeSection === 'video' }" 
      @click="setActiveSection('video')">
      Videos
    </button>
    <button 
      class="nav-button" 
      :class="{ active: activeSection === 'notes' }" 
      @click="setActiveSection('notes')"
      v-if="showNotes">
      Notes
    </button>
    <button 
      class="nav-button" 
      :class="{ active: activeSection === 'reference' }" 
      @click="setActiveSection('reference')"
      v-if="showReference">
      Reference
    </button>
    <button 
      class="nav-button" 
      :class="{ active: activeSection === 'questions' }" 
      @click="setActiveSection('questions')"
      v-if="showQuestions">
      Questions
    </button>
    <button 
      class="nav-button focus-button" 
      :class="['nav-button', { active: isFocusModeEnabled }]"
      @click="toggleFocusMode">
      Focus
    </button>
  </div>

  <!-- Sections -->
  <div v-if="activeSection === 'video' && videoData.length > 0" class="section section-content active">
    <VideoPlayer :videoData="videoData" />
  </div>

  <div v-if="activeSection === 'notes'" class="section section-content active">
    {{ props.chapterData.helloo }}
    <notes />
  </div>

  <div v-if="activeSection === 'reference'" class="section section-content active">
    <div v-if="bookData.length > 0"><ShowBooks :books="bookData" /></div>
  </div>

  <div v-if="activeSection === 'questions'" class="section section-content active">
    <h2>Questions</h2>
  </div>
</div>
</template>



<style scoped>
/* Custom fixed navigation below the main navbar */

.page-switch-nav {
  width: 100%;
  max-width: 800px;
  position: sticky;
  background-color: rgb(255, 255, 255);
  display: flex;
  top: 70px;
  justify-content: space-around; /* Center the navigation items horizontally */
  align-items: center; /* Center the items vertically */
  padding: 10px;
  z-index: 21;
  border-radius: 40px;
  transition: transform 0.5s ease, opacity 0.5s ease, top 0.5s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
}
.page-switch-nav.at-top {
  top: -100px; /* Adjust the position if needed */
  transition: transform 0.5s ease, top 0.5s ease;
}
.page-switch-nav.focus-mode-enabled {
  top: 8px; /* Move closer to the top */
  transition: transform 0.5s ease, top 0.5s ease; /* Smooth transition for top property */
}

/* Hidden state for the nav */
.page-switch-nav.hidden {
  transform: translateY(-200%); /* Move the element completely off-screen vertically */
  visibility: hidden; /* Hide the element while maintaining its space */
  z-index: 0; /* Remove the element from the stacking context */
}

/* Buttons styling */
.nav-button {
  padding: 10px 20px;
  border-radius: 50px;
  background-color: #fff;
  cursor: pointer;
  font: "Google Sans",arial,sans-serif;
  font-weight: 500;
  font-size: 1rem;
  color: rgb(95, 99, 104);
  opacity: 85%;
  transition: all 0.08s ease;
}

.nav-button.active {
  background-color:rgb(218, 218, 218);
  color: rgb(32, 33, 36);
}

.nav-button:hover {
  background-color:rgb(218, 218, 218);
}



/* Sections styling */
.section {
  display: none;
}

.section.active {
  display: block;
}

.section-content {
  padding-top: 40px; /* Add space for the fixed navbar */
}

#VPContent {
  padding: ""; /* Default padding */
  transition: padding 0.3s ease;
}

#VPContent.focus-mode {
  padding: 0; /* Padding for focus mode */
  transition: padding 0.3s ease;
}



/* For screens smaller than 600px (you can adjust the breakpoint as needed) */
@media (max-width: 960px) {
  .page-switch-nav {
    width: 100%;
    top: 52px;
    gap: 1px;
    padding: 8px; 
  }

  /* When at the top of the page on small screens */
  .page-switch-nav.at-top {
    top: 0px; /* Adjust the position if needed */
    transition: top 0.5s ease;
  }

  .nav-button {
    padding: 5px 11px; /* Adjust padding for buttons */
  }
  .focus-button {
    display: none;
  }
}

</style>
