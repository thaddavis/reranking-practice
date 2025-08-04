---
video_title: "Code a D3.js timeline with React + Typescript"
video_url: "https://www.youtube.com/watch/A8T3KghaipA"
---

00:00:02.159 in this video we are going to learn how
00:00:04.019 to use D3 in a react project via a real
00:00:06.960 world example
00:00:08.880 this video assumes basic to intermediate
00:00:11.280 understanding of react Concepts such as
00:00:13.440 typescript JavaScript hooks bloody blah
00:00:16.500 and what we're going to do is transform
00:00:18.660 this into this
00:00:22.439 this is our starting point
00:00:25.140 first let's comment out the original
00:00:28.199 timeline component by coming over to our
00:00:31.199 source code
00:00:32.460 and finding the file for the parent
00:00:34.980 component in which the original timeline
00:00:37.079 component sits
00:00:38.640 and once we find the relevant jsx
00:00:42.960 we can comment it out and start building
00:00:47.280 the new and improved D3 timeline
00:00:51.360 components
00:00:52.739 here it is
00:00:54.840 commented out save
00:00:57.960 and poof the original timeline component
00:01:00.360 is gone now let's start building up the
00:01:03.359 new D3 timeline component
00:01:07.619 now let's create a folder that will
00:01:09.600 house the new D3 timeline component in
00:01:12.659 some area of your source code
00:01:14.820 I have put mine here
00:01:17.460 and inside of this folder create
00:01:20.939 a DOT TSX file that will house the jsx
00:01:25.500 for this new component we will build
00:01:28.740 because I'm using vs code and I have a
00:01:31.200 special vs code extension installed I
00:01:33.900 can simply type
00:01:36.619 rafc
00:01:38.159 to generate a boilerplate react
00:01:40.680 component
00:01:42.540 if you're not using vs code then just
00:01:45.780 create a react component that looks
00:01:47.880 something like this
00:01:50.159 now let's go back to the parent
00:01:52.079 component again and import our new D3
00:01:55.500 timeline component
00:01:59.520 let's come over to the parent component
00:02:02.579 collapse the file explorer to have more
00:02:04.979 space
00:02:07.079 and because we want this new component
00:02:09.840 at the top of our UI that is where we
00:02:12.959 will put it
00:02:15.360 so uncomment this bit of jsx
00:02:19.620 save
00:02:22.680 and we still need to import the
00:02:24.420 component at the top of the file so
00:02:26.340 because we're using vs code we can
00:02:27.959 simply type command
00:02:30.200 dot enter
00:02:32.700 save
00:02:35.040 and look at that
00:02:37.319 here is our new D3 timeline component
00:02:44.660 let's edit the D3 timeline components to
00:02:48.959 return the following UI elements each
00:02:51.300 time it's rendered
00:02:53.340 we want to replace the default div with
00:02:55.680 a div that has an ID of D3 Dash timeline
00:02:58.920 Dash widget and we also want to create a
00:03:01.620 use ref hook that allows us to make
00:03:03.720 edits to this section of our Dom without
00:03:06.480 automatically triggering re-renders
00:03:08.700 react is famous for automatically
00:03:11.459 re-rendering the screen each time state
00:03:14.040 in our component changes
00:03:15.780 this ensures that the UI is always
00:03:18.300 showing the latest state
00:03:20.280 sometimes however this is not desired
00:03:22.860 for example in what we're trying to do
00:03:25.620 the use ref hook allows us to make edits
00:03:29.220 to state in our component without
00:03:32.540 triggering the default behavior of react
00:03:35.879 which is to automatically refresh the
00:03:37.980 screen
00:03:38.819 that is what userf allows us to do
00:03:42.120 now we are going to add a custom hook to
00:03:45.840 our D3 timeline component
00:03:48.780 the custom hook we will add is called
00:03:51.319 use resize
00:03:54.540 here is the code
00:03:56.459 for the use resize hook
00:04:02.580 what the user size hook will do
00:04:05.640 is trigger a re-render
00:04:08.280 of our D3 timeline component each time
00:04:13.080 the window is adjusted in size
00:04:16.978 now let's add a use effect hook to the
00:04:19.500 D3 timeline component the purpose of the
00:04:22.500 use effect Hook is to co-locate related
00:04:25.139 logic that will get triggered upon
00:04:26.759 certain State changes
00:04:28.259 so let's create a use effect hook that
00:04:30.840 will trigger some code each time the
00:04:33.000 window size is adjusted
00:04:36.479 you can see in the logs that each time
00:04:38.820 the window size is adjusted
00:04:41.699 we received the updated width and height
00:04:44.340 in our code
00:04:49.259 for step 7
00:04:51.180 we are going to install all of the D3
00:04:54.419 related npm packages we will need for
00:04:57.120 the rest of this video
00:05:00.419 now we will add an SVG canvas inside of
00:05:04.020 our D3 timeline component that will
00:05:06.300 allow us to paint pretty pretty pictures
00:05:08.520 pretty pretty charts
00:05:10.979 if we come over to the elements pane in
00:05:14.280 the Chrome console
00:05:16.380 and inspect our D3 timeline component
00:05:20.460 we see that an SVG canvas has been
00:05:23.580 appended
00:05:26.160 just to make sure the SVG canvas is
00:05:28.560 working let's draw a blue rectangle
00:05:34.020 and it's looking good
00:05:35.820 the way I have organized the code is all
00:05:39.479 of the draw logic will be stored inside
00:05:41.759 of this helpers folder
00:05:43.800 here is the code for drawing the blue
00:05:46.380 rectangle if you're wondering about this
00:05:49.080 other color this other color is the gray
00:05:51.960 background
00:05:53.340 seen Elsewhere on this overview page
00:05:58.680 much more subtle
00:06:00.419 but we're just verifying the canvas is
00:06:03.360 working
00:06:05.639 now let's draw the timeline on top of
00:06:08.400 the SVG canvas
00:06:12.139 the leftmost time in this timeline is
00:06:14.880 going to be the first event in the list
00:06:16.800 of events that we pass to our D3
00:06:19.380 timeline component if you remember back
00:06:21.660 to the original timeline component it
00:06:24.240 was showing a sequence of events or a
00:06:26.039 list of events so the first event will
00:06:28.080 be the leftmost time and the last event
00:06:30.020 will be the rightmost time
00:06:33.419 here is the code that draws the timeline
00:06:36.180 just to be exhaustive
00:06:44.340 now let's draw our events on top of this
00:06:47.520 timeline
00:06:48.479 each event is going to be represented as
00:06:51.300 a DOT on top of this timeline
00:06:55.080 here is the code for drawing the dots
00:06:58.319 that represents each event on the
00:07:00.720 timeline
00:07:13.680 okay so we're drawing an ordered list of
00:07:16.500 events on a timeline fantastic
00:07:19.500 now let's add one more dot to represent
00:07:22.560 the current point in time in order to do
00:07:25.020 that I'm going to create a new escrow
00:07:27.360 agreement because I've been using this
00:07:28.560 escrow agreement for a while now and all
00:07:30.300 the dates on this timeline are long
00:07:31.740 passed so let's come over to the
00:07:33.900 contracts Library choose escrow
00:07:36.060 agreement click create contract
00:07:38.940 provide our password
00:07:43.259 sign the create contract request
00:07:46.620 and when the request is done mining
00:07:50.039 we will have a new timeline
00:07:54.180 with fresh dates
00:07:56.940 let's update the code to include the
00:07:59.880 code for drawing the current event and
00:08:03.000 you can see a DOT that is blue moving
00:08:07.199 across towards the end of the timeline
00:08:09.840 as I manually refresh the UI
00:08:15.960 right
00:08:18.360 you can see the blue dot moving from
00:08:20.340 left
00:08:21.300 to right
00:08:26.639 fantastic
00:08:28.800 let's animate this so that we don't have
00:08:32.039 to constantly refresh the page
00:08:34.760 [Music]
00:08:36.059 here we are back in our D3 timeline.tsx
00:08:39.479 component
00:08:41.159 we are now about to add the code for
00:08:43.559 implementing the automated animation
00:08:45.420 feature for animating the current point
00:08:47.399 in time across the timeline from left to
00:08:49.080 right here is the code
00:08:51.480 so you can see we've added another use
00:08:53.580 ref hook this one is keeping track of
00:08:56.160 the state of the animation as far as
00:08:57.899 timing is concerned
00:09:00.000 and we are also using another use effect
00:09:03.000 hook
00:09:04.140 and this use effect Hook is leveraging
00:09:06.060 the request animation frame API the
00:09:09.000 request animation frame API allows us to
00:09:11.760 trigger a function each time the browser
00:09:14.820 is about to repaint the screen
00:09:18.000 this animate function is the function
00:09:21.540 that we want to call each time the
00:09:24.240 browser is about to repaint the screen
00:09:25.740 in it
00:09:26.940 we are calculating the amount of
00:09:28.800 milliseconds
00:09:30.060 between each frame and after that amount
00:09:33.120 of milliseconds has elapsed we are
00:09:35.660 drawing the next frame of the animation
00:09:39.060 to the screen
00:09:41.700 go back
00:09:43.560 to our app
00:09:47.040 launch a fresh
00:09:49.560 contract
00:09:51.000 sign
00:09:53.880 the
00:09:55.260 contract transaction request
00:09:59.220 and once it's done mining
00:10:01.500 we should see the current point in time
00:10:03.920 animating across from left to right
00:10:07.800 we have some cosmetic work to do but
00:10:10.800 we have done the heavy lifting of
00:10:13.380 implementing this feature so far
00:10:16.700 and after we layer on some minor
00:10:20.580 cosmetic tweaks we arrive at the final
00:10:23.820 state of our D3 timeline widget
00:10:31.459 if you hover over each dot you get more
00:10:34.380 information about the event
00:10:40.339 and if we create a fresh contract with
00:10:44.040 fresh dates
00:10:46.920 we should see a clean animation moving
00:10:50.220 across from left to right
00:10:52.040 [Music]
00:11:04.680 ah so satisfying
00:11:07.920 hopefully you enjoyed this
00:11:11.779 walkthrough of how to use D3 in
00:11:14.700 combination with react enjoy peace
00:11:17.640 blessings so much Prosperity wish you
00:11:20.279 all the best
