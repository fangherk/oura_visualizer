import React from "react";
import Card from "./Card";

class Main extends React.Component {
  render() {
    return (
      <div className="Main">
        <Card title="Sleep" value="1" />
        <Card title="Readiness" value="2" />
        <Card title="Activity" value="3" />
      </div>
    );
  }
}

export default Main;
