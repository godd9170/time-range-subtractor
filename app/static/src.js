"use strict";
const e = React.createElement;
const HOURS = [...Array(24).keys()];
const MINUTES = [...Array(4).keys()].map(m => m * 15);

const pad = num => {
  return num.toString().padStart(2, "0");
};

class ReadOnlyTimeRange extends React.Component {
  formatTimeRange = () => {
    const { ranges } = this.props;
    return ranges
      .map(x => `${x.h1}:${pad(x.m1)} - ${x.h2}:${pad(x.m2)}`)
      .join(", ");
  };

  render() {
    return <div>({this.formatTimeRange()})</div>;
  }
}

class TimeRange extends React.Component {
  render() {
    const {
      allowRangeRemove,
      onRangeChange,
      onRangeRemove,
      range: { h1, m1, h2, m2 }
    } = this.props;
    return (
      <li>
        <select value={h1} onChange={e => onRangeChange("h1", e.target.value)}>
          {HOURS.map((h, i) => {
            return (
              <option key={i} value={h}>
                {h}
              </option>
            );
          })}
        </select>
        :
        <select value={m1} onChange={e => onRangeChange("m1", e.target.value)}>
          {MINUTES.map((m, i) => {
            return (
              <option key={i} value={m}>
                {pad(m)}
              </option>
            );
          })}
        </select>
        -
        <select value={h2} onChange={e => onRangeChange("h2", e.target.value)}>
          {HOURS.map((h, i) => {
            return (
              <option key={i} value={h}>
                {h}
              </option>
            );
          })}
        </select>
        :
        <select value={m2} onChange={e => onRangeChange("m2", e.target.value)}>
          {MINUTES.map((m, i) => {
            return (
              <option key={i} value={m}>
                {pad(m)}
              </option>
            );
          })}
        </select>
        {allowRangeRemove ? (
          <span className="delete-range" onClick={onRangeRemove}>
            x
          </span>
        ) : null}
      </li>
    );
  }
}

class TimeRangeList extends React.Component {
  render() {
    const { name, ranges, addRange, onRangeChange, onRangeRemove } = this.props;
    return (
      <ul className="time-range-list">
        {ranges.map((range, i) => {
          return (
            <TimeRange
              allowRangeRemove={ranges.length > 1}
              range={range}
              key={i}
              onRangeChange={(column, value) =>
                onRangeChange(name, i, column, value)
              }
              onRangeRemove={() => onRangeRemove(name, i)}
            />
          );
        })}
        <li className="add-new-range" onClick={() => addRange(name)}>
          +
        </li>
      </ul>
    );
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      a: [{ h1: 9, m1: 0, h2: 10, m2: 0 }],
      b: [{ h1: 9, m1: 30, h2: 10, m2: 0 }]
    };
  }

  addRange = name => {
    this.setState({
      [name]: [...this.state[name], { h1: 0, m1: 0, h2: 0, m2: 0 }]
    });
  };

  onRangeChange = (name, index, column, value) => {
    const ranges = this.state[name];
    this.setState({
      [name]: [
        ...ranges.slice(0, index),
        { ...ranges[index], [column]: value },
        ...ranges.slice(index + 1)
      ]
    });
  };

  onRangeRemove = (name, index) => {
    const ranges = this.state[name];
    this.setState({
      [name]: [...ranges.slice(0, index), ...ranges.slice(index + 1)]
    });
  };

  onSubmit = async e => {
    e.preventDefault();
    const { a, b } = this.state;
    const difference = await (await fetch("subtract", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ a, b })
    })).json();
    this.setState({ difference });
  };

  render() {
    const { a, b, difference } = this.state;
    return (
      <form className="app" onSubmit={this.onSubmit}>
        <div className="column">
          <TimeRangeList
            name="a"
            addRange={this.addRange}
            ranges={this.state.a}
            onRangeChange={this.onRangeChange}
            onRangeRemove={this.onRangeRemove}
          />
          <TimeRangeList
            name="b"
            addRange={this.addRange}
            ranges={this.state.b}
            onRangeChange={this.onRangeChange}
            onRangeRemove={this.onRangeRemove}
          />
        </div>
        <div className="column">
          <ReadOnlyTimeRange ranges={a} />
          <ReadOnlyTimeRange ranges={b} />
          <button type="submit">=</button>
          <div>
            {!!difference ? <ReadOnlyTimeRange ranges={difference} /> : null}
          </div>
        </div>
      </form>
    );
  }
}

const domContainer = document.querySelector("#root");
ReactDOM.render(e(App), domContainer);
