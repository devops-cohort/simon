from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateTableForm, DeleteForm
from flask_login import login_user, current_user, logout_user, login_required, LoginManager

@app.route('/')
@app.route('/home')
def home(): 
    postData = Posts.query.all() 
    return render_template('home.html', title='Home', posts=postData)
    
#@app.route('/about')
#def about():
#    return render_template('about.html', title='About')

@app.route('/post', methods=['GET','POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                englishh=form.englishh.data,
                spanishh=form.spanishh.data,
                comment=form.comment.data,
                author=current_user
        )
        
        db.session.add(postData)
        db.session.commit()
    
        return redirect(url_for('home'))
    else:
        print(form.errors)
    
    return render_template('post.html', title='Post', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data, 
                password=hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    #form = DeleteAccount()
    #if form.delete.data:
    # delete_row = Posts.query.filter_by(id=form.id.data).delete()
    #deleteAccount = Users(id=form.id.data)
    #db.session.delete()
    #db.session.commit()
    #return redirect(url_for('register'))
    #elif form.validate_on_submit(): and the rest 
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email 
    return render_template('account.html', title='Account', form=form)

@app.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    form = UpdateTableForm()
    #login_user(user, remember=form.remember.data)
    post = Posts.query.all() #jinja2 su
    if form.validate_on_submit():
       # post = Posts(
       #         englishh=form.englishh.data,
       #         spanishh=form.spanishh.data,
       #         comment=form.comment.data,
       #         author=current_user
       # )
#        post.englishh = form.englishh.data
 #       post.spanishh = form.spanishh.data
  #      post.comment = form.comment.data
   #     db.session.commit()
        return redirect(url_for('update'))
    #elif request.method == 'GET':
     #   form.englishh.data = post.englishh
      #  form.spanishh.data = post.spanishh
       # form.comment.data = post.comment
    return render_template('update.html', title='Update', form=form)

@app.route("/delete") # , methods=['GET','POST'])
def delete():
    if current_user.is_authenticated:
        form = DeleteForm()
        if form.validate_on_submit:
            user_id = Users.query.filter_by( id=current_user.get_id() ).first()

            posts = Posts.query.filter_by( user_id=user_id.id )
            for post in posts:
                db.session.delete(post)

            db.session.delete(user_id)

            db.session.commit()
            return redirect(url_for("login"))

        return render_template('about.html', title='About', form=form)
    return redirect(url_for("login"))

   # if current_user.is_authenticated:
    #    return redirect(url_for('home'))
#    form = DeleteForm()
#    if form.validate_on_submit():
       # delete_user(user, delete=form.delete.data)
       # user = Users(
#                first_name=form.first_name.data,
 #               last_name=form.last_name.data,
  #              email=form.email.data,
   #             password=hashed_pw
    #    )
     #   db.session.delete(user)
      #  db.session.commit()
       # return redirect(url_for('register'))
#    return render_template('about.html', title='About', form=form)
