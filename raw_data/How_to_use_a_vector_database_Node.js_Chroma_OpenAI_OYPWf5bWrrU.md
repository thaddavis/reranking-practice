---
video_title: "How to use a vector database [Node.js + Chroma + OpenAI]"
video_url: "https://www.youtube.com/watch/OYPWf5bWrrU"
---

00:00:02.670 [Music]
00:00:04.240 for this demo we'll take a look at the
00:00:06.279 vector database side of things just like
00:00:09.639 SQL tables or SQL databases store
00:00:12.480 uniformly labeled data and nosql
00:00:15.639 databases or collections store objects
00:00:18.320 or dictionaries Vector databases store
00:00:22.160 vectors at the time of recording in 2023
00:00:25.640 there are many Vector databases
00:00:27.279 available on the market for example pine
00:00:29.560 cone or chroma or milis and all of them
00:00:32.800 are valid but in this demo we'll use
00:00:36.079 chroma simply because it is free the
00:00:39.239 steps for installing chroma DB are one
00:00:42.800 clone the git
00:00:45.039 repository two build the image in the
00:00:47.879 Clone
00:00:50.600 project if everything works you should
00:00:52.719 see a chroma DB server running in your
00:00:55.559 console two common use cases for Vector
00:00:58.840 databases or Vector stores would be
00:01:01.920 similarity search and anomaly
00:01:05.360 detection from this list of common
00:01:07.600 consumer facing applications of vector
00:01:09.360 stores content moderation on social
00:01:11.759 media would be an example of similarity
00:01:14.240 search with similarity search you are
00:01:16.960 comparing vectors that represent user
00:01:18.680 data against vectors that represent
00:01:20.640 Concepts defined as unacceptable by a
00:01:22.759 given platform and when you find the
00:01:25.200 similarity to cross a certain threshold
00:01:27.560 you will Mark the relevant user data for
00:01:29.600 hiding or
00:01:30.840 deletion unusual activity associated
00:01:33.159 with your bank account on the other hand
00:01:34.600 is an example of anomaly detection and
00:01:37.079 involves generating vectors for all the
00:01:38.880 actions you perform against your bank
00:01:40.240 account and raising a flag whenever a
00:01:42.680 particular Vector crosses a certain
00:01:44.159 threshold of dis similarity the general
00:01:47.119 technique for how to do similarity
00:01:48.399 search or anomaly detection yourself is
00:01:50.320 outlined here one break up your data
00:01:53.000 into chunks the chunks if your data is
00:01:55.799 text would commonly be broken up by
00:01:58.039 paragraph sentence or word for example
00:02:00.759 you'll need to tune the size of the
00:02:02.119 chunks to your use case two generate an
00:02:05.200 embedding Vector for each Chunk in your
00:02:07.039 data set using an embedding model like
00:02:09.318 text embedding Ada
00:02:11.959 002 three convert your query to a vector
00:02:15.319 using the same embedding model used in
00:02:17.000 step two and if you're performing
00:02:19.879 similarity search you return the chunks
00:02:21.920 associated with the vectors that score
00:02:23.480 the highest in similarity to the query
00:02:26.080 chunk if you're performing anomaly
00:02:28.560 detection you compare your query against
00:02:31.000 the vectors for each chunk and raise a
00:02:32.760 flag if the query Vector scores below a
00:02:35.400 certain
00:02:36.680 threshold let's take a look at this
00:02:38.560 skills
00:02:40.360 Matrix if we search for mobile
00:02:42.319 development let's see what gets
00:02:48.720 returned we can see we get matches even
00:02:51.200 though the text mobile development is
00:02:53.080 nowhere to be found on this
00:02:55.760 document now let's search for AWS
00:03:02.400 we can see we get matches of various AWS
00:03:04.519 Services even though they're not exactly
00:03:06.519 matching the string we're looking
00:03:08.080 for if you look closely you see the top
00:03:11.000 results score lower and this is
00:03:13.159 inconsistent with what we were seeing
00:03:14.720 before with the dot
00:03:16.360 product this is because the dot product
00:03:18.760 is one of several formulas for measuring
00:03:21.280 the similarity of two
00:03:22.799 vectors chroma DB uses a distance
00:03:25.519 formula instead of the dot product which
00:03:27.159 is why the higher results are showing
00:03:29.120 with a lower number number the exact
00:03:31.480 matches are showing as zero a lower
00:03:34.840 score means closer in distance I.E
00:03:37.040 higher in similarity and a score of zero
00:03:39.680 means your query is identical to the
00:03:41.680 match chunk here's a quick overview of
00:03:44.439 the code behind what we're seeing on
00:03:47.439 line 56 you see we're breaking things up
00:03:50.200 I.E our text by either spaces or
00:03:55.000 commas lines 85 to 88 show us generating
00:03:59.280 the embedded vectors for each
00:04:03.439 chunk and on lines 96 to 99 we are
00:04:07.040 searching for the top 10 results that
00:04:09.159 match our query
