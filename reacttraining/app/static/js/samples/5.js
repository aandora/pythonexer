var PostListThree = React.createClass({
  render: function() {
    var postNodes = this.props.data.map(function (comment, index) {
      return (
        <Post key={index} author={comment.author}>
          {comment.post}
        </Post>
      );
    });
    console.log(postNodes)
    return (
      <div>
        {postNodes}
      </div>
    );
  }
});

var PostBox = React.createClass({

  render: function() {
    return (
      <div>
        <h1>Posts</h1>
        <PostListThree data={this.props.data}/>
        <PostForm />
      </div>
    );
  }

});