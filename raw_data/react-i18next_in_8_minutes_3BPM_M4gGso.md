---
video_title: "react-i18next in 8 minutes"
video_url: "https://www.youtube.com/watch/3BPM_M4gGso"
---

00:00:00.000 No text
00:00:00.000 so let's jump in this is a video on iat
00:00:02.800 next iat next is a library used for
00:00:05.359 setting your apps up for multi-language
00:00:07.759 support i am going to show you with a
00:00:09.920 setup of a react app on the front end
00:00:12.400 and using the translations within the
00:00:14.799 react app and also a variation where you
00:00:16.960 can set up the translations to be loaded
00:00:19.039 from another endpoint a remote endpoint
00:00:21.680 here is variation one on the left
00:00:24.400 it's going to have iat next included in
00:00:27.519 a react app and all of the translations
00:00:30.080 are going to be delivered to the client
00:00:32.719 with the front-end application and all
00:00:34.399 the translations are going to happen on
00:00:36.320 the front-end application for variation
00:00:38.239 number two
00:00:39.440 it's gonna be very similar except that
00:00:40.960 the front-end application is going to be
00:00:42.640 loading all of the translation data from
00:00:44.320 a third-party endpoint this is better if
00:00:46.960 you're going to have a huge app with
00:00:48.719 loads and loads and loads of
00:00:49.920 translations and you don't want all of
00:00:51.600 that translation
00:00:53.039 information to be loaded to the client
00:00:54.800 when someone visits your site for the
00:00:56.160 first time
00:00:57.000 No text
00:00:59.440 so let's get started by
00:01:02.320 creating a boilerplate react app and
00:01:04.879 then after we have the boilerplate react
00:01:06.640 app i'm going to add in i18 next and
00:01:09.920 you'll get the gist of it so here we are
00:01:12.320 on the create react app website
00:01:15.119 if you come to
00:01:16.799 this section and click adding typescript
00:01:20.240 you can generate the boilerplate app
00:01:22.560 like so
00:01:24.000 i'm going to call this
00:01:29.280 i18
00:01:31.680 next
00:01:33.520 demo
00:01:36.079 and i'm using i think node version 14
00:01:39.600 i'm going to check after this is
00:01:40.960 finished
00:01:42.600 [Music]
00:01:52.240 as i suspected node version 14.
00:01:55.040 aka lts forward slash fermium
00:01:59.119 anyway let's jump in
00:02:03.600 no i don't trust them but i must click
00:02:05.759 this button
00:02:08.080 here we have the boilerplate react app
00:02:09.758 now let's layer on iat next or i18n i
00:02:12.879 found this tutorial which i will link in
00:02:14.400 the description below that very simply
00:02:16.400 describes how to integrate it pretty
00:02:17.760 much you just have to install these
00:02:19.200 packages
00:02:21.520 all right
00:02:24.319 like that
00:02:26.720 when those are done installing
00:02:29.599 you create an
00:02:31.319 i18n.t.s because i'm using typescript
00:02:33.519 file with this content to initialize the
00:02:36.080 i18n or i18 next module
00:02:40.720 all right i did it already
00:02:43.840 let me restart the app
00:02:46.400 then you come to your entry point make
00:02:49.120 sure you initialize this module before
00:02:51.680 you launch your react app
00:02:53.920 and you react that this is how you do
00:02:55.280 translations so
00:02:57.040 you use the use translation hook from
00:02:59.599 the react i18 next library
00:03:02.720 then you initialize the hooks like so
00:03:07.920 right
00:03:09.760 and
00:03:11.120 this should be enough
00:03:13.120 to test this out
00:03:15.360 reload there you go look at that so our
00:03:17.760 language is english with the u.s
00:03:19.760 variation
00:03:21.040 and
00:03:22.000 this is the key
00:03:23.440 that we have established and we want to
00:03:25.280 translate this
00:03:26.879 so
00:03:27.760 inside of our module you can see that we
00:03:30.879 don't have any translations right so
00:03:33.920 each dot
00:03:35.120 is like a nested object right so
00:03:37.760 greeting
00:03:40.640 hello
00:03:43.120 hello
00:03:44.840 world look at that
00:03:47.120 all right
00:03:48.159 now let's add the translations
00:03:50.799 for spanish
00:03:54.239 code for spanish is yes right
00:03:56.560 so we'll say
00:03:59.439 hola papi
00:04:02.720 so now look what happens when i switch
00:04:05.920 my language i already have my settings
00:04:08.159 open over here so english is the highest
00:04:11.120 priority language i'm going to shift
00:04:12.959 spanish
00:04:14.400 right to be the top priority language in
00:04:16.798 my browser
00:04:18.000 look at that
00:04:20.160 right so it's that simple
00:04:22.000 No text
00:04:24.400 so now for variation two
00:04:26.479 right like we were saying well first of
00:04:28.160 all let me say forgive the audio there
00:04:30.080 is a tropical storm happening in the
00:04:31.600 background
00:04:32.720 so anyways variation number two right so
00:04:34.560 we did variation number one this is with
00:04:36.880 all of the translations bundled in the
00:04:38.479 front and application right we were able
00:04:40.479 to switch between english and spanish
00:04:42.800 and you could extrapolate out that
00:04:44.080 pattern to build a full app
00:04:46.160 but eventually if your app becomes
00:04:48.320 enormous right which is if you have the
00:04:50.720 privilege to have an app that becomes
00:04:52.240 that big
00:04:53.440 eventually you're going to want to move
00:04:54.560 the translations off of the app right
00:04:56.720 onto another server and load the
00:04:58.160 translations as they're requested by the
00:04:59.759 user it doesn't make sense to load
00:05:01.759 all of this translation data when most
00:05:03.600 of it is not even get used by the client
00:05:05.520 okay so i'm going to describe what i'm
00:05:07.120 going to do and i'm going to speed up
00:05:08.320 the video so you don't die of boredom
00:05:10.479 i'm going to create a file server that's
00:05:12.560 going to hold all the translations and
00:05:14.160 the front end application is going to
00:05:15.520 request the translations on the fly on
00:05:18.240 demand instead of all the translations
00:05:19.759 being loaded on the client right let's
00:05:21.600 say that you have like five languages
00:05:23.039 russian japanese swedish
00:05:26.080 english
00:05:27.520 hungarian why are you gonna load all of
00:05:29.440 those translations on the client most
00:05:30.960 people aren't gonna use all of that data
00:05:32.400 right so it's much
00:05:33.680 better designed to have the user request
00:05:36.160 the translations they need on the fly
00:05:37.759 right from the server that's we're going
00:05:38.960 to do right
00:05:42.160 that was a wise move to not have you sit
00:05:44.160 through me setting up the file server
00:05:45.759 right so here we have our folder this is
00:05:47.600 the overview we're doing variation
00:05:49.039 number two right now here's the front
00:05:50.960 end that we set up right create racked
00:05:52.560 up with typescript and then this is the
00:05:54.400 back end express the typescript so here
00:05:56.479 it is
00:05:57.680 you have the entry point
00:05:59.520 the back end is listening on port 4000
00:06:02.160 the front end has the dev server on port
00:06:04.400 3000
00:06:06.319 inside of the server
00:06:08.000 we have this debug middleware and cores
00:06:10.639 allowing requests from the front end on
00:06:12.240 port 3000 and we have all of the
00:06:14.720 translation data inside of the locales
00:06:16.639 directory right so we have one
00:06:17.919 translation for hello world in english
00:06:20.240 and hello world in spanish
00:06:22.479 and then we have a catch all middleware
00:06:25.919 so this is what we change on the front
00:06:27.440 end
00:06:28.319 to load the translations from the
00:06:30.400 backend so we installed this http
00:06:33.360 backend and then we just tweaked the iat
00:06:36.800 next configuration like so so we had all
00:06:39.360 the translations sitting on the front
00:06:40.639 end now we are loading them from the
00:06:42.560 back end like so
00:06:45.360 right
00:06:46.240 you want english and spanish
00:06:48.479 and then
00:06:49.520 we have to enable this like so
00:06:53.440 and in the front end
00:06:56.400 we switched
00:06:57.919 our key from greeting.hello to
00:07:01.199 the namespace translations and then the
00:07:03.360 hello world key in the translations
00:07:06.080 namespace right so
00:07:08.000 translations is a namespace as i
00:07:10.240 mentioned namespaces allow you to group
00:07:12.560 translations into different files right
00:07:15.440 you can imagine as you get lots and lots
00:07:17.360 of translations it'd be nice to break
00:07:19.520 them up into files so you can have
00:07:21.759 different groups of translations in each
00:07:24.080 file and each file is referred to as a
00:07:26.319 name space in i18 next
00:07:28.639 so let me demonstrate
00:07:30.800 and then that will be it
00:07:32.960 so i'm running the back end
00:07:35.199 front end is working
00:07:37.680 we're running rather
00:07:39.759 right
00:07:41.199 hello world why is that not going hello
00:07:44.479 hold on
00:07:46.160 what do we not do correctly translations
00:07:50.319 anything that's right we have to enable
00:07:51.680 the name spaces right that's what i
00:07:53.039 didn't do
00:07:54.160 there we go hello world
00:07:56.479 right
00:07:57.520 and then if i switch my browser to
00:08:01.039 have spanish as the priority right we
00:08:03.280 get our translations
00:08:04.639 right so that's the gist of it right you
00:08:06.639 can get much deeper with it it's not too
00:08:09.120 complicated but there are some nuances
00:08:11.599 to it so that's how you use iat next
