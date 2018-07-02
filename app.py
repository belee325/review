from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0 : {
        'post_id': 0,
        'title':'Hello',
        'content': 'first post'
    }
}
@app.route('/')
def home():
    return 'hello'

@app.route('/post/<int:post_id>')
def post(post_id):
    f_post = posts.get(post_id)
    if not f_post:
        return render_template('404.jinja2', message=f'Post with with ID {post_id} was not found')
    return render_template('post.jinja2', post=f_post)

@app.route("/post/create")
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post_id = len(posts)
    posts[post_id] = {'post_id':post_id, 'title':title, 'content':content}
    return redirect(url_for('post', post_id = post_id))

@app.route('/post/form')
def form():
    return render_template('create.jinja2')

if __name__ == '__main__':
    app.run(debug=True)