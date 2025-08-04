---
video_title: "How to run DeepSeek AI models on a Laptop"
video_url: "https://www.youtube.com/watch/kE_bBML0xW0"
---

00:00:00.900 [Music]
00:00:03.840 we are now going to show how anyone with
00:00:05.720 a laptop can run one of the smaller R1
00:00:08.280 series models from Deep seek AI using a
00:00:10.639 combination of three tools olama open
00:00:14.879 web UI and
00:00:16.720 Docker the only requirements you'll need
00:00:19.039 are a sufficient amount of hard drive
00:00:20.640 space at least 100 gigb is more than
00:00:23.359 enough and a sufficient amount of ram at
00:00:26.400 least 16 GB is recommended while running
00:00:29.679 a models locally is not going to be a
00:00:31.519 fit for everyone or every use case the
00:00:33.840 nice thing about it is that the data
00:00:35.200 regarding your interactions with
00:00:36.559 whatever AI model you're running are
00:00:38.160 going to be kept private and the data
00:00:39.640 will not be leaked off your machine the
00:00:42.280 exact model we're going to be running is
00:00:44.239 called Deep seek R1 distill llama 8B for
00:00:48.520 Simplicity I'm just going to refer to
00:00:49.960 this model as r18 moving forward in the
00:00:53.039 latest batch of models released by deeps
00:00:55.000 AI in January 2025 six of them are
00:00:58.399 referred to as quote unquote distill
00:01:01.239 models what I understand this distill
00:01:04.000 term to mean is that the team at deeps
00:01:06.240 AI started with a handful of open-
00:01:08.479 source AI models for example quen 2.5
00:01:11.560 math 7B from Alibaba or llama 3.1 8B
00:01:15.280 from meta and then used deep seek R1
00:01:19.040 671b aka the largest of the R1 models to
00:01:22.560 generate 800,000 synthetic training
00:01:25.159 examples that were subsequently used for
00:01:27.640 fine-tuning the term synthetic training
00:01:30.159 examples means that instead of
00:01:31.400 collecting data from The Real World AI
00:01:33.759 researchers simply prompted deep seek R1
00:01:36.200 671b AKA The Big Daddy of the R1 series
00:01:39.240 models 800,000 times and took whatever
00:01:41.720 the outputs were for each prompt as the
00:01:44.079 correct answers a common analogy you'll
00:01:46.960 hear for describing how this fine-tuning
00:01:49.280 or distillation process works is it's
00:01:51.520 sort of like a teacher showing a student
00:01:53.880 a bunch of examples of how to respond to
00:01:55.719 various inputs and having the student
00:01:58.240 emulate the teacher's responses let's
00:02:00.560 now move away from this technical stuff
00:02:02.280 and show how to actually use this
00:02:04.000 technology while I'll show how to do
00:02:05.920 this on a Mac the general flow of what
00:02:07.759 you'll see will apply for Windows and
00:02:09.598 Linux as well here's a diagram showing
00:02:12.360 what we're about to
00:02:14.000 do if you've never heard of AMA olama is
00:02:17.120 a free open- source tool that makes it
00:02:18.920 easy to download and run AI models AMA
00:02:22.120 offers support for Mac windows and Linux
00:02:24.239 and can be installed in less than a
00:02:25.840 minute let me show you come over to
00:02:28.319 ama.com and and you should see this
00:02:30.720 download button and after you click that
00:02:33.239 download button you can select the
00:02:34.720 appropriate version for your OS mine is
00:02:37.080 Mac OS so I'll click this download for
00:02:38.879 Mac OS button and that'll kick off the
00:02:42.440 download after the download is complete
00:02:45.080 you should see a zip file in your
00:02:46.760 downloads folder unzip the zip file and
00:02:49.720 drag the resulting
00:02:51.360 application into your applications
00:02:53.480 folder you can then launch AMA just like
00:02:56.040 you would launch any other application
00:02:58.400 first time you launch it you should
00:02:59.840 should see some consent
00:03:03.040 dialogues I'm providing my account
00:03:06.159 password and that's it when AMA is
00:03:09.720 running you should see this little llama
00:03:11.400 icon in the top menu of your desktop
00:03:14.440 olama is primarily a command line tool
00:03:16.560 so while you can launch it and shut it
00:03:18.640 down with your graphics interface you
00:03:20.799 will need a shell to interact with it so
00:03:22.959 let's pop open a shell and for example
00:03:26.400 let's type O
00:03:28.280 Lama list
00:03:30.840 this will show you the list of models
00:03:32.159 that you've downloaded we haven't
00:03:33.840 downloaded any yet so that's why this
00:03:35.519 list is empty now let's type AMA PS this
00:03:40.480 shows you the list of models that are
00:03:41.879 running you can see that we're not
00:03:43.879 running any models yet and if you type
00:03:47.560 AMA help you'll see the complete list of
00:03:50.840 commands that ama offers if you've never
00:03:54.239 heard of open web UI open web UI is a
00:03:56.840 free open source web application that
00:03:58.519 has a very similar interface the chat
00:04:00.159 GPT in order to run open webui though we
00:04:02.840 have to download another free open
00:04:04.400 source tool called Docker downloading
00:04:06.760 and installing Docker should only take a
00:04:08.239 few minutes let me show you come over to
00:04:11.360 doer. and download the appropriate
00:04:13.680 version for your machine for me this is
00:04:16.000 Apple silicone that'll kick off a
00:04:19.440 download when the download is complete
00:04:22.160 you should see a DMG file in your
00:04:24.560 downloads folder you can double click to
00:04:28.320 open and you can can drag the docker
00:04:31.240 doapp icon into your applications
00:04:34.759 folder after that's done you can open
00:04:37.720 Docker just like you would open any
00:04:39.400 other
00:04:42.120 application provide your consent this is
00:04:45.280 the first time we're launching it right
00:04:47.400 and when Docker is running you should
00:04:49.240 see this little whale icon in the top
00:04:52.080 menu of your desktop now that we have
00:04:54.759 Ama installed we can run r18 B with a
00:04:57.759 single command and now that we have
00:05:00.000 Docker installed we can launch open web
00:05:02.360 UI with a single command to here is how
00:05:05.360 we run r18 B so let's come back to our
00:05:07.759 shell and enter the following
00:05:11.680 command ol Run Deep seek D R1 colon
00:05:16.160 8B the model's name in ama is slightly
00:05:18.919 different than the model's name as shown
00:05:20.400 in the original research paper from deep
00:05:22.080 cki but close enough
00:05:25.280 right while r18 is downloading let's
00:05:28.160 come over to ama.com for quick browse so
00:05:30.960 we're familiar with the landing page of
00:05:32.319 ama.com we're familiar with the download
00:05:34.319 page let's come over to the models page
00:05:36.960 and see what's going on here so this is
00:05:39.919 a leaderboard of the most popular models
00:05:42.080 that are currently being used in the AMA
00:05:44.240 ecosystem and we can see at the top of
00:05:46.479 this leaderboard is deeps car1 we can
00:05:49.000 click this item to be taken over to a
00:05:51.840 detail page that gives us a little bit
00:05:53.560 more information about all of the
00:05:54.840 related
00:05:55.880 models here we can see there is one 2 2
00:05:59.960 3 4 5 6 7 models associated with deep
00:06:04.080 seek R1 and this lines up with what the
00:06:06.759 Deep seek R1 research paper says we're
00:06:09.280 going to be playing around with the 8B
00:06:11.840 right and we can see that it is based on
00:06:15.000 llama we can see that if we were to
00:06:17.720 download this model onto our computer
00:06:19.479 it'll take up 4.9 gigs of hard drive
00:06:23.360 space for reference let's also take a
00:06:25.880 look at the big daddy the 671b
00:06:30.400 so here we can see deep seek R1 671b is
00:06:35.479 based on deep seek 2 and if we were to
00:06:38.720 download this model onto our machine it
00:06:40.520 would take up 404 gigs of hard drive
00:06:43.039 space in regards to Ram there is this
00:06:47.080 handy note on the
00:06:49.880 olama GitHub
00:06:52.120 repo that
00:06:54.120 reads you should have at least 8 gigs of
00:06:56.800 RAM available to run 7B models 16 gigs
00:07:00.360 to run 13B models and 32 gigs to run 33b
00:07:04.280 models now that I've been playing around
00:07:06.479 with olama for several months now the
00:07:09.240 pattern that I'm picking up on is that
00:07:12.560 for every 1 billion parameters a model
00:07:14.680 has you'll need about 1 gig of RAM so to
00:07:18.160 drive this home on the machine that I'm
00:07:20.039 demoing on I have 500 gigs of hard drive
00:07:22.639 space and I have 16 gigs of RAM so in
00:07:25.199 regards to the Big Daddy the R1 671b
00:07:27.560 model I do have enough hard drive space
00:07:29.759 to store it right because 404 gigs is
00:07:32.120 less than 500 but I don't have enough
00:07:34.440 RAM to run it but in regards to the r18
00:07:37.639 B the r18 B only requires about 4.9 gigs
00:07:40.960 of hard drive space and only about 8
00:07:44.560 gigs of ram my machine has 60 gigs of
00:07:46.879 RAM which is more than 8 gigs so we're
00:07:48.520 good hopefully you have a feel for how
00:07:50.400 this all works FYI hard drive memory is
00:07:53.120 a type of memory technology used for
00:07:54.800 long-term storage whereas Ram is used
00:07:56.960 for running applications Ram AKA random
00:08:00.400 access memory is a type of memory
00:08:02.000 technology that's capable of being read
00:08:04.000 and updated much faster compared to hard
00:08:06.080 drive memory but is not designed for
00:08:08.400 long-term
00:08:11.840 storage okay now it looks like deeps r18
00:08:15.039 B is running so next let's run open web
00:08:17.560 UI if we come over to openweb ui.com
00:08:21.879 and click on this get open web UI button
00:08:26.199 it'll take us over to the GitHub repo
00:08:28.080 for open web UI
00:08:30.159 and if we scroll down to the read me
00:08:32.440 eventually we'll see some commands that
00:08:34.479 we can copy
00:08:35.958 paste and this is the one that we want
00:08:38.880 if AMA is on your computer use this
00:08:40.919 command so I'm going to copy this and
00:08:44.399 let's come back to our shell open up a
00:08:46.760 new tab paste run and when this command
00:08:51.880 is finished we should be able to visit
00:08:53.600 Port 3000 in our browser and we should
00:08:56.120 see the open webui web application
00:09:02.519 okay now that this Docker command has
00:09:04.480 finished running we should be able to
00:09:06.320 come over to our browser visit Local
00:09:09.320 Host Port
00:09:11.519 3000 here I'm
00:09:14.320 reloading and there we go it did take a
00:09:17.360 couple of seconds to boot up after the
00:09:20.000 docker command finished as you saw but
00:09:21.959 here we are Local Host Port 3000 and we
00:09:25.920 have our open web UI application running
00:09:29.839 on our machine next let's shut off our
00:09:33.320 internet connection just to prove that
00:09:35.560 there are ways of using deep seek AI
00:09:37.600 technology
00:09:39.160 privately and let's get started this is
00:09:41.959 a bit strange but this is how open web
00:09:43.720 UI works so by default it comes with a
00:09:46.040 login system so you'll need to provide
00:09:49.519 some credentials these are going to be
00:09:51.120 stored in a local SQ light
00:09:54.640 database whatever you
00:09:58.000 want and here we are we're logged
00:10:01.399 in and because we already have deeps R1
00:10:04.120 8B downloaded and running open web UI
00:10:07.279 should pick it up automatically in case
00:10:09.440 you're not seeing it you can enter the
00:10:11.200 olama model ID for deeps car18 here and
00:10:15.000 click this button that says pull deeps
00:10:17.120 r1ab from ama.com right that'll set
00:10:19.079 everything up for you but it looks like
00:10:21.240 we're good to go and hopefully this user
00:10:23.959 interface seems very familiar to you in
00:10:26.600 the sense that it's very much like chat
00:10:28.600 GPT you have your chats over here and
00:10:32.040 you can send messages to a model here so
00:10:35.200 if I
00:10:36.600 say hello we are now interacting with
00:10:40.560 deep seek r18 right here's the next
00:10:44.360 prompt that we'll test tell me an
00:10:46.760 inspirational quote from Nelson
00:10:48.839 Mandela if we pop open this we can see
00:10:52.040 the internal dialogue the model is
00:10:55.360 having with itself and then we get the
00:10:57.760 final response
00:11:00.920 here is the next prompt that we'll test
00:11:03.680 write some marketing copy for promoting
00:11:05.360 a
00:11:06.040 workshop we can pop open this drop down
00:11:10.120 to see the internal
00:11:16.800 dialogue and there we
00:11:19.519 go so the way these reasoning models
00:11:22.000 work is they'll generate a chain of
00:11:26.880 thought that's what you're seeing here
00:11:30.519 and once the Chain of Thought completes
00:11:32.399 you'll see the final output
00:11:34.600 printed so as we can see while this
00:11:37.000 locally hosted r1ab model is supposedly
00:11:39.399 on par or even beating leading AI models
00:11:41.959 like GPT 40 and Cloud 3.5 Sonet the fact
00:11:45.160 that it's not multimodal and has this
00:11:47.120 slower system two style ux tells me that
00:11:49.440 in the immediate it's not going to be
00:11:51.360 replacing apps like chat gbt and Cloud
00:11:54.120 but this technology definitely looks
00:11:55.800 very promising and I definitely keep an
00:11:57.639 eye out on any future models released by
00:11:59.560 Deep seek AI piss
