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

var PostListTwo = React.createClass({
  render: function() {
    return (
      <div>
        <Post bgcolor="#FF6600" author="Ali">Hello!</Post>
        <Post bgcolor="#99CCFF" author="Jeru">And again, another greeting!</Post>
      </div>
    );
  }
});