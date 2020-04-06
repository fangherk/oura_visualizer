import React from "react";
import { axisBottom, axisLeft } from "d3-axis";
import { select } from "d3-selection";
import { scaleLinear, ScaleLinear, scaleUtc, ScaleTime } from "d3-scale";
import { line } from "d3-shape";
import { max, extent } from "d3-array";
import { DataPoint } from "./interfaces";

interface SvgData {
  height: number;
  width: number;
}

interface Props {
  data: DataPoint[];
  idName: string;
}

class LineGraph extends React.Component<Props, SvgData> {
  ref: SVGSVGElement; // TODO: figure out if this can move into state or props in rendering
  constructor(props: any) {
    super(props);
    this.state = { height: 500, width: 500 };
  }

  /**
   *  Generate the svg axes from the grid's height upstream
   **/
  resize() {
    this.setState({
      height: document.getElementById(this.props.idName).offsetWidth * 0.8,
      width: document.getElementById(this.props.idName).offsetHeight * 0.8,
    });
  }

  componentDidMount() {
    this.resize();
    // Generate values to use
    let yMax = max(this.props.data, (d) => d.close);
    let xTranslation = this.state.width * 0.8;
    let yTranslation = this.state.height * 0.8;
    let linearYScale = this.linearScale(
      scaleLinear,
      [0, yMax],
      [yTranslation, 0]
    );
    let linearXScale = this.linearScale(
      scaleUtc,
      extent(this.props.data, (d) => new Date(d.date)),
      [0, xTranslation]
    );

    // Make the graph
    this.addXAxis(linearXScale as ScaleTime<number, number>, xTranslation);
    this.addYAxis(linearYScale as ScaleLinear<number, number>);
    this.addPath(
      linearXScale as ScaleTime<number, number>,
      linearYScale as ScaleLinear<number, number>
    );
  }

  /**
   *  Generate the X axis
   **/
  addXAxis(scaleTime: ScaleTime<number, number>, translation: number) {
    select(this.ref)
      .append("g")
      .attr("class", "x axis")
      .attr(
        "transform",
        "translate(0," + translation + ")" // moves the axis down since it starts at the top
      )
      .call(axisBottom(scaleTime));
  }

  /*
   *  Generate the Y axis
   **/
  addYAxis(yScale: ScaleLinear<number, number>) {
    select(this.ref).append("g").attr("class", "y axis").call(axisLeft(yScale));
  }

  /**
   *  Helper to generate a linear scale
   **/
  linearScale(
    scale: any,
    domainValues: [any, any],
    rangeValues: [any, any]
  ): ScaleLinear<number, number> | ScaleTime<number, number> {
    return scale().domain(domainValues).nice().range(rangeValues);
  }

  /**
   *  Add the line graph.
   **/
  addPath(
    scaleTime: ScaleTime<number, number>,
    yScale: ScaleLinear<number, number>
  ) {
    var values = line<DataPoint>()
      .x((d) => scaleTime(new Date(d["date"])))
      .y((d) => yScale(d["close"]));

    select(this.ref)
      .append("path")
      .datum(this.props.data)
      .attr("fill", "none")
      .attr("stroke", "green")
      .attr("stroke-width", 2.5)
      .attr("class", "line")
      .attr("d", values);
  }

  render() {
    return (
      <svg
        ref={(ref: SVGSVGElement) => (this.ref = ref)}
        width={this.state.width}
        height={this.state.height}
      ></svg>
    );
  }
}

export default LineGraph;
