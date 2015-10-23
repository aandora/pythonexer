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

var PostBox = React.createClass({
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
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
  render: function() {
    return (
      <div>
        <h1>Posts</h1>
        <PostListThree data={this.state.data}/>
        <PostForm />
      </div>
    );
  }

});