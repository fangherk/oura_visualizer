import React from "react";

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
      <div className="card">
        <h2> {this.props.title} </h2>
        <p> {this.props.value} </p>
      </div>
    );
  }
}

export default Card;
