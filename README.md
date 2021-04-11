# HateBot

## The idea

Negativity is all around us - from the news on theTV through our social networks and even our
conversations with family and friends. What if wewant to avoid that at least on social networks where
some posts are simply hate speech, they don’t addany kind of value to our life? Well, with the hatebot
we can detect if a Tweet is using hate speech or offensivelanguage. Once we know that, the user can
decide for themself if they want to read a tweet (thisway not affecting anyone's right to express their
opinion no matter what it is while still giving theuser the choice to filter out negativity). Also,the
hatebot gives us the option to analyze all the tweetsa person has created and classify the person as a
hater or not thus allowing the user to choose if theywant to affiliate with that user.

## Social relevance and the need for a hate bot

Bullying. One of the biggest issues that all youthface. 59% of U.S. teens have been bullied or
harassed online. The vast majority of teens believeonline harassment is a problem that affects people
their age, and 63% say this is a major problem. 7in 10 young people experience cyberbullying before
they hit the age of 18.^1 Those statistics are frighteningto say the least.

However, the problem is bigger than that, bullyingis not something only the young people have
to deal with - even people like the ex-President ofthe United States of America, a position that is
probably one of the most important in the world, DonaldTrump is doing it and dealing with it. One of
his latest tweets ended with him being blocked fromTwitter. In a part of Twitter’s official explanationon
why they blocked him, we can also see clearly theneed for such a bot:

After close review of recent Tweets from the @realDonaldTrumpaccount and the context around
them — specifically how they are being received andinterpreted on and off Twitter — we have permanently
suspended the account due to the **_risk of further incitementof violence_**.^2

The important part in that statement is the **risk offurther incitement of violence**. Social media
should be platforms where people can freely and trulyexpress themselves and their opinion. However,
sometimes people’s opinions do more harm than good.Right now, in such cases usually, the account of
the offender either gets suspended or nothing happens.Sometimes we also have the opposite case -
perfectly fine tweets can be marked as harmful eventhough they are not. It is very complicated to
understand the difference between intentional hatespeech and radical ideas. This also comes from
cultural differences. For example, there are stillcountries where homosexuality is not something
accepted so calling someone gay can be hate speechat its finest while in others it can just be usedto
describe a man who is in love with another man.

(^2) Full statement can be read athttps://blog.twitter.com/en_us/topics/company/2020/suspension.html
(^1) According to the following research
https://www.pewresearch.org/internet/2018/09/27/a-majority-of-teens-have-experienced-some-form-of-cyberbullying/


All social networks are trying to fight hate speech,racism and sexism. Their success of course
varies. But the need for something that detects anytype of hate speech is there. What makes the
hatebot difference than all the other options we currently have is the fact that it does not delete the
tweet. Even if it goes over community standards, itcan still be viewed but the user is given a caution
that it’s hate speech.
This way we can make sure that:

- Bullying is slowed down. Users get to ignore peopleand tweets that might hurt them
- We have less negativity in our lives - less hate speech,more meaningful content
- Accounts that are created for spamming negativity,sexism, racism or bullying are detected and
    can be stopped
- We understand if something is indeed hate speech orwe simply do not like it. However, things
    aren’t always black and white.

However, the hate bot might have a dark side too.Classifying algorithms are racist to begin with

- there is not enough data from black people or indigenousfor example to be able to train a model as
good as if we only looked at white people. This mightalso influence our hate speech classifier or even
make the racist detector racist which can defeat thepurpose of the project. This is a complicated issue
that araises in all kind of machine learning solutionsthat we should be aware of. To prevent it, we
should make sure that we have data for different typesof people and not for example only straight
white people living in Los Angeles.
    Also, this technology can be used against certain(ethnic) groups and (social) classes.
Depending on the data that the bot is trained with,it might become biased thus ruling out a totally
normal opinion as hate speech. This is something thatthe developers should be aware of when
developing the solution. The worst possible thingthat can happen using the hatebot is having normal
opinions marked as hate speech but that is somethingthat is possible with any kind of solution. To
prevent it from affecting people, the users shouldbe made aware of that side effect.

To sum up, the need for a system to detect if a tweetis hate speech is there. By developing this
solution, we can make sure that there is less hatespeech in Twitter users’ life thus improving the
mental being of the social media users’.


## Target users

Hey you! My name is Sophie. I am what you might callthe classic Twitter user - I post a lot and
sometimes get hate speech from people I don’t evenknow. I was born and raised in a European
country. Other than Twitter I use a lot of other socialmedia - Facebook, Instagram, even Pinterest. I
never got into TikTok and Twitter is still my favouritesocial media because of the text limits. Daily I
spent more than 4 hours on social networks, I wantto see more memes and cat videos and less
negativity. All the hate speech on Twitter reallybothers me, I wish i could ignore it but I alwaysread it. I
am currently in a university so most of my time inthe lockdown is spent in front of the PC/phone.


## Technical approach

To be able to understand if a tweet is hate speech,machine learning will be used. The algorithm
will be given a tweet as a text and then will be ableto tell us using classification if the tweet is using
hate language or not. The classification model willbe trained with the datasets mentioned inDatasets.
The data we have will be split into test and traindata with the ratio of 30 (test) to 70 (train). Ifthe
classification model is less than 60% accurate (accordingto a confusion matrix) and the model can not
be tweaked to become better at it, a neural networkmight be trained.^3

In the future, the algorithm might be upgraded to also detect if a Twitter user is sexist/racist
based on all of his recent tweets. However, at themoment that seems like the labeling is a bit toomuch
unless the algorithm is extremely accurate.

When we are able to classify a tweet as hate speechor not, a website will be built where the
user can enter the text of the Tweet and the web applicationwill tell him if it is hate speech or not. In
the future another page to the web application willbe made where the user can enter a url to a Twitter
user’s profile and a machine learning algorithm willtell him how many percent the user is using hate
speech. However, this requires some more computationalpower so it might become a premium
feature this way allowing the project to be monetized.

## Datasets to use

Hate speech dataset:Hate Speech and offensive languagedataset
Normal tweets dataset:Twitter tweets dataset
Kaggle dataset -Twitter hate speech
Manually marked by users dataset of offensive tweets-github repo

## Summary

Hate speech is something that is a big issue nowadaysespecially with social media like Twitter.
Negativity that comes out of it can take a toll ona person’s mental health. To minimize the damageof
that, the HateBot can return if a tweet is hate speechor not by being given a Tweet. This way we can
ensure that the world becomes if not a better placethen at least a place where we can influence the
amount of negativity we get.

(^3) If I have the time, I would like to work on thateven if the model is successful to see if it can beimproved that way.
However, my estimate is that I won’t have the timebefore the first deadline so


# Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/XJwM8FtzMd8/0.jpg)](https://www.youtube.com/watch?v=XJwM8FtzMd8)
