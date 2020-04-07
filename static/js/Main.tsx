import React from "react";
import Card from "./Card";
import Grid from "@material-ui/core/Grid";
import LineGraph from "./LineGraph";
import { DataPoint } from "./interfaces";

interface Score {
  scores: any;
  allData: any;
}

class Main extends React.Component<{}, Score> {
  constructor(props: any) {
    super(props);
    this.state = {
      scores: {},
      allData: {
        sleep: [],
        activity: [],
        readiness: [],
      },
    };
  }
  componentDidMount() {
    fetch("http://localhost:5000/latest_scores")
      .then((res) => res.json())
      .then((json) => this.setState({ scores: json }));
    fetch("http://localhost:5000/all_data")
      .then((res) => res.json())
      .then((json) => this.setState({ allData: json }));
  }
  render() {
    console.log(this.state);
    var data: DataPoint[] = [
      { date: "2007-04-23", value: 5 },
      { date: "2008-04-24", value: 5 },
      { date: "2009-04-25", value: 5 },
      { date: "2010-04-26", value: 5 },
      { date: "2012-04-27", value: 16 },
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
            <LineGraph data={this.state.allData["sleep"]} idName="sleep" />
          </Grid>
          <Grid item xs={4} id="readiness">
            <LineGraph data={this.state.allData["readiness"]} idName="readiness" />
          </Grid>
          <Grid item xs={4} id="activity">
            <LineGraph data={this.state.allData["activity"]} idName="activity" />
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default Main;
