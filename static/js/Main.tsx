import React from "react";
import Card from "./Card";
import Grid from "@material-ui/core/Grid";
import LineGraph from "./LineGraph";
import { DataPoint } from "./interfaces";

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
    var data: DataPoint[] = [
      { date: "2007-04-23", close: 5 },
      { date: "2008-04-24", close: 5 },
      { date: "2009-04-25", close: 5 },
      { date: "2010-04-26", close: 5 },
      { date: "2012-04-27", close: 16 },
    ];
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
          <Grid item xs={4} id="sleep">
            <LineGraph data={data} idName="sleep" />
          </Grid>
          <Grid item xs={4} id="readiness">
            <LineGraph data={data} idName="readiness" />
          </Grid>
          <Grid item xs={4} id="activity">
            <LineGraph data={data} idName="activity" />
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default Main;
