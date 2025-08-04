---
video_title: "Performance Testing Fastify vs. Express [EXPERIMENT]"
video_url: "https://www.youtube.com/watch/7TUZjl-hjro"
---

00:00:03.600 here we are on fastify's website
00:00:06.960 and if we come over here to this section
00:00:09.480 where it says benchmarks
00:00:13.320 we see that it claims fastify can serve
00:00:17.220 about five times the requests per second
00:00:21.840 then express.js can
00:00:25.500 so let's verify
00:00:27.900 if this is actually true
00:00:34.200 here is the code
00:00:37.620 express.js
00:00:39.899 and the API has the same interface or
00:00:43.860 shape
00:00:45.840 that the fastify API does
00:00:50.039 so if I come here and run
00:00:54.180 the fastify API
00:00:57.960 and
00:01:00.360 run our Postman collection or
00:01:02.520 integration test against it
00:01:06.060 foreign
00:01:09.180 we see that everything passes
00:01:11.880 I can run the express JS API here
00:01:15.960 and run the same tests again
00:01:18.840 to reuse the tests
00:01:30.360 supposedly
00:01:34.200 this is our request per second
00:01:38.880 so if we divide that by five
00:01:42.500 we get
00:01:46.619 um
00:01:46.930 [Music]
00:01:48.299 maybe 700 something
00:01:51.899 hundred something 700 or so
00:01:56.100 I do rough math in my head
00:01:58.860 so let's run the same Benchmark or load
00:02:01.979 test
00:02:04.380 this time against
00:02:06.299 the express API that has the same
00:02:09.360 interface
00:02:11.580 as
00:02:13.260 the
00:02:14.760 fastify API
00:02:22.440 not
00:02:23.459 a fifth of the requests as was claimed
00:02:26.040 on the fastify website
00:02:29.040 maybe my tools are flawed but I guess
00:02:31.260 the point I am trying to make is always
00:02:33.860 verify and audit all of the information
00:02:36.480 that you are in taking
