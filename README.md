
=======
# Tumblelog
This application permits to create and edit a collection in the MongoDB database(database_tumble) with a python shell.
it's the first step towards a site tumblelog application

# Requirements
This app is made in an Ubuntu 14.04 environment. 
So the install is quite easy. As shown in the MongoDB tutorial, you must 

* Have the python environment:

** sudo pip install virtualenv
** virtualenv tumblelog
** source tumblelog/bin/activate

* All the frameworks you need (at this level):

** sudo pip install \

** flask \

** flask-script \

** mongoengine \

** flask_mongoengine \

** ipython

It's obvious that you already have a mongodb instance running on.

# Build

after have cloned the repository, 
you must run the python command:

    python manage.py shell

The ipyhton terminal will come up. Inside it, you can post(title,slug,body) some and comment(author,body) about it.

# Exemple:

+ Build a collection named post:

    post = Post(
    
    'title':'The post',
    
    'slug':'Interesting post',
    
    'body':'This is my first post, and my first application build on Mongo')
    
+ Save the data in the post collection:

* post.save() 

+ Now, it's time to add comments on the post:

    comment = Comment(
    
    'author':'Gilles ESSOKI NDAME',
    
    'body':"This is my first comment on the 'The post' post")

+ Then, add the comment in the appropriate post:

* post.comments.append(comment)

# Verify

Now you should verify wether or no the things done in the shell have succeeded.

You should open a terminal and do:

    mongo
    use database_tumble
    db.post.find().pretty()

# Result

As the result of the last part, you should have:

{
	"_cls" : "Post",
    
	"_id" : ObjectId("56f7fecc44004a1d494341e7"),
    
	"body" : "This is my first post, and my first application build on Mongo",
    
	"comments" : [
		{
			"created_at" : ISODate("2016-03-27T17:46:18.818Z"),
            
			"body" : "This is my first comment on the 'The post' post",
            
			"author" : "Gilles ESSOKI NDAME"
		}
	],
	"created_at" : ISODate("2016-03-27T17:39:12.335Z"),
    
	"slug" : "Interesting post",
    
	"title" : "The post"
}





