---
video_title: "Development or Dev Containers in 5 minutes"
video_url: "https://www.youtube.com/watch/Un2Nw00oL2s"
---

00:00:00.000 [Music]
00:00:01.880 development containers are a
00:00:03.360 specification being developed at
00:00:04.960 Microsoft that allows you to attach your
00:00:07.160 IDE to a Docker container containing
00:00:09.400 your development environment at the time
00:00:11.599 of recording the only IDE that have
00:00:13.799 solid support for Dev containers are vs
00:00:17.000 code and intellig so if you don't use
00:00:19.720 these idees this video is probably not
00:00:21.960 going to be too practical for you to
00:00:23.840 easily follow along you'll need at least
00:00:25.560 a rudimentary understanding of the
00:00:27.240 following tools SLC Concepts docker
00:00:30.640 Docker desktop VSS code I.E the world's
00:00:33.360 most popular application for editing
00:00:34.879 code vs code extensions particularly you
00:00:38.280 will need the docker extension and the
00:00:39.960 dev containers extension installing
00:00:41.640 these extensions should only take a few
00:00:43.440 clicks and a few seconds and also
00:00:46.320 General software development Concepts
00:00:48.199 like git CLI commands apis and
00:00:51.160 programming languages will definitely
00:00:52.480 help you out with following
00:00:56.120 along here we are starting with an empty
00:00:58.840 folder on our computer
00:01:00.920 let's start by creating AEV container
00:01:03.399 folder at the root of our
00:01:05.640 project inside of this folder let's
00:01:07.720 create an empty file called Dev
00:01:09.960 container. Json what should we put in
00:01:12.680 this file you might ask well if we take
00:01:14.840 a look at the official Dev container
00:01:16.799 spec we'll see all of the individual
00:01:18.840 keys we could specify but to get us
00:01:21.799 moving along I'll just paste in this
00:01:23.240 Json content right here this devc
00:01:26.079 container. Json file is where we specify
00:01:28.159 the details of our development container
00:01:30.720 the name key is where we specify the
00:01:32.399 name we want to give our Dev container
00:01:34.520 this is arbitrary the build key is where
00:01:36.960 we put the reference to the docker file
00:01:38.520 that will act as the base point of our
00:01:40.200 development environment this will make
00:01:42.040 more sense later the customizations key
00:01:44.439 is where we can customize many things
00:01:46.200 here we're customizing which VSS code
00:01:48.759 extensions we want installed into the
00:01:50.399 VSS code instance that gets attached to
00:01:53.000 our development
00:01:54.079 container line 18 I don't think we need
00:01:56.759 but I put it here because it doesn't
00:01:58.520 hurt this is where we can specify which
00:02:00.600 ports on our host machine will get
00:02:02.320 forwarded to ports on our
00:02:04.320 container the workspace
00:02:06.640 Mount is where we specify the location
00:02:11.200 inside of the development container that
00:02:13.680 our project files will get mounted into
00:02:16.680 on line 22 we have a key that says
00:02:19.080 workspace folder this is the folder that
00:02:21.640 will get opened by default when we open
00:02:24.080 our development
00:02:25.319 container and on line 23 we have an
00:02:28.200 empty run args array this is where we
00:02:30.560 can specify some further customizations
00:02:33.080 that we're not going to need for the
00:02:33.959 moment next we'll add the docker file
00:02:36.720 referenced on line 4 this will give us
00:02:39.360 most of the software we need for
00:02:41.200 development
00:02:42.920 environment and I will populate this
00:02:45.519 file with the following content you
00:02:48.599 remember how I suggested you install the
00:02:51.159 docker vs code extension this
00:02:53.599 functionality where you can
00:02:55.239 rightclick and inspect what's going on
00:02:59.560 is powered by that
00:03:02.080 extension we're
00:03:05.400 using 312
00:03:08.040 slim
00:03:10.159 anyways in this tutorial I'm using VSS
00:03:13.480 code so I'll show you how I like to open
00:03:15.360 the development container there are
00:03:17.159 other techniques for doing so like
00:03:19.599 running scripts to open it or you can
00:03:22.000 follow other techniques that use other
00:03:23.599 Ides but like I said I'm just going to
00:03:25.760 show you how to do it with vs code for
00:03:27.200 now shift command p this will open up
00:03:31.159 the command pallet as it's so-called and
00:03:34.120 I can locate an option that says Dev
00:03:37.040 containers reopen in container I will
00:03:40.239 select this by pressing
00:03:43.879 enter and now our development container
00:03:47.439 is being built if I pull up Docker
00:03:51.080 desktop we can see that we currently
00:03:53.519 have no containers that are registered
00:03:56.480 with this
00:03:57.560 application after the development
00:03:59.319 container has been built we will see it
00:04:01.879 listed here two very boring minutes
00:04:05.280 later okay that took about 2 to 3
00:04:07.400 minutes for me note the first time you
00:04:11.120 run a Docker container it will tend to
00:04:13.519 be very slow but as Docker caches a lot
00:04:17.279 of files on your behalf subsequent runs
00:04:20.079 of your container will tend to be faster
00:04:22.919 also note if for some reason you have to
00:04:25.520 edit either the dev container
00:04:27.520 specification or the docker file you
00:04:29.919 will probably need to rebuild your
00:04:31.800 development container and take that two
00:04:33.759 to three minute hit of wait time where
00:04:36.560 you're waiting for the container to be
00:04:38.120 rebuilt also note that we are using a
00:04:41.680 specific version of a python container
00:04:43.800 called python 12
00:04:47.000 slim this is a version of a python
00:04:49.759 container that gives us python but
00:04:51.520 strips out a lot of unnecessary files in
00:04:53.759 order to keep our development
00:04:54.880 environment super lean let's quickly
00:04:57.560 smoke test this development container to
00:05:00.039 make sure it's
00:05:01.919 legit let's check and make sure we have
00:05:04.360 G installed we
00:05:06.110 [Music]
00:05:07.160 do let's make sure we have curl
00:05:10.919 installed we
00:05:12.800 do let's make sure we have python
00:05:17.039 installed we
00:05:19.199 do and let's double check which version
00:05:22.919 of Linux we're
00:05:26.600 using Debian
00:05:29.759 so at this point we have pretty much
00:05:32.080 most of what we need to develop any
00:05:34.240 python application
