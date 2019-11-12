import React from 'react';
import { Col } from 'react-bootstrap'

export default class SidNav extends React.Component {
  render() {
    return (
      <Col lg="2" className="sidebar">
        <div className="sidebar-item">Shows Per Year</div>
        <div className="sidebar-item">Shows By State</div>
      </Col>
    );
  }
}