import React, { Component } from "react";
import axios from "axios";
import ZipInfo from "./ZipInfo";

class ZipSearch extends Component {
  constructor(props) {
    super(props);

    this.state = {
      zip: [],
      code: "",
      match: false,
      type: "electronics",
    };

    // changed initial type to electronics as it is the first item on the list
    // this stops a bug where if you hit submit right away it
    // does nothing
    // maybe also make for zip?
    // having a value would remove the place holder though

    // change the name of the api call

    // jsx is only for the return statement

    //this.componentDidMount = this.componentDidMount.bind(this);
    this.fetchZipCode = this.fetchZipCode.bind(this);
    this.getType = this.getType.bind(this);
    this.doStuff = this.doStuff.bind(this);
  }

  // maybe do not need to bind do stuff?

  setZip = (event) => {
    this.setState({
      code: event.target.value,
    });
  };

  // componentDidMount(){
  //     this.fetchZipCode();
  // }

  // need an if statement for which api account

  // can use if else

  fetchZipCode() {
    if (this.state.type === "electronics") {
      axios
        .get(
          `https://data.cityofnewyork.us/resource/wshr-5vic.json?zipcode=${this.state.code}`
        )
        .then((result) => {
          if (result.data.length > 0) {
            this.setState({
              zip: result.data,
              match: true,
            });
          } else {
            this.setState({
              match: false,
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    } else if (this.state.type === "textiles") {
      axios
        .get(
          `https://data.cityofnewyork.us/resource/qnjm-wvu5.json?zipcode=${this.state.code}`
        )
        .then((result) => {
          if (result.data.length > 0) {
            this.setState({
              zip: result.data,
              match: true,
            });
          } else {
            this.setState({
              match: false,
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    } else if (this.state.type === "pharmaceuticals") {
      axios
        .get(
          `https://data.cityofnewyork.us/resource/edk2-vkjh.json?zipcode=${this.state.code}`
        )
        .then((result) => {
          if (result.data.length > 0) {
            this.setState({
              zip: result.data,
              match: true,
            });
          } else {
            this.setState({
              match: false,
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }

  getType(event) {
    event.preventDefault();
    this.setState({ type: event.target.value });
  }

  // the naming conventions for dropoffsite name are inconsistent for each api

  // .get(`https://data.cityofnewyork.us/resource/qnjm-wvu5.json?zipcode=${this.state.code}`)

  // .get(`https://data.cityofnewyork.us/resource/edk2-vkjh.json?zipcode=${this.state.code}`)

  // this.itemType

  // will have to use ternary operator
  // not a fan
  // will not look clean
  // maybe there ia a better way

  // change to redux

  doStuff() {
    {
      this.setState({ match: false });
    }
  }

  // need an if statement here for the items

  render() {
    return (
      <div className="zipsearch">
        <p>Type of object</p>
        <select onChange={this.getType}>
          <option value="electronics"> Electronics </option>
          <option value="pharmaceuticals"> Pharmaceuticals </option>
          <option value="textiles"> Textiles </option>
        </select>

        <p>Zip Code: </p>
        <input
          name="code"
          type="text"
          onChange={(e) => {
            this.setZip(e);
          }}
          value={this.state.code}
          placeholder="Try 10016"
        />
        <button onClick={this.fetchZipCode}>Search</button>

        {this.state.match ? (
          <div>
            {this.state.zip.map((item, index) => (
              <ZipInfo
                key={index}
                address={item.address}
                dropoff_sitename={
                  item.dropoff_sitename ||
                  item.vendor_name ||
                  item.drop_off_site_name
                }
                zipcode={item.zipcode}
              />
            ))}
          </div>
        ) : (
          <p>No Result</p>
        )}
      </div>
    );
  }
}
export default ZipSearch;

/*

{this.setState((prevState) => ({
              match: !prevState.match,
            }))}



{this.state.match ? (
          <div>
            {this.state.zip.map((item, index) => (
              <ZipInfo
                key={index}
                address={item.address}
                dropoff_sitename={item.dropoff_sitename}
                zipcode={item.zipcode}
              />
            ))}
          </div>
        ) : (
          <p>No Result</p>
        )}


*/
