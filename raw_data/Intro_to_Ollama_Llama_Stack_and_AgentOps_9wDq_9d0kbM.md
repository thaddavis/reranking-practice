---
video_title: "Intro to Ollama, Llama Stack, and AgentOps"
video_url: "https://www.youtube.com/watch/9wDq_9d0kbM"
---

00:00:00.320 the development of a llama stack and
00:00:01.959 agent Ops integration is entering its
00:00:03.719 final stages for those unfamiliar with a
00:00:05.879 llama ecosystem llama stack is an agent
00:00:08.320 framework authored by meta and it pairs
00:00:10.120 nicely with another tool called olama
00:00:12.960 olama is a tool that allows you to run
00:00:14.799 llms locally on your own machine AKA
00:00:17.359 your laptop or desktop or whatever
00:00:19.279 homebuilt device you want to run these
00:00:20.480 models on yes while llama ecosystem
00:00:23.119 models tend not to be as large as safe
00:00:25.439 frontier models like gbt 40 or claw 3.5
00:00:27.960 Sonet you'll be surprised to hear that
00:00:29.599 for many use cases they are actually on
00:00:31.920 par due to how much data these llama
00:00:33.480 models have been trained on the real
00:00:35.840 benefit of using these llama models
00:00:37.200 however has nothing to do with
00:00:38.200 benchmarks but has more to do with the
00:00:39.520 fact that you can audit with 100%
00:00:41.000 certainty that the model weights are not
00:00:42.600 changing and that your interactions with
00:00:44.160 them are kept completely private but
00:00:46.559 anyways the growth of the Llama
00:00:48.280 ecosystem in the coming years is
00:00:49.559 inevitable and long story short the
00:00:51.440 agent Ops team is ahead of the curve on
00:00:53.039 this one in this video we are going to
00:00:55.079 show how to use llama stack o llama as
00:00:58.320 well as show how to monitor llama stack
00:01:00.000 applications using aops keep in mind
00:01:02.559 though that in regards to agent Ops what
00:01:03.879 you're going to see is a sneak peek of
00:01:05.400 what's in the release pipeline so keep
00:01:07.320 your eyes peeled on the official agent
00:01:09.040 Ops release notes for when this
00:01:10.200 eventually lands at the time of
00:01:12.080 recording this integration is being
00:01:13.640 audited and
00:01:16.520 tested here is a diagram of what we are
00:01:19.040 going to set up in this video and let's
00:01:21.960 start by setting up the olama server to
00:01:25.159 download and install olama come over to
00:01:27.439 ama.com click the download button and
00:01:31.840 download the appropriate version for
00:01:33.320 your OS for me this is Mac OS from this
00:01:37.040 point forward I'm just going to show you
00:01:38.240 how I did this on my Mac so I clicked
00:01:41.079 the download for Mac OS
00:01:42.799 button and it downloaded this ZIP
00:01:46.439 file so after you have that downloaded
00:01:48.920 you unzip the zip file and drag the
00:01:51.719 resulting application into your
00:01:54.159 applications
00:01:55.280 folder then you launch the olama
00:01:59.399 application
00:02:01.600 accept all of the permission
00:02:03.640 dialogues and then you'll be presented
00:02:05.719 with this little wizard click next cck
00:02:09.919 install I have to put in my account
00:02:14.680 password and click finish and that's
00:02:18.319 it then should be able to
00:02:22.280 type-v on the command line and see the
00:02:25.879 AMA client version printed out also note
00:02:28.840 how we can start and and stop AMA via
00:02:31.280 this llama icon in the menu bar to start
00:02:34.519 AMA you launch it just like you would
00:02:36.720 launch any other
00:02:38.040 application when AMA is running you
00:02:40.480 should see this little llama icon in
00:02:42.239 your menu bar as olama is a command line
00:02:45.720 tool you'll need to pop open a shell to
00:02:47.920 use it here's an overview of some of
00:02:50.800 ama's commands I hope you find these
00:02:54.319 intuitive in regards to the model IDs I
00:02:57.239 personally love this table on the olama
00:02:59.519 GitHub REO that shows some of the more
00:03:01.440 used models that people like to run
00:03:03.480 along with their
00:03:04.720 IDs it's not of particular relevance to
00:03:07.400 this video but just know that the full
00:03:09.120 list of models that ama supports
00:03:11.400 stretches well into the hundreds and
00:03:13.680 even includes models from outside of
00:03:15.959 llama's ecosystem but anyways Focus to
00:03:20.239 keep things light we will run one of the
00:03:21.799 smallest models that ama offers that
00:03:24.280 being llama 3.2 1B instruct
00:03:27.879 fp16 the 3.2 tells us the family of
00:03:30.640 models it was released with the 1B tells
00:03:33.360 us the amount of parameters that the
00:03:34.720 model has the instruct tells us that the
00:03:36.920 model was fine-tuned for performing
00:03:38.599 instructions and the fp16 does get a bit
00:03:41.120 technical but tells us that when the
00:03:42.360 model generates text the internal
00:03:44.400 calculations are performed using numbers
00:03:45.840 with up to four decimal places if I'm
00:03:47.920 wrong about this fp16 detail please
00:03:49.799 leave a comment you can think of the
00:03:51.760 number of parameters as a rough
00:03:53.200 indication of how many simulated brain
00:03:54.879 cells a model has the more parameters or
00:03:58.079 brain cells than the smart the model
00:04:00.400 will be assuming it's been trained on a
00:04:02.400 sufficient amount of data that is I
00:04:04.400 don't want to get bogged down in
00:04:05.400 excessive detail but what I'm trying to
00:04:06.799 highlight here is that depending on
00:04:08.079 training details a smaller model can
00:04:10.480 outperform a larger one in certain cases
00:04:13.120 if you're interested in learning more
00:04:14.200 about how AI training works I suggest
00:04:15.959 watching this video entitled what is p
00:04:18.358 torch The Unofficial movie or
00:04:20.279 researching topics like neural networks
00:04:21.839 and back propagation as a starting point
00:04:23.919 to use a particular model with olama
00:04:26.919 enter the olama Run command followed by
00:04:29.440 the models
00:04:31.840 ID as a rough guideline you'll need
00:04:34.160 about 8 gigs of RAM for running models
00:04:35.919 with about 7 billion parameters about 16
00:04:38.759 gigs of RAM for running models with
00:04:40.120 about 13 billion parameters and about 32
00:04:42.919 gigs of RAM for running models with
00:04:44.199 about 33 billion parameters the model
00:04:46.800 we're using in this video only has 1
00:04:48.320 billion parameters so it should work on
00:04:50.560 just about any
00:04:54.039 computer AMA supports interactive
00:04:56.880 sessions with the models you run
00:05:00.880 and also in the background serves an
00:05:04.080 API to see the logs of the olama API
00:05:07.919 open up a new
00:05:09.960 terminal and type this command tail-f
00:05:14.840 followed by the path to the olama server
00:05:18.680 logs and move this over here like
00:05:24.080 this and back in the original
00:05:27.680 terminal we can curl the AMA
00:05:32.039 API by closing this interactive
00:05:36.080 session
00:05:38.120 and sending curl statements like
00:05:44.800 so there are other ways to use AMA so
00:05:47.880 feel free to experiment but hopefully
00:05:49.639 this gives you a great gist of how it
00:05:53.880 works now that we have Ama running let's
00:05:56.560 run a llama stack server we're going to
00:05:58.639 run llama stack using Docker which is a
00:06:00.639 tool that makes running all sorts of
00:06:02.000 different types of software super easy
00:06:04.759 fun fact it appears that the CEO of
00:06:07.280 olama Jeffrey Morgan worked as a product
00:06:09.880 manager at Docker for almost 5 years if
00:06:13.120 you don't have Docker installed come
00:06:14.960 over to
00:06:16.000 doer. and download the appropriate
00:06:18.280 version for your machine for me this is
00:06:20.680 Apple
00:06:22.520 silicone and after the download
00:06:24.880 completes open it and drag the docker do
00:06:29.639 app icon into your applications folder
00:06:33.319 I've already done this so I'll click
00:06:35.199 stop but that's it it's that
00:06:37.840 easy in order to launch
00:06:40.560 Docker you
00:06:42.360 simply open the docker application just
00:06:45.240 like you would open any other
00:06:46.840 application when Docker is running you
00:06:50.000 should see this whale icon in your top
00:06:52.759 menu bar after Docker is set up here are
00:06:56.400 the steps for how to run a llama stack
00:06:58.400 server first let's create an empty
00:07:00.919 folder somewhere on our computer I'm
00:07:03.599 calling mine llama stack agent Ops and
00:07:07.000 let's enter this folder we just created
00:07:09.400 and open it with our code
00:07:12.199 editor next let's add a yamamo file that
00:07:16.360 will allow us to configure how llama
00:07:19.240 stack
00:07:20.479 works so I'm going to create a file
00:07:23.280 called run.
00:07:24.630 [Music]
00:07:25.919 yo and let's populate this run. yo file
00:07:29.640 [Music]
00:07:31.520 with the following content that I
00:07:33.919 adapted from the olama example found in
00:07:37.319 Lama stxs GitHub repo here is the
00:07:40.639 content that we will paste into this
00:07:44.759 r.o and just so you can see what it
00:07:47.000 looks like here we are llama stack is an
00:07:50.280 SDK that provides common functionality
00:07:52.159 for building a gentic applications like
00:07:54.440 tool calling and memory modules for
00:07:56.479 example llama stack relies on a separate
00:07:58.919 service for powering the llm inside of
00:08:01.879 llama Stack's GitHub repo you'll see
00:08:03.960 examples for how to plug llam stack into
00:08:06.840 llm and points powered by AWS Bedrock
00:08:10.039 hugging face as well as
00:08:13.800 fireworks but in the name of Freedom
00:08:16.720 Liberty and everything America stands
00:08:18.360 for we are going to be using AMA for
00:08:20.520 powering our llm okay so here's how we
00:08:23.159 do this first we have to make sure AMA
00:08:27.120 is
00:08:28.080 running then we can pop up in a terminal
00:08:31.159 and type the O Lama PS command to see
00:08:36.080 what models are being served and we can
00:08:39.039 see that no models are currently being
00:08:43.120 served and if we
00:08:45.519 type this AMA command AMA run followed
00:08:50.279 by the model ID we're also going to
00:08:52.680 include a flag that says keep alive 60
00:08:56.760 Minutes that will keep the model running
00:08:59.480 running for an hour after we close the
00:09:03.040 interactive session that by default AMA
00:09:06.839 presents to us when we run a model so
00:09:09.519 I'm running this command here we see the
00:09:11.519 interactive
00:09:12.520 [Music]
00:09:14.000 session model's running and if we close
00:09:17.480 the interactive session by typing contrl
00:09:21.880 D and type the oama PS command again we
00:09:27.440 can see that the model will be served
00:09:31.440 for another hour now we can run this
00:09:35.160 Docker command to run a llama stack
00:09:38.560 server powered by this AMA
00:09:42.000 model if you look closely at this Docker
00:09:45.040 command you'll see we're including two
00:09:46.920 environment variables and these are the
00:09:48.959 environment variables that plug llama
00:09:51.200 stack into oama here you can see we're
00:09:54.480 telling llama stack to find AMA at this
00:09:58.480 URL
00:10:00.560 and this is a little confusing but this
00:10:03.240 is how it works the model ID that you
00:10:06.920 want to
00:10:09.800 use is different in lamama stack
00:10:12.800 compared to the same models ID in O Lama
00:10:16.920 so this model llama 3.2 1B instruct
00:10:21.200 fp16 has this model ID in llama
00:10:26.320 stack so after you run this Docker
00:10:30.120 command we should have a running llama
00:10:45.079 stack okay that looks good and we can
00:10:48.079 smoke test this by popping open second
00:10:51.600 terminal and hitting the Llama stack
00:10:55.120 api's health check
00:10:56.839 endpoint and we see the status is okay
00:11:00.279 let's now run two more quick tests so
00:11:02.760 you get a feel for what using llama
00:11:04.399 stack is like if you've done any AI
00:11:07.279 agent development at all you should find
00:11:08.880 this very familiar so
00:11:12.600 first you'll need python installed I'm
00:11:17.160 using Python
00:11:20.000 3.13 and next up let's create a virtual
00:11:23.839 environment so that we can install
00:11:25.560 packages into our project without
00:11:27.760 affecting any other Pyon projects on our
00:11:32.519 system and if that command works you
00:11:35.639 should see a VM folder at the root of
00:11:38.440 the
00:11:39.880 project let's activate our virtual
00:11:42.800 environment like
00:11:44.040 [Music]
00:11:46.720 so and create a requirements.txt
00:11:51.500 [Music]
00:11:54.000 file and
00:11:56.480 add these packages and package versions
00:12:00.399 into the requirements.txt
00:12:04.560 and then we can install these packages
00:12:08.279 with the PIP install
00:12:13.639 command and when the installation
00:12:17.000 process has
00:12:18.880 finished let's add a
00:12:21.720 file called Simple inference
00:12:26.800 dopy and
00:12:30.079 here is the code we'll put in this
00:12:33.320 simple inference dopy file hopefully
00:12:36.000 this should look very familiar you can
00:12:37.760 see all we're doing here is pointing
00:12:40.800 this code to the Llama stack API running
00:12:43.519 on Port
00:12:45.480 5001 this is the model ID we'd like to
00:12:49.880 use and this is the prompt that we're
00:12:52.560 going to send via code right a
00:12:54.760 three-word poem about the moon so let's
00:12:57.199 run this script and see what happen
00:13:03.760 happens silent lunar
00:13:06.519 glow and for this second quick example
00:13:09.519 let's show how to use llama Stack's
00:13:11.519 agent class we're going to build an
00:13:15.680 agent that has one
00:13:18.680 tool and that one tool will be the
00:13:21.560 ability to use the brave browser API so
00:13:26.959 we'll need to add a EMV file to our
00:13:32.000 project that will include an entry for
00:13:36.440 holding our brave browser API key you
00:13:40.800 can provision an API key on the brave
00:13:44.800 search API
00:13:46.440 console you can sign up for
00:13:49.279 here once you have that API key
00:13:51.600 provision copy it into your
00:13:56.560 project and in order to make
00:13:59.720 these API Keys available to our code
00:14:02.920 we're going to need to
00:14:04.560 install python.
00:14:09.480 M and after the installation
00:14:12.560 completes let's create a file called
00:14:15.800 Simple
00:14:17.560 agent and populate this simple agent. py
00:14:21.480 file with the following
00:14:25.639 code here you can see we're plugging
00:14:27.800 into the Llama stack AP on Port 50001
00:14:30.920 here's the model ID we're going to
00:14:32.959 use here's where we configure the
00:14:37.079 agent and this is the prompt that we're
00:14:39.639 going to send to our agent who won the
00:14:41.839 NBA championship in 2020 please use
00:14:44.880 tools so let's run this and see what
00:14:55.320 happens and that is the right answer it
00:14:57.759 was the Lakers
00:15:00.639 so hopefully you have a great idea or a
00:15:03.600 great gist at least of what llama stack
00:15:06.360 is all
00:15:08.560 about now let's show how to set up agent
00:15:10.839 Ops for monitoring applications that
00:15:12.639 Leverage The lamaack Client python
00:15:15.720 SDK first come over to app. aent ops.
00:15:19.240 and sign up if you haven't already there
00:15:20.920 is a free tier
00:15:22.440 supported and after you're signed up
00:15:25.199 come over to the API key section
00:15:30.639 and provision an API
00:15:32.519 key and once you've done that you can
00:15:34.959 copy the API key and let's add it to our
00:15:39.440 project in the EMV
00:15:43.360 file let's add a new entry that reads in
00:15:47.399 all caps
00:15:49.920 agent
00:15:52.160 opscore API unor key equals and then
00:15:56.720 paste in the API key that you copied
00:16:00.480 and then we add agent Ops as a
00:16:03.540 [Music]
00:16:04.800 dependency and run the PIP install
00:16:10.560 command and after the installation is
00:16:13.040 complete we can test out agent Ops on
00:16:15.680 our two example scripts first let's set
00:16:19.079 up monitoring on this simple inference
00:16:21.120 dopy file
00:16:24.680 so let's add these packages
00:16:30.040 the top of the
00:16:33.600 file and because we now need to
00:16:36.680 reference an environment variable you
00:16:39.519 have to add this command
00:16:41.360 in this is where I like to paste these
00:16:45.079 commands and then we
00:16:47.600 initialize AG
00:16:50.160 Ops when you set the auto start session
00:16:53.160 parameter to be false it gives you more
00:16:55.000 control of when you can track the calls
00:16:59.319 and notice how we're also going to add a
00:17:01.560 custom tag this will allow us to easily
00:17:04.799 filter in the Hops dashboard for the
00:17:09.039 calls that we're going to make with this
00:17:12.720 application so the final thing to do
00:17:16.679 is wrap the
00:17:19.199 code that we want to
00:17:21.650 [Music]
00:17:23.039 monitor like so
00:17:30.240 and let's give it a spin and see what
00:17:34.120 happens so I'm going to clear the
00:17:45.039 console notice how agent Ops is now
00:17:47.840 printing out this link that we can man
00:17:55.480 click and you can see that we now
00:17:59.679 now have an overview of the call along
00:18:04.080 with the specs of the environment was
00:18:06.799 ran in and Yep this looks good and now
00:18:11.000 let's show how to monitor the other
00:18:12.760 example the one that uses llama Stacks
00:18:15.159 agent
00:18:16.600 class as we've already done the agent
00:18:19.159 Ops and API key installation steps let's
00:18:21.000 go straight to the simple agent. py file
00:18:25.240 and add the following code
00:18:29.880 let's import agent
00:18:35.559 Ops and initialize agent Ops after our
00:18:39.440 environment variables have been loaded
00:18:44.000 in and the last thing we have to do is
00:18:48.400 wrap the code that we want to track do
00:18:52.039 that here
00:19:00.640 and let's clear the
00:19:03.360 console
00:19:06.039 and give this a
00:19:13.840 spin okay if we click the link that the
00:19:18.039 agent Ops
00:19:20.320 SDK presents to us we're taken to an
00:19:24.679 overview of this session that we had
00:19:26.520 with our simple tool use agent so yeah
00:19:31.000 hopefully that gives you a gist of how
00:19:32.360 to use agent Ops for monitoring llama
00:19:34.480 stack
00:19:35.520 applications okay so in this video we
00:19:37.799 learned about ol Lama llama stack as
00:19:40.240 well as how to monitor llama stack
00:19:41.559 applications using agent Ops in the link
00:19:43.720 section of this description you should
00:19:45.440 see links for AMA as well as llama stack
00:19:48.440 and you'll see the signup links for
00:19:50.000 agent Ops and the brave search API
00:19:51.840 console plus you'll see links for
00:19:53.440 purchasing me a virtual coffee as well
00:19:55.880 as buying a yoga ball via an Amazon
00:19:57.760 affiliate link make sure you leave a
00:19:59.520 like And subscribe and let me know in
00:20:01.720 the comments what you want to see next
00:20:02.760 from the channel and peace health and
00:20:06.360 blessings
