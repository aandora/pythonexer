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

// ===========================
var ProductItem = React.createClass({
  getInitialState: function(){
    return {
      id: this.props.pindex,
      pname: this.props.pname,
      pprice: this.props.pprice,
      pquantity: 0
    }
  },
  handleClick: function(e){
    e.preventDefault();
    val = $('#order_'+this.state.id).val();
    if(isNaN(val)){
      return;
    }
    else{
      console.log('id['+this.state.id+'] '+val);
      if(val>0){
        $.ajax({
          url: '/add_to_cart',
          dataType: 'json',
          type: 'POST',
          data: {item_name: this.state.pname, item_price: this.state.pprice, item_qty:val},
          success: function(data) {
            console.log(JSON.stringify(data));
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
          }.bind(this)
        });
      }
    }
  },
  render: function() {
    var textid = "order_"+this.props.pindex
    return (
      <form onSubmit={this.handleClick}>
        <span>{this.state.pname}</span>
        <span>{this.state.pprice}</span>
        <input type="text" id={textid} />
        <input type="submit" value="Add to Cart" />
      </form>
    );
  }
});

var ProductList = React.createClass({
  render: function() {
    var nodes = this.props.data.map(function (item, index) {
      return (
        <ProductItem key={index} pindex={index} pname={item.name} pprice={item.price} />
      );
    });
    return (
      <div>
        {nodes}
      </div>
    );
  }
});


var AddProductForm = React.createClass({
  handleSubmit: function(e) {
    e.preventDefault();
    var form = e.target;
    var name = form.product_name.value.trim();
    var price = form.product_price.value.trim();
    if (!name || !price) {
      return;
    }
    this.props.onFormSubmit({item_name: name, item_price: price});
    // TODO: send request to the server
    form.product_name.value = '';
    form.product_price.value = '';
    return;
  },
  render: function() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input type="text" placeholder="Product Name" name="product_name" />
        <input type="text" placeholder="Price" name="product_price" />
        <input type="submit" value="Add Item" />
      </form>
    );
  }
});

var Inventory = React.createClass({
  loadProductsFromServer: function(){
    $.ajax({
      url: this.props.geturl,
      dataType: 'json',
      cache: false,
      success: function(data) {
        var postDict = JSON.parse(JSON.stringify(data));
        console.log(JSON.stringify(data));   
        this.setState({data: postDict['items']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.geturl, status, err.toString());
      }.bind(this)
    });
  },
  handleFormSubmit: function(product) {
    $.ajax({
      url: this.props.posturl,
      dataType: 'json',
      type: 'POST',
      data: product,
      success: function(data) {
        var postDict = JSON.parse(JSON.stringify(data));   
        this.setState({data: postDict['items']});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.posturl, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadProductsFromServer();
  },
  render: function() {
    return (
      <div>
        <h4>Products</h4>
        <br />
        <ProductList data={this.state.data} />
        <br />
        <AddProductForm onFormSubmit={this.handleFormSubmit} />
      </div>
    );
  }
});

var CartList = React.createClass({
  render: function(){
    return(
        <h3>Summary</h3>
      );
  }
});
