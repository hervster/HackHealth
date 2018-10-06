function Cribs(props) {
  return (
  <button className="crib" onClick={props.onClick}>
      {props.value}
      </button>
  );
}

class Floor extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      cribs: Array(10).fill(null),
      boolTest: true,
    };
  }
  handleClick(i) {
    const cribs = this.state.cribs.slice();
    cribs[i] = this.state.boolTest ? 'Clicked' : 'Not Clicked';
    this.setState({
      cribs: cribs,
      boolTest: !this.state.boolTest,
    });
  }
  
  renderCrib(i) {
    return <Cribs
             value ={this.state.cribs[i]}
             onClick={() => this.handleClick(i)}
             />;
  }
  
  render() {
    return (
    <div>
        {/* <div className="Row Name">{"Row Name"}</div> */}
        <div className="row-name">
          {this.renderCrib(0)}
          {this.renderCrib(1)}
          {this.renderCrib(2)}
          {this.renderCrib(3)}
          {this.renderCrib(4)}
        </div>
        <div className="row-name">
          {this.renderCrib(5)}
          {this.renderCrib(6)}
          {this.renderCrib(7)}
          {this.renderCrib(8)}
          {this.renderCrib(9)}
        </div>
      </div>
    );   
  }
}

class NICU extends React.Component {
  render() {
    return (
    <div className="NICU">
        <div className="floor">
          <Floor />
        </div>
        <div className="crib-layout">
          <div>{/*info*/}</div>
          <ol>{/* MORE */}</ol>
        </div>
       </div>
    );
  }
}
// ========================================

ReactDOM.render(
  <NICU />,
  document.getElementById('root')
);
