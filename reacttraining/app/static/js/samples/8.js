var Post = React.createClass({
  render: function() {
    var style = {
      backgroundColor: this.props.bgcolor
    }
    return (
      <div style={style}>
        {this.props.author}: {this.props.children}
      </div>
    );
  }
});

var PostListThree = React.createClass({
  render: function() {
    var postNodes = this.props.data.map(function (comment, index) {
      return (
        <Post key={index} author={comment.author}>
          {comment.post}
        </Post>
      );
    });
    return (
      <div>
        {postNodes}
      </div>
    );
  }
});

var PostForm = React.createClass({
  handleSubmit: function(e) {
    e.preventDefault();
    var form = e.target;
    var author = form.author.value.trim();
    var text = form.post.value.trim();
    if (!text || !author) {
      return;
    }
    this.props.onCommentSubmit({author: author, post: text});
    // TODO: send request to the server
    form.author.value = '';
    form.post.value = '';
    return;
  },
  render: function() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input type="text" placeholder="Your name" name="author"/>
        <input type="text" placeholder="Say something..." name="post"/>
        <input type="submit" value="Post" />
      </form>
    );
  }
});

var PostBox = React.createClass({
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        var postDict = JSON.parse(JSON.stringify(data));   
        this.setState({data: postDict['posts']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  handleCommentSubmit: function(comment) {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: comment,
      success: function(data) {
        var postDict = JSON.parse(JSON.stringify(data));   
        this.setState({data: postDict['posts']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadCommentsFromServer();
    setInterval(this.loadCommentsFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div>
        <h1>Posts</h1>
        <PostListThree data={this.state.data} />
        <PostForm onCommentSubmit={this.handleCommentSubmit}/>
      </div>
    );
  }
});