---
video_title: "Automate Deployments to GCP ☁️ Cloud Run 🏃 with GitHub Actions"
video_url: "https://www.youtube.com/watch/kZYsoav104w"
---

00:00:01.920 there are many tools we could use for
00:00:03.840 automating our deployments but today we
00:00:06.600 are going to be checking out GitHub
00:00:09.639 actions this is the repository we will
00:00:12.120 be using to test out GitHub actions if
00:00:15.280 you don't already know this repository
00:00:16.960 holds a fast API and each time we update
00:00:19.960 the code in the main branch of our fast
00:00:22.640 API we would like to trigger an
00:00:24.160 automation that will automatically
00:00:25.640 deploy a new version of our application
00:00:28.039 to Google Cloud run the process for
00:00:30.080 doing this is actually quite simple
00:00:32.238 first we need to come over to our gcp
00:00:34.840 account and provision a service account
00:00:39.280 which is a fancy way of saying access
00:00:42.160 credential so we will create a service
00:00:45.640 account called how to deploy doize fast
00:00:49.239 apis to Google Cloud
00:00:52.399 run let create and continue continue
00:00:56.399 done and then what we want to do is add
00:01:00.519 a
00:01:02.039 key download our
00:01:05.159 key this is our password that will give
00:01:10.600 GitHub the permissions to push new
00:01:14.040 services to our gcp account so we come
00:01:17.200 back to our GitHub
00:01:19.159 repository we come over to the settings
00:01:22.759 section and we come over to the secrets
00:01:26.280 and variables
00:01:27.560 section actions and we are going to
00:01:30.759 create a new repository secret we'll
00:01:34.439 paste in our service account credentials
00:01:39.439 as it's so calleded and the name of this
00:01:42.000 secret will be
00:01:44.479 gcpsa key add the secret and the
00:01:48.360 integration work of making GitHub talk
00:01:50.799 to our gcp account has been completed
00:01:53.399 now we'll specify the details of our
00:01:55.759 deployment automation or our GitHub
00:01:58.560 action the way that we do this is by
00:02:01.600 creating a special folder in our project
00:02:05.320 directory called
00:02:08.399 GitHub and inside of this. GitHub folder
00:02:12.440 we place another folder called
00:02:20.720 workflows inside of this workflows
00:02:22.879 folder you can place a yo file that I
00:02:25.640 believe can be called whatever we like I
00:02:27.560 have called it cicd doyo this is the
00:02:31.120 content that I will use to populate this
00:02:33.800 file with if we scan this file we can
00:02:36.920 see it consists of a series of
00:02:39.800 instructions whereby we authenticate the
00:02:44.280 gcp
00:02:46.239 and then issue some instructions that
00:02:49.040 deploy a new service to GCR on our
00:02:53.239 behalf so let's push this to our GitHub
00:02:56.440 repository and hopefully it works the
00:02:59.000 first time
00:03:06.080 if we come back to our repository and go
00:03:09.120 over to the actions tab we can now
00:03:12.360 see an automation is in flight and we
00:03:15.799 can view the build logs in real time
00:03:32.280 holy it
00:03:34.480 worked so let's come to our endpoint
00:03:39.319 again which is already loaded here and
00:03:41.080 if we reload
00:03:42.799 this it's still working now let's do a
00:03:47.400 quick end to end test and let's put a
00:03:51.400 Emoji here
00:04:00.799 okay we see
00:04:02.760 another automation has been
00:04:13.439 triggered okay let's reload the
00:04:17.079 service and now we see our update you
00:04:19.720 might run into some issues with
00:04:21.759 permissions between GitHub and
00:04:25.120 gcp or you might run into some
00:04:27.639 permissions issues with your service
00:04:30.520 account and gcp I included some tips in
00:04:34.039 the GitHub repository for how to add
00:04:36.600 permissions you'll probably need but if
00:04:38.280 you run into any issues leave a comment
00:04:41.280 and we made it
