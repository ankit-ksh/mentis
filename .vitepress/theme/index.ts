import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import VideoPlayer from '../components/VideoPlayer.vue'
import HelloWorld from '../components/LinkCards.vue'
import ShowBooks from '../components/ShowBooks.vue'
import ResourceSwitcher from '../components/ResourceSwitcher.vue'
import CoursePage from '../components/CoursePage.vue'; 
import DropDown from '../components/DropDown.vue'
import SidebarToggler from '../components/SidebarToggler.vue'
import CreateFileLink from '../components/CreateFileLink.vue'
import RenderMarkdown from '../components/RenderMarkdown.vue'
import CoursePageLayout from './CoursePageLayout.vue'
import MyLayout from '../components/MyLayout.vue'




export default {
  ...DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    app.component('CoursePage', CoursePage);
    app.component('VideoPlayer', VideoPlayer);
    app.component('HelloWorld', HelloWorld);
    app.component('ResourceSwitcher', ResourceSwitcher);
    app.component('SidebarToggler', SidebarToggler);
    app.component('ShowBooks', ShowBooks);
    app.component('DropDown', DropDown);
    app.component('CreateFileLink', CreateFileLink);
    app.component('RenderMarkdown', RenderMarkdown);
    app.component('MyLayout', MyLayout);
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-top': () => h(ResourceSwitcher)
    })
  }
}
