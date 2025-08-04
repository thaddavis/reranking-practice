---
video_title: "Code an OpenAI integration with Python and Flask"
video_url: "https://www.youtube.com/watch/Vo1_9-qVCM4"
---

00:00:00.120 in this video we will look at how to
00:00:02.700 interact with open AI models via a
00:00:05.040 python Library called Lang chain
00:00:08.220 Lang chain is a tool that makes
00:00:09.960 interacting with open AI models a bit
00:00:12.840 easier
00:00:14.099 here are some of the modules that Lang
00:00:16.619 chain provides
00:00:19.800 most relevant to us for the time being
00:00:21.840 is this prompt module
00:00:25.019 the code we will throw together
00:00:26.580 demonstrates a technique often referred
00:00:29.039 to as prompt engineering
00:00:32.220 which as you will see is not complicated
00:00:34.860 at all and is actually more of an Arts
00:00:38.340 the specific feature that the code we
00:00:40.860 will write will be related to is this
00:00:42.899 interactive world map that plots
00:00:44.340 information related to arbitrary queries
00:00:47.460 you can literally ask anything and the
00:00:49.800 model we will be using will do a darn
00:00:51.600 good job of plotting relevant locations
00:00:54.180 to your query on the map
00:00:56.219 for example
00:00:57.780 what are the hottest cities in Africa
00:01:06.439 or where is the best seafood in Brazil
00:01:14.780 Expedia and or Travelocity please
00:01:17.640 contact me if you want something like
00:01:19.200 this integrated into your applications
00:01:22.560 this video is important because it
00:01:24.540 demystifies a good portion of the AI
00:01:27.060 apps being released during this 2023
00:01:29.340 artificial intelligence craze we are in
00:01:31.320 the middle of as simple applications of
00:01:34.259 prompt engineering techniques
00:01:37.090 [Music]
00:01:38.400 first I should say you will need to
00:01:40.979 create an account with openai and get an
00:01:43.500 API key for authenticating your model
00:01:45.360 requests
00:01:46.920 the API key is how open AI tracks how
00:01:49.740 everyone is using their models and is
00:01:51.720 also what allows them to limit each
00:01:53.220 person's usage
00:01:54.479 there are ways of running models on your
00:01:56.520 own computers instead of paying a
00:01:58.140 monthly fee to access models over the
00:02:00.060 internet but we will leave that topic
00:02:02.040 for another video
00:02:03.600 so this will be our starting point you
00:02:06.299 can see this is a flask server with one
00:02:08.399 endpoint that's not doing much to begin
00:02:10.199 with
00:02:11.160 in the project folder not much to look
00:02:13.500 at but you can see that I'm using poetry
00:02:15.540 for doing the package management and
00:02:18.420 you can also see this dot EMV file this
00:02:20.700 is where I am storing the open AI API
00:02:23.700 key
00:02:25.140 the purpose of this video is just to
00:02:26.640 give you the broad Strokes of how this
00:02:27.959 goes and you can apply it to your own
00:02:30.120 application however you like
00:02:32.520 so in this terminal I will run the flask
00:02:36.959 server and in this terminal I will issue
00:02:40.580 curl request to the end point as we
00:02:44.160 develop it
00:02:45.180 right you can see as I send curl
00:02:47.700 requests you'll see the logs in the left
00:02:49.500 panel right
00:02:51.360 you can see we are importing some Lang
00:02:53.400 chain modules at the top now and in the
00:02:56.580 controller for our flask endpoint we are
00:02:59.180 instantiating an llm a large language
00:03:02.040 model
00:03:03.239 this object allows us to tweak or
00:03:06.540 configure the large language model for
00:03:08.459 example we can pass in a temperature
00:03:11.360 parameter that can be minimum zero
00:03:14.400 maximum one the closer to zero means the
00:03:17.459 less random the responses will be
00:03:18.959 meaning that if we send a request back
00:03:21.720 to back we should get the same exact
00:03:23.640 response if we have a temperature closer
00:03:26.099 towards one that means the responses
00:03:29.040 will be more random here is where we can
00:03:31.379 choose which model we want to use GPT
00:03:34.739 3.5 turbo that's the one everybody is
00:03:37.860 most familiar with and
00:03:40.140 this is how we send requests via code to
00:03:44.519 the model
00:03:45.840 so let's run the
00:03:48.360 flask server again and
00:03:51.000 we will
00:03:52.319 send a curl request and that should
00:03:54.599 trigger a request to the model
00:03:59.040 here is what the model responded with as
00:04:01.739 an AI language model I can tell you that
00:04:04.260 the answer is four the next update to
00:04:07.260 the code you can see we're doing some
00:04:08.940 validation on the input we're making
00:04:11.099 sure we receive an application Json
00:04:13.620 content type that has a key of prompt
00:04:17.940 with the prompt that the caller of this
00:04:21.540 endpoint wants to send to the llm
00:04:25.139 so let's test this out
00:04:30.660 and I have some example curl requests
00:04:33.720 over here so let's send the first one
00:04:36.139 the first one reads what is three plus
00:04:39.000 three so it should say something like
00:04:40.919 six right
00:04:43.139 and it does
00:04:45.600 let's send the second one
00:04:47.880 the second
00:04:49.259 curl example reads what is the color of
00:04:52.800 an orange
00:04:54.419 should say orange right
00:04:58.020 the color of an orange is orange perfect
00:05:01.440 okay for this next step we are getting
00:05:04.020 into some prompt engineering techniques
00:05:06.780 you can see that when you break it down
00:05:08.699 prompt engineering is really just string
00:05:12.419 templating you can see that we're now
00:05:14.460 pre-pending the prompt with this text
00:05:19.500 that reads please respond as Donald
00:05:22.500 Trump would to the following query
00:05:26.460 that's really all there is to it is
00:05:28.020 being creative with your string
00:05:29.580 templates that is prompt engineering
00:05:33.300 so let's test this out
00:05:38.460 and
00:05:41.940 now
00:05:43.740 The Prompt reads what is the color of an
00:05:47.460 orange just like before remember it said
00:05:51.000 the color of an orange is orange that
00:05:52.860 was the previous response but now that
00:05:54.720 we've changed the template it reads look
00:05:58.020 nobody knows orange is better than me
00:05:59.880 believe me I know oranges
00:06:01.919 and let me tell you the color of an
00:06:03.539 orange is orange okay for this one we
00:06:06.060 really haven't done much all that we've
00:06:07.500 done is add an additional class called
00:06:09.180 The Prompt template class this is
00:06:11.039 utility for being able to do string
00:06:13.800 templating all prompt engineering boils
00:06:16.380 down to at the end of the day is string
00:06:18.300 templating so this class allows us to
00:06:20.400 reuse a prompt over and over again
00:06:22.020 reason why we want to do this is so that
00:06:23.940 we can send more examples to the model
00:06:26.699 we're using
00:06:27.960 so that it has more context of how it
00:06:30.060 should respond to Future requests so
00:06:32.759 when you send or craft a prompt and also
00:06:36.000 include some examples of how it should
00:06:39.000 respond to some questions they call that
00:06:41.699 few shot prompt templating right all of
00:06:44.699 this stuff is very simple right so it's
00:06:46.740 a bunch of lingo Let's test this out
00:06:49.020 we'll run the flask server and
00:06:51.780 let's send
00:06:53.720 this prompt an empty prompt it doesn't
00:06:56.819 matter all that we're doing when we test
00:06:59.580 this step is checking out what the
00:07:03.240 prompt template class does for us right
00:07:04.919 so you can see that it's gonna
00:07:07.620 format this prompt twice with two
00:07:12.180 example queries along with their
00:07:14.160 corresponding responses right you can
00:07:16.139 see
00:07:17.520 this class is just spitting out strings
00:07:20.639 okay I minimize the text a little bit to
00:07:22.860 fit all of the code in
00:07:24.599 but in this step we really haven't done
00:07:26.699 much
00:07:27.599 we added an additional helper class this
00:07:31.500 one is called length based example
00:07:34.020 selector so what this will do is
00:07:38.940 limit the amount of examples we're
00:07:41.880 giving to our prompt so that we can
00:07:46.580 not cross any thresholds that are
00:07:50.160 imposed Upon Us by the endpoints open AI
00:07:53.520 provides
00:07:54.720 so on the docs you'll see that openai
00:07:58.500 has a limit on how many requests you can
00:08:01.319 send per minute and how many tokens you
00:08:03.900 can send per minute
00:08:05.039 so tokens
00:08:06.960 according to my understanding is similar
00:08:09.900 to words right so token count would be
00:08:12.060 word count long story short is the
00:08:15.000 length based example selector allows you
00:08:17.400 to limit
00:08:18.599 how many tokens or words you're going to
00:08:21.840 be including in your final prompt okay
00:08:25.620 now things are coming together you can
00:08:27.180 see that we've now included another
00:08:28.680 class called few shot prompt template
00:08:31.319 class right so this is what ties
00:08:33.839 everything together
00:08:35.958 and builds our final prompt that we will
00:08:39.719 send off to the model we're using
00:08:42.240 so if we test this out
00:08:44.459 you'll see what I mean
00:08:47.459 let's use this
00:08:50.339 example curl
00:08:52.560 and you can see this is the final prompt
00:08:57.360 answer each query please respond as
00:08:59.820 Donald Trump would what is the greatest
00:09:01.800 country in the world well America of
00:09:03.779 course
00:09:04.560 please respond as Donald Trump would
00:09:07.019 what is the greatest country in the
00:09:08.580 history of mankind
00:09:10.980 and that is the total prompt to which
00:09:14.700 the llm we're using or the model we're
00:09:17.220 using will respond to
00:09:19.320 nice so all we're going to do for this
00:09:21.360 next step is tie in this code with the
00:09:24.120 flask endpoints that we can receive the
00:09:26.100 response to our request from wherever we
00:09:28.860 issue our request
00:09:31.200 so let's start the flask
00:09:35.160 server and test this out
00:09:38.519 here is the
00:09:40.620 curl and we should receive a response to
00:09:43.500 our request
00:09:44.640 in the same terminal where we issued the
00:09:47.339 request
00:09:48.360 right so here we have it there's no
00:09:51.360 question about it folks the greatest
00:09:52.620 country in the history of mankind is the
00:09:55.620 United States of America we've got the
00:09:57.060 best people the best economy the best
00:09:59.220 military nobody can compete with us okay
00:10:01.800 that pretty much does it so now I will
00:10:04.620 tweak the prompt from being this
00:10:07.740 Donald Trump AI app to being the prompt
00:10:11.339 needed for the interactive world map app
00:10:14.700 here is the prompt that I have crafted
00:10:17.940 can you return an array of objects as a
00:10:20.160 Json formatted string that are
00:10:21.540 geographically relevant to an arbitrary
00:10:23.100 query
00:10:24.000 here are the requirements each object in
00:10:26.339 the array should contain three keys law
00:10:28.440 and lat and blurb Lon is the longitude
00:10:31.440 lat is the latitude blurb is the one to
00:10:35.459 three sentence answer to the query along
00:10:38.100 with information about the environmental
00:10:40.019 concerns of the city or region in which
00:10:42.060 the coordinates exist
00:10:44.579 the array should be max length three
00:10:46.980 items the overall length of the answer
00:10:49.620 should be maximum 500 characters
00:10:53.820 blah blah
00:10:55.560 let's run the flask server and test this
00:10:58.500 out here we are running the server here
00:11:01.079 is the first query
00:11:03.779 what is the greatest country in the
00:11:06.300 history of mankind
00:11:08.279 let's wait for the
00:11:10.680 llm or model to respond
00:11:19.500 okay so it responded appropriately
00:11:22.560 fantastic
00:11:25.920 I should say that
00:11:28.440 I moved the examples
00:11:31.320 over to a separate file
00:11:34.680 all right so I'm still using the few
00:11:36.899 shot prompt template technique but maybe
00:11:39.540 you already knew that
00:11:40.980 okay so that's the first request and it
00:11:44.279 looks good
00:11:45.600 and the second request
00:11:51.300 what are the hottest cities in America
00:11:54.060 so let's see what it says
00:12:00.600 okay that looks good as well it says Las
00:12:03.660 Vegas
00:12:05.880 Phoenix Arizona
00:12:07.090 [Music]
00:12:09.000 and
00:12:10.320 San Diego looks great I should say that
00:12:14.760 the
00:12:16.200 llm
00:12:18.060 is not
00:12:19.860 necessarily a source of Truth
00:12:23.100 it has been trained to spit out things
00:12:26.120 and if it was trained on
00:12:30.360 inaccurate or untruthful data it will
00:12:32.820 spit out inaccurate or untruthful
00:12:35.339 results That's all folks
