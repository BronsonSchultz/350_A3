import React from 'react';
import ReactDOM from 'react-dom';

class MessageBox extends React.Component {
  render() {
    return (
      <form>
        <h1>Hello</h1>
        <p>Enter and message:</p>
        <input type="text" />
      </form>
    );
  }
}

ReactDOM.render(<MessageBox />, document.getElementById('root'))
