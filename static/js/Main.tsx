import React from "react";
import Card from "./Card";
import Grid from "@material-ui/core/Grid";

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
        <Grid container justify="space-between" alignItems="stretch">
          <Grid item xs={4}>
            <Card title="Sleep" value={this.state.scores["sleep"]} />
          </Grid>
          <Grid item xs={4}>
            <Card title="Readiness" value={this.state.scores["readiness"]} />
          </Grid>
          <Grid item xs={4}>
            <Card title="Activity" value={this.state.scores["activity"]} />
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default Main;
