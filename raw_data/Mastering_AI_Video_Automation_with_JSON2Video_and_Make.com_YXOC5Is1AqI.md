---
video_title: "Mastering AI Video Automation with JSON2Video and Make.com"
video_url: "https://www.youtube.com/watch/YXOC5Is1AqI"
---

00:00:00.000 No text
00:00:00.160 welcome to mastering AI video automation with JSON tovideandmake.com you're in the right
00:00:07.000 place this intro is itself an example of AI video automation in action behold the
00:00:13.519 branding this is a combination of an intro and an advertisement for a software project management generation
00:00:19.760 platform called PDEV check out pre.dev today enjoy the master class hello in
00:00:26.880 this video we are going to cover the topic of AI video automation we're going to cover the building blocks the basics
00:00:33.680 of AI video automation particularly using a platform called JSON to video
00:00:39.120 strap in this is going to be an incredible adventure you are going to learn a ton and I claim by the end of
00:00:44.960 this master class that's what I'm going to call it you are going to be a master in the topic of AI video automation
00:00:51.039 let's go we are going to be combining many different platforms throughout this
00:00:52.000 No text
00:00:56.160 master class but the three platforms that we are primarily going to be using are one make.com make.com is an
00:01:02.640 automation platform and you should be able to get through everything on the free plan but in case you run into any issues you can try the core plan or the
00:01:08.799 pro plan the core plan is about 10 bucks per month and you can cancel at any time the pro plan is about 20 bucks per month
00:01:14.560 and you can cancel at any time as well primary platform number two is going to be the open AI API the Open AI API is
00:01:22.000 credits based $5 worth of credits is going to be more than enough for what we're doing here and then primary platform number three is of course JSON
00:01:28.320 to video json to video will give you some free credits when you sign up but when your free credits run out you will
00:01:33.920 likely need to spend $49.95 for context one JSON to video credit gets you about 1 second of
00:01:40.320 rendered HD footage or a quarter second of 4K footage we're not going to be playing around with 4K video here the
00:01:46.880 max resolution we're going to be playing around with is HD or full HD as you'll see it called but hopefully that gives
00:01:52.479 you some context of the basic requirements so let's get started by jumping into make.com and we're going to
00:01:58.079 start building from scratch here we are in the make.com dashboard and if we come
00:02:03.520 over to the scenarios page I've created a folder called AI video automation
00:02:10.680 masterclass here is where we're going to be storing all of the automations or scenarios as they're so-called in
00:02:16.760 make.com as we move through this adventure i have also deleted all of the thirdparty connections that I had set up
00:02:23.840 prior to recording this video so that I'm forced to show you how to set them up as well as all of the web hooks too
00:02:30.640 so we're starting from the same place if you come back to the scenarios page come
00:02:36.239 over to our folder and let's jump in by creating a new automation or scenario
00:02:43.200 let's click outside of this menu and here is where we're going to start so this is the primary interface that
00:02:48.640 make.com offers when building automations this is a type of interface called a node editor it's a very common
00:02:55.040 type of interface you're going to see it in many places if you're new to this and when you're starting from scratch you're
00:03:01.040 going to see this purple dot that you can click on that will open up this menu that you can scroll through to see all
00:03:06.319 of the different platforms that make.com is integrated with when you click on one
00:03:12.000 of these platforms or apps you'll then see the different modules or functions
00:03:17.599 that are supported right when you click on one of these modules it's going to be added to
00:03:25.120 your automation click outside again right so if I right click on the node it opens up
00:03:33.200 this little submen and I can delete a node by clicking this option right and
00:03:39.440 now that I started playing around with this we don't see that purple dot again but it's the same thing now it's gray
00:03:44.879 and this little icon is what indicates to us where our automation starts so we
00:03:51.280 can add a module or node this menu we can also add it to this menu here pretty
00:03:57.680 much does the same thing so I'll click on this do got right the visual folks
00:04:02.959 and the first module that we're going to add is going to be found inside of the
00:04:08.480 tools app and the exact module is the set variable module this module allows
00:04:15.599 us to set a variable in our automation so first variable that we're going to create will be called prompt and the
00:04:24.000 value of this variable will be hello a variable for those who don't know is a place where
00:04:31.199 you can store data and you can give that place you're storing data a name so when
00:04:38.240 you configure a node right you have to click save in order to lock in those changes sometimes
00:04:45.199 if you don't save by clicking outside of it for example and come back you'll see your
00:04:51.759 changes are erased or gone so in order to lock them in you have to click save that saves the changes on the level of
00:04:57.680 the node in order to save your changes on the level of the automation you have to do another save
00:05:04.320 so if you back out of this right you'll see we're getting a warning that asks us if we want to save our changes let me
00:05:11.199 close that and show you another way how to save this button here you can click
00:05:16.479 that will also save you can do command S right and now you back out right or
00:05:22.960 refresh your page you'll have your changes saved right so
00:05:31.080 refresh right then click in here you'll get to know this interface quickly trust
00:05:36.880 me it's not that complicated and now that we've covered the basics let's get going so the next level up in complexity
00:05:42.960 is not using a single module although this is actually quite powerful but
00:05:48.000 let's now start to string together some more modules right so you can add a module by
00:05:54.199 right-clicking then pressing this add a module button and that's going to open
00:05:59.600 that same menu where you can scroll through or search for a particular module you're interested in using right
00:06:07.039 the next module we're going to be using is the Open AI create a completion module
00:06:14.759 right one quick thing though before we hop over to OpenAI let me just mention for the people who are complete
00:06:22.120 beginners how to connect two nodes together so if two nodes are unconnected
00:06:28.560 and they're compatible you can drag them next to each other and they'll autolink another way that you can create a
00:06:34.880 connection is by dragging the input side of a particular node
00:06:40.520 and connecting it to the output side of another node right each node well I
00:06:46.479 guess except for the first one each node is going to have if I right click and unlink again an input side and an output
00:06:53.120 side right so let's reconnect that and depending on the module that you use you
00:07:00.160 might have to do some additional steps to set it up for example OpenAI requires
00:07:06.080 us to get an API key from the OpenAI dashboard which I'm going to show you how to do now and then add it into
00:07:12.479 make.com that is the way that make.com is authenticated with our OpenAI account
00:07:18.880 okay now let's get this OpenAI stuff sorted out so if we click on the OpenAI module and then click this create a
00:07:24.880 connection button it pops open another menu where we're asked to provide an API
00:07:30.160 key and our organization ID this field you can leave as default as you get to
00:07:35.759 know make you'll find this is actually quite intuitive of a name but anyhow to
00:07:41.120 provide the OpenAI API key and organization ID we have to come over to the OpenAI platform this is a separate
00:07:48.160 portal to Chad GPT it's also ran by OpenAI and if you don't have an account
00:07:54.080 sign up i already have an account so I'm going to log in and to get our API key we can come
00:08:02.960 over to the dashboard and on the side you should see
00:08:08.639 a option that says API keys and if it's not there just have a
00:08:15.680 look around you should be able to find it and once we're on this page click create
00:08:21.599 a new key and let's call this
00:08:27.160 AI video automation and leave all this as default
00:08:33.360 we'll create the API key copy it this is the only time I think we'll be able to
00:08:39.039 see it so we'll copy it come back to make and paste it into this field as far as
00:08:46.080 the organization ID come over to our profile and here is where we will find
00:08:51.600 our organization ID so if we copy that paste it in here then click
00:08:58.440 save that should connect our OpenAI account with
00:09:04.399 our make.com account and that's looking great so we can save this if we
00:09:12.760 want all right so we can't click save but we can close this and then save like
00:09:18.560 this we get another warning haha save anyway okay so let's keep going if we open up the
00:09:26.720 OpenAI module the first thing that we have to provide is what AI model we want to
00:09:32.279 use you can see that OpenAI offers many and the one that we're going to be going with is GPT40 you could use others
00:09:40.480 others might work but that's the one that I'm going to go with after you select the model you can send
00:09:46.240 messages to this AI model via this API it might seem weird if you've never seen it before but this is how it works each
00:09:53.920 message that you send has to be labeled as either a user assistant or system
00:09:59.680 message the way that I think about this is a user message is a message that's sent from our perspective to the AI
00:10:07.120 not going to make sense if you've never used it before but anyways an assistant message is a message that the AI sends
00:10:12.880 back to us why would we label a message that we're sending to the AI as an assistant message well imagine that
00:10:20.000 we're sending the history of past messages right so we ask a question maybe we're having a conversation AI
00:10:26.079 responds and we send something else ai responds right at that point we have a history of messages where it's
00:10:32.480 alternating as far as ones that we're sending and ones that the AI are sending right so we can send that message
00:10:38.200 history the AI in some cases that's what we want to do for example if we're conversing with
00:10:44.399 the AI that's not what we're doing here but anyways I'm being a little bit too pedantic and a system message is usually
00:10:50.640 a message used to configure the persona of the AI that's how I think of it
00:10:56.560 anyways for now we're just going to send a user message this is a message sent from our perspective to the AI and we
00:11:02.560 can type our message here right so let's enter hello right then click save and
00:11:10.800 now we can run our automation so if we click run once it looks like it ran successfully
00:11:18.399 and these little bubbles allow us to see what each node outputed in the
00:11:24.959 automation right so if you hover over this one and click it you can see the response that the AI
00:11:32.959 sent back to us right we said hello the said "Hello how can I assist you?" Make sense so instead
00:11:43.000 of hard- coding the message that we're going to be sending the AI let's
00:11:48.800 reference the value that we have in another node which we can do via this little panel right here this little
00:11:55.680 panel has many different tabs and each of these
00:12:01.320 tabs gives you different functionality that you'll learn about over time this
00:12:06.480 first one with a star icon allows you to reference values that are sitting in other nodes of the automation so instead
00:12:13.680 of hard- coding the text hello let's reference whatever we write into our prompt variable and that's how we do it
00:12:20.639 so we can click on different fields and
00:12:25.680 reference them so if we click save now let's
00:12:31.560 say 2 + 2 equals should say four right at least
00:12:38.800 that's what I'm expecting 2+ 2 equals 4 that makes sense
00:12:45.519 that does it for this little make.com crash course if you're intermediate to advanced in automations and make.com
00:12:53.440 this probably was a little bit pedantic not too valuable but this part of the master class was designed for people who
00:12:59.440 are brand new to this there's a lot of those people out there and yeah so a lot
00:13:05.760 of what we learned is definitely going to be applicable throughout this master class and now let's move on to the
00:13:12.560 second part where we learn about JSON and how to use JSON with make.com
00:13:17.839 and that should give us the final basics or fundamentals that we need to start learning how to generate videos using
00:13:24.480 automation with JSON to video if you've never heard of the term JSON it probably sounds a little bit
00:13:27.000 No text
00:13:31.279 intimidating but I assure you it's quite simple all that JSON is is a way of
00:13:36.560 using key value pairs to represent things let me give you an example so if
00:13:41.839 we were going to represent something for example me with JSON we would use a series of keys and values for example
00:13:48.639 the first key we would use would be name the value of the key name would be tad
00:13:55.040 the second key we would use would be the key age the value of the key age would be 35 then we would go to the next key
00:14:03.199 it might be the key weight the value of the key weight would be 155 right
00:14:09.120 hopefully that makes sense once again it's not making sense i assure you it's very very simple so now let's jump into
00:14:17.440 make.com and see how we can use JSON in the context of building AI automations
00:14:23.519 here we are in the make.com dashboard let's come over to the scenarios page
00:14:29.120 i'm going to be doing my work inside this folder and let's create a new scenario
00:14:38.320 and I'll call this scenario JSON the first thing that we're going to
00:14:45.120 do is add a set variable node so let's come over to the tools app and this set
00:14:52.880 variable module should be found inside of it and this variable is going to be
00:14:58.720 called our prompt and for now let's just say hello
00:15:07.040 let's save that and make sure we save our automation the next node that we will be
00:15:13.600 adding will be an OpenAI create a completion node i've already connected
00:15:18.800 my make.com account with OpenAI if you haven't done so already you'll need to get an API key from your OpenAI platform
00:15:24.680 dashboard then copy it into the configuration of this node anyways I've already set this up let's move along
00:15:31.920 and the model that we're going to be using is going to be
00:15:37.240 GPT40 and at the time of recording when we want to send messages to the GPT40 API we have to label each message that
00:15:43.760 we send as either being a user message assistant message or system
00:15:49.959 message a user message means a message that we're sending to the AI an assistant message means a message that
00:15:55.759 the AI is sending to us an assistant message is a message that is used to configure the persona of the AI so for
00:16:02.399 example you are a lawyer with 10 years of experience in New York law blah blah blah let's stick with the user message
00:16:08.480 for now and the message that we're going to send is whatever value we've provided in the prompt variable so let's save
00:16:15.639 that and run this as a smoke test and looks like things are working so we said
00:16:22.399 hello and the AI responded "Hello how can I assist you today great so now
00:16:28.800 let's get to the JSON part so if we open up the OpenAI node
00:16:34.360 again we can see this little check box on the bottom that says show advanced
00:16:40.920 settings let's turn that on and that's going to add a couple more
00:16:46.519 configurations that we can set and there's a bunch more of them the
00:16:52.720 one that we need is response format so instead of having the AI respond to us
00:16:59.120 in text we would like it to respond to us in JSON and we would also like the AI to
00:17:05.760 automatically parse this JSON for us or rather the OpenAI node to automatically
00:17:11.039 parse this JSON for us what this does is automatically set these key value pairs
00:17:17.439 right that's all JSON is it's just a list of key value pairs it sets it up for us so that we can automatically
00:17:22.959 pluck them out we don't have to do that setup step of converting the JSON into this pluckable thing this will make
00:17:30.160 sense shortly so let's save that and run it to see what happens i
00:17:37.120 think it's going to fail right and the error that we see here says if you're going to be using
00:17:44.400 JSON mode your prompt has to contain the words JSON in some form right so
00:17:54.039 Let's ask the AI to give us back some JSON let's
00:17:59.480 say represent a
00:18:05.799 person as a JSON
00:18:11.160 object so let's save that and then run it now that our prompt contains the words JSON we don't get the error let's
00:18:18.640 see what the AI responded with right it created a person for us
00:18:24.080 john Doe 30 male his email phone number etc right
00:18:29.720 now let's do something a little bit more creative instead of returning a person
00:18:35.120 in JSON let's say write
00:18:41.120 uh three scene movie as a JSON object
00:18:50.960 we'll save that run it again and let's take a look so the title
00:18:57.679 of the movie is Whispers of the Forest the genre is fantasy here are the scenes
00:19:03.039 this is a list and each scene has a title as well
00:19:08.400 as a plot a location characters and the dialogue right so I
00:19:14.880 went all out there is one more thing that we have to understand for now how we can learn the rest as we go regarding JSON notice
00:19:22.240 how we weren't very specific with the list of key value pairs that we wanted returned to us when asking for a JSON
00:19:28.600 object but when we build AI automations we will need to be very specific so here
00:19:34.559 is how we can ask or tell the AI to give us back JSON with a very specific set of
00:19:40.720 key value pairs so let's adjust this prompt and write as a JSON object
00:19:46.600 following this schema schema is a fancy word it just
00:19:52.160 means general structure or rules and when you're creating a JSON object or
00:19:57.760 JSON structure or JSON schema you're going to write a set of curly braces and
00:20:04.000 then within these curly braces you can list key value pairs and it's conventional to put some spaces before
00:20:10.880 listing the key value pairs it makes it a little bit easier to read each key is going to be put inside of
00:20:18.280 quotes and after you provide the key you'll write colon and then you'll
00:20:25.200 usually write a space it's easier to read and then here is where you will provide the value of this key
00:20:32.320 in JSON there are a limited set of types or value types that you can put so JSON
00:20:38.960 supports text the way that you say text in JSON schema is the word string this
00:20:44.880 will make sense later keep your mind open and relaxed this stuff is really not that complicated you're going to
00:20:50.080 learn it super fast the other data type is numbers good old math numbers like 1 2 3 or decimals like 3.141 right like pi
00:20:59.360 you can also have lists right the way that you write lists is with square
00:21:04.400 braces right so if you wanted a list of numbers you would write it like this right and you can
00:21:11.159 also have values which themselves are JSON so you can nest JSON at various
00:21:17.080 levels right so we could create another JSON structure as the value of this
00:21:22.960 first key so let me show you what this looks like
00:21:28.159 just to move things along and not be too pedantic hopefully you have enough of a framework to pick this up as we go so
00:21:35.520 because we're describing a movie we want our movie to have a title and we don't want to write the title we want the AI
00:21:42.000 to come up with this movie for us so let's say generically we want some text
00:21:47.280 as a value of this title so we'll write string here for each key value pair in
00:21:52.880 the JSON you're going to end it with a semicolon then you can add another key value pair so I'll put another set of
00:22:00.240 spaces and then we're going to ask for some scenes and put a colon each
00:22:09.720 scene will be a JSON object
00:22:15.480 itself that has a title and the title will be a string
00:22:21.440 just like the movie title and the scene will also have for
00:22:28.600 simplicity at the moment a short description and the short description
00:22:33.919 will also be a string and because we don't want one scene we want a list of
00:22:39.679 scenes right square braces and that does it so if we save
00:22:46.039 this and run the automation again let's see what the AI responds
00:22:53.080 with take a look and you can see we have a title and a list of scenes and each scene has a
00:22:59.840 title and a short description just like we asked for you can use this general technique in many different use cases
00:23:06.000 there are many internet connected systems that use JSON as the primary data transfer format for example there
00:23:12.400 are systems out there that you can send JSON to and in response to a specific formatted JSON with specific key value
00:23:18.960 pairs will return to you for example a movie or for example there are systems
00:23:24.240 out there where you can send some JSON right and that JSON will get stored in a database there's many many different
00:23:28.000 No text
00:23:31.440 systems out there that you can use JSON for so this is a very practical thing to know now let's move on to part
00:23:37.960 three we are now going to walk through the elements or basic building blocks of a platform called JSON to video json to
00:23:44.960 video is exactly what it sounds like it's an API that you can send some JSON to and in response it'll render a video
00:23:50.320 for you according to the details of your JSON now would be the time to sign up to jsontovideo.com if it's your first time
00:23:56.880 signing up you will get some free credits which is great and as a heads up when you run out of those free credits
00:24:02.640 you will need to make a purchase of about 50 bucks but my goal is to avoid you having to make that purchase and the
00:24:08.960 other thing that you're going to have to set up is a file storage system like for example Dropbox or Google Drive and if
00:24:14.640 you're more technical you can even set up your own file server but I recommend you use Dropbox dropbox is free it's
00:24:20.559 simple and it integrates really well with the automation platform we're going to be using make.com and the other pro
00:24:26.720 tip I'll give you before we jump in is to make sure that while you're learning this platform jsontothevideo.com make sure that each
00:24:32.799 video you render is max 2 seconds to 5 seconds for context one JSON video
00:24:38.720 credit gives you about 1 second of rendered video so if you make the videos really short it'll stretch those free
00:24:44.000 credits really far make sense here is the complete list of elements supported
00:24:49.039 by JSON to Video's API audio elements video elements voice elements image
00:24:54.080 elements subtitles HTML text components and audiograms we're going to walk
00:24:59.120 through each one one by one let's get started by creating a new
00:25:05.559 scenario and the first module we're going to add is going to be in the tools
00:25:11.360 app we're going to add a set variable module and we're going to call this
00:25:18.360 variable movie
00:25:24.520 and we will provide the variable value soon let's add another module and this
00:25:33.120 one is going to be JSON to video right the exact module that we
00:25:41.279 want is going to be this one create a movie from JSON
00:25:48.720 so now we have to sign up to JSON to video and get an API key if you've
00:25:57.520 already signed up to JSON to video you can come over to your
00:26:03.240 dashboard and you see this page here that says API keys i'm going to mask
00:26:09.440 mine out but this is where you can find an API key for connecting make with JSON
00:26:15.520 to video
00:26:22.559 and that's it and we could write our JSON in here
00:26:28.559 but I prefer to reference the variable value out
00:26:35.799 here and let's save this and align everything all right let's get going by
00:26:44.240 starting with this baseline JSON and I'm going to be using this tool called JSON
00:26:50.600 formatter this is a tool that makes it a little bit easier to work with JSON you can collapse sections of the JSON when
00:26:57.520 it starts to get large and if and when the JSON gets a little bit misformatted you can easily fix that by
00:27:05.679 clicking this format button right so let's bring that back over here here you can see the overview
00:27:13.200 of a movie.json object according to the JSON to video API each movie or video is
00:27:21.679 going to have a certain resolution this is a code that means 1920 pixels by 1080 pixels right this
00:27:31.360 has to do with how pixelated the video is going to be lower or low I should say will make the
00:27:40.240 video more pixelated but it'll render faster and we're actually going to put
00:27:45.600 SD here sd I think is 720 pixels across and maybe like 480 pixels up i might
00:27:52.000 have that wrong but anyways we're setting things up so that as we learn it's cheap and it's fast that's the
00:27:59.399 rationale and the other aspect of a movie is it's going to consist of scenes right and each scene has a comment where
00:28:06.480 we can put the scene's name it's going to be scene one and each scene is comprised of elements haha and you can
00:28:13.120 see there's also a key for elements that sits at the base of the movie object so
00:28:20.399 this would be useful for putting like a backing track across the entire video but we'll learn about this stuff as we
00:28:26.559 get deeper anyways let's now add a audio element
00:28:34.159 so I'm going to add a JSON object inside of this elements array and the way that
00:28:39.440 we add an audio element is by adding the key type colon space another set of quotes
00:28:47.360 and then here we're going to type audio we're going to provide the source key right src colon space and then another
00:28:55.200 set of quotes here we're going to provide the URL to some audio file i
00:29:01.279 think JSON to video supports MP3 wave maybe a couple other file types as well but
00:29:06.840 anyways I've shared all these media assets with you so you don't have to waste time finding your own and here in
00:29:12.799 the audio folder if you copy the link to this file and then come back to the JSON
00:29:20.240 you can paste it here the only thing that we have to change is this last URL param we have to change this to be raw
00:29:26.880 equals 1 this tells Dropbox that we want to download the file not view it inside
00:29:32.240 of the Dropbox application and because we're trying to avoid that $50 credits
00:29:39.760 charge from JSON to video let's make sure that this video is going to be very
00:29:46.799 short so we'll say duration 3 seconds and I think that'll work so if
00:29:53.679 we format this yeah this is important so sometimes
00:29:59.840 there's characters that you're not seeing in the UI but are embedded in the JSON has to be formatted properly in
00:30:06.799 order for it to work so you can click that format button copy this and then if we come back to
00:30:13.720 make.com let's paste in our first official movie save that and if everything's set
00:30:21.799 up we can run this and you see it looked like it completed
00:30:27.640 successfully if we come to our JSON to video dashboard over to the render logs
00:30:34.520 page we should see a new entry was I right i said 720x 480 i was wrong it's
00:30:42.399 640x 480 i was close but we can see the video is 3 seconds it took 3 seconds to
00:30:47.600 make we click this we can see it right so that's our first movie it's
00:30:55.600 just an audio file all right let's rinse and repeat so let's start with that
00:31:03.240 same base movie
00:31:08.679 and because we're professional SD
00:31:13.880 low and then let's add a video element so let's
00:31:21.200 add that JSON object to the elements array of the first scene
00:31:26.440 and put type
00:31:34.919 video and here we put the URL of the video i've provided
00:31:44.240 uh video files so you don't have to waste time looking for your own technically this could be whatever
00:31:51.279 you want anyhow let's come back here and paste in the URL and we have
00:31:57.799 to fix this this
00:32:04.279 Let's JSON the video download the file instead of trying to view it in the Dropbox UI
00:32:12.159 and the last thing that we'll do is make sure we don't burn our free credits if
00:32:19.679 we're still on them and let's make this video only 3
00:32:26.360 seconds so let's format this it's hidden behind this ad
00:32:31.399 unfortunately we're using a free JSON formatter it is very spammy with the ads
00:32:37.600 yeah we can click format and copy this into
00:32:45.880 make and save and let's run this
00:32:52.039 again and come back to the render
00:33:01.159 logs and here we are
00:33:06.559 there we go okay now that you're familiar with the general pattern of what we're doing here we're walking
00:33:12.000 through each of the basic elements provided by the JSON to video API we're going to move a little bit faster so the
00:33:18.080 next element is going to be the voice element and if we come over to the JSON
00:33:26.000 formatter application paste this in here is how we specify a voice element so
00:33:31.679 type voice here's where we put the text that we want spoken there are two or
00:33:37.600 three model providers I guess you could say for powering the text to speech
00:33:43.919 there's Azure and then 11 Labs right but using 11 Labs is going to burn some of
00:33:50.480 your credits so that's why I'm suggesting Azure there's this other page on the JSON video documentation where
00:33:56.320 you can choose the specific Azure voice and let's keep this simple let's go with
00:34:01.960 English and just to mix it up let's go with Duncan and let's replace
00:34:10.199 Emma with Duncan and format this
00:34:17.480 copy it into the make.com automation save
00:34:25.239 run that looked like it worked and let's refresh the render logs
00:34:36.159 and play this hello world great next up is the image
00:34:43.639 element so let's come back to the JSON formatter paste this
00:34:50.280 in we have to provide the URL to the image so let's come back here i've
00:34:57.440 provided an example image to you want to use it use your own as
00:35:03.640 well copy this come back to JSON formatter
00:35:11.400 paste fix that and we're positioning the image in the
00:35:18.400 center of the window and we're going to show the image
00:35:24.480 for one second let's format this copy and paste it into
00:35:31.580 [Music] m.com save
00:35:37.880 run let's come back to the render logs
00:35:44.920 refresh and take a look perfect the next element will be the
00:35:51.200 subtitles element so let's come back to
00:35:56.240 JSON formatter application and paste this in as you can see the JSON's starting to get a little bit
00:36:02.119 larger we can collapse it to get a better
00:36:08.680 overview right so for the subtitles element
00:36:13.760 you're going to need actually two elements you're going to need a voice
00:36:19.880 element or some audio that has audible
00:36:25.720 dialogue if you use the subtitles element with nonaudible dialogue or like a piece
00:36:33.680 of audio that doesn't have dialogue who knows what it might spit out but anyways you'll see how it works here I've
00:36:40.040 customized this and I am showing you here how to use a
00:36:48.000 custom font json the video comes with some pre-built fonts or some built-in fonts but for branding you're probably
00:36:55.280 going to want to choose your own font so all you have to do is come over to
00:37:01.720 Google Fonts and you can download one of these
00:37:07.359 TTF files and place it somewhere on the internet
00:37:14.079 i've included it in the media assets that I'm sharing you get the link and reference
00:37:22.240 it like this make sure to change the URL param if you're using Dropbox and these are styling changes
00:37:29.200 anyways I'm being a little bit pedantic so let's format this copy it
00:37:35.960 into make.com save that run
00:37:41.480 it that looked like it worked let's come back to our render logs
00:37:47.720 refresh take a look hello world right so it generates on the-fly captions based
00:37:54.960 on some audible audio that's what the subtitles element does next up is the
00:38:00.720 HTML element and this element is pretty cool except that you cannot do
00:38:07.200 animations that's my only gripe with it but here we
00:38:13.320 are so we're going to paste this in and here you can see some HTML code
00:38:22.280 and let's format it copy paste this
00:38:29.480 into make.com save
00:38:34.599 run come back to the render logs refresh take a look
00:38:41.960 right so this could be useful the next element is the text element
00:38:51.560 and it does come with some animations and customizability
00:38:58.320 we're just going to test it with this plain Jane version but yeah you can customize the font
00:39:04.839 and do some things right it does have some
00:39:11.000 animation templates I guess you could say right so you can do some things with
00:39:17.359 this let's come back here format it copy
00:39:22.960 paste save run render logs
00:39:29.079 refresh play it right next up is the component element
00:39:35.680 this is a fancier or more spruced up text like
00:39:41.240 element this is what it looks like and let me show you some
00:39:46.599 other components that come with JSON to video i wish the JSON to Video platform
00:39:53.599 let you build your own custom components hopefully that's on the road map yeah definitely get creative with
00:40:01.440 some of these also these
00:40:13.119 right format copy paste save
00:40:21.720 run render logs refresh there we go let's play
00:40:29.000 it right we got a little newslike title little news crawl the next element is
00:40:36.320 the audiogram element which believe it or not I was not able to get working
00:40:41.680 this is what the audiogram element looks like though it's pretty
00:40:46.760 cool i guess you have to play some audio in the background and then it'll animate this waveform according to the amplitude
00:40:54.640 of the waves in the audio but anyways if you're wondering how I figured out all this stuff I pretty much read through
00:41:00.640 all the documentation so as a heads up there are two versions of the JSON to
00:41:06.319 video docs this to me looks like it's the V1 version and then there is the V2
00:41:12.480 version over here right the documentation is pretty good some of the
00:41:18.160 information is a bit sprawled across V1 and V2 but anyhow that covers all of the
00:41:24.720 JSON to video elements or basic building blocks that you can combine with each other to automate the creation of your
00:41:32.000 No text
00:41:32.280 videos okay okay to play around with JSON to video scenes let's create a new
00:41:38.839 scenario call this JSON to video
00:41:44.450 [Music] scenes and let's add a set variable
00:41:54.040 module call this movie and we'll provide this soon and
00:42:02.400 let's also add a JSON to video create a movie from JSON
00:42:10.359 node and this will be whatever we provide here save all right so let's provide the
00:42:22.359 movie.json this is the first movie.json that
00:42:27.480 we'll take a look at so you can see that the movie consists
00:42:35.599 of one scene here and another scene
00:42:41.000 here and each scene is comprised of elements and we're keeping this very
00:42:47.040 simple for now just to illustrate this concept so if we copy
00:42:52.520 this then paste it here
00:42:58.599 save then run this come over to the render logs
00:43:11.800 refresh play scene one scene two make
00:43:18.119 sense just uh hammer it home let's do a movie with three
00:43:26.760 scenes format and you can see here we have scene one scene
00:43:33.319 two scene three let's copy that and provide the
00:43:39.440 value here save run come back to the render logs on JSON
00:43:47.119 the video refresh and let's take a look scene one
00:43:55.040 scene two scene three make sense okay let's get a little
00:44:01.760 bit creative here is the next movie.json that we're going to use so this is very
00:44:08.560 similar to what it was before but now we have uh Azure voice an AI
00:44:17.400 texttospech voice system reciting some text for us or
00:44:23.200 reading some text for us rather so let me format that let's come back
00:44:31.400 to make save that send it to JSON to
00:44:38.040 video come back to dashboard and JSON to video refresh and let's take a look
00:44:44.720 george Washington John Adams makes sense so the next iteration of
00:44:51.200 this will be layering on some subtitles and here's the updated
00:45:00.520 movie.json so let me collapse this so you can get an overview of what's going
00:45:05.680 on so that's scene one that's scene two and the way that the subtitles
00:45:12.400 element works is you can only have one per movie in JSON video and here you can
00:45:18.880 see I've customized the font you can control a couple other dimensions or aspects of the subtitles that get
00:45:26.359 generated anyways let's keep this simple copy paste this in save send
00:45:35.079 this to the JSON to video API still rendering there we go george Washington
00:45:44.079 john Adams all right george Washington john Adams
00:45:50.720 great so hopefully you got a feel for how you can combine these elements and start to get creative and I'll see you
00:45:57.200 in the last part finally all of that buildup for
00:46:00.000 No text
00:46:03.599 this you now have all of the fundamental knowledge under your belt for being able to do AI video automation let's now take
00:46:10.880 a look at how we can put all these things together here I am in the make.com dashboard let's create a new
00:46:19.160 scenario and we'll call this one
00:46:25.079 AI video automation and the first node that we're
00:46:31.920 going to add is going to be a tools node we'll make it uh set variable
00:46:38.680 module and we're going to call this config the value of this config will be
00:46:46.040 this shift commandV
00:46:51.480 save and the next node is going to be a
00:46:57.560 JSON parse JSON module and we're going to parse whatever
00:47:03.680 we write into the first node save
00:47:09.720 and the next node will be an
00:47:15.960 iterator and we will be iterating over h yeah that's what's weird about
00:47:22.880 make.com sometimes you have to run the scenario in order to
00:47:29.000 see the values available to you so here we are we're going to iterate over the
00:47:35.119 scenes that we provide in this configuration node so let me save that align this zoom
00:47:44.319 out a little bit and the next node is going to be a
00:47:51.240 tools compose a string
00:47:56.359 node and here is the value that we'll paste in here
00:48:04.560 shift commandV and we'd like to reference the
00:48:12.440 script of the current scene that we're iterating
00:48:17.720 through and you can see we're including that in a voice element so let's save that
00:48:26.319 next thing is we're going to add a JSON parse JSON module and we're going
00:48:34.160 to reference the output of this
00:48:40.300 [Music]
00:48:46.200 node save and then we're going
00:48:51.319 to aggregate all of these values array aggregator okay so this is
00:49:00.720 a little bit weird but this is how it looks like this is actually a for loop so for the people who are
00:49:06.040 programmers pretty much what you have to do with these iterators and array aggregators this is how I think of it
00:49:13.720 you link them like this so this is like
00:49:18.960 the end of the for loop we're defining where the loop
00:49:24.200 starts and sometimes you have to run things before you can actually see the
00:49:32.280 values okay so now if we come in here we can see that we have these available to
00:49:38.880 us so to explain what is happening here
00:49:44.160 we're providing some configuration for a movie we want generated we parse that into JSON we
00:49:52.400 then iterate over each scene and as we're iterating over each
00:49:57.920 scene we build out the elements for each scene and we aggregate all of those elements
00:50:06.720 for each scene into another array
00:50:12.280 and we're building an object for each scene that consists of these
00:50:18.440 keys so we'll save that and the next
00:50:24.920 thing is adding a JSON transform to JSON node going to
00:50:33.040 reference the array that we build in the array
00:50:38.359 aggregator and finally we can include that in a JSON config that will get sent
00:50:48.119 to the JSON to video API shift
00:50:53.319 commandV there we go and we're going to
00:50:58.760 reference the JSON config from the previous
00:51:06.359 node so we'll save that and run
00:51:12.040 it and let's come over to the JSON to video render
00:51:17.079 logs and check it out george Washington John Adams
00:51:23.160 yep so we took a little config that we provided and generated a movie all right
00:51:29.599 let's continue iterating on this AI video automation let's spruce it up a
00:51:35.520 little bit more so let's add a
00:51:42.359 photo for each scene so let's
00:51:50.319 put a photo of George Washington to accompany the
00:51:57.559 script and let's also include a photo of John Adams these
00:52:06.480 are the founding fathers of the United States of America for those who don't know and save that
00:52:15.200 and the next thing is we will reference these URLs as we're iterating
00:52:24.680 over each scene shift
00:52:30.970 [Music] commandV and yep we have to
00:52:36.520 run animation and now we should see the
00:52:43.119 photo URL available to us
00:52:49.480 save run and let's come to the render logs
00:52:56.319 and JSON to video and take a look george Washington John Adams yep and let's do
00:53:05.839 some final tweaks let's add
00:53:14.440 the Let me say that before I exit out so let's
00:53:19.480 add the
00:53:24.760 two nodes from this
00:53:33.000 setup so I shift selected them both now I'm going to copy these
00:53:39.240 modules over to the AI video automation that we're
00:53:44.520 building click in and paste them and we will not need these anymore
00:53:53.119 so I'm going to shift click this one shift click this one right click delete
00:53:59.040 this is going to be our starting point let's delete this and connect
00:54:04.920 this align everything take a quick
00:54:11.160 look connect our OpenAI
00:54:18.920 account and we're going to send a user message and we're going to reference the
00:54:24.559 prompt that we write here so here's the prompt
00:54:32.240 that we will include shift
00:54:37.800 commandV write a two scene movie about the founding fathers of the USA each scene should be 5 to 10 seconds then we
00:54:45.680 put some reference information like the link to the URLs and this is the output schema that
00:54:53.280 we're going to ask the AI to produce for us and we're giving it an example of what a valid final output would look
00:55:00.319 like just for additional context so let's save this
00:55:05.880 and take a look at what's going on here save that too and now we have to
00:55:11.880 reference not the scenes from before but we're going to reference the actually we have to run
00:55:19.280 this before we can see the value so let me save this let's run it
00:55:27.720 okay now we should be able to see we do see the scenes
00:55:35.160 but we still need to do one little thing need to show the advanced
00:55:42.599 settings and we need to parse this here we go
00:55:48.359 text format JSON and then we want to automatically parse it
00:55:53.960 save save that run it one more
00:56:01.799 time and then we can grab the scenes that are produced by the
00:56:07.960 AI save that and I think we should be
00:56:14.280 good so let's come back to the render logs and take a look
00:56:20.880 in 1776 George Washington contemplates the future of a new nation john Adams
00:56:27.440 passionately argues for independence during the Continental Congress
00:56:32.480 all right that's kind of cool i think we need to adjust the
00:56:41.000 styling so let's make the text
00:56:46.440 smaller and save that try
00:56:53.240 again come over here take another look george Washington
00:56:59.839 contemplating the future of a new nation john Adams passionately discussing independence
00:57:07.079 cool so that pretty much does it the last
00:57:12.880 thing that you would do after everything is solid you would take up the resolution to wherever you want
00:57:21.680 it to be and we can also do another little thing
00:57:31.040 now that we've made the aspect ratio larger let's add this little config to
00:57:37.839 the images say
00:57:44.680 resize fit save save
00:57:55.880 run still rendering all right that finished let's take a
00:58:01.000 look in a dimly lit room George Washington ponders over the challenges
00:58:06.079 of a new nation john Adams passionately discusses the future of the republic with fellow patriots
00:58:13.200 cool so we're just scraping the tip of the iceberg of how creative you can get
00:58:18.480 with this platform have fun with it and you can use this for doing many
00:58:24.960 different things definitely for automating the creation of your branded social media is one thing welcome to
00:58:30.240 JSON to
