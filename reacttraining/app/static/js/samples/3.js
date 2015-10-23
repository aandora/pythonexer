var PostBox = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Posts</h1>
        <PostList />
        <PostForm />
      </div>
    );
  }
});