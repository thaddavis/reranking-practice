---
video_title: "Understanding RAG Agents with Pinecone and LangChain"
video_url: "https://www.youtube.com/watch/bsVrSenBmn0"
---

00:00:00.000 No text
00:00:02.290 [Music]
00:00:08.000 No text
00:00:12.400 here we have an agent powered by Claude
00:00:14.240 and Lang chain we can chat with it just
00:00:16.320 like we would with Chad
00:00:20.600 gbt this agent even has memory you can
00:00:23.560 see it remembers my
00:00:25.039 name okay let's now ask this llm agent
00:00:28.199 something very specific and see how it
00:00:29.800 does
00:00:30.640 I'm going to ask about a weekly Meetup
00:00:32.159 in Miami called GP Tuesday that I've
00:00:33.800 been attending over the past year to
00:00:35.120 help me learn more about AI I'll say I
00:00:38.480 missed the last GP Tuesday Meetup I'd
00:00:40.559 like a recap of what was
00:00:47.360 discussed the outputs of llms like
00:00:49.800 Claude are only based on the data they
00:00:51.360 were trained on and we can see that the
00:00:53.000 version of Claude we're using hasn't
00:00:54.399 been updated since June 2024 I'm
00:00:56.960 recording this 2 months after June 2024
00:00:59.239 in August so there's no chance Claude
00:01:01.239 would know the specifics of last week's
00:01:02.680 GP Tuesday Meetup in the next demo we're
00:01:05.239 going to combine this llm agent with the
00:01:07.600 use of
00:01:08.000 No text
00:01:09.070 [Music]
00:01:11.600 vectors here we have an llm agent that
00:01:14.080 I've called the GP Tuesday agent unlike
00:01:16.720 the previous agent this one uses rag rag
00:01:20.079 or retrieval augmented generation is a
00:01:22.240 technique that combines the use of an
00:01:23.799 llm with the use of a vector
00:01:27.079 database here's how it works the only
00:01:29.920 only prerequisite for using rag is
00:01:31.640 collecting some accurate data regarding
00:01:33.280 the domain that we want the llm agent to
00:01:35.119 focus on for our use case I've generated
00:01:37.560 40 q&as related to the GP Tuesday Meetup
00:01:40.360 that we will convert into vectors and
00:01:41.799 then upload to Pine Cone I'm storing
00:01:43.880 these q&as in a text file with one Q&A
00:01:46.240 on each line we could just as easily
00:01:48.360 have recorded these q&as in a Google
00:01:50.079 spreadsheet but I prefer text files
00:01:52.880 anyways here is a snippet of code that
00:01:55.000 will a read the q&as one by one B
00:01:58.119 convert each Q&A into a vector using a
00:02:00.280 free embedding model provided by hugging
00:02:02.119 face called all mini LM L6 V2 I have
00:02:05.520 this embedding model running in my
00:02:06.680 Google Cloud account and C upload the
00:02:09.520 resulting vectors to pine cone with
00:02:11.038 metadata that includes the original
00:02:12.480 question and answer each Vector
00:02:13.920 represents after we run this script and
00:02:15.920 see our vectors in Pine Cone we can
00:02:17.959 start doing rag before we run this
00:02:20.000 script though we have to create the
00:02:21.560 database and database index that will
00:02:23.680 hold our vectors to create a pine cone
00:02:26.160 database all we have to do is sign up on
00:02:28.319 Pine cone.
00:02:30.280 and create a project I will call the
00:02:32.640 project we will use full stack vectors
00:02:36.080 after creating the project we then have
00:02:38.000 to create what is called an index a pine
00:02:40.200 cone index is where we can store vectors
00:02:42.280 or records for our index we'll use the
00:02:44.519 default cosine similarity algorithm and
00:02:47.040 specify that our vectors will have 384
00:02:49.640 Dimensions as our embedding model all
00:02:52.200 mini LM L6 V2 generates vectors with 384
00:02:56.319 Dimensions different embedding models
00:02:58.440 which are just types of neural network
00:03:00.239 will generate different size vectors for
00:03:02.000 representing the data being passed
00:03:03.360 through them you can call your indexes
00:03:05.120 whatever you like but I like to call my
00:03:07.000 indexes after the embedding models being
00:03:08.680 used to generate the vectors they will
00:03:11.599 hold now that we have our Vector
00:03:13.640 database and index set up let's run the
00:03:16.200 script to ingest our
00:03:19.210 [Music]
00:03:24.360 data notice that we now have 80 vectors
00:03:27.159 in our index which is double the amount
00:03:28.799 of q&as we had in our our file this is
00:03:30.760 expected as we are generating a vector
00:03:32.680 for each question and each answer so
00:03:36.040 that we can match against either half of
00:03:38.040 a Q&A now we can try retrieval augmented
00:03:41.000 generation let's send this message to
00:03:43.599 the GP Tuesday agent I missed the last
00:03:46.040 GP Tuesday Meetup I'd like a recap of
00:03:47.959 what was
00:03:49.920 discussed now we're getting responses
00:03:52.000 that are more catered to our
00:03:54.599 domain here is a diagram walking us
00:03:56.879 through what just happened one we sent
00:03:59.040 some prompt to our agent two our prompt
00:04:01.640 got converted into a vector three we
00:04:03.720 searched our pine cone knowledge base
00:04:05.640 for the vectors that are most similar to
00:04:07.799 the vector representing our prompt and
00:04:09.680 pine cone returned to us the original
00:04:11.640 data represented by the highest matching
00:04:13.360 vectors four we combined the most
00:04:16.199 relevant data to our prompt with the
00:04:17.880 original prompt and sent that to our llm
00:04:20.079 and five we returned our final output
00:04:22.880 two business use cases I can think of
00:04:24.560 for rag agents would be one generating
00:04:26.800 social media content AKA create vectors
00:04:29.080 representing your highest performing
00:04:30.440 posts and work with a rag agent to
00:04:31.840 generate new material in your style and
00:04:33.720 two drafting emails text messages or any
00:04:36.479 other forms of Correspondence AKA create
00:04:38.560 vectors representing your communication
00:04:40.039 history and have a rag agent
00:04:41.440 automatically draft responses to save
00:04:43.000 No text
00:04:43.280 you
00:04:43.840 [Music]
00:04:46.360 time we will now show how you can use a
00:04:48.800 reason and act or react agent for
00:04:51.120 accessing multiple knowledge bases using
00:04:52.919 pine cone the first knowledge base we
00:04:54.919 will use will hold vectors representing
00:04:56.560 q&as related to the famed Miami based
00:04:58.560 weekly AI Meetup GP Tuesday and the
00:05:01.120 second knowledge base we will use will
00:05:02.360 hold vectors representing Q&A related to
00:05:04.199 me yours truly let's ingest our
00:05:06.759 knowledge here is a script that will a
00:05:09.560 read in a batch of q&as B convert each
00:05:12.199 Q&A into a vector using a free embedding
00:05:14.280 model provided by hugging face all mini
00:05:16.320 LM L6 V2 and C upload the resulting
00:05:20.000 vectors to Pine Cone along with metadata
00:05:22.039 that includes the original question and
00:05:23.440 answer each Vector represents pine cone
00:05:25.800 allows us to partition the vectors held
00:05:27.240 inside of a single database index into
00:05:29.160 groups called namespaces so what we'll
00:05:31.199 do is upload the first batch of vectors
00:05:32.919 representing data related to the Miami
00:05:34.400 based Meetup GP Tuesday into a namespace
00:05:37.199 or group called GP Tuesday and upload
00:05:39.840 the second batch of vectors representing
00:05:41.720 data related to me yours truly into a
00:05:44.039 namespace or group called Tad both of
00:05:46.560 these groups of vectors will sit inside
00:05:48.280 of the same database index first let's
00:05:50.520 upload the q&a's related to GP Tuesday
00:05:54.450 [Music]
00:06:00.600 and second let's upload the q&a's
00:06:02.680 related to Tad aka
00:06:08.950 [Music]
00:06:13.840 me now that we've ingested the data for
00:06:16.199 our two knowledge bases we should see
00:06:17.960 some vectors as well as some name spaces
00:06:20.039 inside of our index let's now test out
00:06:22.880 our react agent when we ask our agent
00:06:24.960 about the GP Tuesday Meetup we want
00:06:26.639 relevant info from the GP Tuesday name
00:06:28.479 space to be returned and when we ask
00:06:30.199 about Tad aka me we want relevant info
00:06:32.599 from the Tad name space to be returned
00:06:34.479 let's say tell me about GP Tuesday
00:06:36.880 notice the bold black text below the
00:06:38.520 message loader that indicates which
00:06:40.039 group of vectors is being accessed that
00:06:42.319 looks good let's now say tell me about
00:06:48.240 Tad that also looks good let's walk
00:06:51.639 through What's Happening Here one we
00:06:53.199 send some prompt to our agent two the
00:06:55.440 llm powering our agent will decide if
00:06:57.160 this prompt is related to any supported
00:06:58.800 knowledge bases if it's not the llm
00:07:00.680 returns directly if it is though we
00:07:02.360 continue three we convert our input
00:07:04.280 prompt into a vector four we compare the
00:07:06.440 vector representing our input prompt
00:07:08.000 against the vectors in any knowledge
00:07:09.560 basis the llm has decided as being
00:07:11.080 relevant and retrieve the original data
00:07:12.759 represented by the highest matching
00:07:14.039 vectors five we combine all retrieve
00:07:16.160 data with the original prompt and send
00:07:17.639 that to our llm and finally in six you
00:07:19.919 receive the final output from the llm
00:07:21.520 and return that to whomever is using our
00:07:23.199 agent react agents are powerful and can
00:07:25.479 be expanded to search across many
00:07:26.960 knowledge bases two business use cases I
00:07:29.000 can think of for for react agents would
00:07:30.759 be one customer relationship management
00:07:32.960 where each group of vectors is
00:07:34.160 associated with a particular customer
00:07:35.960 for generating individualized sales
00:07:37.879 marketing and support scripts and two
00:07:40.120 higher education where each group of
00:07:41.759 vectors is associated with a course
00:07:43.319 offered by an institution so that
00:07:44.680 students approved to take the course
00:07:46.280 have course material available at their
00:07:47.840 fingertips full stack vectors pine cone
00:07:50.840 Edition GP Tuesday edition 305 Edition
00:07:54.639 like share comment subscribe Edition
