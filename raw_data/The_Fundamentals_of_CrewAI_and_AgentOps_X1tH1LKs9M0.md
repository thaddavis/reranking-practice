---
video_title: "The Fundamentals of CrewAI and AgentOps"
video_url: "https://www.youtube.com/watch/X1tH1LKs9M0"
---

00:00:00.000 No text
00:00:00.070 [Music] creai is a multi-agent framework and agent Ops is an agent observability tool
00:00:06.960 crei is one of the leaders in their space as is Agent Ops for reference here's a list showing the leading open-
00:00:13.320 Source multi-agent Frameworks ordered by GitHub stars as of October 2024 for the remainder of this video we
00:00:20.080 will demo how you can use crew aai with agent Ops via two beginner friendly
00:00:25.439 examples in demo number one we will show how to build a crew AI project up from scratch so we get a solid understanding
00:00:32.479 of how a crew AI project Works in demo number two we will show how to build a crew AI project using the crew AI CLI
00:00:40.480 we'll be building a team of songwriting agents to help us write a hit
00:00:44.000 No text
00:00:46.920 song If you want to code along step by step you'll need to install two tools onto your machine Docker desktop and VSS
00:00:54.079 code both of these tools are free and offer extremely easy to use installation processes with support for Mac windows
00:01:00.559 and Linux I'll be using Mac in this video but the general process of what we'll be doing will be the same for Windows or Linux let me now show you how
00:01:08.040 I installed these two tools on my Mac so you get a feel for how easy it was for me but if your experience is not as
00:01:13.520 straightforward please leave a comment so I'm aware or I suggest you put detailed descriptions of the issues you're running into into either Google
00:01:20.280 or chat GPT for help troubleshooting here's how to download and install Docker desktop on Mac go to the official
00:01:22.000 No text
00:01:26.840 download page download the appropriate version for me this is Apple
00:01:32.240 silicone open the downloaded DMG file and drag and drop the docker doapp
00:01:39.280 icon into your applications folder I've already done this so I'll click stop but
00:01:45.880 that's it it's that easy and here's how to download and install vs code on Mac
00:01:46.000 No text
00:01:51.799 go to the official download page download the appropriate version for me this is Apple silicone unzip the
00:01:59.240 downloaded zip file and drag the visual studio code.
00:02:04.399 apppp icon into your applications folder I've already done this so I'll
00:02:10.000 click stop but that's it it's that easy after installing VSS code you'll need to
00:02:15.239 do one last thing open vs code and come over to the extensions Marketplace on
00:02:21.040 the side menu and you'll need to install two extensions a the docker extension
00:02:28.200 you can search for it in the search bar and once you find it in the panel you click on it and then you'll see these
00:02:35.480 buttons right here you can click to install it should only take one click it's that simple B you'll need the dev
00:02:43.280 containers extension you should see some buttons right here and you can just click to
00:02:49.159 install it super simple and that should be all the setup you need all right here
00:02:52.000 No text
00:02:54.800 we go from scratch crew AI agent Ops let's do it here here we have an empty
00:03:01.040 folder somewhere on our computer that we're going to use as our starting point first we're going to set ourselves up
00:03:06.840 with a very solid foundation to build this crew aai application on top of or I should say I find this Foundation to be
00:03:14.159 very solid but let me know what you think in the comments let's start by adding the following folder and files to
00:03:20.480 this empty project at the root let's create a folder calledd container inside of thisd container
00:03:27.720 folder let's create a file called devc container. Json and at the root of this project
00:03:34.640 let's also create a file called Docker file.
00:03:39.680 deev here is the content we will paste into the devc container. Json
00:03:45.799 file you'll understand what the content of this file does
00:03:54.120 shortly and here is the content we'll paste into the docker file. deev
00:04:00.480 you understand what the content of this file does shortly as well all righty now that we have these files set up we can
00:04:07.239 launch our Dev container we won't go into detail but when I say launch our
00:04:12.680 Dev container what I mean is we will build a mini computer that will run on top of our actual computer inside of
00:04:19.238 this mini computer we'll play around with crew aai close or kill the mini computer when we're done and then our
00:04:25.680 base machine AKA our laptop or desktop or whatever we're using will be left clean as if nothing ever happened AKA
00:04:33.800 this is a fantastic technique for experimenting with new software without cluttering our base machine with
00:04:40.240 potentially messy software installations here's how we build our Dev container in vs code we type shift
00:04:47.600 command p and that opens this menu called the command pallet inside the
00:04:52.720 command pallet we look for an option that says Dev containers reopening
00:04:58.440 container I think this menu option will only be available if you have the dev containers vs code extension installed
00:05:05.199 when we select it our Dev container will begin being built in my experience building a Dev
00:05:11.880 container takes about 1 to 3 minutes it depends on the number of factors like how fast my machine is or the details of
00:05:19.759 the dev container I'm building Etc but after the dev container is right so that
00:05:25.479 took like what like a minute maybe even less but after a Dev container is built
00:05:30.960 we can shut it down turn it on shut it down turn it on shutting it down and turning it on only takes a few seconds
00:05:38.840 anyways it might take longer for you it might be shorter I don't know the details of your environment but
00:05:43.880 hopefully that gives you a feel for how this works let's quickly test out this development container to make sure it's
00:05:49.199 looking good as crew aai is a python based tool let's confirm we have python
00:05:55.120 installed and we do and let's try try running some python
00:06:00.600 code to make sure that works too so here I've created a file called
00:06:06.319 main.py let's add some code into this file and pass this main.py file to the
00:06:14.000 python interpreter on the dev container and it looks like it works if
00:06:19.360 we look closer at the docker file. deev we can see we asked Docker to build us a
00:06:24.680 mini machine with python 3.12 installed on it and we also asked for some
00:06:29.880 additional C++ libraries to be installed as well because these will be needed by crew aai the remaining lines of this
00:06:36.639 file outline where we want to work inside of this Dev container for example
00:06:42.759 if we enter the PWD command or present working directory on our Dev container we can see we are in a folder called
00:06:49.280 code at the root of the file system if we were to look at the root of the file system on our base machine we would not
00:06:55.599 see any folder by the name of code the mental model keep in mind is that we
00:07:01.280 have two separate systems running on our machine we have the dev container and we have our base machine each of these two
00:07:08.520 systems has its own file system and is capable of having completely different software installed moving forward we're
00:07:15.919 going to be working inside of the code folder at the root of the file system of the development container or our mini
00:07:22.639 machine that's running on top of our base machine hopefully that makes sense let's remove this main.py file that we
00:07:29.560 Ed for performing a quick hello world test and move along now that we have a solid foundation we can start building
00:07:33.000 No text
00:07:36.000 our crew AI project the way we're going to do this is not recommended at all but for the purposes of learning how cre
00:07:42.319 works it will be fantastic what we're going to do is build up a simple crei
00:07:47.360 project from scratch one file at a time here on cre ai's documentation they
00:07:52.599 provide an outline of what a crew aai application looks like we can see a crew AI project contains a source folder
00:07:58.840 inside of the source folder we have another folder here it's called my project inside of my project folder we have a main.py file a crew. py file a
00:08:05.840 tools folder a config folder inside the config folder we have an agents. yo file and a task. yo file okay got it so in
00:08:13.599 the same way a chef can take a look at a recipe get the gist of it and improvise on it when cooking a dish we are going
00:08:19.479 to build an application that follows the general outline of what a crew AI application looks like let's add the
00:08:25.280 following folders and file to our Dev container at the root of our project let's create a folder called Source
00:08:31.159 inside of this Source folder let's create a folder called R crew of agents and inside of this R crew of Agents
00:08:36.440 folder let's create a file called main.py when a file ends inp it
00:08:42.320 indicates to us that it will hold python code when you're looking at python projects it's very common to see some
00:08:48.120 file called main.py for our purposes main.py will be the file we use to launch our agents and give them tasks
00:08:55.760 for the beginners watching I find it important to tell you that when programming we can call call files folders and many other aspects of the
00:09:01.839 code we write whatever we like for example we could have called main.py blah. let me show you let's rename
00:09:10.079 main.py to be called blah. py and let's add simple instruction into
00:09:17.519 blah. piy for example this is the instruction to print telling my agents
00:09:22.560 to do something to the screen and then let's pass this BL Pi file to the python
00:09:27.920 interpreter and then you can see we get the text printed telling my agents to do something names are just labels and when
00:09:35.240 programming there are an infinite number of ways to organize your code in practice though so it's easier to
00:09:40.640 collaborate and build with others we follow conventions these conventions are learned through experience over time so
00:09:46.920 be patient if you're feeling unfamiliar with what you're looking at watch the whole video and come back to any
00:09:52.160 confusing Parts later let's rename this blah. py file back to main.py because
00:09:58.519 that's more conventional and quickly confirm that everything
00:10:04.440 works and let's pass the main.py file to the python interpreter and as we can see
00:10:11.279 everything works just the same now instead of Simply printing out the text telling my agents to do something let's
00:10:12.000 No text
00:10:17.720 add some code provided to us by the team at crew aai we could add all of the code of this product into a single file AKA
00:10:24.720 this main.py file but that is not advised as over time that would mean we would constantly be scrolling up and
00:10:30.240 down across the main.py file as we added more lines therefore let's add another file to our project called crepy let's
00:10:37.680 add this crew. py file inside of the r crew of Agents folder and here is the content that we
00:10:43.760 will paste into this crew. py file and we can call the code in this
00:10:49.839 crew. py file from the main.py file like so okay remember this Docker file. deev
00:10:57.440 file and how it included this line that's says python path equals SLC code
00:11:03.639 this line configures the python interpreter on the dev container to look for code we import at this specified
00:11:09.279 path for example if we look at the path of the crew. pi file we can see the path is slode Source SLR crew of Agents crew.
00:11:18.160 I know in the main.py file paths are specified with dots in our Imports
00:11:23.320 instead of slashes but in this context it means the same thing also note that
00:11:29.320 we don't have to write Pi at the end of python files we Import in our code quick
00:11:35.160 side notes so in my vs code I was seeing a warning that said select interpreter the warning was showing right here vs
00:11:42.079 code should automatically detect The Interpreter path on the dev container right so hopefully you don't see this
00:11:47.160 issue but I've seen it happen from time to time and if this is happening for you this is how you fix it in vs code Type
00:11:53.560 shift command P that'll open up the command pallet and search for an option that says python select interpreter if you don't see this menu option you can
00:11:58.959 start typing python they'll start filtering out the menu options then you can select this one right this is the appropriate one python select
00:12:04.440 interpreter hit enter and that'll take you to a submenu as I mentioned vs code
00:12:09.920 should automatically detect The Interpreter path right hopefully you see a recommended option you can just select it and that'll make the warning go away
00:12:16.440 if for some reason you don't see a recommended option in the submenu you can manually enter the path to The
00:12:21.560 Interpreter on the dev container here right by selecting this option enter interpreter path the path to The
00:12:26.720 Interpreter is slash user SL local bin
00:12:32.680 python then you can click enter and that should make the warning go away as well if you recall you know I guess 30 60
00:12:40.440 seconds ago crew was colored white as was the r crew of agent symbol right and
00:12:46.680 after I selected The Interpreter path everything became colored appropriately as I expected Etc
00:12:52.360 so like I said if everything's colored as you're seeing it or you know everything's working smoothly ignore
00:12:58.959 this section but if you have a warning showing somewhere in your vs code UI that says you know select interpreter
00:13:04.920 path I just showed you how to fix it so let's move forward let's try running our crew of agents for the first
00:13:06.000 No text
00:13:11.120 time module not found error no module named crei when we fed this main.py file to
00:13:17.480 the python interpreter the code or the instructions outline began being executed from top to bottom on line one
00:13:23.800 you can see we're doing an import we're importing source. our crew of agents. crew that popped the python interpreter
00:13:29.680 over to the crew. py file in this file you can see on line one we're also doing an import we're
00:13:35.160 importing this thing called crei and you can see as indicated by vs code has this
00:13:40.360 yellow squiggly line underneath it if we hover over we see the text import cre aai
00:13:46.760 could not be resolved so as indicated by the error in the console and as
00:13:52.120 indicated by vs code this crei thing is nowhere to be found so what we're going to do is add this crei thing to our
00:13:59.279 container and hopefully this error will go away python has a system in its ecosystem called ppie which is short for
00:14:05.880 python package index that allows us to easily download code published by other members of the Python Community if we
00:14:11.680 enter this command to our terminal code published to Pipi by the crei team will be downloaded to our Dev container in a
00:14:17.199 way that the python interpreter can access if we omit the version number and just type pip install creai the latest
00:14:24.800 version of the cre package will be downloaded but to not confuse things especially for those following along
00:14:30.560 let's just download this version which is the latest version as of the time of
00:14:36.079 recording it looked like the installation worked and we can see that the warnings and VSS code went away so
00:14:42.320 let's now try running our crew again and see what
00:14:50.600 happens okay we see a different error which is fantastic that means we fixed the crew aai import error but now we're
00:14:57.120 seeing an error that says file not found no such file directory code Source or
00:15:02.880 crew of Agents config agents. yaml I wonder what this could
00:15:08.820 [Music] mean the way crew AI is designed
00:15:11.000 No text
00:15:14.120 requires us to add this agents. yo file at a very specific location so let's add this file like so inside of the r crew
00:15:21.519 of Agents folder let's create another folder called config and inside of this config folder
00:15:27.639 let's add a file called agents.
00:15:33.240 yo let's paste this content into the agents. yo file as of the time of recording in
00:15:40.000 October 2024 the content of this agents. file has to follow a very specific structure with no indentation we put the
00:15:46.920 name of each agent in our crew and then at one level of indentation below the name we specify the agent's role goal
00:15:53.160 and backstory in natural language there are other properties that we can specify for our agents but these the required
00:15:59.560 ones all the other ones are optional FYI this way of outlining configuration is
00:16:05.040 extremely common in programming and is called yamamo format yo allows you to specify key value pairs of information
00:16:11.279 that can be nested at various levels in the context of a yammo file this angled bracket character is known as a folding
00:16:17.720 block symbol this character allows you to write the value associated with a key or property on multiple lines instead of
00:16:23.600 one big long line the way we connect this agents. yo config with the crew in
00:16:28.720 our crew. piy file is like so we reference the relevant key so that
00:16:34.600 it lines up with a method name that generates each agent and let's do this for the other agent real quick as
00:16:45.160 well and that's it and oops we never imported the agent class from creai
00:16:51.759 let's do that and now all of our warnings go away
00:16:57.000 and we're looking good taking a step back we can see that our crew class is coming together nicely for the beginners
00:17:04.000 watching in the context of programming a class is a blueprint for creating things to use another cooking analogy let's say
00:17:10.280 that we have the recipe for a dish the recipe is not the dish it's the instructions for how to make the dish
00:17:16.839 similarly in programming a class defines the ingredients or components of code when we pass a class to The Interpreter
00:17:23.400 of a particular programming language for example the python interpreter we are left with runnable code that implements
00:17:28.919 the blueprint defined in the class we can see in this class we're defining a group of two agents with one of them
00:17:34.559 being George Washington and the other being Thomas Jefferson now that we've defined the details of our agents let's
00:17:40.160 try running our crew again okay we see a different error and
00:17:46.480 that's fantastic that means we fixed the error related to the missing agents. yo file but now we're seeing an error that
00:17:52.559 says file not found no such file or directory code Source our crew of Agents
00:17:59.159 config tasks. yo I wonder what this could [Music]
00:18:06.000 No text
00:18:06.440 be in addition to configuring our agents the creai framework requires us to specify a file called task. yaml that
00:18:13.640 outlines the task we want the agents in our crew to perform so let's create this task. yo file at the exact location
00:18:20.000 given to us by this last error inside of this file let's paste the following
00:18:25.960 content as of the time of recording in October 2024 the content of this file has to follow a very specific structure
00:18:33.080 at no level of indentation we specify the name of each task and then at one level of invitation below the task we
00:18:38.720 specify its description its expected output and the agent we want to assign the task to the way we let our crew
00:18:46.280 class or blueprint know about the tasks outlined in this tasks. yo file is like
00:18:52.080 so we come over to the crew. py file and add the following code
00:18:59.400 and we have to format this according to Python's rules one
00:19:06.760 sec and that's looking good we just have to import the task class from the crew
00:19:15.600 AI package as well as the task decorator if you've never seen a
00:19:22.039 decorator before this is a decorator all a decorator is is a fancy
00:19:28.200 way of writing writing a function that takes a function as an input and returns another function don't stress out about
00:19:34.760 it just look at this stuff from a high level zooming out we can see we're
00:19:40.000 designing our crew to consist of two agents who will work together to accomplish two tasks by default Qi
00:19:47.080 executes the tasks outlined in the task. yo file sequentially from top to bottom so here we can see we're assigning
00:19:53.440 Thomas Jefferson to write us a declaration of independence and the Declaration of Independence he spits out will be fed into George Washington who
00:19:59.840 will then generate a military strategy for us there are other patterns besides sequential execution when giv groups of
00:20:06.799 Agents tasks to accomplish your goals but we'll leave those topics for another video as we're keeping this super simple
00:20:12.400 and beginner friendly all right let's try running our crew again and see what
00:20:20.720 happens all right well we get a different error so we fixed that missing task. yo file error that's great and now
00:20:28.679 now we're getting an error that says something went wrong kickoff should return only one task output
00:20:35.360 so sometimes when you see errors it's very straightforward but other times
00:20:40.600 it's not so if we come to crew.
00:20:46.000 py okay so this should have been written like so
00:20:53.000 excuse me so yeah I think that should
00:21:00.320 work and let's run our crew again and see what
00:21:06.799 happens okay cool yeah so we have to define the tasks inside of our class and
00:21:12.720 we also have to link them with the crew object here so hopefully that makes
00:21:19.600 sense and now we're getting a different error this error says open AI exception
00:21:27.080 API key client option must be set
00:21:32.640 right authentication error I wonder what this could [Music]
00:21:40.000 No text
00:21:40.320 be this error is happening because we haven't authenticated our project with open ai's platform crew AI supports
00:21:47.640 various llms for powering the agents in a crew but by default it uses open AI if
00:21:53.080 you're unfamiliar with the term llm an llm is the part of an agent we would consider its brain the details of how an
00:21:59.919 llm Works can be explored outside of this video if interested but for our purposes we'll be calling an llm powered
00:22:06.080 by open AI via its API each time one of the agents in our crew is performing the task currently assigned to it connecting
00:22:13.000 our project with open aai is simple all we have to do is come to platform.
00:22:18.360 open.com in our browser and if this is a new account for
00:22:25.279 you you will have to add a couple dollars open AI pricing model is usage based
00:22:32.480 it's like a gas station you will need some credits and after you have that set up you can browse around and look for
00:22:40.960 the API key [Music]
00:22:48.320 section API Keys have been replaced by project API Keys view project API
00:22:54.080 keys so here we can create a new API key so so let's click this button
00:23:02.200 and we can leave everything as default and click create secret
00:23:08.120 key and make sure you keep this private but let's copy it and we'll be using it
00:23:14.600 later so make sure that no one else besides you gets access to this API key
00:23:20.840 and here is how we securely add this API key to our project for the beginners watching pay attention closely because
00:23:27.480 this technique is very common at the root of our project we're going to create aemv file inside of this EMV file
00:23:35.720 we will type on a single line in all caps open
00:23:40.960 aior aior key equals and then we will paste
00:23:46.919 in the API key that we provisioned on open ai's platform we'll save this and the next
00:23:54.760 thing we'll do is install this special package called python.
00:24:00.279 MV this is the version that we'll be using and then we'll come over to the
00:24:05.880 main.py file and add these
00:24:12.360 lines these lines will read in any secrets that we have in the M file and
00:24:17.480 make them available to our code so now if we run our crew let's see what
00:24:24.640 happens hopefully this should work
00:24:30.960 and yeah things look like they're working the console looks [Music]
00:24:39.440 beautiful and interesting we only see George
00:24:47.399 Washington performing a task let's see what's going
00:24:56.440 on oh I see what happened so The Decorator was accidentally
00:25:03.320 deleted so if we run our crew
00:25:09.559 again yep now we see Thomas Jefferson writing the Declaration of Independence
00:25:14.799 and when he's finished George Washington will write us or I guess he'll come up with a military
00:25:23.919 strategy right there goes the Declaration of
00:25:29.600 Independence [Music] and here is the military
00:25:34.799 strategy so that's fantastic we have a working crew remember the way we built up our
00:25:38.000 No text
00:25:40.919 crew of Agents up from scratch manually is not recommended at all but for the purpose of learning how crei works I
00:25:47.120 hope you found it useful let's do one final thing before we wrap this up let's show how we can track our agents using a
00:25:53.640 tool Called Agent Ops agent Ops is compatible with many different multi-agent Frameworks and allows us to
00:25:59.360 track metrics such as the cost of the agents in our crew how long it's taking the agents in our crew to complete its
00:26:04.480 tasks and it'll also track any errors our agents run into as well the process of integrating agent Ops is extremely
00:26:10.720 easy and is very similar to how we integrated with open AI to integrate with agent Ops come over to app. agent
00:26:19.440 ops. if you haven't signed up already create an account and come over to the
00:26:25.480 API key section once you're logged into your dashboard you should already have an API key
00:26:30.559 provision for you by default and copy this API key and come back to the cre
00:26:39.679 project that we've been building and inside of the M file or the EMV file
00:26:44.880 let's add a new line and in all caps let's write agent
00:26:51.880 opscore API uncore key equals and then paste in the API key that you copied
00:26:58.080 from from the agent Ops dashboard save and then let's come over to the main.py
00:27:04.080 file and let's add the following
00:27:12.919 lines make sure you add these lines after the load. M command so that the
00:27:18.120 agent Ops API key is available to be used and make sure you add this agent Ops tracking code before you call your
00:27:24.559 agents so that they're ready to be tracked before doing tasks but hold up
00:27:30.480 notice how VSS code is giving this little warning indicator telling us that there's something up with this agent Ops
00:27:36.440 import and we've seen this before it's because we haven't installed this package yet so let's type this pip
00:27:43.519 command into our
00:27:48.640 terminal and after the installation completes we should see this warning go away in vs code and it does so now let's
00:27:57.080 run our crew again and see what
00:28:09.240 happens and when our crew is done we see some
00:28:14.440 analytics right see the cost and we see this link that we can
00:28:19.840 click on and inspect we can see it gives us a
00:28:25.559 dashboard with an overview of this session that we just had with our crew
00:28:31.080 and this can be very useful for troubleshooting issues and getting an overview of what's going on as you
00:28:37.200 leverage agentic workflows more and more you're going to need a tool like agent Ops for monitoring what's going on okay
00:28:42.000 No text
00:28:44.120 let's now wrap this up so I'm going to move these two lines to the top of the
00:28:50.480 file just to be a bit cleaner and that looks
00:28:56.799 good and and let's also record all of the piie packages that we use throughout
00:29:03.039 the building process so the conventional way of doing this is
00:29:09.919 to create a file at the root called requirements.txt
00:29:16.240 and inside of this requirements.txt file let's paste the following content to
00:29:22.880 record the various piie packages we used as well as their versions
00:29:28.679 and now let's store a copy of this code on GitHub add a
00:29:34.679 file called Dog
00:29:40.919 ignore and inside of thisg ignore file let's
00:29:48.559 add this entry git is no longer tracking the M
00:29:53.720 file which is great that's what we want never expose your AP API Keys let's
00:29:59.519 create a repo on GitHub then add a remote to our local git
00:30:07.279 configuration and then push our code to
00:30:18.480 GitHub and let me take a look at our code in GitHub we don't see the EMV file that's
00:30:26.480 what we want and we also need to upload all the tags because I've been tracking
00:30:31.600 each step along the way so we'll say get push Das D
00:30:38.080 tags fantastic then when we reload yeah fantastic so you can easily
00:30:45.120 follow along so what we can do now
00:30:52.399 is close our Dev container and poof
00:30:58.279 it's like nothing ever happened if you want to follow along you
00:31:02.000 No text
00:31:05.399 only need two things installed on your computer Docker desktop and VSS code
00:31:10.480 Docker desktop allows us to run these little mini computers on top of our actual computer AKA our laptop or
00:31:16.880 desktop and inside of these little mini computers called Dev containers we can experiment with new
00:31:23.200 software as you'll soon see using Dev containers for doing software development is a great way to stay
00:31:29.679 organized VSS code on the other hand is a code editor think of VSS code AS
00:31:35.440 Microsoft Word but for viewing and editing code instead of documents after installing VSS code
00:31:41.960 you'll also need to install two VSS code plugins or extensions namely the docker
00:31:48.000 extension and the dev containers extension both Docker desktop and vs
00:31:53.480 code are free and offer support for Mac windows and Linux let me show you how I
00:31:59.039 installed them onto my Mac so you get a feel for how easy it was for me but if you run into issues I suggest leaving a
00:32:05.600 comment or pasting detailed descriptions of what you're running into into either Google or chat GPT here's how to
00:32:11.000 No text
00:32:12.240 download and install Docker desktop on Mac go to the official download page
00:32:17.960 download the appropriate version for me this is Apple silicone open the downloaded DMG
00:32:24.840 file and drag and drop the docker do app icon into your applications folder I've
00:32:31.919 already done this so I'll click stop but that's it it's that easy and here's how
00:32:36.000 No text
00:32:37.840 to download and install vs code on Mac go to the official download page
00:32:43.960 download the appropriate version for me this is Apple silicone unzip the downloaded zip file and drag the visual
00:32:52.519 studio code. apppp icon into your applications folder I've already already done this so
00:32:59.120 I'll click stop but that's it it's that easy after installing vs code you'll
00:33:04.320 need to do one last thing open vs code and come over to the extensions
00:33:09.399 Marketplace on the side menu and you'll need to install two extensions a the
00:33:15.799 docker extension you can search for it in the search bar and once you find it
00:33:20.840 in the panel and click on it and then you'll see these buttons right here you
00:33:26.240 can click to install it should only take one click it's that simple B you'll need
00:33:31.799 the dev containers extension you should see some buttons right here and you can just click to
00:33:38.440 install it super simple and that should be all the setup you need here we go
00:33:42.000 No text
00:33:44.399 from scratch AKA and empty project this is the first set of files
00:33:49.600 that we're going to add to this empty project first we're going to add a folder by the name ofev container
00:33:58.639 inside of this folder we're going to place a file called devc container.
00:34:04.960 Json and at the root of the project we're also going to create a file called
00:34:10.399 Docker file. deev these files are related to Docker
00:34:15.918 and we'll configure a little mini machine or Dev container that runs on top of our base machine this is the
00:34:22.520 content that we're going to use to populate these files this is what we'll paste into the dev container. Json
00:34:32.599 file let me expand this and here is the content we will
00:34:39.719 paste into the docker file.
00:34:46.960 deev these files will make sense shortly now that we have these files added let's
00:34:53.480 build or launch our mini computer or Dev container before we do that though let's take a
00:35:00.160 quick look at the docker desktop UI and we can notice there's no containers running and let's also set up a timer so
00:35:08.800 that we can time how long it takes to build this Dev container so if we come back to VSS code
00:35:16.800 here's how we launch the dev container so we'll type shift command P that'll
00:35:22.640 open up this command pallet as it's soall and you'll find an option in the
00:35:28.280 menu called Dev containers reopen in container this menu option will only be
00:35:34.560 available if you have the dev containers extension installed we'll click enter and quickly
00:35:42.400 start the timer and let's see how long it
00:35:49.880 takes is that it took less than 10 seconds for me but
00:35:55.960 yeah I would say on average building a Dev container usually takes about like 1 minute maybe 3 minutes it depends on the
00:36:03.720 details of your machine and how much software you're packing into the dev container the next thing to notice
00:36:11.720 is in the docker desktop UI remember before we had no container showing but
00:36:17.680 now you can see we do have a container showing let's run a little smoke test on this Dev container to make sure it
00:36:23.400 behaves as we expect so because crew AI is a python based tool let's make sure we have
00:36:30.280 python installed and we do python 3.12 this aligns with line one of the
00:36:38.000 docker file. deev this is configuring the mini machine to come installed with python
00:36:45.920 3.12 and let's make sure that we can execute python code on this Dev
00:36:51.640 container let's create a little hello world script and see what happens when we pass
00:36:59.440 it to the python [Music] interpreter and that
00:37:05.319 works let's delete this main.py script because we won't need it moving
00:37:11.000 forward and the last little smoke test that we'll do is confirm the
00:37:17.160 location that we're in on the dev container and we can see that we're at the root of the file system in a folder
00:37:24.880 called code if we were to look at the root of the file system on our basee machine we would see no folder called
00:37:32.680 code the mental model to keep in mind is that we have two machines running on our
00:37:37.800 computer we have the dev container and we have the base machine both of these
00:37:43.200 machines have independent file systems and are capable of having completely different software
00:37:48.560 installed moving forward we're going to be working in the dev container and once we're done with this
00:37:55.720 walkth through we're going to kill the dev container along with all the software that we install on it and our
00:38:01.920 base machine will be left clean now that we have a solid foundation let's install crew from the python package index AKA
00:38:03.000 No text
00:38:11.240 piie let's type this command pip install crew AI equals equals
00:38:17.200 0.671 this is the latest version as of the time of
00:38:25.800 recording after installing the crew AI package we can use the crew AI CLI like
00:38:36.200 so I don't know what's going on here but here is the crew AI CLI menu
00:38:45.960 and you can see the crew AI CLI offers commands for doing
00:38:52.200 training for replaying sessions that you've had
00:38:57.599 with your crew and of particular note or importance to us there is this create
00:39:04.680 command for creating Crews so because we're going to be creating
00:39:10.720 a ACC claimed group of musicians to help us write a hit song Let's enter the
00:39:18.280 following command crew AI create crew hit music
00:39:23.720 only hit music only is the name of our project or crew this is customizable you
00:39:29.280 can put whatever you want here in the console we can see all of these generated files and folders and this is
00:39:36.800 great because using the CLI saves us time from having to create
00:39:42.280 all these files and folders manually ourselves and also note how all these
00:39:47.480 files and folders were created within this folder in our project these files that were
00:39:54.680 generated adhere to the gu guidelines of python poetry python poetry is a popular
00:40:02.839 python framework that has gained a lot of traction over the past few years the other thing to note is that if
00:40:11.200 we dig a Little Deeper we can see that we actually have a working crew called
00:40:18.040 the hit music only crew in this code and at the moment this crew
00:40:24.599 consists of a researcher agent and a reporting analyst
00:40:30.280 agent because all of these generated files were added in a subfolder of our
00:40:36.240 project route and not the project route itself we have a very minor technical
00:40:41.720 tweak that we have to perform and the way that we do this little tweak is by coming over to the
00:40:47.280 dev container. Json file and adjusting the workspace folder key here is the
00:40:54.400 updated value that we will specify we'll put the name of our generated crew
00:41:03.640 aai project and because this is an update to
00:41:10.040 the configuration of the dev container we actually have to rebuild the dev container as a reminder the specs of the
00:41:17.599 dev container are determined by the content we put inside of the dev container. Json and Docker file. deev
00:41:24.359 files from step one there are a couple of ways that we can perform this rebuild
00:41:30.319 but for Simplicity we're going to do it like this let's come over to the docker
00:41:35.760 desktop UI stop our Dev
00:41:42.079 container and then delete it we might have been able to just delete it right away but anyways I chose
00:41:49.520 to shut it down first and then delete it so here we are deleting it right so if
00:41:54.599 we come back to vs code vs code's like what happened Dev container is no longer here
00:42:03.680 you know it's like an error right so anyways let's cancel this and close vs
00:42:10.000 code and the way we're going to reopen It Is by opening the project folder just
00:42:15.560 like we would open any other coding project with VSS code
00:42:21.359 so I'll open it on the command line but you can do this via the gooey as
00:42:28.119 well but I'm going to navigate
00:42:33.680 to the project folder we've been working in then open this project folder with vs
00:42:40.240 code like [Music] so and because we placed this Dev
00:42:46.760 container. Json file in the appropriate location vs code picks up that we would
00:42:52.599 like to open a Dev container and this is courtesy of the dev container containers vs code
00:43:00.000 extension so that proba went away but there's a button on it you can click to trigger the rebuild of the dev container
00:43:07.240 but we can also trigger the rebuild by going to the command pallet and
00:43:12.680 selecting this option Dev containers reopen in container so we'll select
00:43:18.319 that and we should be directly in the Poetry
00:43:25.200 project right and that is the case if we come to the terminal on the dev
00:43:31.520 container and check out where we are on the file system you can see we're no longer in the code folder but we're in
00:43:39.040 the code SL hitmusic only folder so the reason why we did this is because we want VSS code to play nicely with our
00:43:45.920 poetry project if VSS code opens at the project route our poetry product is
00:43:52.200 nested one folder down so vs code has a process when it launches where it tries to detect the type of project being
00:43:59.079 opened and now it can detect that our project is a python poetry project and it'll give us some extra nice to have
00:44:05.480 features that will enhance our developer experience that's why we did this but check this out let's open the crew AI CI
00:44:13.359 menu again but what happened it's saying crew
00:44:19.160 AI command not found but we installed it right so what happened was when we
00:44:25.720 rebuilt def container it lost some of its state or it lost its state I should
00:44:31.839 say so you can shut down and turn on and shut down and turn on a Dev container
00:44:36.880 and that will preserve its state but if you rebuild a Dev container it will lose its state so now what we have to do is
00:44:44.880 reinstall crew
00:44:50.480 aai FYI if we want to avoid reinstalling the crei package each time we rebuild
00:44:58.160 the dev container we can edit the docker file dodev but let's not worry about that for
00:45:05.559 now and move forward okay we're back in the hit music only subfolder right so
00:45:10.720 the present working directory is SL codeit music only we're almost ready to run the crew but we have to do one last
00:45:19.440 thing before we do so because this code is based on the python poetry framework
00:45:27.000 we have to run the standard poetry setup or install process so let's time this
00:45:33.559 just for reference and the First Command we got
00:45:39.040 to type or we got to enter rather is this
00:45:44.880 one then the second one is poetry
00:45:53.599 install let's see how long this takes
00:46:06.119 I think why this poetry setup process took so long was because this generated
00:46:12.400 cre AI project comes with tools and crei seems to have many tools
00:46:18.359 I looked on their website and they have tools for connecting to databases for scraping websites for searching YouTube
00:46:25.760 Etc if you're if you're not familiar with the term tools in the context of agent development tools are the
00:46:32.000 Integrations made between our agents and the outside world now let's run our
00:46:42.119 crew and then it looks like the crew started to run but then an error was
00:46:48.880 thrown and we can see here the eror is related to a missing API key and to be exact a missing open AI
00:46:58.880 API key so believe it or not we're actually in really good shape so crew AI
00:47:05.599 by default uses open aai for powering the agents in a
00:47:10.640 crew crew AI supports other llms as well but like I said by default it uses open
00:47:16.880 AI before we add our open AI API key to the project and fix this error though
00:47:22.960 let's recap what's happened up till this point first we started from scratch AKA
00:47:28.119 an empty folder we then set up a Dev container which is like a little mini computer that runs on top of our laptop
00:47:33.880 or desktop whatever we're using then we installed the crew aai package from piie
00:47:39.240 in order to use the crew AI CLI then we generated a crew aai project called hit
00:47:44.880 music only then we noticed how the generated project was placed into a subfolder and because we wanted our VSS
00:47:51.720 code Editor to play well with this generated poetry based project we had to adjust the configuration of our Dev
00:47:57.359 container to open the generated subfolder when launching so we edited the dev container. Json config and
00:48:03.079 rebuilt our Dev container after the new Dev container finished launching we were placed directly into the generated poetry
00:48:09.680 project which allowed VSS code to give us some extra nice to have development features like import inspection and
00:48:15.240 syntax highlighting then because our Dev container lost its state after being killed we had to reinstall the crew AI
00:48:21.760 package we then ran the standard poetry setup process AKA pip install poetry followed by poetry install and after the
00:48:28.720 Poetry setup process completed we ran our crew AI project and successfully launched our default crew of Agents
00:48:34.920 before they aired out due to missing access credentials when trying to connect to open AI I hope this makes
00:48:41.440 sense let's now move forward by adding an open aai API key to our project
00:48:46.000 No text
00:48:47.800 connecting a crew AI project with open aai is simple all we have to do is come over to platform.
00:48:54.400 open.com and sign up if this is a new account for you you will need to add some credits to your account open AI
00:49:01.480 system is usage based it's like a gas station so you will need some credits to use it you can always add more later so
00:49:08.440 I recommend adding the minimum amount and after you have that set up look for
00:49:14.680 the section that reads API keys I found it in the dashboard section right on the
00:49:20.559 Side Bar there's this API Keys option and we can click this button here to
00:49:26.160 open up a little model for configuring some aspects of this API key let's just leave it default then click create
00:49:32.760 secret key and then we'll be given an API key that we can use to connect our crew AI project with the open aai
00:49:39.359 platform the way we add it to our project is like so inside of the Poetry project at the root there is this EMV
00:49:47.559 file let's make sure that this file includes a line that reads in all caps
00:49:53.359 open aior aior key equals then we will paste in the value that we
00:49:59.599 copied from open AI after we have that set up let's run our crew again and
00:50:06.040 hopefully everything works so we'll type cre AI
00:50:12.440 run and there goes the researcher
00:50:18.200 and this is the output generated by the researcher and that output got fed into the analyst
00:50:26.480 and and this is the final report generated by the analyst so no we were able to run our crew successfully so
00:50:32.440 that's great let's now customize our crew by replacing the default agents and the default tasks that were given to us
00:50:33.000 No text
00:50:38.920 when we generated the project we can do that by coming over to the source hit music only or whatever
00:50:45.960 your Project's name is config folder and inside of the config folder we should see a file called agents.
00:50:51.920 yaml you can see by default we were given a researcher agent and a a reporting analyst
00:50:58.440 agent let's replace these agents with the following
00:51:03.760 agents A songwriter agent and a producer
00:51:09.520 agent you can see for each of these agents we're outlining its role goal and
00:51:15.160 backstory in natural language and there are other properties that we can supply but if you want to learn about those go
00:51:21.880 to crei documentation let's now update the tasks that will be assigned to our agents by coming over to the tasks. file
00:51:29.799 and you can see this is the list of tasks that was provided to us by the QI
00:51:36.359 CLI here we have a research task followed by a reporting task by default
00:51:42.920 Qi will execute the tasks listed in this task. yo file sequentially from top to
00:51:48.920 bottom so let's replace this content
00:51:54.359 with these tasks here you can see we're first going to
00:52:00.119 assign a songwriting task to the songwriter agent and after the output is
00:52:06.280 generated by this songwriter we will pass it and have a producing task executed by
00:52:13.960 the producer so what we're doing here is having a songwriter write lyrics and
00:52:19.520 beautiful Melodies and those raw ideas are getting passed to a producer who will compose it into a full song after
00:52:26.000 No text
00:52:27.160 saving these updates to our crew's config we have to link it with the crew class in the crew. py file so let's come
00:52:34.240 over to the crew class and make the following
00:52:39.319 updates our researcher agent has now become a
00:52:47.520 songwriter and the reporting analyst agent has now
00:52:53.559 become a producer
00:52:59.440 and let's also update the tasks that we're assigning to
00:53:13.440 them and the producer is also going to
00:53:18.799 Output a file so we can check out the final result the final song and let's update the name of this
00:53:27.200 file that it'll spit out results to to be called song. MD so zooming out what
00:53:34.240 we've done here is create a internationally acclaimed songwriting
00:53:41.000 Duo and task them with writing us a number one hit
00:53:46.799 song and we're almost ready to run this crew and have a hit on our hands but before we do that let's do one more
00:53:53.280 thing that being adding in agent Ops so that in addition to having our song
00:53:58.520 written to a file on our local computer we have a backup in the cloud as well as
00:54:03.920 you know can see some metrics about how this crew generated the song Here's how
00:54:08.000 No text
00:54:10.079 easy it is to add agent Ops from monitoring our crew first come over to app. agent ops.
00:54:17.280 and sign up if you haven't already they do have a free here and that should be
00:54:22.520 enough for what we're doing here and after you're signed up come over to the API key
00:54:31.119 section and you should see a default API key that you can copy and the way that
00:54:38.760 we add this API key to our project is by coming over to the EMV file at the root
00:54:44.720 of the Poetry project and on a new line let's add a entry that reads in all caps
00:54:54.319 agent opscore a apore key equals then we'll paste in the API key that we
00:55:01.040 copied from the agent Ops dashboard after we have that set up let's come over to the main.py file and add a few
00:55:10.319 lines these are the lines that we're going to add make sure to add them at the top of the
00:55:17.839 file so that by the time you run your crew tracking is set up by agent Ops but
00:55:26.599 observe how VSS code is telling us there's an issue with this agent Ops import and we can read the warning that
00:55:33.079 says import agent Ops could not be resolved this is because we haven't yet installed the agent Ops package from
00:55:40.720 piie so let's do that now by entering this
00:55:46.359 command I should say before we enter this that because this project is a
00:55:51.680 poetry project we have to use the Poetry ad command if this was a PL old python
00:55:57.359 project we would type something or enter something along the lines of pip install
00:56:03.000 agent Ops right but because this is a poetry project we have to use the Poetry ad
00:56:09.079 command so let's enter this and see what
00:56:15.359 happens okay that looks good it looked like it worked and notice that even though we installed the Hops package
00:56:21.319 with the Poetry ad command correctly we still have this warning
00:56:26.440 this is because by default VSS code does not know where poetry installs packages
00:56:32.799 and we can easily fix this minor issue like so first we have to find out the
00:56:37.920 location where poetry is installing packages and we can do that by typing or
00:56:43.319 entering poetry EMV info and you can see this
00:56:51.720 path is where packages are being installed by po Tre so let's copy this
00:56:58.760 path value and once we have it copied we'll enter the following keystrokes into vs
00:57:06.240 code shift command P to open up the command pallet and let's look for an option that reads python select
00:57:13.200 interpreter let's select this option and then you'll see a recommended option I
00:57:19.520 think this might work but just to make sure it's the same exact one that we just copied there's also an option that
00:57:25.760 says enter interpreter path so we can select that paste in the path value that
00:57:31.400 we just copied click enter and that should fix the import
00:57:37.000 error and it does in summary we're using one tool AKA pip for installing the crew AI CLI and
00:57:44.359 we're using another tool AKA poetry for adding packages to the project generated by the crew AI clii I know it's
00:57:51.760 confusing but welcome to python development finally let's run this crew and generate a hit song to review
00:57:53.000 No text
00:57:58.960 everything we've done up till this point the agents. yo file looks
00:58:04.480 great the tasks. yo file looks great the crew. py class looks
00:58:13.440 great and the main.py file looks
00:58:18.520 great as well but notice this this wouldn't affect us if we ran
00:58:23.799 it now but we like to be clean so crew AI allows you to pass in values
00:58:29.160 dynamically when running or kicking off your crew so if we wanted to use this
00:58:35.280 feature we would use it like so let's say for example we wanted to customize the genre that our hit making
00:58:44.240 Duo is specialized in so we could put curly braces then specify some variable like
00:58:51.119 this right and we would also put this template variable
00:58:57.839 over here and we would pass in a
00:59:05.240 dictionary that includes the value we would like to replace that template variable with for example hiop
00:59:13.240 right maybe country pop you get the point but we're not
00:59:19.640 going to use this feature for now we're going to keep it simple you can explore the more advanced features offered by crew AI outside of this video
00:59:27.480 and let's delete all this inputs stuff we're not
00:59:33.640 going to do any training but let's just delete that right let's
00:59:41.799 delete these template variables from the agents. file and
00:59:48.559 now let's cook up this number one hit by
00:59:53.760 entering the crew AI run
01:00:04.920 command Okay agent Ops looks like it's tracking our crew and we can see that our songwriter is writing a song about
01:00:12.000 total accountability and here are the lyrics generated by the
01:00:17.400 songwriter and these lyrics are then going to be passed to the music producer
01:00:23.359 who will you know compose a song around them and that'll leave us with our
01:00:30.079 number one hit this looks very
01:00:36.200 usable and we have a copy of this hit in this song. MD file
01:00:45.280 reference and if we click on this link provided by agent
01:00:50.559 Ops we can see we also have a copy of this hit recorded to the aops console
01:00:58.000 and we get some additional metrics too for example you can see that the songwriter
01:01:05.160 went first in this session and after the
01:01:11.440 songwriter was finished producer got to work here we can see the cost of
01:01:16.599 generating this song and yeah this is fantastic
01:01:22.000 so now let's actually make this song and see what it sounds like [Music]
01:01:23.000 No text
01:01:34.640 in the mirror I see the
01:01:41.680 truth every scar every
01:01:49.599 bruise all the choices that I've made
01:01:58.279 they shaped the man that I
01:02:04.760 become come on no more running no more games Standing Tall I'll take the blame
01:02:14.599 no more running no more gamees Standing Tall I'll take the
01:02:21.839 BL I'm going to own it on my pth every moment every
01:02:29.960 blast through the storm I'll stand so proud accountability shout it
01:02:37.799 loud I'll take the way I'll bear the cost in this life I'm never
01:02:46.079 lost total freedom it starts within when you [Music]
01:02:53.000 No text
01:02:53.920 it okay so I did adapt the raw output let's take a look at the original
01:03:00.440 version of the song so I did use the name or I guess I will use the name I
01:03:06.680 like the name right own it I did use the same recommended BPM beats per minute
01:03:13.319 that's like the tempo of the song how fast it is this chord progression I did
01:03:18.760 use and the chorus I switched it up a little
01:03:25.000 bit so I adapt what was spit out here so here it had
01:03:30.039 four chords and what I did was similar but I did something a little
01:03:36.920 different and I did use for the most part the lyrics provided for the
01:03:43.720 verse the melody to me didn't make much sense I didn't like the way it fit with
01:03:49.599 the chords so I just came up with a Melody that sounded good to me and I
01:03:55.839 didn't use these and I did use the lyrics for the chorus I did adapt them a
01:04:02.480 bit but yeah these Melodies that were suggested for each line of the chorus I
01:04:08.240 did not use those either and I only did the first verse
01:04:13.480 and one of the choruses to do the whole song would be a little bit you know a little bit much I think
01:04:19.799 let's wrap this video up by doing one final thing let's copy this adapted
01:04:25.000 version of the out output generated by our crew and send it to a service called
01:04:30.039 sunno sunno allows you to put in a prompt and it'll generate a song for you and you can see sunno generated two
01:04:37.000 songs and let's see what the first one sounds
01:04:41.000 No text
01:04:46.190 [Music] like afraid to fight dreams are calling
01:04:52.520 my name I won't be the same steping to start my day not time for any shame
01:04:59.119 running through these city streets Ry in my feet voices my name making me stars
01:05:07.240 are shining my eyes lighting up the feel the heart my chest watch me as
01:05:14.200 I I Will Never Let It Fade breaking on the
01:05:20.520 walls that life is there me I it own it
01:05:26.000 me when I say this is my life and I'll take it all the way
