---
video_title: "How to deploy a dockerized FastAPI to Cloud Run"
video_url: "https://www.youtube.com/watch/DQwAX5pS4E8"
---

00:00:00.000 No text
00:00:01.400 welcome to how to deploy a dockerized
00:00:03.959 fast API to Google Cloud run cicd
00:00:07.200 included this video is the culmination
00:00:09.760 of years of struggle and sauce and
00:00:12.280 you'll be FASTT tracking your way to web
00:00:13.920 development success if you pay attention
00:00:16.960 closely I suggest first watching this
00:00:19.279 video all the way through to understand
00:00:21.279 its overall message and then returning
00:00:23.519 to individual sections as needed this
00:00:26.800 tutorial is in four parts in part one
00:00:30.080 one we will create a Dev container in
00:00:33.160 part two we will build a simple fast API
00:00:37.399 in part three we will deploy the API to
00:00:40.440 GCR and in part four we will set up cicd
00:00:44.760 so sit back enjoy and if you want to
00:00:47.520 follow along with the code I've included
00:00:49.399 a link to a GitHub repository in the
00:00:52.000 No text
00:00:53.480 description development containers are a
00:00:55.920 specification being developed at
00:00:57.559 Microsoft that allows you to attach your
00:00:59.640 I to a Docker container containing your
00:01:02.160 development environment at the time of
00:01:04.360 recording the only idees that have solid
00:01:06.760 support for Dev containers are vs code
00:01:10.119 and intellig so if you don't use these
00:01:12.640 idees this video is probably not going
00:01:14.640 to be too practical for you to easily
00:01:16.799 follow along you'll need at least a
00:01:18.280 rudimentary understanding of the
00:01:19.840 following tools SLC Concepts Docker
00:01:23.240 Docker desktop vs code I.E the world's
00:01:25.960 most popular application for editing
00:01:27.479 code VSS code extensions particularly
00:01:30.759 you will need the docker extension and
00:01:32.439 the dev containers extension installing
00:01:34.280 these extensions should only take a few
00:01:36.040 clicks and a few seconds and also
00:01:38.960 General software development Concepts
00:01:40.799 like git CLI commands apis and
00:01:43.759 programming languages will definitely
00:01:45.079 help you out with following
00:01:48.680 along here we are starting with an empty
00:01:51.439 folder on our computer let's start by
00:01:54.159 creating AEV container folder at the
00:01:56.719 root of our
00:01:58.200 project inside of this folder let's
00:02:00.399 create an empty file called Dev
00:02:02.600 container. Json what should we put in
00:02:05.320 this file you might ask well if we take
00:02:07.439 a look at the official Dev container
00:02:09.399 spec we'll see all of the individual
00:02:11.480 keys we could specify but to get us
00:02:14.440 moving along I'll just paste in this
00:02:15.920 Json content right here this Dev
00:02:18.680 container. Json file is where we specify
00:02:20.800 the details of our development container
00:02:23.319 the name key is where we specify the
00:02:25.000 name we want to give our Dev container
00:02:27.120 this is arbitrary the build key is where
00:02:29.519 we put the reference to the docker file
00:02:31.160 that will act as the base point of our
00:02:32.840 development environment this will make
00:02:34.680 more sense later the customization key
00:02:37.080 is where we can customize many things
00:02:38.840 here we're customizing which VSS code
00:02:41.360 extensions we want installed into the
00:02:43.040 VSS code instance that gets attached to
00:02:45.640 our development container line 18 I
00:02:48.560 don't think we need but I put it here
00:02:50.640 because it doesn't hurt this is where we
00:02:52.200 can specify which ports on our host
00:02:54.200 machine will get forwarded to ports on
00:02:55.959 our
00:02:56.920 container the workspace mount
00:03:00.280 is where we specify the location inside
00:03:04.400 of the development container that our
00:03:06.560 project files will get mounted into on
00:03:09.519 line 22 we have a key that says
00:03:11.680 workspace folder this is the folder that
00:03:14.239 will get opened by default when we open
00:03:16.680 our development
00:03:17.920 container and on line 23 we have an
00:03:20.799 empty run args array this is where we
00:03:23.120 can specify some further customizations
00:03:25.640 that we're not going to need for the
00:03:26.560 moment next we'll add the docker file
00:03:29.239 reference online 4 this will give us
00:03:31.959 most of the software we need for a
00:03:33.760 development
00:03:35.480 environment and I will populate this
00:03:38.120 file with the following content you
00:03:41.159 remember how I suggested you install the
00:03:43.720 docker vs code extension this
00:03:46.239 functionality where you can
00:03:47.799 rightclick and inspect what's going on
00:03:52.239 is powered by that
00:03:54.640 extension we're
00:03:57.920 using 312
00:04:00.640 slim
00:04:02.760 anyways in this tutorial I'm using VSS
00:04:06.079 code so I'll show you how I like to open
00:04:07.959 the development container there are
00:04:09.760 other techniques for doing so like
00:04:12.159 running scripts to open it or you can
00:04:14.560 follow other techniques that use other
00:04:16.199 Ides but like I said I'm just going to
00:04:18.358 show you how to do it with VSS code for
00:04:19.759 now shift command P this will open up
00:04:23.759 the command pallet as it's socalled and
00:04:26.759 I can locate an option that says Dev
00:04:29.720 containers reopen in container I will
00:04:32.880 select this by pressing
00:04:36.440 enter and now our development container
00:04:40.039 is being built if I pull up Docker
00:04:43.680 desktop we can see that we currently
00:04:46.199 have no containers that are registered
00:04:49.080 with this
00:04:50.160 application after the development
00:04:51.960 container has been built we will see it
00:04:54.479 listed here two very boring minutes
00:04:57.880 later okay that took about 2 2 to 3
00:05:00.080 minutes for me note the first time you
00:05:03.759 run a Docker container it will tend to
00:05:06.120 be very slow but as Docker caches a lot
00:05:09.880 of files on your behalf subsequent runs
00:05:12.680 of your container will tend to be faster
00:05:15.440 also note if for some reason you have to
00:05:18.120 edit either the dev container
00:05:20.120 specification or the docker file you
00:05:22.520 will probably need to rebuild your
00:05:24.400 development container and take that two
00:05:26.360 to three minute hit of wait time where
00:05:29.160 you're waiting for the container to be
00:05:30.720 rebuilt also note that we are using a
00:05:34.319 specific version of a python container
00:05:36.440 called python 12
00:05:39.600 slim this is a version of a python
00:05:42.360 container that gives us python but
00:05:44.160 strips out a lot of unnecessary files in
00:05:46.319 order to keep our development
00:05:47.479 environment super lean let's quickly
00:05:50.199 smoke test this development container to
00:05:52.600 make sure it's
00:05:54.520 legit let's check and make sure we have
00:05:56.960 G installed we do
00:06:00.759 let's make sure we have curl installed
00:06:04.520 we
00:06:05.400 do let's make sure we have python
00:06:09.680 installed we
00:06:11.800 do and let's double check which version
00:06:15.520 of Linux we're
00:06:19.160 using
00:06:21.199 Debian so at this point we have pretty
00:06:24.080 much most of what we need to develop any
00:06:26.840 python application setting up this Dev
00:06:29.919 container is the first step in our
00:06:31.639 larger goal of deploying a fast API to
00:06:34.479 GCR what we're really doing here is a
00:06:37.160 building something cool and be sharing
00:06:38.960 it with the world as quickly cheaply and
00:06:41.080 simply as possible we'll continue in the
00:06:43.440 next sections by building the fast API
00:06:46.599 deploying it to GCR and then setting up
00:06:48.759 a cicd
00:06:50.000 No text
00:06:51.319 pipeline now we are going to build a
00:06:53.720 simple fast API remember the focus is
00:06:57.840 not building some crazy API here but
00:07:00.080 rather learning the overall process of
00:07:02.240 how to deploy dockerized containers to
00:07:05.319 GCR setting up a fast API just entails
00:07:08.800 adding some files and folders to our
00:07:10.560 project I will speed this up to not bore
00:07:12.759 you
00:07:15.930 [Music]
00:07:32.800 notice how we have These Warnings on our
00:07:36.440 Imports and the warning says something
00:07:38.560 along the lines of import could not be
00:07:41.120 resolved this is because we have not yet
00:07:43.400 installed our packages so let's do that
00:07:45.680 really
00:07:47.800 quick notice that after we install our
00:07:50.800 packages the import warnings go
00:07:56.759 away let's run two quick smoke tests to
00:08:00.120 make sure everything is working so let's
00:08:04.479 run the fast API
00:08:07.520 and open up a new terminal and let's hit
00:08:12.680 an endpoint on the fast API make sure
00:08:15.000 it's working hello world
00:08:17.560 fantastic now let's also make sure that
00:08:20.639 our breakpoint debugger works so let's
00:08:24.199 add a integration for vs codes
00:08:27.319 breakpoint debugger and we want to
00:08:29.199 remove Ely attach to our debug server
00:08:31.919 listening on Port
00:08:35.200 5678 fantastic now let's run the
00:08:40.279 breakpoint debugger and if we put a
00:08:42.640 breakpoint here and hit the endpoint
00:08:46.920 again it pauses on our break point so
00:08:50.920 debugging works as well so everything is
00:08:52.760 looking great now that we have our API
00:08:55.200 developed let's ship it to the world
00:08:57.000 No text
00:09:03.240 we have now arrived at the meat of the
00:09:05.240 matter I.E deploying a containerized
00:09:08.079 fast API to GCR let's install gcp CLI
00:09:12.800 into our development container here is
00:09:15.399 the new version of the development
00:09:17.560 Docker file you can look through it and
00:09:19.959 see that it will install gcloud which is
00:09:23.040 gcps CLI this is a change to the docker
00:09:26.079 file so we will need to rebuild our
00:09:28.800 development container how do we do that
00:09:32.079 we type shift command
00:09:34.839 p and reload
00:09:41.760 window after doing that you should see
00:09:44.079 the dev containers extension pick up
00:09:46.760 that there was a change to the docker
00:09:48.480 file you can click this rebuild button
00:09:51.440 if you're wondering how I figured out
00:09:52.760 the instructions of how to install
00:09:54.079 gcloud onto Debian Linux what I did was
00:09:58.399 search the webs and I found this
00:10:03.000 documentation on
00:10:06.200 gcp with pretty clear instructions for
00:10:08.560 how to install g-cloud onto Debi and
00:10:10.959 Linux
00:10:14.630 [Music]
00:10:31.320 after our Dev container has been rebuilt
00:10:34.160 we can run this smoke test to confirm
00:10:36.200 that g-cloud has been
00:10:39.560 installed and indeed it has when you're
00:10:42.959 working with gcp or any cloud provider
00:10:45.519 for that part you want to stay organized
00:10:48.279 and the suggested technique for doing
00:10:49.760 this is to organize the resources you
00:10:52.079 provision into
00:10:54.480 projects so let's create a project and
00:10:59.000 we'll we call it how to deploy a fast
00:11:04.040 API to GCR we'll click create and we'll
00:11:08.760 be able to easily delete all of the
00:11:10.519 resources we provision by simply
00:11:12.440 deleting this project so we'll select
00:11:15.360 this project the next thing to do is
00:11:18.800 authenticate our Dev container with our
00:11:23.120 gcp account so the way we do that is by
00:11:27.160 typing gcloud
00:11:32.639 init yes I would like to log
00:11:35.380 [Music]
00:11:37.880 in it'll spit out a URL that you can go
00:11:42.560 to in your
00:11:47.600 browser I will choose my
00:11:54.200 account
00:11:55.760 type my password
00:12:00.440 accept and then I will eventually be
00:12:03.160 given
00:12:05.240 a verification code that I can use to
00:12:09.279 authenticate my Dev container with gcp
00:12:12.519 then I will select the project that we
00:12:16.240 just
00:12:16.959 created and now our Dev container is set
00:12:21.399 up to provision resources in this
00:12:26.600 hyphenated project that we just created
00:12:28.560 as perfect our development container is
00:12:30.680 for several reasons it's not quite
00:12:32.360 suitable for production so what we'll do
00:12:34.519 now is prepare our application to be
00:12:36.279 deployed starting by first creating
00:12:38.199 what's called a repository in our gcp
00:12:41.000 account our repository is a place where
00:12:43.880 we can store our images to give you an
00:12:46.240 analogy if you're confused by this
00:12:47.560 Docker lingo the docker file is sort of
00:12:50.120 like a blueprint we will read the
00:12:52.120 instructions in our Docker file and that
00:12:53.639 will leave us with what's called an
00:12:55.120 image an image will be a Deployable
00:12:57.839 version or runnable version of our
00:12:59.760 application and all of the dependencies
00:13:01.480 it requires including its OS
00:13:03.320 requirements let's check out
00:13:06.639 our Google Cloud console and go over to
00:13:10.000 the artifact registry enable it for our
00:13:14.720 project this is where we will be storing
00:13:17.160 our images now let's create a repository
00:13:20.279 that will store all of the images for
00:13:22.560 the production versions of our
00:13:24.120 application here's how we do this
00:13:30.000 great and now if we reload the console
00:13:33.760 we see we have a repository created in
00:13:36.800 our artifact registry let's now create
00:13:41.000 another Docker file in our project this
00:13:43.959 one will house the instructions for how
00:13:46.199 to build our application for deployment
00:13:49.399 purposes this one is called Docker
00:13:52.639 file. and this is the content that we
00:13:56.320 will populate this file with now that we
00:13:59.519 have our production Docker file we will
00:14:01.440 add one more file called Cloud build.
00:14:06.610 [Music]
00:14:10.600 yaml now we can issue a command to gcp
00:14:15.600 through the gcloud CLI that will read
00:14:19.240 these instructions and build our Docker
00:14:22.399 file in a way that's compatible with the
00:14:25.079 GCR platform let's give this a spin what
00:14:29.639 you're seeing here is something you'll
00:14:31.600 see often when interacting with the gcp
00:14:34.800 platform they do their best to ask for
00:14:37.519 your consent before using new features
00:14:41.000 on their platform I will say yes so
00:14:45.199 let's pop over to our repository once
00:14:49.160 again I reload
00:14:52.480 this eventually we should see our image
00:14:56.040 stored here and there it is so once
00:14:58.560 again what we we did was create another
00:15:01.440 Docker file that includes the
00:15:02.759 instructions for how to build our
00:15:04.560 application in a way that we can deploy
00:15:06.320 to GCR we also included a file called
00:15:09.600 Cloud build. yo we ran the command to
00:15:12.600 perform our build on gcloud and when
00:15:15.519 that succeeded we now have an image in
00:15:17.920 our repository now that we have our
00:15:20.160 production image stored in a repository
00:15:22.600 in Google artifact registry we can issue
00:15:25.040 a command to GCR to pull our image from
00:15:28.639 our repository and run it let's see what
00:15:31.440 that looks like first what we'll do is
00:15:33.440 create another file in our project
00:15:36.040 called service. yo and we will populate
00:15:39.040 this file with the following
00:15:44.279 content and now let's run our
00:15:48.240 application in
00:15:50.800 GCR here is some more permission
00:15:54.440 stuff yes I would like to enable GCR on
00:15:58.480 this project
00:16:00.680 and look at that we've been given a URL
00:16:04.199 that will allow us to interact with the
00:16:05.720 deployed version of our application so
00:16:08.120 if I command click let's see what we
00:16:13.240 find this is expected because by default
00:16:17.240 GCR services are not publicly accessible
00:16:21.560 so we have to do one last thing update
00:16:26.800 our service policy and and the way we do
00:16:29.519 that is by creating another file in our
00:16:32.920 project and we will populate this
00:16:36.480 file with the following
00:16:39.399 content this is a policy that allows
00:16:42.639 anybody to invoke our service so let's
00:16:47.079 apply this policy to our
00:16:49.480 service and now when we load our
00:16:51.759 endpoint let's see what we
00:16:57.040 find we've come a long way you now know
00:17:00.720 how to take containers that run on your
00:17:02.480 local machine and deploy them to an
00:17:04.720 amazing managed service like
00:17:08.039 GCR it's quite annoying though to have
00:17:10.599 to manually trigger a build and manually
00:17:13.559 update our GCR service each time we want
00:17:16.280 new code to be pushed to our endpoint so
00:17:19.359 what we'll do in the final part of this
00:17:21.359 tutorial is set up an automation on
00:17:24.640 GitHub so that each time we push code to
00:17:27.359 our main branch it will automatically
00:17:30.120 trigger our builds and automatically
00:17:32.240 update our GCR service let's see what
00:17:35.240 that looks like in the final
00:17:38.000 No text
00:17:39.080 installation there are many tools we
00:17:41.280 could use for automating our deployments
00:17:43.880 but today we are going to be checking
00:17:45.720 out GitHub actions this is the
00:17:49.400 repository we will be using to test out
00:17:51.760 GitHub actions if you don't already know
00:17:54.400 this repository holds a fast API and
00:17:57.200 each time we update the code in the main
00:17:59.600 branch of our fast API we would like to
00:18:01.880 trigger an automation that will
00:18:03.240 automatically deploy a new version of
00:18:05.000 our application to Google Cloud run the
00:18:07.799 process for doing this is actually quite
00:18:09.480 simple first we need to come over to our
00:18:12.240 gcp account and provision a service
00:18:16.760 account which is a fancy way of saying
00:18:19.880 access credential so you will create a
00:18:23.440 service account called how to deploy
00:18:26.400 doize fast apis to Google Cloud
00:18:30.520 run yes create and continue continue
00:18:34.559 done and then what we want to do is add
00:18:38.679 a
00:18:40.200 key download our
00:18:43.320 key this is our password that will give
00:18:48.760 GitHub the permissions to push new
00:18:52.200 services to our gcp account so we come
00:18:55.360 back to our GitHub
00:18:57.280 repository we come over to the settings
00:19:01.080 section and we come over to the secrets
00:19:04.440 and variables
00:19:05.760 section actions and we are going to
00:19:08.919 create a new repository secret we'll
00:19:12.640 paste in our service account credentials
00:19:17.600 as it's so calleded and the name of this
00:19:20.159 secret will be
00:19:22.640 gcpsa key add the secret and the
00:19:26.520 integration work of making GitHub talk
00:19:28.960 to our gcp account has been completed
00:19:31.559 now we'll specify the details of our
00:19:33.919 deployment automation or our GitHub
00:19:36.720 action the way that we do this is by
00:19:39.760 creating a special folder in our project
00:19:43.480 directory called.
00:19:46.559 GitHub and inside of this. GitHub folder
00:19:50.640 we place another folder called workflows
00:19:59.880 inside of this workflows folder you can
00:20:01.880 place a yo file that I believe can be
00:20:04.360 called whatever we like I have called it
00:20:06.679 cicdl this is the content that I will
00:20:10.720 use to populate this file with if we
00:20:13.760 scan this file we can see it consists of
00:20:16.400 a series of
00:20:17.960 instructions whereby we authenticate the
00:20:22.440 gcp
00:20:24.400 and then issue some instructions that
00:20:27.200 deploy a new service to GCR on our
00:20:31.400 behalf so let's push this to our GitHub
00:20:34.600 repository and hopefully it works the
00:20:37.159 first
00:20:43.200 time if we come back to our repository
00:20:46.720 and go over to the actions tab we can
00:20:49.640 now
00:20:50.480 see an automation is in flight and we
00:20:53.840 can view the build logs in real time
00:21:10.440 holy it
00:21:12.679 worked so let's come to our endpoint
00:21:17.480 again which is already loaded here and
00:21:19.240 if we reload
00:21:20.960 this it's still working now let's do a
00:21:25.559 quick end to end test and let's put a
00:21:29.559 Emoji
00:21:38.000 here okay we see
00:21:40.919 another automation has been
00:21:51.520 triggered okay let's reload the
00:21:55.279 service and now we see our update you
00:21:57.880 might run into some issues with
00:21:59.919 permissions between GitHub and
00:22:03.320 gcp or you might run into some
00:22:05.799 permissions issues with your service
00:22:08.679 account and gcp I included some tips in
00:22:12.200 the GitHub repository for how to add
00:22:14.760 permissions you'll probably need but if
00:22:16.480 you run into any issues leave a comment
00:22:19.440 and we made it
