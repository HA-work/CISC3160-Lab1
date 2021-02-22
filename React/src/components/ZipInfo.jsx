import React, { Component } from "react";

class ZipInfo extends Component {
  render() {
    return (
      <div className="Info">
        <header className="head">
          <h1>
            {this.props.dropoff_sitename}, {this.props.zipcode}
          </h1>
        </header>
        <ul>
          <li>
            {" "}
            <h2>Address: {this.props.address}</h2>{" "}
          </li>
        </ul>
      </div>
    );
  }
}
export default ZipInfo;
