---
video_title: "How to set up Llama Stack in 14 minutes"
video_url: "https://www.youtube.com/watch/KCZSQIX5ET8"
---

00:00:00.000 No text
00:00:02.120 here is a diagram of what we are going
00:00:03.879 to set up in this video and let's start
00:00:06.839 by setting up the olama server to
00:00:09.760 download and install olama come over to
00:00:12.080 ama.com click the download button and
00:00:16.440 download the appropriate version for
00:00:17.960 your OS for me this is Mac OS from this
00:00:21.680 point forward I'm just going to show you
00:00:22.880 how I did this on my Mac so I click the
00:00:25.800 download for Mac OS
00:00:27.400 button and it downloaded this Z zip
00:00:31.040 file so after you have that downloaded
00:00:33.520 you unzip the zip file and drag the
00:00:36.320 resulting application into your
00:00:38.760 applications
00:00:39.879 folder then you launch the olama
00:00:45.160 application accept all of the permission
00:00:48.199 dialogues and then you'll be presented
00:00:50.280 with this little wizard click next click
00:00:54.480 install I to put in my account password
00:01:00.239 and click finish and that's
00:01:02.920 it then should be able to type ol- Fe on
00:01:08.000 the command line also note how we can
00:01:10.640 start and stop AMA via this llama icon
00:01:13.520 in the menu bar to start olama you
00:01:16.799 launch it just like you would launch any
00:01:18.560 other
00:01:19.360 application when AMA is running you
00:01:21.759 should see this little llama icon in
00:01:23.560 your menu bar as olama is a command line
00:01:27.079 tool you'll need to pop open a shell to
00:01:29.200 use it here's an overview of some of
00:01:32.079 ama's commands I hope you find these
00:01:35.640 intuitive in regards to the model IDs I
00:01:38.560 personally love this table on the olama
00:01:40.880 GitHub repo that shows some of the more
00:01:42.759 used models that people like to run
00:01:44.799 along with their
00:01:46.040 IDs it's not of particular relevance to
00:01:48.759 this video but just know that the full
00:01:50.439 list of models that olama supports
00:01:52.680 stretches well into the hundreds and
00:01:55.000 even includes models from outside of
00:01:57.200 llama's ecosystem but anyways
00:02:00.360 Focus to keep things light we will run
00:02:02.759 one of the smallest models that ama
00:02:04.640 offers that being llama 3.2 1B instruct
00:02:09.199 fp16 the 3.2 tells us the family of
00:02:12.000 models it was released with the 1B tells
00:02:14.720 us the amount of parameters that the
00:02:16.080 model has the instruct tells us that the
00:02:18.280 model was fine- tuned for performing
00:02:19.959 instructions and the fp16 does get a bit
00:02:22.480 technical but tells us that when the
00:02:23.680 model generates text the internal
00:02:25.760 calculations are performed using numbers
00:02:27.160 with up to four decimal places if I'm
00:02:29.280 wrong about this fp16 detail please
00:02:31.160 leave a comment you can think of the
00:02:33.160 number of parameters as a rough
00:02:34.560 indication of how many simulated brain
00:02:36.200 cells a model has the more parameters or
00:02:39.440 brain cells and the smarter the model
00:02:41.720 will be assuming it's been trained on a
00:02:43.760 sufficient amount of data that is I
00:02:45.760 don't want to get bogged down in
00:02:46.760 excessive detail but what I'm trying to
00:02:48.159 highlight here is that depending on
00:02:49.440 training details a smaller model can
00:02:51.840 outperform a larger one in certain cases
00:02:54.480 if you're interested in learning more
00:02:55.560 about how AI training works I suggest
00:02:57.319 watching this video entitled what is
00:02:59.400 piie toward The Unofficial movie or
00:03:01.640 researching topics like neural networks
00:03:03.200 and back propagation as a starting point
00:03:05.280 to use a particular model with olama
00:03:08.239 enter the olama Run command followed by
00:03:10.879 the model's
00:03:13.200 ID as a rough guideline you'll need
00:03:15.480 about 8 gigs of RAM for running models
00:03:17.280 with about 7 billion parameters about 16
00:03:20.120 gigs of RAM for running models with
00:03:21.480 about 13 billion parameters and about 32
00:03:24.280 gigs of RAM for running models with
00:03:25.519 about 33 billion parameters the model
00:03:28.159 we're using in this video only has 1 B
00:03:30.000 parameters so it should work on just
00:03:32.080 about any
00:03:35.360 computer AMA supports interactive
00:03:38.200 sessions with the models you
00:03:41.200 run and also in the background serves an
00:03:45.439 API to see the logs of the olama API
00:03:49.239 open up a new
00:03:51.280 terminal and type this command tail-f
00:03:56.159 followed by the path to the olama server
00:03:58.400 logs
00:04:01.319 and move this over here like
00:04:05.360 this and back in the original
00:04:09.040 terminal we can curl the AMA
00:04:13.319 API by closing this interactive
00:04:17.399 session
00:04:19.399 and sending curl
00:04:22.000 statements like
00:04:26.080 so there are other ways to use AMA so
00:04:29.199 feel free to to experiment but hopefully
00:04:30.960 this gives you a great gist of how it
00:04:33.000 No text
00:04:33.320 works now that we have Ama running let's
00:04:36.000 run a llama stack server we're going to
00:04:38.080 run llama stack using Docker which is a
00:04:40.080 tool that makes running all sorts of
00:04:41.440 different types of software super easy
00:04:44.199 fun fact it appears that the CEO of
00:04:46.720 olama Jeffrey Morgan worked as a product
00:04:49.320 manager at Docker for almost 5 years if
00:04:52.560 you don't have Docker installed come
00:04:54.440 over to
00:04:55.440 doer. and download the appropriate
00:04:57.720 version for your machine me this is
00:05:00.160 Apple
00:05:02.000 silicone and after the download
00:05:04.360 completes open it and drag the docker
00:05:08.600 doapp icon into your applications folder
00:05:12.800 I've already done this so I'll click
00:05:14.680 stop but that's it it's that easy in
00:05:18.440 order to launch
00:05:20.039 Docker you
00:05:21.880 simply open the docker application just
00:05:24.720 like you would open any other
00:05:26.360 application when Docker is running you
00:05:29.400 should see this whale icon in your top
00:05:32.280 menu bar after Docker is set up here are
00:05:35.880 the steps for how to run a llama stack
00:05:38.039 server first let's create an empty
00:05:40.400 folder somewhere on our computer I'm
00:05:43.080 calling mine llama stack agent Ops and
00:05:46.479 let's enter this folder we just created
00:05:48.880 and open it with our code
00:05:51.680 editor next let's add a yamamo file that
00:05:55.880 will allow us to configure how llama
00:05:58.720 stack works
00:06:00.960 so I'm going to create a file called
00:06:03.120 run.
00:06:04.100 [Music]
00:06:05.400 yo and let's populate this run. yo
00:06:10.000 file with the following content that I
00:06:13.400 adapted from the olama example found in
00:06:16.800 llam Stacks GitHub repo here is the
00:06:20.120 content that we will paste into this
00:06:24.240 run. and just so you can see what it
00:06:26.479 looks like here we are llam stack is an
00:06:29.759 SDK that provides common functionality
00:06:31.599 for building agentic applications like
00:06:33.919 tool calling and memory modules for
00:06:35.960 example llam stack relies on a separate
00:06:38.400 service for powering the llm inside of
00:06:41.319 llast Stack's GitHub repo you'll see
00:06:43.440 examples for how to plug llast stack
00:06:45.280 into llmm points powered by AWS Bedrock
00:06:49.520 hugging face as well as
00:06:53.240 fireworks but in the name of Freedom
00:06:56.160 Liberty and everything America stands
00:06:57.800 for we are going to be using all Lama
00:06:59.840 for powering our llm okay so here's how
00:07:02.520 we do this first we have to make sure
00:07:06.039 oama is
00:07:07.599 running then we can pop open in the
00:07:09.680 terminal and type the O Lama PS command
00:07:15.039 to see what models are being served and
00:07:18.160 we can see that no models are currently
00:07:20.479 being
00:07:22.400 served and if we
00:07:24.960 type this AMA command AMA run followed
00:07:29.759 by the model ID we're also going to
00:07:32.120 include a flag that says keep alive 60
00:07:36.160 Minutes that will keep the model running
00:07:39.879 for an hour after we close the
00:07:42.440 interactive session that by default AMA
00:07:46.319 presents to us when we run a model so
00:07:48.960 I'm running this command here we see the
00:07:50.960 interactive
00:07:51.990 [Music]
00:07:53.440 session model's running and if we close
00:07:56.919 the interactive session by typing contrl
00:08:01.319 D and type the oama PS command again we
00:08:06.879 can see that the model will be served
00:08:10.919 for another hour now we can run this
00:08:14.599 Docker command to run a llama stack
00:08:18.039 server powered by this olama
00:08:21.479 model if you look closely at this Docker
00:08:24.560 command you'll see we're including two
00:08:26.400 environment variables and these are the
00:08:28.440 environment variables that plug llama
00:08:30.720 stack into oama here you can see we're
00:08:33.958 telling llama stack to find oama at this
00:08:38.799 URL and this is a little confusing but
00:08:42.640 this is how it works the model ID that
00:08:46.320 you want to
00:08:49.279 use is different in llama stack compared
00:08:52.680 to the same model's ID in
00:08:55.240 olama so this model llama 3.21 B
00:08:59.640 instruct
00:09:00.680 fp16 has this model ID in llama
00:09:05.839 stack so after you run this Docker
00:09:09.600 command we should have a running llama
00:09:24.560 stack okay that looks good and we can
00:09:27.560 smoke test this by popping open
00:09:30.440 a second terminal and hitting the Llama
00:09:34.320 stack api's health check
00:09:36.240 endpoint and we see the status is okay
00:09:39.000 No text
00:09:39.760 let's now run two more quick tests so
00:09:42.200 you get a feel for what using llama
00:09:43.880 stack is like if you've done any AI
00:09:46.680 agent development at all you should find
00:09:48.320 this very familiar so
00:09:52.000 first you'll need python installed I'm
00:09:56.640 using python 3.13
00:10:00.640 and next up let's create a virtual
00:10:03.279 environment so that we can install
00:10:05.040 packages into our project without
00:10:07.160 affecting any other python projects on
00:10:09.920 our
00:10:11.959 system and if that command works you
00:10:15.079 should see a VM folder at the root of
00:10:17.880 the
00:10:19.320 project let's activate our virtual
00:10:22.240 environment like
00:10:23.510 [Music]
00:10:26.200 so and create a requirement .txt
00:10:30.960 [Music]
00:10:33.440 file and
00:10:35.880 add these packages and package versions
00:10:39.839 into the requirements.txt
00:10:44.000 and then we can install these packages
00:10:47.720 with the PIP install
00:10:53.079 command and when the installation
00:10:56.440 process has finished
00:10:59.360 let's add a
00:11:01.200 file called Simple inference
00:11:06.079 dopy
00:11:08.560 and here is the code we'll put in this
00:11:12.800 simple inference dopy file hopefully
00:11:15.519 this should look very familiar you can
00:11:17.279 see all we're doing here is pointing
00:11:20.279 this code to the llam stack API running
00:11:23.000 on Port
00:11:24.959 50001 this is the model ID we'd like to
00:11:28.800 use
00:11:30.320 and this is the prompt that we're going
00:11:32.240 to send via code right a three-word poem
00:11:35.000 about the moon so let's run this script
00:11:37.839 and see what
00:11:43.240 happens silent lunar
00:11:46.000 No text
00:11:46.000 glow and for this second quick example
00:11:49.040 let's show how to use llama Stack's
00:11:51.040 agent class we're going to build an
00:11:55.160 agent that has one
00:11:58.040 tool and and that one tool will be the
00:12:01.040 ability to use the brave browser API so
00:12:06.440 we'll need to add aemv file to our
00:12:11.519 project that will include an
00:12:14.279 entry for holding our brave browser API
00:12:19.560 key you can provision an API key on the
00:12:23.320 brave search API
00:12:25.920 console you can sign up for here
00:12:29.720 once you have that API key provision
00:12:31.720 copy it into your
00:12:35.959 project and in order to make
00:12:39.160 these API Keys available to our code
00:12:42.360 we're going to need to
00:12:43.920 install python.
00:12:48.959 M and after the installation
00:12:51.959 completes let's create a file called
00:12:55.279 Simple
00:12:57.000 agent and populate this simp simple
00:12:59.480 agent. py bio with the following
00:13:05.120 code here you can see we're plugging
00:13:07.279 into the Llama stack API on Port 50001
00:13:10.360 here's the model ID we're going to
00:13:12.399 use here's where we configure the
00:13:16.519 agent and this is the prompt that we're
00:13:19.079 going to send to our agent who won the
00:13:21.320 NBA championship in 2020 please use
00:13:24.320 tools so let's run this and see what
00:13:34.760 happens and that is the right answer it
00:13:37.240 was the
00:13:39.079 Lakers so hopefully you have a great
00:13:41.720 idea or a great gist at least of what
00:13:45.160 llama stack is all about
