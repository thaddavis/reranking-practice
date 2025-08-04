---
video_title: "What is Ollama?"
video_url: "https://www.youtube.com/watch/glkQIUTCAK4"
---

00:00:01.920 olama is a tool that allows you to run
00:00:03.760 llms locally on your own machine AKA
00:00:06.319 your laptop or desktop whatever
00:00:08.240 homebuilt device you want to run these
00:00:09.400 models on yes while llama ecosystem
00:00:12.040 models tend not to be as large as say
00:00:14.360 Frontier models like GPT 40 or Cloud 3.5
00:00:16.880 Sonet you'll be surprised to hear that
00:00:18.560 for many use cases they are actually on
00:00:20.880 par due to how much data these llama
00:00:22.439 models have been trained on the real
00:00:24.800 benefit of using these llama models
00:00:26.160 however has nothing to do with
00:00:27.160 benchmarks but has more to do with the
00:00:28.480 fact that you can audit with 100%
00:00:30.000 certainty that the model weights are not
00:00:31.519 changing and that your interactions with
00:00:33.120 them are kept completely private to
00:00:35.520 download and install olama come over to
00:00:37.800 ama.com click the download button and
00:00:42.200 download the appropriate version for
00:00:43.719 your OS for me this is Mac OS from this
00:00:47.440 point forward I'm just going to show you
00:00:48.640 how I did this on my Mac so I clicked
00:00:51.440 the download for Mac OS
00:00:53.160 button and it downloaded this ZIP
00:00:56.840 file so after you have that downloaded
00:00:59.280 you unzip the zip file and drag the
00:01:02.160 resulting application into your
00:01:04.559 applications
00:01:05.680 folder then you launch the olama
00:01:10.960 application accept all of the permission
00:01:14.000 dialogues and then you'll be presented
00:01:16.119 with this little wizard click next click
00:01:20.280 install I have to put in my account
00:01:24.000 password and click finish and that's
00:01:27.680 it then should be able to
00:01:31.600 type-b on the command line and see the
00:01:35.200 AMA client version printed out also note
00:01:38.200 how we can start and stop AMA via this
00:01:40.720 llama icon in the menu bar to start AMA
00:01:44.560 you launch it just like you would launch
00:01:46.360 any other
00:01:47.360 application when AMA is running you
00:01:49.759 should see this little llama icon in
00:01:51.560 your menu bar as olama is a command line
00:01:55.079 tool you'll need to pop open a shell to
00:01:57.240 use it here's an overview of some of
00:02:00.159 ama's commands I hope you find these
00:02:03.640 intuitive in regards to the model IDs I
00:02:06.560 personally love this table on the olama
00:02:08.878 GitHub repo that shows some of the more
00:02:10.758 used models that people like to run
00:02:12.800 along with their
00:02:14.040 IDs it's not a particular relevance to
00:02:16.760 this video but just know that the full
00:02:18.440 list of models that ama supports
00:02:20.720 stretches well into the hundreds and
00:02:23.040 even includes models from outside of
00:02:25.200 llama's ecosystem but anyways Focus to
00:02:29.519 keep things light we will run one of the
00:02:31.160 smallest models that ama offers that
00:02:33.599 being llama 3.2 1B instruct
00:02:37.239 fp16 the 3.2 tells us the family of
00:02:40.040 models it was released with the 1B tells
00:02:42.720 us the amount of parameters that the
00:02:44.080 model has the instruct tells us that the
00:02:46.319 model was fine-tuned for performing
00:02:47.959 instructions and the fp16 does get a bit
00:02:50.480 technical but tells us that when the
00:02:51.720 model generates text the internal
00:02:53.760 calculations are performed using numbers
00:02:55.159 with up to four decimal places if I'm
00:02:57.280 wrong about this fp16 detail please
00:02:59.159 leave a comment
00:03:00.480 you can think of the number of
00:03:01.519 parameters as a rough indication of how
00:03:03.159 many simulated brain cells a model has
00:03:05.959 the more parameters or brain cells and
00:03:08.640 the smarter the model will be assuming
00:03:11.040 it's been trained on a sufficient amount
00:03:12.280 of data that is I don't want to get
00:03:14.200 bogged down in excessive detail but what
00:03:15.680 I'm trying to highlight here is that
00:03:17.000 depending on training details a smaller
00:03:19.159 model can outperform a larger one in
00:03:21.159 certain cases if you're interested in
00:03:23.120 learning more about how AI training
00:03:24.560 works I suggest watching this video
00:03:26.519 entitled what is pi torch The Unofficial
00:03:28.680 movie or researching topics like neural
00:03:30.840 networks and back propagation as a
00:03:32.159 starting point to use a particular model
00:03:34.640 with olama enter the olama Run command
00:03:38.360 followed by the models
00:03:41.159 ID as a rough guideline you'll need
00:03:43.480 about 8 gigs of RAM for running models
00:03:45.239 with about 7 billion parameters about 16
00:03:48.080 gigs of RAM for running models with
00:03:49.439 about 13 billion parameters and about 32
00:03:52.280 gigs of RAM for running models with
00:03:53.480 about 33 billion parameters the model
00:03:56.120 we're using in this video only has 1
00:03:57.640 billion parameters so it should work on
00:03:59.959 just about any
00:04:03.360 computer AMA supports interactive
00:04:06.200 sessions with the models you
00:04:09.200 run and also in the background serves an
00:04:13.439 API to see the logs of the olama API
00:04:17.238 open up a new
00:04:19.279 terminal and type this command tail-f
00:04:24.160 followed by the path to the olama server
00:04:28.000 logs and
00:04:30.320 move this over here like
00:04:33.360 this and back in the original
00:04:37.039 terminal we can curl the AMA
00:04:41.320 API by closing this interactive
00:04:45.400 session
00:04:47.400 and sending curl statements like
00:04:54.080 so there are other ways to use AMA so
00:04:57.199 feel free to experiment but hopefully
00:04:58.960 this gives you a great gist of how it
00:05:01.000 works
