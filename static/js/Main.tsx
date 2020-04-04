import React from "react";
import Card from "./Card";

interface Score {
  scores: any;
}

class Main extends React.Component<{}, Score> {
  constructor(props: any) {
    super(props);
    this.state = { scores: [] };
  }
  componentDidMount() {
    fetch("http://localhost:5000/latest_scores")
      .then((res) => res.json())
      .then((json) => this.setState({ scores: json }));
  }
  render() {
    return (
      <div className="Main">
        <Card title="Sleep" value={this.state.scores["sleep"]} />
        <Card title="Readiness" value={this.state.scores["readiness"]} />
        <Card title="Activity" value={this.state.scores["activity"]} />
      </div>
    );
  }
}

export default Main;
