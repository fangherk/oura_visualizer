import React from "react";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";

interface Props {
  title: string;
  value: string;
}

class Card extends React.Component<Props> {
  constructor(props: any) {
    super(props);
  }
  render() {
    return (
      <Paper className="paper">
        <Typography variant="h4">{this.props.title}</Typography>
        <Typography variant="h1">{this.props.value}</Typography>
      </Paper>
    );
  }
}

export default Card;
